from django.test import TestCase
from snapxPhotography.categories.forms import CategoryBaseForm
from django.core.files.uploadedfile import SimpleUploadedFile


class CategoryBaseFormTest(TestCase):

    def test_valid_category_image(self):
        image = SimpleUploadedFile("test.png", b"file_content", content_type="image/png")
        form_data = {'name': 'Test Category'}
        form_files = {'category_image': image}
        form = CategoryBaseForm(data=form_data, files=form_files)

        self.assertTrue(form.is_valid())

    def test_invalid_category_image(self):
        image = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        form_data = {'name': 'Test Category'}
        form_files = {'category_image': image}
        form = CategoryBaseForm(data=form_data, files=form_files)

        self.assertFalse(form.is_valid())
        self.assertIn('category_image', form.errors)
        self.assertEqual(form.errors['category_image'][0], 'Only .png files are allowed')

    def test_no_category_image(self):
        form_data = {'name': 'Test Category'}
        form = CategoryBaseForm(data=form_data)

        self.assertFalse(form.is_valid())
