from django.contrib import admin

from pet.models import PetInfo, Sex

# Register your models here.
admin.site.register(PetInfo)
admin.site.register(Sex)
