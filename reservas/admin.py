from django.contrib import admin
from .models import Stand, Reserva


@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = [
        'localizacao', 'valor'
    ]


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = [
        'stand', 'nome_empresa', 'categoria_empresa',
        'cnpj', 'quitado'
    ]
