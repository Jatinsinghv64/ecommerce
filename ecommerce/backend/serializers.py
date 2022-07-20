from dataclasses import fields
from django.forms import ValidationError
from .models import *
from rest_framework import serializers, status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class CustomerSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = Customer
        fields = ("name","phone_no","gender","username","password")
        # exclude

    def validate(self,validated_data):
        user_obj = User.objects.filter(username=validated_data['username']).first()
        if user_obj is None:
            user_obj = User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        else:
             raise ValidationError("user exist with this username") 
        customer_obj = Customer.objects.create(user = user_obj,name=validated_data['name'],gender = validated_data['gender'],phone_no = validated_data['phone_no'])
        return super().validate(validated_data)



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		print('in')
		user = authenticate(username=attrs['username'], password=attrs['password'])
		if user is not None:
			if user.is_active:
				data = super().validate(attrs)
				refresh = self.get_token(self.user)
				refresh['username'] = self.user.username
				try:
					obj = UserProfile.objects.get(user=self.user)
					refresh['employeeRole'] = obj.employeeRole
					data["refresh"] = str(refresh)
					data["access"] = str(refresh.access_token)
					data["employee_id"] = self.user.id
					data['user_name']= self.user.username
					data["employeeRole"] = obj.employeeRole
					data['first_name']= self.user.first_name
					data['last_name']= self.user.last_name
				except Exception as e:
					raise serializers.ValidationError('Something Wrong!')
				return data
			else:
				raise serializers.ValidationError('Account is Blocked')
		else:
			raise serializers.ValidationError('Incorrect userid/email and password combination!')

class ProductSerializers(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

