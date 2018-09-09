from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name='Test Product')

    def test_creation(self):
        product = Product.objects.get(name='Test Product')
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, 'Test Product')