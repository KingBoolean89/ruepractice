from django.db import models

class Product(models.Model):

    po = models.CharField(primary_key=True, max_length=100)
    item = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField()
    qty = models.IntegerField()

def __str__(self):
    return 'Item: {0} Color: {1} Size: {2} Description: {3} QTY: {4}'.format(
        self.item,
        self.color,
        self.size,
        self.description,
        self.qty
    )


