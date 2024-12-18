from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SQLQuery(models.Model):
    yes_no_choices = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    sql_text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_queries')
    add_filter = models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add a timestamp for creation
    
    def __str__(self):
        return self.name

class UserQueryAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.ForeignKey(SQLQuery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Add auto_now_add

    def __str__(self):
        return f"{self.user.username} - {self.query.name}"
