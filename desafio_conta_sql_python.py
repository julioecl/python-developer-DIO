from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    create_engine,
    inspect,
    select)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    Session)

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (f'Cliente(id={self.id},'
                f'nome={self.nome},'
                f'endereco={self.endereco})')


class Conta(Base):
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Float)

    cliente = relationship(
        "Cliente", back_populates="conta"
    )

    def __repr__(self):
        return (f'Conta(id={self.id},'
                f'tipo={self.tipo}), '
                f'agencia={self.agencia},'
                f'num={self.num},'
                f'saldo={self.saldo}')


engine = create_engine('sqlite://')

Base.metadata.create_all(engine)

inspetor = inspect(engine)

with Session(engine) as session:
    julio = Cliente(
        nome='Julio Lima',
        endereco='Rua A, 25 - Indaial-SC',
        conta=[Conta(tipo='fisica', agencia='001', num=40155, saldo=255.12)]
    )
    juliana = Cliente(
        nome='Juliana Mascarenhas',
        endereco='Rua B, 45 - Blumenau-SC',
        conta=[Conta(tipo='fisica', agencia='001', num=35996, saldo=1550.18)]
    )

    session.add_all([julio, juliana])

    session.commit()

stmt = select(Cliente)
for cliente in session.scalars(stmt):
    print(cliente)

stmt_join = select(Cliente.id, Cliente.endereco, Conta.tipo, Conta.saldo).join_from(Conta, Cliente)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print(results)
