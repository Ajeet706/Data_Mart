# # queryapp/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.query_list, name='query_list'),  # The main view to list queries
#     path('download/<int:query_id>/', views.execute_query_and_download, name='download_query'),
# ]
# queryapp/urls.py
# queryapp/urls.py
# queryapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_list, name='query_list'),  # List of available queries
    path('download/<int:query_id>/', views.execute_query_and_download, name='download_query'),  # Download as Excel
    path('download-excel/', views.download_excel, name='download_excel'),
    path('upload_page/', views.upload_excel, name='upload_excel'),   
    path('view_page/', views.view_page, name='view_page'),   

]
