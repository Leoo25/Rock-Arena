from django.db import models
from django.contrib.auth.models import User 

class Pagina(models.Model):
   
    nome_do_site = models.CharField(max_length=100)
    logo_do_site = models.ImageField(upload_to='logo/') 
    texto_chamada = models.TextField()
    texto_sobre = models.TextField()
    imagem_sobre = models.ImageField(upload_to='sobre/')
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=15)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_do_site

class Produto(models.Model):
  
    nome = models.CharField(max_length=100)
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='produtos/')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Contato(models.Model):
   
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.usuario.username} - {self.produto.nome}"