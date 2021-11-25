from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250) #department of worker
    work_number = models.CharField(max_length=250) #this allows for codes that can be used to identify workers from same department

    def __str__(self) -> str:
        return f"{self.name} {self.designation}"


class Item(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} -> N{self.cost}"