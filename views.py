from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer,PhotoGrapherSerializer,RatingSerializer,BookingSerializer
from .models import ShootUser,Booking,Photographers,Rating,User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = ShootUser.objects.all()

class RatingViewSet(viewsets.ModelViewSet):
	serializer_class = RatingSerializer
	queryset = Rating.objects.all()
	authentication_classes = (TokenAuthentication,)







class PhotographerViewSet(viewsets.ModelViewSet):
	serializer_class = PhotoGrapherSerializer
	queryset = Photographers.objects.all()
	authentication_classes = (TokenAuthentication,)

	@action(detail=True,methods=['POST'])
	def ratePhotographer(self,request,pk=None):
		if 'stars' in request.data:
			Phtgr = Photographers.objects.get(id=pk)
			#print(Phtgr.Name,Phtgr.Location)
			stars = request.data['stars']
			user = request.user
			#user = ShootUser.objects.get(id=1)
			#print("user:",user.email)
			try:
				rate_set = Rating.objects.get(User=user.id,GrapherName = Phtgr.id)
				rate_set.Stars = stars
				rate_set.save()
				serializer = RatingSerializer(rate_set,many=False)
				response ={'message':'Rating Updated','Result':serializer.data}
				return Response(response,status=status.HTTP_200_OK)
			except:
				rate_set=Rating.objects.create(GrapherName=Phtgr,User=user,Stars=stars)
				serializer = RatingSerializer(rate_set,many=False)
				response ={'message':'Rating Created','Result':serializer.data}
				return Response(response,status=status.HTTP_200_OK)
		else:
			response={'message':'You need to provide rating'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)

class BookingViewSet(viewsets.ModelViewSet):
	serializer_class = BookingSerializer
	queryset = Booking.objects.all()
	authentication_classes = (TokenAuthentication,)

	@action(detail = True,methods = ['POST'])
	def bookPhotographer(self,request,pk=None):
		if 'grapherName' in request.data:
			getUser = ShootUser.objects.get(id=pk)
			getPhotogapher = Photographers.objects.get(id=pk)
			user = request.user
			grapherName = request.data['grapherName']
			bookDate = request.data['bookDate']
			ShootDate = request.data['ShootDate']
			Loc_of_shoot = request.data['Loc_of_shoot']
			ShootPurpose = request.data['ShootPurpose']
			Payment_Status = request.data['Payment_Status']
			Address = request.data['Address']

			book_set = Booking.objects.create(User = user.id, GrapherName=getPhotogapher.GrapherName)
			book.set.Address = Address
			book.set.ShootPurpose = ShootPurpose
			book.set.Loc_of_shoot = Loc_of_shoot
			book.set.Payment_Status = Payment_Status
			book.set.DateOfShoot = ShootDate
			book.set.BookDate = bookDate
			book_set.save()
			serializer = BookingSerializer(book_set,many=True)
			response = {'message': 'Booking Done', 'Result' : serializer.data}
			return Response(response,status=HTTP_200_OK)
		else:
			response={'message':'Missing Information'}
			return Response(response,status=status.HTTP_400_BAD_REQUEST)



