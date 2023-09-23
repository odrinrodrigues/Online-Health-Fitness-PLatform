from django.contrib import admin

# Register your models here.
from .models import video_content,Eat_better

admin.site.register(video_content),
admin.site.register(Eat_better)

