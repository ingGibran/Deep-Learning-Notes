
'''
FUNCIÓN A USAR
'''
from pydantic import BaseModel, Field

class EnviarEmailInput(BaseModel):
    correo_destino: str = Field(description="El correo electrónico del destinatario.")
    mensaje: str = Field(description="El texto del recordatorio que se enviará.")


'''
ESTADO DEL AGENTE
'''
from typing import TypeDict, Annotated
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypeDict):
    messages: Annotated[list[BaseMessage], operator.add]