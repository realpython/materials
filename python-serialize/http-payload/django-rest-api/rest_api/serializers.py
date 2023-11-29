from rest_framework import serializers

from . import models


class UserSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class UserSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["name"]
