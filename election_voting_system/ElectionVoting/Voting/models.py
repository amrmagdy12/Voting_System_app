from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin , User
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from datetime import datetime

from .managers import VoterManager


class Region(models.Model): 
    class Governorates(TextChoices):
        ELSHARQIYAH = "ELSHARQIYAH" , "el Sharqiyah"
        CAIRO = "CAIRO" , "Cairo"
        GIZA = "GIZA" , "Giza"
        ELMENYA = "ELMENYA " , "el Menya"

    class Countries(TextChoices):
        EGYPT = "EGYPT" , "Egypt"
        QATAR = "QATAR" , "Qatar"
        LIBYA = "LIBYA" , "Libya"

    country = models.CharField(max_length=20 ,choices = Countries.choices , blank= False)
    region = models.CharField(max_length=30 , choices = Governorates.choices , primary_key=True ,unique = True)


class Voter(AbstractBaseUser , PermissionsMixin) :
     first_name = models.CharField(max_length=20,verbose_name="First Name" , blank=False)
     last_name = models.CharField(max_length=20,verbose_name="Last Name")
     personal_id = models.CharField(max_length=14 , verbose_name="P.id" ,unique = True)
     region = models.ForeignKey(Region , on_delete=models.CASCADE)   
     password = models.CharField(max_length=5 , verbose_name= "vote key" ,unique=True) 
     is_staff = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)
     is_superuser = models.BooleanField(default=False) 
     USERNAME_FIELD = 'personal_id'
     REQUIRED_FIELDS = ['password' , 'region']   
                                
     objects = VoterManager()   

#-------------------------------------------------
class Election(models.Model): 
    election_name = models.CharField(max_length=40 ,unique = True , blank  = False)
    region = models.ForeignKey(Region ,on_delete= models.CASCADE)

class Candidate(models.Model) :

    class Symbols(models.TextChoices):
        BOOK = "BOOK" , "Book"
        CHAIR = "CHAIR" , "Chair"
        ROCKET = "ROCKET" , "Rocket"
        TREE = "TREE" , "Tree"

    name = models.CharField(max_length= 30 , blank = False)
    id = models.CharField(max_length=8 , primary_key=True ,verbose_name="ID")
    description = models.CharField(max_length = 200 , default=" I'am a proffesional and trustful , Hope i suites u")
    symbol = models.CharField(max_length=15 ,choices= Symbols.choices ,blank= False, unique = True)   
    mobile = models.CharField(max_length=12 , serialize= False , blank= True ,unique= True)
    election = models.ForeignKey(Election ,on_delete=CASCADE)



class Voting_on (models.Model) :
    voter = models.ForeignKey(Voter , on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate , on_delete = models.CASCADE)
    election  = models.ForeignKey(Election , on_delete=models.CASCADE)
    date = models.DateTimeField(default = datetime.now() , blank=True)
