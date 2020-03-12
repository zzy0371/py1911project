from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *
class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["flower","num","id"]

class CartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    flower = serializers.PrimaryKeyRelatedField(queryset= Flower.objects.all(),label="商品", help_text="商品",error_messages={
        'required':"商品必选"
    })
    num = serializers.IntegerField(help_text="数量",label="数量", min_value=1, error_messages={
        "min_value":"不能少于1个",
        'required': "数量必选"
    })

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        """
        创建购物车记录时 先查看商品是否已经在购物车  在购物车中则更改数目否则 新添加一个记录
        :param validated_data:
        :return:
        """
        exist = Cart.objects.filter(flower=validated_data["flower"],user=self.context["request"].user).first()
        if exist:
            print(exist)
            exist.num += validated_data["num"]
            exist.save()
            return exist
        else:
            return Cart.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        更改购物车 商品数量
        :param instance:
        :param validated_data:
        :return:
        """
        exist = Cart.objects.filter(flower=validated_data["flower"], user=self.context["request"].user).first()
        if exist:
            instance.num = validated_data.get("num",instance.num)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("当前商品不存在")

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ["trader_sn","order_sn","user"]

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    state = serializers.CharField(read_only=True)
    trader_sn = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    money = serializers.IntegerField(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from random import Random
        import time
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id, ranstr=random_ins.randint(10, 99))

        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    def create(self, validated_data):
        hascarts = Cart.objects.filter(user=self.context["request"].user).exists()
        if hascarts:
            return Order.objects.create(**validated_data)
        else:
            raise serializers.ValidationError("购物车没有商品数据")



