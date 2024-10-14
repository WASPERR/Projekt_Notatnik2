from django.urls import path
from . import views
app_name = 'notatki'
urlpatterns = [
 path('', views.notes_list, name='notes_list'),
 path('<int:id>/', views.notes_detail, name='notes_detail'),
]#