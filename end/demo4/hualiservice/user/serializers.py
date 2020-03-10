from django.db.models import Q
from rest_framework import serializers
from .models import *
from django.contrib.auth import hashers
from datetime import timedelta,datetime
from utils.sendmsg import SendMsg
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id","email","username","telephone","headImg","sex","birthday"]
        read_only_fields = ["id"]

class UserResetPasswordSerializer(serializers.Serializer):
    telephone = serializers.CharField(label="手机号",max_length=11,min_length=11, help_text="请输入手机号",error_messages={
        "min_length": "最小长度11",
        "max_length": "最大长度11",
        'blank': "手机号不能为空"
    })
    code = serializers.CharField(label="验证码",write_only=True, max_length=6,min_length=6,help_text="请输入6位数字验证码",error_messages={
        "min_length": "最小长度6",
        "max_length": "最大长度6",
        'blank': "验证码不能为空"
    })
    password = serializers.CharField(label="密码", help_text="请输入密码", min_length=6, max_length=20,
                                     error_messages={
                                         "min_length": "最小长度6",
                                         "max_length": "最大长度20",
                                         'blank': "密码不能为空"
                                     })
    password2 = serializers.CharField(label="重复密码", min_length=6, max_length=20, help_text="请输入重复密码",
                                      error_messages={
                                          "min_length": "最小长度6",
                                          "max_length": "最大长度20",
                                          'blank': "重复密码不能为空"
                                      })
    def validate(self, attrs):
        if self.initial_data["password"] != attrs["password2"]:
            raise serializers.ValidationError("密码不一致")
        del attrs["password2"]
        attrs["password"]=hashers.make_password(attrs["password"])
        telephone = attrs["telephone"]
        code = attrs["code"]
        history = Code.objects.filter(telephone=telephone,code=code,type="update")
        if history.count()<=0:
            raise serializers.ValidationError("验证码无效")
        # if attrs["code"] != "000000":
        #     raise serializers.ValidationError("验证码错误")
        history.first().delete()
        del attrs["code"]
        return attrs

    def update(self, instance, validated_data):
        instance.password = validated_data.get("password",instance.password)
        instance.save()
        return instance

class UserRegistSerializer(serializers.Serializer):
    telephone = serializers.CharField(label="手机号",max_length=11,min_length=11, help_text="请输入手机号",error_messages={
        "min_length": "最小长度11",
        "max_length": "最大长度11",
        'blank': "手机号不能为空"
    })
    password = serializers.CharField(write_only=True,label="密码",help_text="请输入密码",min_length=6,max_length=20,error_messages={
        "min_length":"最小长度6",
        "max_length":"最大长度20",
        'blank': "密码不能为空"
    })
    password2 = serializers.CharField(write_only=True,label="重复密码",min_length=6,max_length=20,help_text="请输入重复密码",error_messages={
        "min_length":"最小长度6",
        "max_length":"最大长度20",
        'blank': "重复密码不能为空"
    })
    code = serializers.CharField(label="验证码",write_only=True, max_length=6,min_length=6,help_text="请输入6位数字验证码",error_messages={
        "min_length": "最小长度6",
        "max_length": "最大长度6",
        'blank': "验证码不能为空"
    })

    def validate(self, attrs):
        if self.initial_data["password"] != attrs["password2"]:
            raise serializers.ValidationError("密码不一致")
        del attrs["password2"]
        telephone = attrs["telephone"]
        if UserProfile.objects.filter(telephone = telephone ).count()>0:
            raise serializers.ValidationError("手机号已经注册")
        code = attrs["code"]
        history = Code.objects.filter(telephone=telephone,code=code,type="regist")
        if history.count()<=0:
            raise serializers.ValidationError("验证码无效")
        del attrs["code"]
        history.first().delete()

        attrs["username"] = attrs["telephone"]
        return attrs

    def create(self, validated_data):
        username = validated_data.pop("username")
        print(validated_data)
        return UserProfile.objects.create_user(username,**validated_data)

class UserCodeSerializer(serializers.Serializer):
    telephone = serializers.CharField(label="手机号",max_length=11,min_length=11, help_text="请输入手机号",error_messages={
        "min_length": "最小长度11",
        "max_length": "最大长度11",
        'blank': "手机号不能为空",
    })
    type = serializers.CharField(label="验证码类型", max_length=6,min_length=6,help_text="请输入验证码类型",error_messages={
        "min_length": "最小长度6",
        "max_length": "最大长度6",
        'blank': "验证码类型不能为空"
    })
    def validate(self, attrs):
        telephone = attrs["telephone"]
        codetype = attrs["type"]
        if codetype not in ["regist","update"]:
            raise serializers.ValidationError("验证码类型不合法")
        history = Code.objects.filter(telephone=telephone,type=codetype)
        if history.count() >0:
            oneminutesago = datetime.now() - timedelta(minutes=1)
            if history.filter(create_time__gt = oneminutesago):
                raise serializers.ValidationError("已经发送过验证码")
            else:
                history.delete()
                code = SendMsg(telephone).send()
                attrs["code"] = code
        else:
            code = SendMsg(telephone).send()
            attrs["code"] = code
        return attrs

    def create(self, validated_data):
        try:
            code = Code.objects.create(**validated_data)
            return code
        except Exception as e:
            print(e)
            raise serializers.ValidationError("失败了")