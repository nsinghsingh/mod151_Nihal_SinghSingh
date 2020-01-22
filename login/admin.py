from django.contrib import admin
from login.models import User


class AllUser(admin.ModelAdmin):
    list_display = ('username', 'password')
    search_fields = ('username', 'password')


admin.site.register(User, AllUser)


