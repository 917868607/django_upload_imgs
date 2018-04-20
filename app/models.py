from django.db import models

# Create your models here.


class Uploat_imags(models.Model):
    img_src = models.ImageField(upload_to='%Y/%m')
    img_name = models.CharField(max_length=50)
    class Meta():
        db_table = 'img'
