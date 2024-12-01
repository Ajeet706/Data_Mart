# queryapp/admin.py
from django.contrib import admin
from .models import SQLQuery

@admin.register(SQLQuery)
class SQLQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','Add_filter')
    search_fields = ('name', 'description')
    ordering = ('name',)
