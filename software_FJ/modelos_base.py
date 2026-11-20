# ============================================================
# MÓDULO: modelos_base.py
# DESCRIPCIÓN: Define las clases abstractas y los modelos base
# del sistema mediante programación orientada a objetos.
# ============================================================

# Importamos ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod

# Importamos datetime para registrar la fecha de creación.
from datetime import datetime

# Importamos uuid para generar identificadores únicos.
import uuid

# Importamos las excepciones personalizadas y el logger del primer módulo.
from excepciones_y_logs import (
    logger,
    DatosInvalidosError,
    ParametroFaltanteError
)

# ============================================================
# CLASE ABSTRACTA: ENTIDAD
# ============================================================

# Definimos Entidad como una clase abstracta que hereda de ABC.
class Entidad(ABC):

    # Constructor de la clase abstracta.
    def __init__(self, identificador=None):

        # Asignamos un identificador único si no se proporciona uno.
        self._id = identificador if identificador is not None else str(uuid.uuid4())

        # Guardamos la fecha y hora en la que se crea la entidad.
        self._fecha_creacion = datetime.now()

    # Declaramos un método abstracto para validar los datos de la entidad.
    @abstractmethod
    def validar(self):

        # Documentamos que las clases hijas deben implementar este método.
        pass

    # Declaramos un método abstracto para obtener un resumen de la entidad.
    @abstractmethod
    def obtener_resumen(self):

        # Documentamos que las clases hijas deben implementar este método.
        pass


# ============================================================
# CLASE CLIENTE
# ============================================================

# Definimos Cliente como una clase concreta que hereda de Entidad.
class Cliente(Entidad):

    # Constructor de la clase Cliente.
    def __init__(self, nombre=None, correo=None, telefono=None, identificador=None):

        # Inicializamos los atributos heredados de la clase Entidad.
        super().__init__(identificador)

        # Creamos el atributo privado para almacenar el nombre.
        self.__nombre = None

        # Creamos el atributo privado para almacenar el correo.
        self.__correo = None

        # Creamos el atributo privado para almacenar el teléfono.
        self.__telefono = None

        # Asignamos el nombre mediante su setter para validar el dato.
        self.nombre = nombre

        # Asignamos el correo mediante su setter para validar el dato.
        self.correo = correo

        # Asignamos el teléfono mediante su setter para validar el dato.
        self.telefono = telefono

        # Ejecutamos una validación general de todos los atributos.
        self.validar()

        # Registramos en el log que el cliente se creó correctamente.
        logger.info(
            "Cliente creado exitosamente. ID: %s | Nombre: %s",
            self._id,
            self.__nombre
        )

    # ========================================================
    # PROPIEDAD: NOMBRE
    # ========================================================

    # Creamos una propiedad para consultar el nombre del cliente.
    @property
    def nombre(self):

        # Devolvemos el valor del atributo privado nombre.
        return self.__nombre

    # Creamos el setter para modificar y validar el nombre.
    @nombre.setter
    def nombre(self, valor):

        # Comprobamos si el nombre está ausente o contiene solo espacios.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción si el nombre es obligatorio y falta.
            raise ParametroFaltanteError("El nombre del cliente es obligatorio.")

        # Comprobamos que el nombre sea una cadena de texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción cuando el tipo de dato es incorrecto.
            raise DatosInvalidosError("El nombre debe ser una cadena de texto.")

        # Eliminamos los espacios innecesarios al principio y al final.
        valor = valor.strip()

        # Comprobamos que el nombre no esté vacío después de limpiarlo.
        if not valor:

            # Lanzamos una excepción si el nombre no contiene información.
            raise ParametroFaltanteError("El nombre del cliente no puede estar vacío.")

        # Guardamos el nombre validado en el atributo privado.
        self.__nombre = valor

    # ========================================================
    # PROPIEDAD: CORREO
    # ========================================================

    # Creamos una propiedad para consultar el correo del cliente.
    @property
    def correo(self):

        # Devolvemos el valor del atributo privado correo.
        return self.__correo

    # Creamos el setter para modificar y validar el correo.
    @correo.setter
    def correo(self, valor):

        # Comprobamos si el correo está ausente o vacío.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción si falta el correo obligatorio.
            raise ParametroFaltanteError("El correo electrónico es obligatorio.")

        # Comprobamos que el correo sea una cadena de texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción cuando el tipo de dato es incorrecto.
            raise DatosInvalidosError("El correo debe ser una cadena de texto.")

        # Eliminamos los espacios innecesarios del correo.
        valor = valor.strip()

        # Comprobamos que el correo contenga exactamente un símbolo @.
        if valor.count("@") != 1:

            # Lanzamos una excepción si el correo no tiene un formato básico válido.
            raise DatosInvalidosError("El correo debe contener exactamente un símbolo @.")

        # Separamos el correo en su parte local y su dominio.
        parte_local, dominio = valor.split("@")

        # Comprobamos que ambas partes del correo tengan contenido.
        if not parte_local or not dominio:

            # Lanzamos una excepción si falta información del correo.
            raise DatosInvalidosError("El correo debe tener información antes y después del @.")

        # Guardamos el correo validado en el atributo privado.
        self.__correo = valor

    # ========================================================
    # PROPIEDAD: TELEFONO
    # ========================================================

    # Creamos una propiedad para consultar el teléfono del cliente.
    @property
    def telefono(self):

        # Devolvemos el valor del atributo privado teléfono.
        return self.__telefono

    # Creamos el setter para modificar y validar el teléfono.
    @telefono.setter
    def telefono(self, valor):

        # Comprobamos si el teléfono está ausente o vacío.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción si falta el teléfono obligatorio.
            raise ParametroFaltanteError("El teléfono del cliente es obligatorio.")

        # Comprobamos si el teléfono es un número entero.
        if isinstance(valor, int) and not isinstance(valor, bool):

            # Convertimos el número a texto para conservar un formato uniforme.
            valor = str(valor)

        # Comprobamos que el teléfono sea una cadena de texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción si el tipo de dato no es válido.
            raise DatosInvalidosError("El teléfono debe contener únicamente números.")

        # Eliminamos los espacios al principio y al final.
        valor = valor.strip()

        # Comprobamos que todos los caracteres sean dígitos numéricos.
        if not valor.isdigit():

            # Lanzamos una excepción si existen letras o símbolos.
            raise DatosInvalidosError("El teléfono debe ser numérico.")

        # Guardamos el teléfono validado como texto.
        self.__telefono = valor

    # ========================================================
    # MÉTODO: VALIDAR
    # ========================================================

    # Implementamos el método abstracto heredado de Entidad.
    def validar(self):

        # Comprobamos que el nombre exista y tenga contenido.
        if not self.__nombre:

            # Lanzamos una excepción si falta el nombre.
            raise ParametroFaltanteError("El nombre del cliente es obligatorio.")

        # Comprobamos que el correo exista y tenga contenido.
        if not self.__correo:

            # Lanzamos una excepción si falta el correo.
            raise ParametroFaltanteError("El correo electrónico es obligatorio.")

        # Comprobamos que el correo tenga exactamente un símbolo @.
        if self.__correo.count("@") != 1:

            # Lanzamos una excepción si el correo tiene un formato incorrecto.
            raise DatosInvalidosError("El correo electrónico no es válido.")

        # Comprobamos que el teléfono exista y tenga contenido.
        if not self.__telefono:

            # Lanzamos una excepción si falta el teléfono.
            raise ParametroFaltanteError("El teléfono del cliente es obligatorio.")

        # Comprobamos que el teléfono contenga solamente números.
        if not self.__telefono.isdigit():

            # Lanzamos una excepción si el teléfono no es numérico.
            raise DatosInvalidosError("El teléfono debe contener solamente números.")

        # Retornamos True cuando todos los datos son correctos.
        return True

    # ========================================================
    # MÉTODO: OBTENER RESUMEN
    # ========================================================

    # Implementamos el método abstracto heredado de Entidad.
    def obtener_resumen(self):

        # Construimos y devolvemos un resumen con los datos del cliente.
        return (
            f"ID: {self._id} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono} | "
            f"Fecha de creación: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )
