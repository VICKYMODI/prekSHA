from rest_framework import serializers
from .models import User, Booking,Photographers,Rating

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['shootuser','Age','Sex']
		extra_kwargs = {'password':{'write_only':True}}
	


class PhotoGrapherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photographers
		fields = ['id','GrapherName','Special_IN','Age','Location','no_of_rating','avg_rating','model_pic','bestWo1','bestWo2','bestWo3','bestWo4','bestWo5']
		print("test")

class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = ['id','GrapherName','User','Stars']

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['user_id','user','ShootPurpose','Loc_of_shoot','DateOfShoot','PickGrapher','BookDate','Payment_Status']
			