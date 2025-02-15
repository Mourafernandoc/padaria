from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'core/editar_produto.html', {'form': form, 'produto': produto})


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/listar_produtos.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'core/cadastrar_produto.html',{'form': form})
    