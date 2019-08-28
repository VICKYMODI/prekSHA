from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator ,MinValueValidator
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
	)
from django import forms




    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password."""
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    
    def create_superuser(self, password,email=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    
    

# hook in the New Manager to our Model
 	
class User(AbstractUser):
	email = models.EmailField(
    	verbose_name = 'email address',
    	max_length = 255,
    	unique=True,
    	)
	active = models.BooleanField(default=True)
	is_shootUser = models.BooleanField(default=False)
	is_photoGrapher = models.BooleanField(default=False)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	#UserModel = get_user_model()
	#username_field = UserModel._meta.get_field(getattr(UserModel, 'USERNAME_FIELD', 'username'))
	USERNAME_FIELD = 'email'
	def has_perm(self,perm,obj=None):
		"Does the user have a specific permission"
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin

	@property
	def is_active(self):
		"Is the user active?"
		return self.active
	

	def __str__(self):
		return self.email

	REQUIRED_FIELDS = [] # Email & Password are required by default.
	def get_short_name(self):
		return self.username

	def get_full_name(self):
		return self.username

	objects = UserManager()

class ShootUser(models.Model):
	shootuser = models.OneToOneField(User, on_delete=models.CASCADE)
	Age = models.IntegerField(blank=False)
	#email = models.EmailField(blank=True,unique=True)
	Sex = models.CharField(max_length=10,blank=False)
	Mobile = PhoneField(blank=True, help_text='Contact phone number')
	Address = models.CharField(max_length=60,blank=False)
	District = models.CharField(max_length=20,blank=False)
	
	

	def __str__(self):
		return self.Name

class Photographers(models.Model):
	GrapherName = models.CharField(max_length=36, blank=False)
	Age = models.IntegerField(default=0,blank=True)
	Sex = models.CharField(max_length=10,blank=False)
	Location = models.CharField(max_length=36, blank=False) 
	email = models.EmailField(max_length=254,blank=True)
	Mobile = PhoneField(blank=True, help_text='Contact phone number')
	Password = models.CharField(max_length=50,blank=True)
	Special_IN = models.CharField(max_length=50,blank=True)
	TagLine = models.CharField(max_length=255,blank=True)
	model_pic = models.ImageField(upload_to = 'image/profile/', default = 'image/None/no-img.jpg')
	bestWo1 = models.ImageField(upload_to = 'image/workImages/', default = 'image/None/no-img.jpg')
	bestWo2 = models.ImageField(upload_to = 'image/workImages/', default = 'image/None/no-img.jpg')
	bestWo3 = models.ImageField(upload_to = 'image/workImages/', default = 'image/None/no-img.jpg')
	bestWo4 = models.ImageField(upload_to = 'image/workImages/', default = 'image/None/no-img.jpg')
	bestWo5 = models.ImageField(upload_to = 'image/workImages/', default = 'image/None/no-img.jpg')
	

	def no_of_rating(self):
		ratings = Rating.objects.filter(GrapherName=self)
		return len(ratings)

	def avg_rating(self):
		sum =0
		ratings = Rating.objects.filter(GrapherName=self)
		for rat in ratings:
			sum +=rat.Stars
		if len(ratings)>0:
			return sum/len(ratings)
		else:
			return 0


	def __str__(self):
		return self.GrapherName

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	Address = models.TextField(max_length=256,blank=True)
	Pin_Code = models.CharField(max_length=36,blank=True)
	ShootPurpose = models.CharField(max_length=50,blank=True)
	Loc_of_shoot = models.CharField(max_length=256,blank=True)
	setLocation = models.CharField(max_length=256,blank=True)
	Payment_Status = models.CharField(max_length=50,blank=True,default="NotStarted")
	DateOfShoot = models.CharField(max_length=36)
	BookDate = models.CharField(max_length=36)
	PickGrapher = models.CharField(max_length=36,blank=True)



class Rating(models.Model):
	GrapherName = models.ForeignKey(Photographers,on_delete=models.CASCADE)
	User = models.ForeignKey(User,on_delete=models.CASCADE)
	Stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
	Comments=models.CharField(max_length=255, blank=True)

	class Meta:
		unique_together = (('GrapherName','User'),)
		index_together = (('GrapherName','User'),)

	


