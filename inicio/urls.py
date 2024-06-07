from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.home, name="inicio"),
    path('crear_usuario',views.crear_usuario,name="crear_usuario"),
    path('bienvenido',views.bienvenido,name="bienvenido"),

]
