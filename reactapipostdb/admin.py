from django.contrib import admin
from .models import infomodel
from .views import infoviewset
# Register your models here.


admin.site.register(infomodel)