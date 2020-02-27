from rest_framework import serializers
from .models import *

class GoodSerializer(serializers.ModelSerializer):
    # 在序列化时指定字段  在多方 使用source = 模型名.字段名  read_only= True标识不能更改
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



class CategorySerizlizer(serializers.ModelSerializer):
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


