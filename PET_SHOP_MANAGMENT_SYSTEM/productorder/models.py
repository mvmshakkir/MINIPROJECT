from django.db import models
from product.models import Product

# Create your models here.
# class ProductOrder(models.Model):
#     productorder_id = models.AutoField(primary_key=True)
#     price = models.IntegerField()
#     quantity = models.IntegerField()
#     # product_id = models.IntegerField()
#     product=models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE)
#     reg_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'product_order'
class ProductOrder(models.Model):
    productorder_id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    #product_id = models.IntegerField()
    product=models.ForeignKey(Product,to_field='product_id',on_delete=models.CASCADE)
    reg_id = models.IntegerField()
    status = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'product_order'