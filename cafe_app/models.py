from django.db import models

# Create your models here.
class Menu(models.Model):
    itemname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stockavailabliti=models.CharField(max_length=50)
    # image = models.ImageField(upload_to='menu_images/')
    
    def __str__(self):
        return self.itemname
    
class ItemImg(models.Model):
    image = models.ImageField(upload_to='images')
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item.itemname} - {self.image.name}'