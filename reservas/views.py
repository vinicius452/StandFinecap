from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReservaModelForm
from .models import Reserva


def index(request):
    reservas = Reserva.objects.all()

    nome = request.GET.get('nome')
    valor = request.GET.get('valor')
    quitado = request.GET.get('quitado')
    nao_quitado = request.GET.get('nao_quitado')
    data = request.GET.get('data')

    if nome:
        reservas = reservas.filter(nome_empresa__icontains=nome)

    if valor:
        reservas = reservas.filter(stand__valor=valor)

    if quitado is not None:
        reservas = reservas.filter(quitado=str(quitado))

    if nao_quitado is not None:
        reservas = reservas.filter(quitado=str(nao_quitado))

    if data:
        reservas = reservas.filter(data__gte=data)

    return render(request, 'stands/index.html', {'reservas': reservas})


def detalhe(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, 'stands/reserva.html', {'reserva': reserva})


def cadastro(request):
    if request.method == 'POST':
        form = ReservaModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReservaModelForm()
            return redirect('index')
        else:
            form = ReservaModelForm(request.POST)
    else:
        form = ReservaModelForm()
    return render(request, 'stands/cadastro.html', {'form': form})


def deletar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('index')