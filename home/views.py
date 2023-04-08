from django.shortcuts import render, redirect
from .models import Categoria, Produto
from carrinho.models import Carrinho


def home(request):
    produtos = Produto.objects.all()
    carrinho = len(Carrinho.objects.all())
    context = {
        'produtos': produtos,
        'carrinho': carrinho,
    }
    return render(request, 'home.html', context=context)


def criar_produto(request):

    if request.method == 'GET':
        categorias = Categoria.objects.all()
        context = {
            'categorias':categorias,
        }
        return render(request, 'criar_produto.html', context=context)
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')
        image = request.FILES.get('image')

        
        if image == None:
            print('Nenhuma imagem selecionada')
            return redirect('/home/criar_produto/')

        for i in nome, descricao, categoria, preco:
            if i.strip() == "":
                return redirect('/home/criar_produto/')
            
        categoria_id = Categoria.objects.get(id=categoria)
        
        produto = Produto(
            nome=nome,
            descricao=descricao,
            categoria=categoria_id,
            preco=preco,
            imagem=image,
        )

        produto.save()
        return redirect('/home/')
        
