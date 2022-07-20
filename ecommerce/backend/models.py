from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,User
# Create your models here.


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None,is_superuser=False,  is_staff=False, is_active=True,**fields):
#         if not email:
#             raise ValueError("User must have an email")
#         if not password:
#             raise ValueError("User must have a password")

#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.set_password(password)  # change password to hash
#         # user.profile_picture = profile_picture
   

#         user.staff = is_staff
#         user.active = is_active
#         user.is_superuser = is_superuser
#         user.save(using=self._db,**fields)
#         return user

#     def create_staffuser(self, email,  password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True,
#         )
#         return user

#     def create_superuser(self, email,  password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True,
#             is_superuser=True,
#         )
#         user.is_superuser = True
#         user.is_staff=True
#         user.save()
#         return user

# class User(AbstractUser):
#     username = None
#     email = models.EmailField(blank=True,null=True,unique=True,max_length=200)
#     phone_number = models.CharField(max_length=200,blank=True,null=True)
#     user_type = models.CharField(max_length=20,choices=USER_TYPE_CHOICES,default="User")
#     address = models.CharField(max_length=200,blank=True,null=True)
#     otp = models.IntegerField(blank=True,null=True)
#     web_url = models.CharField(max_length=300,blank=True,null=True)
#     created_by = models.ForeignKey('User',on_delete=models.CASCADE,null=True,blank=True)
#     company_name = models.CharField(max_length=200,blank=True,null=True)
#     support_no = models.CharField(max_length=200,blank=True,null=True)
#     creation_type = models.CharField(max_length=20,choices=USER_CREATION_CHOICES,default="Celetel")
#     creation_id = models.CharField(max_length=400,blank=True,null=True)
#     otp_verified = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     objects = UserManager()

#     def __str__(self):
#         return f"{self.email}"

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=True,null=True)
    gender = models.CharField(max_length=20,blank=True,null=True)
    phone_no = models.IntegerField(default=0)


class Product(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(null=True, blank=True)
    discription = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    totalAmount = models.FloatField(default=0.0)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    address = models.CharField(max_length=100,blank=True,null=True)


class UserProfile(models.Model):
    """
    User Profile Details
    """
    USER_ROLE = (
        ('AD', 'Admin'),
        ('USR', 'User'),
    )

    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE, primary_key=True)
    employeeRole = models.CharField(max_length=6, choices=USER_ROLE)

