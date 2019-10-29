from django.db import models
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    number_of_login = models.IntegerField()

    class Meta:
        db_table = "personmodel"

    def __str__(self):
        return self.first_name + self.last_name

# Create your models here.
