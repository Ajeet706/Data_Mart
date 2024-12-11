# queryapp/models.py
from django.db import models

class SQLQuery(models.Model):
    yes_no_choices=[
        (True,'Yes'),
        (False,'No'),
    ]
    name = models.CharField(max_length=255)          # Name of the query
    description = models.TextField(blank=True, null=True)  # Optional description
    sql_text = models.TextField()                    # SQL query to be executed
    # Excel_upload = models.BooleanField(choices=yes_no_choices,default=True)
    # Date_Filter = models.BooleanField(choices=yes_no_choices,default=True)
    # Both_Filter = models.BooleanField(choices=yes_no_choices,default=True)
    Add_filter=models.BooleanField(choices=yes_no_choices,default=True)
    def __str__(self):
        return self.name


# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)
#     office = models.CharField(max_length=100)
#     age = models.IntegerField()
#     start_date = models.DateField()
#     salary = models.CharField(max_length=20)
#     extra_info = models.TextField()

#     def __str__(self):
#         return self.name
