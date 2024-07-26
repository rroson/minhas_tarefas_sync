from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func
from datetime import datetime

tabela_registro = registry()

@tabela_registro.mapped_as_dataclass # Classe de dados
class Usuario:
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    usuario: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )