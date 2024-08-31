from rest_framework.serializer import ModelSerializer, Serializer
from .models import Course
from users.serializers import UserSerializer

class CourseDisplaySerializer(ModelSerializer):
    student_no=Serializer.IntegerField(sourse='get_enrolled_student')
    author=UserSerializer()

    class Meta:
        model=Course
        fields=[
            'course_uuid',
            'title',
            'student_no',
            'author',
            'price',
            'image_url',
        ]