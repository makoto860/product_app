from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    sell_datetime = models.DateTimeField()
    caption = models.TextField()

    class Meta:
        managed = False
        db_table = 'products'

    def __str__(self):
        return self.name
