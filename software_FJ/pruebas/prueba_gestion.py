# Importamos las herramientas para trabajar con las rutas.
import sys
import os

# Obtenemos la ubicación de la carpeta principal "codigo".
RUTA_PRINCIPAL = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Agregamos la carpeta principal a las rutas de búsqueda de Python.
sys.path.insert(0, RUTA_PRINCIPAL)

# Importamos la clase Cliente.
from modelos_base import Cliente

# Importamos las clases de servicios.
from servicios import ReservaSala

# Importamos el controlador principal.
from gestion_reservas import SistemaGestionFJ

# Importamos el logger del sistema.
from excepciones_y_logs import logger

# Creamos una instancia del controlador.
sistema = SistemaGestionFJ()

# Creamos un cliente con información válida.
cliente = Cliente(
    nombre="Carlos Acuña",
    correo="carlos@gmail.com",
    telefono="3001234567"
)

# Creamos una sala disponible.
sala = ReservaSala(
    nombre="Sala de reuniones",
    tarifa_base=100000,
    capacidad=20,
    tiene_proyector=True
)

# Registramos el cliente en el sistema.
sistema.registrar_cliente(cliente)

# Agregamos el servicio al sistema.
sistema.agregar_servicio(sala)

# Creamos una reserva de dos horas.
reserva = sistema.crear_reserva(
    cliente,
    sala,
    duracion_horas=2
)

# Comprobamos que la reserva se haya creado.
if reserva is not None:

    # Mostramos el resumen inicial.
    print("\nRESERVA CREADA")
    print(reserva.obtener_resumen())

    # Confirmamos y procesamos el pago.
    total = sistema.procesar_reserva(reserva)

    # Comprobamos que el procesamiento haya sido exitoso.
    if total is not None:

        # Mostramos el valor del pago simulado.
        print("\nPAGO PROCESADO")
        print("Total:", total)

    # Mostramos el estado final de la reserva.
    print("\nESTADO FINAL")
    print(reserva.obtener_resumen())

# Mostramos el resumen general del sistema.
print("\nRESUMEN DEL SISTEMA")
print(sistema.obtener_resumen_sistema())

# Registramos la finalización de la prueba.
logger.info("Prueba general del sistema finalizada.")
