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
    # path('apply-filters/', views.apply_filters, name='apply_filters'),  # URL for applying filters
    path('download-excel/', views.download_excel, name='download_excel'),
    # path('download_filtered/<str:filename>/', views.download_filtered_file, name='download_filtered_file'),
    path('upload_page/', views.upload_excel, name='upload_excel'),

    
]
