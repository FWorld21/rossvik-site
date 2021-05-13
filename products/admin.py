from django.contrib import admin
from admin_interface.models import Theme
from django.contrib.auth.models import Group, User
from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Theme)

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Product)
