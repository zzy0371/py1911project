from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import *
class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["flower","num","price","id"]

class CartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    flower = serializers.PrimaryKeyRelatedField(required=True,queryset= Flower.objects.all())
    price = serializers.IntegerField()
    num = serializers.IntegerField()

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        exist = Cart.objects.filter(flower=validated_data["flower"]).first()
        if exist:
            print(exist)
            exist.num += validated_data["num"]
            exist.save()
            return exist
        else:
            return Cart.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.num = validated_data.get("num",instance.num)
        instance.save()
        return instance
