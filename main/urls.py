from django.contrib import admin
from django.urls import path
from reservas.views import index, cadastro, deletar, detalhe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cadastrar/', cadastro, name='cadastrar'),
    path('deletar/<int:id>/', deletar, name='deletar'),
    path('detalhe/<int:id>/', detalhe, name='detalhe'),
]
