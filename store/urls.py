from django.urls import path
from.import views

urlpatterns = [
  path('',views.home,name='home'),
  path('reg/',views.register,name='register'),
  path('log/',views.login,name='login'),
  path('col/',views.collection,name='collection'),
  path('prd/',views.product,name='product'),
]