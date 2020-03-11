from rest_framework import serializers
from .models import *

class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = Category
        fields = "__all__"


class FlowerImageSerializer(serializers.ModelSerializer):
    flower = serializers.CharField(source='flower.name')
    class Meta:
        model = FlowerImage
        fields = "__all__"

class FlowerSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    bannerImgs = serializers.SerializerMethodField()
    infoImgs = serializers.SerializerMethodField()

    class Meta:
        model = Flower
        fields = "__all__"

    def get_infoImgs(self, instance):
        seria = FlowerImageSerializer(instance.flowerimage_set.filter(type="info"), many=True)
        return seria.data

    def get_bannerImgs(self, instance):
        seria = FlowerImageSerializer(instance.flowerimage_set.filter(type="banner"),many=True)
        return seria.data

