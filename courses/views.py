from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework import generics


class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()