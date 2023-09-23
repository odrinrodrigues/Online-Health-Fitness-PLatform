from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#####Creating Models

class video_content(models.Model):
    video_id=models.AutoField(primary_key=True,unique=True)
    video_title=models.CharField(max_length=100,default="")
    video_category=models.CharField(max_length=50,default="")
    video_duration=models.IntegerField(default=0)
    calorie=models.CharField(max_length=40,default=0)
    w_equipment=models.CharField(max_length=60,default="")
    w_difficulty=models.CharField(max_length=60,default="")
    training_type=models.CharField(max_length=50,default="")
    youtube_link=models.CharField(max_length=200,default="")
    embed_link=models.CharField(max_length=300,default="")
    thumbnail=models.ImageField(upload_to="image/thumbnail",default="")
    video_summary=models.TextField(default="")

    def __str__(self):
        return  self.video_title

        # ##Recipe Model
class Eat_better(models.Model):
    recipe_id=models.AutoField(primary_key=True,unique=True)
    recipe_title=models.CharField(max_length=100,default="")
    recipe_category=models.CharField(max_length=50,default="")
    recipe_dietary_type=models.CharField(max_length=50,default="")
    recipe_serves=models.IntegerField(default=0)
    recipe_prep_time=models.IntegerField(default=0)
    recipe_make_time=models.IntegerField(default=0)
    recipe_calorie=models.CharField(max_length=40,default=0)
    recipe_difficulty=models.CharField(max_length=60,default="")
    recipe_ingredients=models.CharField(max_length=255,default="")
    recipe_steps=models.TextField(default="")
    recipe_infos=models.TextField(default="")
    thumbnail=models.ImageField(upload_to="image/thumbnail",default="")

    def __str__(self):
        return  self.recipe_title