from django.contrib import admin
from .models import authenticate
from .models import *

# Register your models here.

admin.site.register(authenticate)
admin.site.register(Customer)