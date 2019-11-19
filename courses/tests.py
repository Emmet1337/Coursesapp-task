from django.test import TestCase

# Create your tests here.

from courses.models import Category
from courses.models import Course
from courses.models import Branch
from courses.models import Contact


class CategoryModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='Gaming',
            imgpath='BoomBamBapBarabaBoomPau',
        )
        course = Course.objects.create(
            name='Cooking',
            description='2number9number9largenumber6withextradeep2number45onewithcheese',
            category=category,
            logo='ddos.png',
        )
        Branch.objects.create(
            latitude='453534535434534543',
            longitude='23424234234252352352',
            address='ul Svyazistov 10 kv 150',
            course=course
        )
        Contact.objects.create(
            type='FACEBOOK',
            value='dragosteadintei',
            course=course,
        )

    def test_category_creation(self):
        category = Category.objects.get(name='Gaming', imgpath='BoomBamBapBarabaBoomPau')
        self.assertEqual(category.name, 'Gaming')
        self.assertEqual(category.imgpath, 'BoomBamBapBarabaBoomPau')

    def test_course_creation(self):
        course = Course.objects.get(name='Cooking', logo='ddos.png')
        self.assertEqual(course.name, 'Cooking')
        self.assertEqual(course.logo, 'ddos.png')

    def test_branch_creation(self):
        branch = Branch.objects.get(latitude='453534535434534543', address='ul Svyazistov 10 kv 150')
        self.assertEqual(branch.address, "ul Svyazistov 10 kv 150")
        self.assertEqual(branch.latitude, "453534535434534543")

    def test_contact_creation(self):
        contact = Contact.objects.get(type='FACEBOOK', value='dragosteadintei',)
        self.assertEqual(contact.value, 'dragosteadintei')
        self.assertEqual(contact.type, 'FACEBOOK')
