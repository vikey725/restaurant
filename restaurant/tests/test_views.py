from django.test import TestCase 
from restaurantAPI.models import Menu
from restaurantAPI.serializers import MenuSerializer

class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        menu = Menu.objects.create(
            title='IceCream', price=80, inventory=100
        )
        menu.save()
        menu = Menu.objects.create(
            title='Chocolate', price=100, inventory=100
        )
        menu.save()

    def test_getall(self):
        items = Menu.objects.all()
        self.assertEquals(str(items[0]), 'IceCream : 80.00')
        self.assertEquals(str(items[1]), 'Chocolate : 100.00')

