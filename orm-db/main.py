from database import db, Usuario, Anuncio

# Conectar ao banco de dados
db.connect()

# Criar as tabelas (se ainda não existirem)
db.create_tables([Usuario, Anuncio])

# Criar um novo usuário
#usuario = Usuario.create(nome="ProgramadorPython", email="teste@teste.com", senha="123456")

# Exibir informações do usuário criado
#print("Novo usuário:", usuario.id, usuario.nome, usuario.email)

# usuario = Usuario.create(nome="Guilherme", email="gui@teste.com", senha="123456")
# usuario = Usuario.create(nome="Joao", email="joao@teste.com", senha="123456")
# usuario = Usuario.create(nome="Maria", email="maria@teste.com", senha="123456")

#    lista_usuarios = Usuario.select()
#    print("listando usuarios:")

# for u in lista_usuarios:
#    print("-", u.id, u.none, u.email)


# usuario1 = Usuario.get(Usuario.id == 1)
# print("usuario pelo id", usuario1.id, usuario1.nome)

# maria = Usuario.get(Usuario.email == "maria@teste.com")
# maria.nome = "Maria Python"
# maria.save()

# print("maria atualizada:", maria.nome)

# print("tentando criar um ususario copm e-mail duplicado")

# print("Tentando criar um usuário com e-mail duplicado")

#try:
#    usuario_duplicado = Usuario.create(nome="Duplicado", email="teste@teste.com", senha="123456")
#    print("Usuário duplicado criado:", usuario_duplicado.id, usuario_duplicado.nome, usuario_duplicado.email)
#except:
#    print("E-mail existente!")
 
#usuario_deletado = Usuario.get( Usuario.email == "teste@teste.com")
#usuario_deletado.delete_instance()
 
#try: 
#    Usuario.get(Usuario.email == "teste@teste.com")
#except:
#    print("Usuário deletado!")    

# maria = Usuario.get(Usuario.email == "maria@teste.com")

#anuncio = Anuncio.create(
#    usuario = maria,
#    titulo = "Video de Banco de Dados"
#    descricao = "O projeto seria criar um video sobre banco de dados e ORM com Python",
#    Valor = 500.0
#)

#print("Novo anuncio:", anuncio.id, anuncio.titulo)

# Criar anúncios para Maria

#  Anuncio.create(usuario=maria, titulo="Anuncio 1", descricao="Deixa o like", valor=1000)
#   Anuncio.create(usuario=maria, titulo="Anuncio 2", descricao="Faça um comentário", valor=5000)
#    Anuncio.create(usuario=maria, titulo="Anuncio 3", descricao="Se inscreva", valor=10000)
 
#print("Anúncios criados com sucesso para Maria!")
#anuncio_maria= Anuncio.select().join(Usuario).where(Usuario.email == "maria@teste.com")
# for a in anuncios_meria:
#   print("-", a.id, a.titulo, a.valor)

Anuncio.delete().execute()
   
print("Quantidade de anuncios:", Anuncio.select().count())