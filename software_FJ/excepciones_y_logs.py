# ============================================================
# MÓDULO: excepciones_y_logs.py
# DESCRIPCIÓN: Manejo centralizado de excepciones y registros
# del sistema mediante la librería logging de Python.
# ============================================================

# Importamos la librería logging para registrar eventos y errores.
import logging

# Importamos os para trabajar con la ruta del archivo de registros.
import os

# ============================================================
# CONFIGURACIÓN DEL SISTEMA DE REGISTROS (LOGGING)
# ============================================================

# Definimos el nombre del archivo donde se almacenarán los registros.
ARCHIVO_LOG = "sistema_eventos.log"

# Creamos un objeto logger con un nombre identificador del sistema.
logger = logging.getLogger("SistemaFJ")

# Establecemos el nivel mínimo de registro en DEBUG.
# Esto permite registrar todos los niveles de importancia.
logger.setLevel(logging.DEBUG)

# Evitamos que los mensajes se propaguen a otros loggers.
logger.propagate = False

# Comprobamos que el logger no tenga manejadores duplicados.
if not logger.handlers:

    # Creamos un manejador para guardar los registros en un archivo.
    manejador_archivo = logging.FileHandler(
        ARCHIVO_LOG,
        encoding="utf-8"
    )

    # Establecemos el nivel mínimo del archivo en DEBUG.
    manejador_archivo.setLevel(logging.DEBUG)

    # Creamos un formato que incluye fecha, hora, nivel y mensaje.
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Aplicamos el formato al manejador del archivo.
    manejador_archivo.setFormatter(formato)

    # Creamos un manejador para mostrar los registros en consola.
    manejador_consola = logging.StreamHandler()

    # Establecemos el nivel mínimo de la consola en DEBUG.
    manejador_consola.setLevel(logging.DEBUG)

    # Aplicamos el mismo formato utilizado en el archivo.
    manejador_consola.setFormatter(formato)

    # Incorporamos el manejador del archivo al logger.
    logger.addHandler(manejador_archivo)

    # Incorporamos el manejador de consola al logger.
    logger.addHandler(manejador_consola)


# ============================================================
# JERARQUÍA DE EXCEPCIONES PERSONALIZADAS
# ============================================================

# Excepción base para identificar errores propios del sistema.
class ErrorSistemaFJ(Exception):

    # Constructor que recibe un mensaje descriptivo del error.
    def __init__(self, mensaje="Se ha producido un error en el sistema."):

        # Inicializamos la clase Exception con el mensaje recibido.
        super().__init__(mensaje)


# Excepción para indicar que los datos ingresados son incorrectos.
class DatosInvalidosError(ErrorSistemaFJ):

    # Constructor que permite personalizar el mensaje del error.
    def __init__(self, mensaje="Los datos ingresados no son válidos."):

        # Enviamos el mensaje a la excepción base.
        super().__init__(mensaje)


# Excepción para indicar que falta un parámetro obligatorio.
class ParametroFaltanteError(ErrorSistemaFJ):

    # Constructor que recibe un mensaje sobre el parámetro faltante.
    def __init__(self, mensaje="Falta un parámetro obligatorio."):

        # Enviamos el mensaje a la excepción base.
        super().__init__(mensaje)


# Excepción para indicar que un servicio no está disponible.
class ServicioNoDisponibleError(ErrorSistemaFJ):

    # Constructor que describe el problema de disponibilidad.
    def __init__(self, mensaje="El servicio solicitado no está disponible."):

        # Enviamos el mensaje a la excepción base.
        super().__init__(mensaje)


# Excepción para indicar que una reserva presenta inconsistencias.
class ReservaInvalidaError(ErrorSistemaFJ):

    # Constructor que describe el problema relacionado con la reserva.
    def __init__(self, mensaje="La reserva solicitada no es válida."):

        # Enviamos el mensaje a la excepción base.
        super().__init__(mensaje)


# Excepción para indicar que un cálculo presenta inconsistencias.
class CalculoInconsistenteError(ErrorSistemaFJ):

    # Constructor que describe el error producido durante un cálculo.
    def __init__(self, mensaje="El resultado del cálculo es inconsistente."):

        # Enviamos el mensaje a la excepción base.
        super().__init__(mensaje)
