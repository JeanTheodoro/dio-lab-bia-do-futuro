
from sqlalchemy import (
    Column, BigInteger, String, Integer, Numeric,
    Boolean, ForeignKey, TIMESTAMP, Date, func,
    CheckConstraint,
    Text, Sequence
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from core.database import Base


class Client(Base):
    __tablename__ = "clientes"
    __table_args__ = {"schema": "dio_bank"}

    id = Column(BigInteger, primary_key=True)
    nome = Column(String(150), nullable=False)
    idade = Column(Integer)
    profissao = Column(String(100))
    renda_mensal = Column(Numeric(15, 2))
    perfil_investidor = Column(String(50))
    objetivo_principal = Column(String(150))
    aceita_risco = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP)

    contas = relationship(
        "CurrentAccount",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )

    objetivos = relationship(
        "Objective",
        back_populates="cliente",
        cascade="all, delete-orphan"
    )


class CurrentAccount(Base):
    __tablename__ = "contas_correntes"
    __table_args__ = {"schema": "dio_bank"}

    id = Column(BigInteger, primary_key=True)
    
    cliente_id = Column(
        BigInteger,
        ForeignKey("dio_bank.clientes.id", ondelete="CASCADE")
    )
    
    cod_conta_corrente = Column(
        Integer,
        Sequence("seq_cod_conta", schema="dio_bank"),
        unique=True,
        nullable=False
    )
    saldo_atual = Column(Numeric(15, 2), default=0)
    limite_conta = Column(Numeric(15, 2), default=1500)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP)

    cliente = relationship("Client", back_populates="contas")

    transacoes = relationship(
        "Transection",
        back_populates="conta",
        cascade="all, delete-orphan"
    )


class Transection(Base):
    __tablename__ = "transacoes"
    __table_args__ = {"schema": "dio_bank"}

    id = Column(BigInteger, primary_key=True)
    conta_corrente_id = Column(
        BigInteger,
        ForeignKey("dio_bank.contas_correntes.id", ondelete="CASCADE")
    )
    descricao = Column(String(100))
    categoria = Column(String(100))
    valor = Column(Numeric(15, 2), nullable=False)
    tipo_operacao = Column(String(10), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    conta = relationship("CurrentAccount", back_populates="transacoes")



class Objective(Base):
    __tablename__ = "metas"
    __table_args__ = {"schema": "dio_bank"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    cliente_id = Column(
        BigInteger,
        ForeignKey("dio_bank.clientes.id", ondelete="CASCADE"),
        nullable=False
    )
    objetivo = Column(String(150), nullable=False)
    valor_necessario = Column(Numeric(15, 2), nullable=False)
    prazo = Column(Date)

    cliente = relationship("Client", back_populates="objetivos")


class FinancialProduct(Base):
    __tablename__ = "produtos_financeiros"
    __table_args__ = (
        CheckConstraint(
            "risco IN ('baixo','medio','alto')",
            name="ck_produto_risco"
        ),
        {"schema": "dio_bank"}
    )

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    categoria = Column(String(100))
    risco = Column(String(20))
    rentabilidade_descricao = Column(Text)
    aporte_minimo = Column(Numeric(15, 2))
    liquidez = Column(String(50))
    prazo_minimo_dias = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
