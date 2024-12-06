from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from snapxPhotography.categories.models import Category


User = get_user_model()


class CategoryEditPageViewTest(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(username="staffuser", email="staff@abv.bg",
                                                   password="password123", is_staff=True)
        self.non_staff_user = User.objects.create_user(username="nonstaffuser", email="nonstaff@abv.bg",
                                                       password="password123")
        self.category = Category.objects.create(name='Test Category', category_image="http://test/test.png",
                                                created_by=self.non_staff_user)
        self.edit_url = reverse('category-edit', kwargs={'pk': self.category.pk})
        self.client = Client()

    def test_category_edit_view_permission_denied(self):
        self.client.login(email="nonstaff@abv.bg", password="password123")
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 403)

    def test_template_used(self):

        self.client.login(email="staff@abv.bg", password="password123")

        response = self.client.get(self.edit_url)
        self.assertTemplateUsed(response, 'categories/edit_category.html')
