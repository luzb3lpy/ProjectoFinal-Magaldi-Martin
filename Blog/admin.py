from django.contrib import admin
from .models import * # importamos el archivo models
admin.site.register(Familiares)
admin.site.register(Amigos)
admin.site.register(Referidos)


# Register your models here.
