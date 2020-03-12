from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from flower.serializer import FlowerSerializer
from .models import *
class UserFavDetailSerializer(serializers.ModelSerializer):
    # flower = FlowerSerializer()
    # flower = serializers.CharField(source='flower.name')

    class Meta:
        model = Collect
        fields = ("flower", "id")


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Collect
        validators = [
            UniqueTogetherValidator(
                queryset=Collect.objects.all(),
                fields=('user', 'flower'),
                message="已经收藏"
            )
        ]

        fields = ("user", "flower", "id")

class CommentImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImg
        fields = "__all__"


class CommentDetailSerializer(serializers.ModelSerializer):
    # flower = FlowerSerializer()
    flower = serializers.CharField(source='flower.name')
    imgs = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ("flower", "rate", "comment", "imgs", "id")

    def get_imgs(self, instance):
        return CommentImgSerializer(instance.commentimg_set.all(),many=True).data



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        validators = [
            UniqueTogetherValidator(
                queryset=Comment.objects.all(),
                fields=('user', 'flower'),
                message="已经评论"
            )
        ]

        fields = ("user", "flower", "rate", "comment")