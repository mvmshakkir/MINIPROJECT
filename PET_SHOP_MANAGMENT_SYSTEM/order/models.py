from django.db import models
from pet.models import Pet

# Create your models here.
class PetOrder(models.Model):
    petorder_id = models.AutoField(primary_key=True)
    # pet_id = models.IntegerField()
    pet=models.ForeignKey(Pet,to_field='pet_id',on_delete=models.CASCADE )
    image = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    reg_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet_order'

