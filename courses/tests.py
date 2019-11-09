from django.test import TestCase

# Create your tests here.

from courses.models import Category
from courses.models import Course
from courses.models import Branch
from courses.models import Contact


class TestModels(TestCase):

    def test_course(self):
        category = Category.objects.create(
            name='Gaming',
            imgpath='BoomBamBapBarabaBoomPau'
        )
        course = Course.objects.create(
            name='Cooking',
            description='2number9number9largenumber6withextradeep2number45onewithcheese',
            category=category,
            logo='ddos.png',
        )
        branch = Branch.objects.create(
            latitude='453534535434534543',
            longitude='23424234234252352352',
            address='ul Svyazistov 10 kv 150',
            course=course
        )
        contact = Contact.objects.create(
            type='FACEBOOK',
            value='dragosteadintei',
            course=course,
        )

        self.assertEqual(category.imgpath, 'BoomBamBapBarabaBoomPau')
        self.assertEqual(course.description, '2number9number9largenumber6withextradeep2number45onewithcheese')
        self.assertEqual(course.logo, 'ddos.png')
        self.assertEqual(branch.address, 'ul Svyazistov 10 kv 150')
        self.assertEqual(branch.longitude, '23424234234252352352')
        self.assertEqual(branch.latitude, '453534535434534543')
        self.assertEqual(contact.value, 'dragosteadintei')
        self.assertEqual(contact.type, 'FACEBOOK')
