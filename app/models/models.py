from sqlalchemy import Column, Integer, String
from models.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    name = Column(String(70))
    email = Column(String(50))
    hashed_password = Column(String(70))
    
class Taxi(Base):
    __tablename__ = 'taxi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    town = Column(String(50))
    km = Column(String(50))
    time = Column(String(50))
    price = Column(String(50))


class Bus(Base):
    __tablename__ = 'bus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    zone_id = Column(String(50))
    origin = Column(String(50))
    dispatch = Column(String(50))
    destination = Column(String(50))
    price = Column(String(50))

class Zone(Base):
    __tablename__ = 'zone'

    id = Column(Integer, primary_key=True, autoincrement=True)
    zone = Column(String(50))


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_llamada = Column(String(10))
    tipo_documento = Column(String(50))
    numero_documento = Column(String(50))
    nombres = Column(String(70))
    apellido = Column(String(70))
    fecha_nacimiento = Column(String(10))
    edad_en_anos = Column(Integer)
    edad_en_meses = Column(Integer)
    curso_vida = Column(String(50))
    regimen = Column(String(50))
    tipo_afiliado = Column(String(50))
    tipo_poblacion = Column(String(50))
    codigo_municipio = Column(String(50))
    nombre_municipio = Column(String(70))
    zona = Column(String(50))
    ips_atencion = Column(String(70))
    numero_telefono_reportado = Column(String(50))
    nombre_y_apellido_acudiente = Column(String(70))
    parentesco = Column(String(50))
    telefono_de_notificacion = Column(String(50))
    motivo_llamada_fallida = Column(String(100))
    observaciones = Column(String(255))