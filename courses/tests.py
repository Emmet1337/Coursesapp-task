from django.test import TestCase

# Create your tests here.

from courses.models import Category
from courses.models import Course
from courses.models import Branch
from courses.models import Contact


class CategoryModelTest(TestCase):
    def create_category(self):
        return Category.objects.create(
            name='Gaming',
            imgpath='BoomBamBapBarabaBoomPau',
        )

    def test_category_creation(self):
        category = self.create_category()
        self.assertEqual(category.name, 'Gaming')


class CourseModelTest(TestCase):
    def create_course(self):
        category = Category.objects.create(
            name='Gaming',
            imgpath='BoomBamBapBarabaBoomPau',
        )
        return Course.objects.create(
            name='Cooking',
            description='2number9number9largenumber6withextradeep2number45onewithcheese',
            category=category,
            logo='ddos.png',
        )

    def test_course_creation(self):
        course = self.create_course()
        self.assertEqual(course.logo, "ddos.png")


class BranchModelTest(TestCase):
    def create_branch(self):
        course = CourseModelTest.create_course(self)
        return Branch.objects.create(
            latitude='453534535434534543',
            longitude='23424234234252352352',
            address='ul Svyazistov 10 kv 150',
            course=course
        )

    def test_branch_creation(self):
        branch = self.create_branch()
        self.assertEqual(branch.address, "ul Svyazistov 10 kv 150")


class ContactModelTest(TestCase):
    def create_contact(self):
        course = CourseModelTest.create_course(self)
        return Contact.objects.create(
            type='FACEBOOK',
            value='dragosteadintei',
            course=course,
        )

    def test_contact_creation(self):
        contact = self.create_contact()
        self.assertEqual(contact.value, 'dragosteadintei')
