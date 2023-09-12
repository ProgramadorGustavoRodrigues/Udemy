from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
   # fromrota, view responsável, nome de referêcia
   # usuarios.com
   path('',views.home,name='home'),
   # usuarios.com/usuasrios
   path('usuarios/',views.usuarios,name='listagem_usuarios')
   
]
