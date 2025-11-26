from django.contrib import admin
from .models import Pagina, Produto, Contato, Pedido


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'criado_em')
    search_fields = ('nome', 'descricao')
    list_filter = ('criado_em', 'atualizado_em')
    
class ContatoAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'email', 'criado_em')
    readonly_fields = ('nome', 'email', 'mensagem', 'criado_em') 
    
class PedidoAdmin(admin.ModelAdmin):
    
    list_display = ('usuario', 'produto', 'quantidade', 'total', 'data')
    list_filter = ('data', 'usuario')


admin.site.register(Pagina)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Pedido, PedidoAdmin)