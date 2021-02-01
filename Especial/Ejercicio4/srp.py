import json
from json2html import * # Instala por medio de pip: https://pypi.org/project/json2html/
from json2xml import json2xml  # Instala por medio de pip: https://pypi.org/project/json2xml/
from json2yaml import json2yaml  # Instala por medio de pip: https://pypi.org/project/json2yaml/


class Usuario(object):
    """docstring for Usuario"""

    def __init__(self, **args):
        self.nombre = args.get('nombre')
        self.edad = args.get('edad')
        self.direccion = args.get('direccion')

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_edad(self):
        return self.edad

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_direccion(self):
        return self.direccion

# Hasta aqui los datos son propios de la clase Usuario

class serializar(object):
    def serialize(self, formato='string'):
        formato = formato.lower()
        
        if formato == 'string':
            return str(self)
        
        if formato == 'dict':
            return self.__dict__
        
        if formato == 'json':
            return json.dumps(self.__dict__)
        
        if formato == 'html':
            return json2html.convert(json=json.dumps(self.__dict__))

        if formato == 'XML':
            return json2xml.convert(json=json.dumps(self.__dict__))

        if formato == 'YAML':
            return json2yaml.convert(json=json.dumps(self.__dict__))

    def __str__(self):
        return "Nombre:{}, Edad:{}, direccion:{}".format(self.nombre, self.edad, self.direccion).strip()

user = Usuario(
    nombre='juanito',
    edad=15,
    direccion='calle x, #y colonia z'
)
user.serializar(object)
print(user)