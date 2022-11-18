from django.db import models

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    date = models.DateField()
    price = models.IntegerField()
    card_number = models.IntegerField()
    cardholder_name = models.CharField(max_length=25)
    cvv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'payment'