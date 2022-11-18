from django.db import models
from registration.models import Registration
# Create your models here.
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=50)
    date = models.DateField()
    rating = models.CharField(max_length=10)
    # reg_id = models.IntegerField()
    reg=models.ForeignKey(Registration,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'feedback'