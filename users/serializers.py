from rest_framework import serializers
from .models import Users

class userserializers(serializers.modelserializers):
    class meta:
        model = Users
        fields = "__all__"