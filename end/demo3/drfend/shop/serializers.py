from rest_framework import serializers
from .models import *






class GoodSerializer1(serializers.ModelSerializer):
    # 在序列化时指定字段  在多方 使用source = 模型名.字段名
    # read_only= True标识不能更改(get 显示  update不显示)
    # write_only=True 标识只能更改（get 不显示 update显示）
    category = serializers.CharField(source='category.name',read_only=True)

    class Meta:
        model = Good
        fields = ('id','name','desc','category')

class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    """
    def to_representation(self, value):
        """
        重写字段的输出格式
        :param value:  需要序列化的对象
        :return: 显示的格式
        """
        return str(value.id) + "--" + value.name + "--" + value.desc



class CategorySerizlizer(serializers.Serializer):
    """
    序列化类 决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=3,error_messages={
        "max_length":"最多10个字",
        "min_length":"最少3个字"
    })

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print("重写创建方法",validated_data)
        instance = Category.objects.create(**validated_data)
        print("创建模型实例",instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        print("重写更新方法",validated_data,instance.name)
        instance.name = validated_data.get("name",instance.name)
        print(instance.name)
        instance.save()
        return instance


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少2个字"
    })
    category = CategorySerizlizer(label="分类")

    def validate_category(self, category):
        """
        处理category
        :param category:  处理的原始值
        :return: 返回新值
        """
        print("category原始值为",category)
        try:
            Category.objects.get(name = category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return category

    def validate(self, attrs):
        print("收到的数据为",attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name = attrs["category"]["name"])
        attrs["category"] = c
        print("更改之后的数据",attrs)

        return attrs

    def create(self, validated_data):
        print("创建good参数",validated_data)
        instance = Good.objects.create(**validated_data)  # name=    category=
        return instance


class CategorySerizlizer1(serializers.ModelSerializer):
    # goods 一定要和 related_name 的值一致

    # StringRelatedField() 可以显示关联模型中的 __str__返回值  many=True 代表多个对象  read_only=True 代表只读
    # goods = serializers.StringRelatedField(many=True)

    # PrimaryKeyRelatedField 显示主键值
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    # SlugRelatedField 显示自定义字段值
    goods = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)

    # 显示资源RestFulAPI
    # goods = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='good-detail')

    # 自定义序列化类
    # goods = CustomSerializer(many=True,read_only=True)

    # goods = GoodSerializer(many=True,read_only=True)

    class Meta:
        model = Category
        # __all__ 代表模型中的所有字段
        # fields = "__all__"

        # fields 指明序列化哪些字段
        fields = ('id','name','goods')


