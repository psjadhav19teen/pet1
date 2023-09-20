from django.contrib import admin

# Register your models here.
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display=("image","name","species","gender","breed","age","description")

    

admin.site.register(Pet,PetAdmin)