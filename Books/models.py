from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime    

# Create your models here.

class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    image = models.ImageField(upload_to='Users/Images/', blank=True)


"""
class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    image = models.ImageField(upload_to='Users/Images/', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""

categories = [ ('Open Source' , 'Open Source' ), ('Mobile' , 'Mobile'), ('Java' , 'Java') , ('Software Engineering' , 'Software Engineering'), ( 'Internet' , 'Internet') ,( 'Web Development' , 'Web Development') ,( 'Miscellaneous' , 'Miscellaneous') , ('Microsoft .NET' , 'Microsoft .NET') , ('Object-Oriented Programming' ,  'Object-Oriented Programming' ), ( 'Networking' , 'Networking' ) ,('Theory', 'Theory') , ('Programming', 'Programming') , ('Python', 'Python') , ('PowerBuilder' , 'PowerBuilder' ) , ('Computer Graphics' , 'Computer Graphics' ) , ( 'Mobile Technology' , 'Mobile Technology' ) , ('Business' , 'Business' ) , ('Microsoft' , 'Microsoft') , ('P' , 'P') , ('XML' , 'XML') , ('Perl' , 'Perl') , ('Client-Server' , 'Client-Server')]

stations_temp = [
    'Tel Aviv - Savidor Center',
    'Tel Aviv - University',
    'Tel Aviv - Ha-Shalom',
    'Tel Aviv - Ha-Hagana',
    'Nahariya',
    'Akko',
    'Karmiel',
    'Ahihod',
    'Kiryat Motskin',
    'Kiryat Haim',
    'Haifa - Hutsot HaMifrats',
    'Haifa - Merkazit HaMifrats',
    'Haifa - Merkaz Hashmuna',
    'Haifa - Bat Galim',
    'Haifa - Hof Hakarmel',
    'Beit Sheaan',
    'Afula',
    'Migdal HaEmek',
    'Yofneaam',
    'Atlit',
    'Binayamina',
    'Keysaria - Pardes Hana',
    'Hedera West',
    'Netanya',
    'Netanya - Sapir',
    'Beit Yehushua',
    'Herzliya',
    'Petah Tikva - Kiryat Arye',
    'Petah Tikva - Sgula',
    'Rosh HaAin North',
    'Kfar Saba - Nordaoo',
    'Hod HaSharon - Sokolov',
    'Raanana South',
    'Airport Ben Gurion',
    "Modi'in outskirts",
    "Modi'in Center",
    'Jerusalem - Yizhak Navon',
    'Kfar Habad',
    'Lud - Ganei Aviv',
    'Lud/Ramla',
    'Beit Shemesh',
    'Jesrualem - Tanahi Zoo',
    'Jerusalem - Malha',
    'Mazkeret Batia',
    'Kiryat Malachi - Yoav',
    'Kiryat Gat',
    "Lehavim/Raha'at",
    "Be'er Sheva North - University",
    "Be'er Sheva Center",
    'Dimona',
    'Ofakim',
    'Netivot',
    'Sderot',
    'Ashkelon',
    'Asdod - Ad Halom',
    'Yavne - West',
    'Yavne - East',
    "Be'er Yakov",
    'Rishon Letsiyon - HaRishonim',
    'Rishon Letsiyon - Moshe Dayan',
    'Bat Yam - HaKomemiyut',
    'Bat Yam - Yoseftal',
    'Holon Junction'
]

stations = []

for s in stations_temp:
    new_tup = (s , s)
    stations.append(new_tup)

class Book(models.Model):
    
 

    ISBN13 = models.CharField(max_length=13 , primary_key=True)
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    gener = models.CharField(max_length=100 , choices=categories , default="")
    page_count = models.IntegerField(null=True)   
    image = models.ImageField(upload_to='Books/Images')
    imageURL = models.URLField(blank=True)
    language = models.CharField(max_length=20)
    description = models.CharField(max_length=2000 , default="")
    cover_type = models.CharField(max_length = 20 , choices=[( 'Hard' ,'Hard'), ( 'Soft' , 'Soft')], default='Hard')
   



class BookStationRelation(models.Model):
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.CharField(max_length=100 , choices=stations , default='Tel Aviv - Savidor Center')

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.IntegerField()
    order_date=models.DateTimeField(default=datetime.now, blank=True)
    returned=models.BooleanField(default=False)

class AddBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ISBN13 = models.ForeignKey(Book , on_delete=models.CASCADE)
    station = models.IntegerField()
    condition = models.CharField( max_length = 20 ,choices=[('Like New' ,'Like New'), ( 'Used' ,'Used'), ( 'Collectible' , 'Collectible')], default='LikeNew')








