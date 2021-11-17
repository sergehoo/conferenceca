from django.contrib import admin
from ca.models import Donateur, Cathegorie , Mensualite, Promesse_dons,Dons
from django.contrib.auth.admin import UserAdmin
#from ca.models import CustomUser

# Register your models here.

admin.site.register(Donateur)
admin.site.register(Cathegorie)
admin.site.register(Mensualite)
admin.site.register(Promesse_dons)
admin.site.register(Dons)


# class CustomUserAdmin(UserAdmin):
#     model=CustomUser
#     list_display=["username", "email", "is_staff"]
    
    
# admin.site.register(CustomUser, CustomUserAdmin)