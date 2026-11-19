# Importamos las herramientas para trabajar con las rutas.
import sys
import os

# Obtenemos la ubicación de la carpeta principal "codigo".
RUTA_PRINCIPAL = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Agregamos la carpeta principal a las rutas de búsqueda de Python.
sys.path.insert(0, RUTA_PRINCIPAL)

# Importamos las tres clases de servicios.
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

# Importamos el logger y las excepciones del sistema.
from excepciones_y_logs import logger, ErrorSistemaFJ

# Creamos una lista para almacenar los diferentes servicios.
servicios = []

# Utilizamos try para controlar posibles errores.
try:

    # Creamos una reserva de sala con proyector.
    sala = ReservaSala(
        nombre="Sala de conferencias",
        tarifa_base=100000,
        capacidad=30,
        tiene_proyector=True
    )

    # Creamos un alquiler de tres computadores.
    equipo = AlquilerEquipo(
        nombre="Alquiler tecnológico",
        tarifa_base=50000,
        tipo_equipo="Computador",
        cantidad_equipos=3
    )

    # Creamos una asesoría de complejidad avanzada.
    asesoria = AsesoriaEspecializada(
        nombre="Asesoría informática",
        tarifa_base=80000,
        especialidad="Programación",
        nivel_complejidad="avanzado"
    )

    # Agregamos los servicios a la lista.
    servicios.extend([sala, equipo, asesoria])

    # Recorremos los servicios para mostrar sus características.
    for servicio in servicios:

        # Mostramos la descripción del servicio.
        print("\n", servicio.describir_servicio())

        # Mostramos el costo normal del servicio.
        print("Costo normal:", servicio.calcular_costo())

        # Mostramos el costo con un descuento del 10%.
        print("Costo con descuento:", servicio.calcular_costo(descuento=0.10))

        # Mostramos el resumen completo del servicio.
        print("Resumen:", servicio.obtener_resumen())

# Capturamos los errores personalizados del sistema.
except ErrorSistemaFJ as error:

    # Registramos el error en el archivo y en la consola.
    logger.error("Error al procesar los servicios: %s", error)
