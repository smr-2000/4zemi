from django.contrib import admin
from .models import login
from .models import hobby
from .models import UserDetail

admin.site.register(login)
admin.site.register(hobby)
admin.site.register(UserDetail)
