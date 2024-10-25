from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
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
    