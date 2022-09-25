from django.urls import path
from .views import *

# app_name = 'note'

urlpatterns = [
    path('', get_notes, name='notes'),
    path('create/', create_note, name='create'),
    path('<str:pk>/update', update_note, name='update'),
    path('<str:pk>/delete', delete_note, name='delete'),

]
