from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, School

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'school')}),
    )
    list_display = ('username', 'email', 'role', 'school', 'is_staff')
    list_filter = ('role', 'school')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
