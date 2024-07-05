from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.

class Carousel(models.Model):
    image = models.ImageField(upload_to='images/carousel',null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    Active_carousel = models.BooleanField(default=False)

class News(models.Model):
    image = models.ImageField(upload_to='images/news', null=True, blank=True)
    description = HTMLField(blank=True, null=True)
    detail = HTMLField(blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    On_homepage = models.BooleanField(default=False)

    def __str__(self):
        return self.description

class Announcement(models.Model):
    image = models.ImageField(upload_to='images/announcement', null=True, blank=True)
    header = models.CharField(max_length=100, null=True, blank=True)
    detail = HTMLField(null=True, blank=True)
    Available = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header

class Principal_Desk(models.Model):
    image = models.ImageField(upload_to='media/announcement', null=True, blank=True)
    header = models.CharField(max_length=100, null=True, blank=True)
    detail = HTMLField(null=True, blank=True)
    Front = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header

class Press_Release(models.Model):
    image = models.ImageField(upload_to='media/announcement', null=True, blank=True)
    header = models.CharField(max_length=100, null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    headlines = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header
    
class Department(models.Model):
    image = models.ImageField(upload_to='media/Department', null=True, blank=True)
    header = models.CharField(max_length=100, null=True, blank=True)
    detail = HTMLField(null=True, blank=True)
    

    def __str__(self):
        return self.header

class lecturerImage(models.Model):
    department = models.ForeignKey(Department, default=None,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/Department', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

class main_department_page(models.Model):
    image = models.ImageField(upload_to='media/Department', null=True, blank=True)
    text1 = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=100, blank=True, null=True)



class Spotlight_staff(models.Model):
    name = models.CharField(max_length=50 ,null=False , blank=False)
    image = models.ImageField(upload_to='media/spstaff', null=True, blank=True)
    detail = models.TextField(null=True, blank= True)
    homepage = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Spotlight_students(models.Model):
    name = models.CharField(max_length=50,null=False , blank=False)
    image = models.ImageField(upload_to='media/spstudents', null=True, blank=True)
    detail = HTMLField(null=True, blank= True)
    homepage = models.BooleanField(default=True)

    def __str__(self):
        return self.name
 
class Spotlight(models.Model):
    name = models.CharField(max_length=50,null=False , blank=False)
    image = models.ImageField(upload_to='media/spotlight', null=True, blank=True)
    category = HTMLField(null=True, blank= True)
    homepage = models.BooleanField(default=True)

    def __str__(self):
        return self.category
 

class Program(models.Model):
    name = models.CharField(max_length=150, null=False,blank=False )
    details = HTMLField( null= False, blank=False)
    category = HTMLField( null=True, blank=True)

    def __str__(self):
        return self.name

class programBrief(models.Model):
    details = HTMLField(null=False, blank=True)



class ResearchDocument(models.Model):
    title = models.CharField(max_length=100)
    category =models.CharField(max_length=100, null= False, blank=False)
    author = models.CharField(max_length=150)
    file = models.FileField(upload_to='documents/')
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Calender(models.Model):
    title = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=150)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title

class History(models.Model):
    header = models.CharField(max_length=100,null=False, blank=True)
    image = models.ImageField(upload_to='media/history')
    detail = HTMLField(blank=False,null=False)

class Purpose(models.Model):
    detail = HTMLField( null=True, blank=True)


class Emblem(models.Model):
    image = models.ImageField(upload_to='media/emblem')
    detail = HTMLField(blank=False,null=False)

class Principal(models.Model):
    header = models.CharField(max_length=100,null=False,blank=True)
    bio = HTMLField(null=True, blank=True)
    
    def __str__(self):
        return self.header

class PrincipalImage(models.Model):
    principal_for = models.ForeignKey(Principal, default=None,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/principal', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)

class Campus(models.Model):
    header = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self): 
        return self.header

class CampusImage(models.Model):
    part = models.ForeignKey(Campus, default=None,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/campus', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    
class Anthem(models.Model):
    header =models.CharField(max_length=100, null=False, blank=False)
    detail = HTMLField(null=False, blank=False)

class SrcCarousel(models.Model):
    image = models.ImageField(upload_to='media/srcCarousel')
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null= True)

    def __str__(self):
        return self.title
    
class SrcAbout(models.Model):
    header = models.CharField(max_length=100, null=False,blank=False)
    detail = HTMLField()

    def __str__(self):
        return self.header
    
class SrcExecutive(models.Model):
    image = models.ImageField(upload_to='media/srcCarousel')
    name = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField( max_length=100,blank=True, null= True)

    def __str__(self):
        return self.name

class SrcBody(models.Model):
    header = models.CharField(max_length=100, blank=False, null=True)
    body = HTMLField()

    def __str__(self):
        return self.header
    
class Accomodation(models.Model):
    image = models.ImageField(upload_to='media/srcCarousel')
    hall_name = models.CharField(max_length=100, blank=True, null=True)
    description = HTMLField(blank=True, null= True)

    def __str__(self):
        return self.hall_name
    
class AccomodationInfo(models.Model):
    image = models.ImageField(upload_to='media/srcCarousel')
    header = models.CharField(max_length=100, blank=True, null=True)
    description = HTMLField(blank=True, null= True)

    def __str__(self):
        return self.header
    