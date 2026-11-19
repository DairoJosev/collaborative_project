# Importamos las herramientas para trabajar con las rutas.
import sys
import os

# Obtenemos la ubicación de la carpeta principal "codigo".
RUTA_PRINCIPAL = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Agregamos la carpeta principal a las rutas de búsqueda de Python.
sys.path.insert(0, RUTA_PRINCIPAL)

# Importamos la clase Cliente desde nuestro segundo módulo.
from modelos_base import Cliente

# Importamos las excepciones y el logger.
from excepciones_y_logs import logger, ErrorSistemaFJ

# Creamos un bloque para controlar posibles excepciones.
try:

    # Creamos un cliente con información válida.
    cliente1 = Cliente(
        nombre="Carlos Acuña",
        correo="carlos@gmail.com",
        telefono="3001234567"
    )

    # Mostramos el resumen del cliente.
    print(cliente1.obtener_resumen())

    # Comprobamos que los datos sean válidos.
    print("¿Cliente válido?:", cliente1.validar())

    # Intentamos modificar el correo del cliente.
    cliente1.correo = "correo_incorrecto"

# Capturamos cualquier excepción personalizada del sistema.
except ErrorSistemaFJ as error:

    # Registramos el error en el archivo y en la consola.
    logger.error("Error durante la prueba: %s", error)
