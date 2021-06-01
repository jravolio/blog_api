from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#criar api flask
app = Flask(__name__)
#criar instancia sqlalchemy
app.config['SECRET_KEY'] = '723y17y3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db:SQLAlchemy

#definit tabela postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer,db.ForeignKey('autor.id_autor'))

#definir tabela autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

def inicializar_banco():
    #executar criação
    db.drop_all()
    db.create_all()

    #criar admins
    autor = Autor(nome = 'Julio', email = 'jravolio892@gmail.com', senha = '123', admin= True)
    db.session.add(autor)

    db.session.commit()

if __name__ == "__main__":
    inicializar_banco()