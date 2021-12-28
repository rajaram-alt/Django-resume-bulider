from django.db import models

# Create your models here

class temp4model(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    degree=models.CharField(max_length=100)
    propoint_1=models.CharField(max_length=200)
    propoint_2=models.CharField(max_length=200)
    propoint_3=models.CharField(max_length=200,blank=True)
    propoint_4=models.CharField(max_length=200,blank=True)
    lang_1=models.CharField(max_length=20)
    lang_2=models.CharField(max_length=20,blank=True)
    lang_3=models.CharField(max_length=20,blank=True)
    Address=models.CharField(max_length=200)
    Date_of_birth=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mobileno=models.IntegerField()
    email=models.EmailField()
    course_1=models.CharField(max_length=50)
    school_1=models.CharField(max_length=200)
    percent_1=models.CharField(max_length=50)
    year_1=models.CharField(max_length=50)
    course_2=models.CharField(max_length=50)
    school_2=models.CharField(max_length=200)
    percent_2=models.CharField(max_length=50)
    year_2=models.CharField(max_length=50)
    course_3=models.CharField(max_length=50)
    college=models.CharField(max_length=200)
    percent_3=models.CharField(max_length=50)
    year_3=models.CharField(max_length=50)
    skill_1=models.CharField(max_length=100,blank=True)
    skill_2=models.CharField(max_length=100,blank=True)
    skill_3=models.CharField(max_length=100,blank=True)
    skill_4=models.CharField(max_length=100,blank=True)
    skill_5=models.CharField(max_length=100,blank=True)
    hobby_1=models.CharField(max_length=100)
    hobby_2=models.CharField(max_length=100,blank=True)
    hobby_3=models.CharField(max_length=100,blank=True)
    intern_1=models.CharField(max_length=100,blank=True)
    intern_2=models.CharField(max_length=100,blank=True)
    declare=models.CharField(max_length=500)

    def __str__(self):
        return self.name



