from django.db import models

# Create your models here.

class Sex(models.Model):
    M = "M"
    F = "F"

    GENDER_CHOICES = (
        (M, 'Male'),
        (F, 'Female')
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    class Meta:
        verbose_name = 'sex'
        verbose_name_plural = 'Sex'

    def __str__(self):
        return self.gender


class PetInfo(models.Model):
    pet_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=150)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    age_in_months = models.IntegerField()
    image = models.ImageField(upload_to='photos/pet')
    color = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    country_of_origin = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'petinfo'
        verbose_name_plural = 'petinfo'


    def __str__(self):
        return self.pet_name
