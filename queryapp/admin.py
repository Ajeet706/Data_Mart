# queryapp/admin.py
from django.contrib import admin
from .models import SQLQuery , UserQueryAccess

@admin.register(SQLQuery)
class SQLQueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')  # Customize columns shown in admin
    exclude = ('created_by',)  # Hide the created_by field in the admin form

    def save_model(self, request, obj, form, change):
        # Automatically set the created_by field to the logged-in user
        if not obj.pk:  # Check if the object is being created (not updated)
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
        
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Limit the queries shown in the admin to those created by the logged-in user
        if not request.user.is_superuser:
            return qs.filter(created_by=request.user)
        return qs

@admin.register(UserQueryAccess)
class UserQueryAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'query')
    search_fields = ('user__username', 'query__query_name')
    
# Register your models with their corresponding admin classes
# Check if SQLQuery is already registered
if not admin.site.is_registered(SQLQuery):
    admin.site.register(SQLQuery, SQLQueryAdmin)
    admin.site.register(UserQueryAccess, UserQueryAccessAdmin)