from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing/', views.searchDukan.as_view()),
    path('listing/<int:pk>/', views.searchDukan.as_view()),
    path('listing/<int:uuid>/', views.searchDukan.as_view()),
    #hello

]
