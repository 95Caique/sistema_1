from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServidorViewSet, perfil_servidor
from. import views

router = DefaultRouter()
router.register(r'servidores', ServidorViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('perfil-servidor/<str:identificador>/', views.perfil_servidor, name='perfil_servidor'),
    path('', views.lista_servidores, name= 'lista_servidores'),
]