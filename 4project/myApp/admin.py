from django.contrib import admin
from .models import login
from .models import hobby
from .models import UserDetail
from .models import personal
from .models import question
from .models import Heart

admin.site.register(login)
admin.site.register(hobby)
admin.site.register(UserDetail)
admin.site.register(personal)
admin.site.register(question)
admin.site.register(Heart)
