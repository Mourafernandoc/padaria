from django.contrib import admin
# Register your models here.
from .models import Produto, Comanda, ItemComanda, Usuario

admin.site.register(Produto)
admin.site.register(Comanda)
admin.site.register(ItemComanda)
admin.site.register(Usuario)
