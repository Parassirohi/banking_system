from django.db import models


class PublicBank(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Banks'
        db_table = 'banks'

    def __str__(self):
        return self.name


class Branch(models.Model):
    ifsc = models.CharField(max_length=255, primary_key=True, unique=True)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank = models.ForeignKey(PublicBank, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Branches'
        db_table = 'branches'


