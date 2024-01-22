from rest_framework import serializers
from Software_Settings import models
from django.contrib.admin.models import LogEntry
# from product.serializers import warehouseSerilizer
from django.contrib.auth.models import Group
# from software_settings import models as settings_models
# from software_settings import serializers as settings_Serializer
from HRM import serializers as hrm_Serializer


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    """serlizers a user profile object"""

    # data = JSONSerializerField()

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class moduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.module
        fields = '__all__'


class sub_moduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.sub_module
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.module:
            response['Module'] = instance.module.name
        return response
