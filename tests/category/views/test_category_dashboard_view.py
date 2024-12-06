from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from snapxPhotography.categories.models import Category


class CategoryDashboardViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        self.categories = [
            Category.objects.create(
                name=f"Category {i}",
                category_image=f"http://image{i}.png",
                created_by=self.user
            )
            for i in range(10)
        ]

    def test_category_dashboard_view_status_code(self):
        response = self.client.get(reverse('category-dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse('category-dashboard'))
        self.assertTemplateUsed(response, 'categories/dashboard_category.html')

    def test_pagination(self):
        response = self.client.get(reverse('category-dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 4)

    def test_second_page_pagination(self):
        response = self.client.get(reverse('category-dashboard') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 4)

    def test_last_page_pagination(self):
        response = self.client.get(reverse('category-dashboard') + '?page=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 2)

    def test_empty_page(self):
        response = self.client.get(reverse('category-dashboard') + '?page=999')
        self.assertEqual(response.status_code, 404)