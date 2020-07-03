from django.db import models

# Create your models here.
class Detail(models.Model):
    Name = models.CharField(max_length=100)
    First_name = models.CharField(max_length=50,default="")
    Last_name = models.CharField(max_length=50,default="")
    Aadhar_number = models.IntegerField(blank=False)
    Email_Address = models.EmailField(default="")
    Contact_Number = models.PositiveIntegerField()


    def __str__(self):
        return self.Name
