from django.urls import path
from . import views
app_name = 'notatki'
urlpatterns = [
 path('', views.note_list, name='note_list'),
 path('<slug:slug>/', views.note_detail, name='note_detail'),
]#