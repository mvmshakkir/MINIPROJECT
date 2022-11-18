from django.db import models

# Create your models here.
class Registration(models.Model):
    reg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    conform_password = models.CharField(max_length=8)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    place = models.CharField(max_length=25)
    post = models.CharField(max_length=25)
    pin = models.IntegerField()
    phone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'registration'
