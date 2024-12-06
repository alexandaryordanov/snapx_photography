from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class CategoryAddPageViewTest(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(username="staffuser", email="staff@abv.bg",
                                                   password="password123", is_staff=True)
        self.non_staff_user = User.objects.create_user(username="nonstaffuser", email="nonstaff@abv.bg",
                                                       password="password123")
        self.client = Client()
        self.add_category_url = reverse('category-add')

    def test_category_add_view_permission_denied(self):
        self.client.login(email="nonstaff@abv.bg", password="password123")
        response = self.client.get(reverse("category-add"))
        self.assertEqual(response.status_code, 403)

    def test_template_used(self):

        self.client.login(email="staff@abv.bg", password="password123")

        response = self.client.get(self.add_category_url)
        self.assertTemplateUsed(response, 'categories/add_category.html')
