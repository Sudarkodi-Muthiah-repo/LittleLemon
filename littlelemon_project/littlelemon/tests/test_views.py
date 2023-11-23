from django.test import TestCase,Client
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        #self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(title="Tomato Pasta", price=5.00, inventory=10)
        self.menu_item2 = MenuItem.objects.create(title="Pepporoni Pizza", price=7.60, inventory=10)

    def loginAsTestUser(self) -> None:
        self.client.login(username='testuser', password='testpassword')

    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu-items') #http://localhost:8000
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

# class MenuItemViewTest(TestCase):
#     def setUp(self) -> None:
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             password='testpassword'
#         )
        
#         self.pizza = MenuItem.objects.create(title='Pizza', price=12.99, inventory=10)
#         self.burger = MenuItem.objects.create(title='Burger', price=8.99, inventory=5)
#         self.pasta = MenuItem.objects.create(title='Pasta', price=15.99, inventory=7)
    
#     def loginAsTestUser(self) -> None:
#         self.client.login(username='testuser', password='testpassword')
    
#     def test_view_authentication(self) -> None:
#         response = self.client.get(reverse('MenuItemsView'))
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#         self.loginAsTestUser()
#         response = self.client.get(reverse('MenuItemsView'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    
#     def test_getall(self):
#         self.loginAsTestUser()
#         response = self.client.get(reverse('MenuItemsView'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        
#         menu = MenuItem.objects.all()
#         serializer = MenuItemSerializer(menu, many=True)
#         self.assertEqual(response.data, serializer.data)