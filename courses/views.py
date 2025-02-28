from rest_framework.response import Response
from courses.models import Sector

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CourseDisplaySerializer


class CoursesHomeView(APIView):

    def get(self,request,*args,**kwargs):
        sectors=Sector.object.order_by("?")[:6]

        sector_response=[]

        for sector in sectors:
            sector_courses=sector.related_courses.order_by("?")[:4]
            course_Serializer=CourseDisplaySerializer(sector_courses,many=True)

            sector_obj={
                'sector_name':sector.name,
                'sector_uuid':sector.sector_uuid,
                'featured_course':course_Serializer.data,
                'sector_image':sector.get_image_absolute_url
            }

            sector_response.append(sector_obj)
        
        return Response(data=sector_response,status=status.HTTP_200_OK)