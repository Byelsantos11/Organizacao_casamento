from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from noivos.models import Convidados, Presentes

def convidados(request):
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)
    presentes = Presentes.objects.filter(reservado=False).order_by('-importancia')
    return render(request, 'convidados.html', {
        'convidado': convidado,
        'presentes': presentes,
        'token': token
    })

def responder_presenca(request):
    resposta = request.GET.get('resposta')
    token = request.GET.get('token')
    convidado = Convidados.objects.get(token=token)

    if resposta not in ['C', 'R']:
        messages.add_message(request, constants.ERROR, 'Você deve confirmar ou recusar')
        return redirect(f'{reverse("convidados")}?token={token}')
    
    convidado.status = resposta
    convidado.save()
    return redirect(f'{reverse("convidados")}?token={token}')


def reservar_presente(request, id):
 token = request.GET.get('token')
 convidado = Convidados.objects.get(token=token)
 presente = Presentes.objects.get(id=id)
 presente.reservado=True
 presente.reservado_por = convidado
 presente.save()
 return redirect(f'{reverse('convidados')}?token={token}')
