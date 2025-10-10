from django.contrib import admin
from .models import Cultivo, Zona, Plaga, FichaTecnica
# Register your models here.

admin.site.register(Cultivo)
admin.site.register(Zona)
admin.site.register(Plaga)
admin.site.register(FichaTecnica)