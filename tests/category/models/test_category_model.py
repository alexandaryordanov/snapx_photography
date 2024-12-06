from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from snapxPhotography.categories.models import Category
from snapxPhotography.contests.models import Contest
from datetime import timedelta


class CategoryModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', email='testuser@example.com', password='testpassword'
        )

        self.category = Category.objects.create(
            name="Test Category",
            category_image="http://test/test.png",
            created_by=self.user
        )

        self.contest_open = Contest.objects.create(
            name="Test Contest",
            award=3000,
            requirements="test requirements",

            category=self.category,
            deadline=timezone.now() + timedelta(days=1),
            created_by=self.user,
        )

        self.contest_closed = Contest.objects.create(
            name="Test Contest2",
            award=3000,
            requirements="test requirements",

            category=self.category,
            deadline=timezone.now() - timedelta(days=1),
            created_by=self.user,
        )

    def test_category_creation(self):
        # Test if the Category is created correctly
        self.assertEqual(self.category.name, 'Test Category')
        self.assertEqual(self.category.category_image, 'http://test/test.png')
        self.assertEqual(self.category.created_by, self.user)

    def test_contests_open_property(self):
        self.assertEqual(self.category.contests_open, 1)

        self.contest_closed.deadline = timezone.now() + timedelta(days=1)
        self.contest_closed.save()

        self.assertEqual(self.category.contests_open, 2)

    def test_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_category_image_field(self):
        self.category.category_image = 'http://test/test.png'
        self.assertEqual(self.category.category_image, 'http://test/test.png')

    def test_category_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, 'Categories')
