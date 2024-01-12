from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name' ,'email', 'password', 'confirm_password']
    
    def save(self):
        # user = User(
        #     username = self.validated_data['username'],
        #     first_name = self.validated_data['first_name'],
        #     last_name = self.validated_data['last_name'],
        #     email = self.validated_data['email'],
        # )
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        # user.set_password(password)
        # user.save()
        # return user
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})
        account = User(email=email, username=username, first_name=first_name, last_name=last_name)
        print(account)
        # return User.objects.create_user(username=username, email=email, password=password)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)