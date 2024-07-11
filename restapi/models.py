import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from datetime import timedelta

def validator_password_length(value):
    if len(value) < 8:
        raise ValidationError('Password must be at least 8 characters long.')

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(unique=True, max_length=500)
    phone_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # Adjusted for hashed passwords

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return str(self.public_id)
    


class Image(models.Model):
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')



class PurifierModel(models.Model):
    public_id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    model_name=models.CharField(max_length=500)
    image = models.ImageField(upload_to='photos/profile_images/')



class PurifierDetails(models.Model):
    public_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    purifiermodel_id=models.ForeignKey(PurifierModel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/purifier_images/')
    price = models.FloatField(default=0.0)
    capacity=models.TextField()
    color=models.CharField(max_length=500)
    purification_features=models.TextField()
    installation_type=models.CharField(max_length=500)
    filtration_capacity=models.CharField(max_length=500)
    power_requirement=models.CharField(max_length=500)
    purification_technology=models.CharField(max_length=600)
    width=models.CharField(max_length=300)
    height=models.CharField(max_length=300)
    depth=models.CharField(max_length=300)
    weight=models.CharField(max_length=300)
    warranty_summary=models.CharField(max_length=500)
    warranty_service_type=models.CharField(max_length=500)
    domestic_warranty=models.CharField(max_length=600)



class Feedback(models.Model):
    public_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    Image=models.ImageField(upload_to='photos/feedback_images/',default=None)
    feedback=models.TextField()
    rating=models.IntegerField()



class Address(models.Model):
    public_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255,default="none")
    phone_number = models.CharField(max_length=15,default="none")
    building_name = models.TextField()
    area = models.TextField()
    nearby = models.TextField()
    city = models.TextField()
    state = models.TextField()
    pincode = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        # Ensure full_name and phone_number are set from the related User instance
        self.full_name = f"{self.user_id.first_name} {self.user_id.last_name}"
        self.phone_number = self.user_id.phone_number
        super(Address, self).save(*args, **kwargs)
   
class Servicing(models.Model):
    public_id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=250,default="none")
    phone_number=models.CharField(max_length=15,default="none")
    Problem=models.TextField()
    images=models.ImageField(upload_to='photos/Issues_images/')
    status=models.CharField(max_length=100,default='Pending')
    def save(self, *args, **kwargs):
        # Ensure full_name and phone_number are set from the related User instance
        self.full_name = f"{self.user_id.first_name} {self.user_id.last_name}"
        self.phone_number = self.user_id.phone_number
        super(Servicing, self).save(*args, **kwargs)
   


class Billing(models.Model):
    public_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='billing')
    purifierdetails_id=models.ForeignKey(PurifierDetails,on_delete=models.CASCADE)
    data=models.DateField(auto_now_add=True)
    warranty_lastdate=models.DateField(default=timezone.now().date() + timedelta(days=365))
    cost=models.FloatField(default=0.0)
    CGST=models.FloatField(default=0.0)
    SGST=models.FloatField(default=0.0)
    total=models.FloatField(default=0.0)
    def save(self,*args,**kwargs):
        self.cost=self.purifierdetails_id.price
        self.CGST = self.cost * (self.CGST / 100)
        self.SGST = self.cost * (self.SGST / 100)
        self.total = self.cost + self.CGST + self.SGST
        super(Billing, self).save(*args, **kwargs)
