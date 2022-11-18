from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=25)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'product'
