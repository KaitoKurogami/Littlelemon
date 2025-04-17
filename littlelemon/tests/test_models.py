from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    
    def setUp(self):
        Menu.objects.create(title="IceCreamDeluxe", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=10, inventory=20)
        Menu.objects.create(title="Lemonade", price=2, inventory=200)

    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        #obtenido por el metodo __str__:
        self.assertEqual(str(item),"IceCream : 80")

    def test_getall(self):
        iceCream = Menu.objects.get(title="IceCreamDeluxe")
        pizza = Menu.objects.get(title="Pizza")
        lemonade = Menu.objects.get(title="Lemonade")
        
        self.assertEqual(str(iceCream),"IceCreamDeluxe : 80.00")
        self.assertEqual(str(pizza),"Pizza : 10.00")
        self.assertEqual(str(lemonade),"Lemonade : 2.00")
