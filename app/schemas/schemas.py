from pydantic import BaseModel
from datetime import date


class CreateUserRequest(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(BaseModel):
    id : int
    username : str

class TaxiBase(BaseModel):
    id: int
    town : str
    km : str
    time : str
    price : str

class ClientBase(BaseModel):
    id: int
    fecha_llamada: str
    tipo_documento: str
    numero_documento: str
    nombres: str
    apellido: str
    fecha_nacimiento: str
    edad_en_anos: int
    edad_en_meses: int
    curso_vida: str
    regimen: str
    tipo_afiliado: str
    tipo_poblacion: str
    codigo_municipio: str
    nombre_municipio: str
    zona: str
    ips_atencion: str
    numero_telefono_reportado: str
    nombre_y_apellido_acudiente: str
    parentesco: str
    telefono_de_notificacion: str
    motivo_llamada_fallida: str
    observaciones: str
