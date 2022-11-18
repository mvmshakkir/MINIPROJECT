from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=8)
    reg_id = models.IntegerField()
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'login'