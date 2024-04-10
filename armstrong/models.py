from django.db import models
from django.contrib.auth.models import User
from  datetime import datetime

# Create your models here.
class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(null=True)  
    from_number = models.IntegerField(null=True) 
    to_number = models.IntegerField(null=True)  
    result = models.CharField(max_length=200,null=True) 
    timestamp = models.DateTimeField(default=datetime.now, blank = True)

   
    def __str__(self) :
        if self.number:
            return f"{self.user}  checked  {self.number}"
        return f"{self.user}  checked   {self.from_number}  AND {self.to_number}"
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    phone_number = models.IntegerField(null=True)
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username
    
class Feedback(models.Model):
    user = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    subject = models.CharField(max_length=200,null=True) 
    message  = models.CharField(max_length=200,null=True)
    timestamp = models.DateTimeField(default=datetime.now, blank = True)

   
    def __str__(self) :
        return self.user
        