from django.shortcuts import render, redirect
from .models import Carrinho
from home.models import Produto

def add(request, nome):
    
    produto = Produto.objects.get(nome=nome)

    if len(Carrinho.objects.all()) == 10:
        return redirect('/carrinho/ver_carrinho/?aviso=2')

    add_carrinho = Carrinho(
        produtos_carrinho=produto,
    )

    add_carrinho.save()

    return redirect('/home/')


def ver_carrinho(request):
    carrinho = Carrinho.objects.all()
    carrinho_quantidade = len(Carrinho.objects.all())
    aviso = request.GET.get('aviso')

    total = sum(float(i.produtos_carrinho.preco) for i in carrinho)

    context = {
        'carrinho': carrinho,
        'carrinho_quantidade': carrinho_quantidade,
        'aviso': aviso,
        'total': f'{total:.2f}',
    }
    return render(request, 'ver_carrinho.html', context=context)


def excluir_produto(request, id):
    excluir = Carrinho.objects.get(id=id)
    excluir.delete()
    return redirect('/carrinho/ver_carrinho/')


def limpar_tudo(request):
    carrinho = Carrinho.objects.all()

    if len(Carrinho.objects.all()) == 0:
        return redirect('/carrinho/ver_carrinho/?aviso=1')

    carrinho.delete()
    return redirect('/carrinho/ver_carrinho/')

