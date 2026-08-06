from django.test import TestCase

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(
            title="Ice Cream",
            price=80,
            inventory=100,
        )
        MenuItem.objects.create(
            title="Greek Salad",
            price=12,
            inventory=50,
        )
        MenuItem.objects.create(
            title="Bruschetta",
            price=10,
            inventory=40,
        )

    def test_getall(self):
        # get data from api
        response = self.client.get("/api/menu-items/")

        # get data directly from test db & serialize it
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        # check if api view shows correct data from test db
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)