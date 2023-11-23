from django.test import TestCase
from restaurant.models import MenuItem,Booking

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Lemon Cheese Cake", price=10.00, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "Lemon Cheese Cake : 10.00")