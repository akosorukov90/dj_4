from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.name}"
