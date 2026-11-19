# Importamos el logger y algunas excepciones.
from excepciones_y_logs import (
    logger,
    DatosInvalidosError,
    ReservaInvalidaError
)

# Registramos el inicio de la prueba.
logger.info("Iniciando pruebas del módulo.")

try:

    # Generamos una excepción personalizada.
    raise DatosInvalidosError("El documento ingresado es incorrecto.")

# Capturamos la excepción personalizada.
except DatosInvalidosError as error:

    # Registramos el error en consola y en el archivo.
    logger.error("Error detectado: %s", error)

# Registramos la finalización de las pruebas.
logger.info("Pruebas finalizadas.")