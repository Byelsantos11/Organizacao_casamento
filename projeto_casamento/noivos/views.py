from django.shortcuts import render, redirect
from .models import Presentes, Convidados

def home(request):
    if request.method=="GET":
        presentes= Presentes.objects.all()
        return render(request, "home.html", {'presentes': presentes})
    elif request.method=="POST":
        nome_presente= request.POST.get("nome_presente")
        preco= request.POST.get("preco")
        importancia= int (request.POST.get("importancia"))
        foto= request.FILES.get("foto")
        
        
        
        if importancia<1 or importancia>5:
            return redirect('home')
        
        presente= Presentes(
            nome_presente =nome_presente, 
            preco= preco,
            foto= foto,
            importancia= importancia
        )
        
        presente.save()
        
        return redirect('home')
    
    
def lista_convidados(request):
    if request.method== "GET":
       convidados= Convidados.objects.all()
       return render (request, 'lista_convidados.html', {'convidados': convidados})
    elif request.method == "POST":
        nome_convidado= request.POST.get("nome_convidado")
        whatsapp= request.POST.get("whatsapp")
        maximo_acompanhantes= int(request.POST.get("maximo_acompanhantes"))
       
       
    convidados = Convidados(
           nome_convidado= nome_convidado,
           whatsapp= whatsapp,
           maximo_acompanhantes= maximo_acompanhantes
       )
       
    convidados.save()
    return redirect('lista_convidados')