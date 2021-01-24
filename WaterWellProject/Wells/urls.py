from django.urls import path
from . import views

app_name = 'Wells'

urlpatterns = [
    path('', views.index, name = 'index')
    # path('edit/<well_id>', views.edit, name='edit'),
    # path('add/', views.add, name='add')
]