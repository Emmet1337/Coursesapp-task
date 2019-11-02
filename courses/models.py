from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    imgpath = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.CharField(max_length=100)


class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')


class Contact(models.Model):
    CONTACT_TYPES = ((1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL'))
    type = models.CharField(choices=CONTACT_TYPES, max_length=10)
    value = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
