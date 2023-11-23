from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    Noofguests = models.IntegerField(6)
    BookingDate = models.DateTimeField()

    def __str__(self):
        return self.Name

# class Menu(models.Model):
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=6,decimal_places=2)
#     menu_item_description =models.TextField(max_length=1000,default='')
    
#     def __str__(self):
#         return f'{self.title} : {str(self.price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {self.price:.2f}'