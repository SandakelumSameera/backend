from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth import get_user_model
from decimal import Decimal
from .helpers import get_timer
from mutagen.mp4 import MP4, MP4StreamInfoError

class Sector(models.Model):
    naem=models.CharField(max_length=255)
    sector_uuid=models.UUIDField(default=uuid.uuid4, unique=True)
    related_course=models.ManyToManyField('Course',blank=True)
    sector_image=models.ImageField(upload_to='sector_image')

    #  /media/sector_image/whaat.png
    def get_image_absolute_url(self):
        return 'http:localhost:8000'+self.sector_image
class Course(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    language=models.CharField(max_length=50)
    course_section=models.ManyToManyField('CourseSection', blank=True)
    comments=models.ManyToManyField('Comment')
    image_url=models.ImageField(upload_to='course_images')
    course_uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)

    def get_brief_description(self):
        return self.description[:100]
    
    def get_enrolled_student(self):
        students=get_user_model().object.filter(paid_courses=self)
        return len(students)
    
    def get_total_lectures(self):
        lectures=0
        for section in self.course_section:
            lectures+=len(section.episodes.all())
        return lectures
    
    def total_course_length(self):
        length=Decimal(0.0)
        for section in self.course_section:
            for episode in section.episodes.all():
                length+=episode.length

        return get_timer(length,type='short')

class CourseSection(models.Model):
    section_title=models.CharField(max_length=255)
    episodes=models.ManyToManyField('Episode',blank=True)

    def total_length(self):
        total=Decimal(0.0)
        for episode in self.episodes.all():
            total+=episode.length

        return get_timer(total,type='min')


class Episode(models.Model):
    title=models.CharField(max_length=255)
    file=models.FileField(upload_to='course_videos')
    length=models.DecimalField(max_digits=10,decimal_places=2)

    def get_video_length(self):
        try:
            video=MP4(self.file)
            return video.info.length
        except MP4StreamInfoError:
            return 0.0
        
    def get_video_length_time(self):
        return get_timer(self.length)
    
    def get_absolute_url(self):
        return 'http://localhost:8000'+self.file
    
    def save(self,*args,**kwargs):
        self.length=self.get_video_length()
        return super().save(*args,**kwargs)

class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)