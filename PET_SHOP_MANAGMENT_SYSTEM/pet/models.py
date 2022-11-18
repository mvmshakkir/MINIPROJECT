from django.db import models

# Create your models here.
class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=25)
    pet_type = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    age = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pet'




