from rest_framework import serializers
from authentication.models import User
from authentication.hashers import MyBcrypt
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.serializers import Serializer


class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'username',
            'password',
            'password2',
            'phone',
            'address',
        ]



    def create(self, validated_data):

        user = User(

            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['username'],
            password=MyBcrypt().anonymous(validated_data['password']),
            password2=MyBcrypt().anonymous(validated_data['password2']),
            phone=validated_data['phone'],
            address=validated_data['address'],

        )

        # user.save()
        return user



