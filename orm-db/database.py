from peewee import * # type: ignore

# Conexão com o banco de dados SQLite
db = SqliteDatabase('freelancers.db')

class Usuario(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db  # Referência ao banco de dados

class Anuncio(Model):
    usuario = ForeignKeyField(Usuario, backref='anuncios')
    titulo = CharField()
    descricao = TextField()
    valor = DecimalField()

    class Meta:
        database = db  # Referência ao banco de dados
