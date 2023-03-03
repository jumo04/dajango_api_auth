from rest_framework import serializers
from auth.models import User

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    birth_date = serializers.DateField()
    address = serializers.CharField(required=True, allow_blank=False, max_length=100)
    token = serializers.CharField(required=False, allow_blank=True)
    
    password = serializers.CharField(required=True, write_only=True, length=120)
    mobile_phone = serializers.CharField(required=True, allow_blank=True, max_length=100)
    email = serializers.CharField(required=True, allow_blank=True, max_length=100)

    def create(self, data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        instance = User.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            birth_date=data.get('birth_date'),
            email=data.get('email'),
            address=data.get('address'),
            mobile_phone=data.get('mobile_phone'),
        )
        instance.set_password(data.get('password'))
        instance.save()
        return instance

    def update(self, instance, data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.birth_date = data.get('birth_date', instance.birth_date)
        instance.email = data.get('email', instance.email)
        instance.token = data.get('token', instance.token)
        instance.address = data.get('address', instance.address)
        instance.mobile_phone = data.get('mobile_phone', instance.mobile_phone)
        instance.set_password(data.get('password'))
        instance.save()
        return instance