from django.db import models

# Create your models here.


class Master_Data(models.Model):
    roll_no = models.IntegerField(null=False)
    name = models.CharField(max_length=50, null=False)
    email1 = models.EmailField(null=False)
    class_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return str(self.roll_no)
