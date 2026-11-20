# ============================================================
# PROYECTO: SISTEMA DE GESTIÓN FJ
# MÓDULO PRINCIPAL: main.py
# DESCRIPCIÓN: Ejecuta una simulación de 12 operaciones
# relacionadas con clientes, servicios y reservas.
# ============================================================

# Importamos el controlador principal del sistema.
from gestion_reservas import SistemaGestionFJ

# Importamos la clase Cliente para crear los clientes.
from modelos_base import Cliente

# Importamos las tres clases de servicios disponibles.
from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

# Importamos el logger y las excepciones personalizadas.
from excepciones_y_logs import logger, ErrorSistemaFJ


# ============================================================
# FUNCIÓN PRINCIPAL DEL PROGRAMA
# ============================================================

# Definimos la función que ejecutará todas las operaciones.
def ejecutar_sistema():

    # Mostramos el encabezado principal del programa.
    print("=" * 60)
    print("       SISTEMA DE GESTIÓN DE RESERVAS FJ")
    print("=" * 60)

    # Registramos el inicio de la simulación.
    logger.info("Inicio de la simulación principal del sistema.")

    # Creamos una instancia del controlador central.
    sistema = SistemaGestionFJ()

    # Inicializamos las variables de los clientes.
    cliente1 = None
    cliente2 = None
    cliente3 = None

    # Inicializamos las variables de los servicios.
    sala = None
    equipo = None
    asesoria = None

    # Inicializamos el contador de operaciones.
    operaciones = 0

    # ========================================================
    # OPERACIONES 1, 2 Y 3: REGISTRO DE CLIENTES
    # ========================================================

    # --------------------------------------------------------
    # OPERACIÓN 1: REGISTRO DEL PRIMER CLIENTE
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Registro del cliente 1")

    # Intentamos registrar el primer cliente.
    try:

        # Creamos un cliente con información válida.
        cliente1 = Cliente(
            nombre="Carlos Acuña",
            correo="carlos@gmail.com",
            telefono="3001234567"
        )

        # Registramos el cliente en el controlador.
        resultado = sistema.registrar_cliente(cliente1)

        # Comprobamos si el registro fue exitoso.
        if resultado:

            # Informamos que el cliente fue registrado.
            print("RESULTADO: Cliente 1 registrado correctamente.")

        # Comprobamos si el controlador rechazó el registro.
        else:

            # Informamos que no se pudo registrar el cliente.
            print("RESULTADO: No se pudo registrar el cliente 1.")

    # Capturamos cualquier error para evitar detener el programa.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 1.")

    # --------------------------------------------------------
    # OPERACIÓN 2: REGISTRO DEL SEGUNDO CLIENTE
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Registro del cliente 2")

    # Intentamos registrar el segundo cliente.
    try:

        # Creamos un segundo cliente con información válida.
        cliente2 = Cliente(
            nombre="María Rodríguez",
            correo="maria@gmail.com",
            telefono="3109876543"
        )

        # Registramos el segundo cliente.
        resultado = sistema.registrar_cliente(cliente2)

        # Comprobamos si el registro fue exitoso.
        if resultado:

            # Informamos que el cliente fue registrado.
            print("RESULTADO: Cliente 2 registrado correctamente.")

        # Comprobamos si el registro fue rechazado.
        else:

            # Informamos que no se pudo registrar.
            print("RESULTADO: No se pudo registrar el cliente 2.")

    # Capturamos cualquier error de la operación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 2.")

    # --------------------------------------------------------
    # OPERACIÓN 3: REGISTRO DE UN CLIENTE INVÁLIDO
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Registro de cliente inválido")

    # Intentamos registrar un cliente con correo incorrecto.
    try:

        # Creamos un cliente cuyo correo no contiene el símbolo @.
        cliente3 = Cliente(
            nombre="Pedro Martínez",
            correo="pedro.gmail.com",
            telefono="3201234567"
        )

        # Intentamos registrar el cliente inválido.
        resultado = sistema.registrar_cliente(cliente3)

        # Comprobamos si el sistema rechazó el registro.
        if not resultado:

            # Informamos que el cliente fue rechazado.
            print("RESULTADO: Cliente rechazado por datos inválidos.")

        # Comprobamos si el registro fue aceptado.
        else:

            # Informamos el resultado del registro.
            print("RESULTADO: Cliente registrado.")

    # Capturamos la excepción generada por los datos incorrectos.
    except Exception as e:

        # Mostramos el mensaje del error.
        print("RESULTADO: Cliente rechazado correctamente.")
        print("DETALLE:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Operación 3: cliente con correo inválido.")

    # ========================================================
    # OPERACIONES 4, 5, 6 Y 7: CREACIÓN DE SERVICIOS
    # ========================================================

    # --------------------------------------------------------
    # OPERACIÓN 4: CREACIÓN DE UNA RESERVA DE SALA
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Creación de servicio: Sala")

    # Intentamos crear y registrar una sala.
    try:

        # Creamos una sala con tarifa y capacidad válidas.
        sala = ReservaSala(
            nombre="Sala de conferencias",
            tarifa_base=100000,
            capacidad=30,
            tiene_proyector=True
        )

        # Agregamos la sala al controlador.
        resultado = sistema.agregar_servicio(sala)

        # Comprobamos si el servicio fue agregado.
        if resultado:

            # Informamos que la sala fue creada correctamente.
            print("RESULTADO: Servicio de sala creado correctamente.")

        # Comprobamos si el servicio fue rechazado.
        else:

            # Informamos que no se pudo agregar la sala.
            print("RESULTADO: No se pudo registrar la sala.")

    # Capturamos cualquier error de creación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 4.")

    # --------------------------------------------------------
    # OPERACIÓN 5: CREACIÓN DE UN ALQUILER DE EQUIPO
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Creación de servicio: Equipo")

    # Intentamos crear y registrar un servicio de equipos.
    try:

        # Creamos un servicio de alquiler de computadores.
        equipo = AlquilerEquipo(
            nombre="Alquiler de computadores",
            tarifa_base=50000,
            tipo_equipo="Computador",
            cantidad_equipos=3
        )

        # Agregamos el servicio al controlador.
        resultado = sistema.agregar_servicio(equipo)

        # Comprobamos si el servicio fue agregado.
        if resultado:

            # Informamos que el alquiler fue registrado.
            print("RESULTADO: Servicio de equipos creado correctamente.")

        # Comprobamos si el servicio fue rechazado.
        else:

            # Informamos que no se pudo agregar el servicio.
            print("RESULTADO: No se pudo registrar el alquiler.")

    # Capturamos cualquier error de creación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 5.")

    # --------------------------------------------------------
    # OPERACIÓN 6: CREACIÓN DE UNA ASESORÍA
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Creación de servicio: Asesoría")

    # Intentamos crear y registrar una asesoría.
    try:

        # Creamos una asesoría especializada válida.
        asesoria = AsesoriaEspecializada(
            nombre="Asesoría en programación",
            tarifa_base=80000,
            especialidad="Desarrollo de software",
            nivel_complejidad="avanzado"
        )

        # Agregamos la asesoría al controlador.
        resultado = sistema.agregar_servicio(asesoria)

        # Comprobamos si el servicio fue agregado.
        if resultado:

            # Informamos que la asesoría fue registrada.
            print("RESULTADO: Asesoría creada correctamente.")

        # Comprobamos si el servicio fue rechazado.
        else:

            # Informamos que no se pudo agregar la asesoría.
            print("RESULTADO: No se pudo registrar la asesoría.")

    # Capturamos cualquier error de creación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 6.")

    # --------------------------------------------------------
    # OPERACIÓN 7: CREACIÓN DE UN SERVICIO INVÁLIDO
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Creación de servicio inválido")

    # Intentamos crear un servicio con tarifa negativa.
    try:

        # Creamos una sala con una tarifa incorrecta.
        servicio_invalido = ReservaSala(
            nombre="Sala inválida",
            tarifa_base=-50000,
            capacidad=20,
            tiene_proyector=False
        )

        # Intentamos agregar el servicio al controlador.
        resultado = sistema.agregar_servicio(servicio_invalido)

        # Comprobamos si el sistema rechazó el servicio.
        if not resultado:

            # Informamos que el servicio fue rechazado.
            print("RESULTADO: Servicio rechazado por tarifa negativa.")

        # Comprobamos si el servicio fue aceptado.
        else:

            # Informamos el resultado del registro.
            print("RESULTADO: Servicio registrado.")

    # Capturamos la excepción de tarifa negativa.
    except Exception as e:

        # Mostramos el mensaje del error.
        print("RESULTADO: Servicio rechazado correctamente.")
        print("DETALLE:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Operación 7: tarifa negativa.")

    # ========================================================
    # OPERACIONES 8, 9, 10, 11 Y 12: GESTIÓN DE RESERVAS
    # ========================================================

    # --------------------------------------------------------
    # OPERACIÓN 8: RESERVA EXITOSA DE UNA SALA
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Reserva exitosa de sala")

    # Intentamos crear, confirmar y procesar la reserva.
    try:

        # Creamos una reserva de dos horas para el primer cliente.
        reserva1 = sistema.crear_reserva(
            cliente1,
            sala,
            duracion_horas=2
        )

        # Comprobamos que la reserva haya sido creada.
        if reserva1 is not None:

            # Confirmamos y procesamos el pago con un descuento del 10%.
            total = sistema.procesar_reserva(
                reserva1,
                descuento=0.10,
                impuesto=0.19
            )

            # Comprobamos si el pago fue procesado.
            if total is not None:

                # Mostramos el resultado de la operación.
                print("RESULTADO: Reserva confirmada y pago procesado.")
                print("TOTAL PAGADO:", total)

            # Informamos si el procesamiento falló.
            else:

                # Mostramos que no se completó el pago.
                print("RESULTADO: La reserva se creó, pero el pago falló.")

        # Informamos si no se pudo crear la reserva.
        else:

            # Mostramos el resultado de la creación fallida.
            print("RESULTADO: No se pudo crear la reserva.")

    # Capturamos cualquier error de la operación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 8.")

    # --------------------------------------------------------
    # OPERACIÓN 9: RESERVA EXITOSA DE EQUIPOS
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Reserva exitosa de equipos")

    # Intentamos crear, confirmar y procesar la segunda reserva.
    try:

        # Creamos una reserva de equipos durante dos horas.
        reserva2 = sistema.crear_reserva(
            cliente2,
            equipo,
            duracion_horas=2
        )

        # Comprobamos que la reserva haya sido creada.
        if reserva2 is not None:

            # Confirmamos la reserva y procesamos el pago.
            total = sistema.procesar_reserva(
                reserva2,
                descuento=0.05,
                impuesto=0.19
            )

            # Comprobamos si el pago se procesó correctamente.
            if total is not None:

                # Mostramos el resultado de la operación.
                print("RESULTADO: Reserva de equipos confirmada.")
                print("TOTAL PAGADO:", total)

            # Informamos si el procesamiento del pago falló.
            else:

                # Mostramos el mensaje correspondiente.
                print("RESULTADO: No se pudo procesar el pago.")

        # Informamos si no se pudo crear la reserva.
        else:

            # Mostramos el resultado de la creación fallida.
            print("RESULTADO: No se pudo crear la reserva.")

    # Capturamos cualquier error de la operación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 9.")

    # --------------------------------------------------------
    # OPERACIÓN 10: RESERVA CON SERVICIO NO DISPONIBLE
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Reserva con servicio no disponible")

    # Intentamos realizar una reserva con un servicio deshabilitado.
    try:

        # Comprobamos que la sala exista.
        if sala is None:

            # Informamos que no se puede realizar esta prueba.
            print("RESULTADO: No existe una sala registrada para la prueba.")

        # Continuamos cuando la sala está disponible como objeto.
        else:

            # Guardamos el estado original de disponibilidad.
            disponibilidad_original = sala.disponible

            # Deshabilitamos temporalmente el servicio.
            sala.disponible = False

            # Intentamos crear una reserva con la sala no disponible.
            try:

                # Intentamos crear una reserva para el segundo cliente.
                reserva_no_disponible = sistema.crear_reserva(
                    cliente2,
                    sala,
                    duracion_horas=1
                )

                # Comprobamos si el sistema rechazó la reserva.
                if reserva_no_disponible is None:

                    # Informamos que el servicio fue rechazado.
                    print("RESULTADO: Reserva rechazada por falta de disponibilidad.")

                # Informamos si el sistema aceptó incorrectamente la reserva.
                else:

                    # Mostramos el resultado obtenido.
                    print("RESULTADO: Reserva creada.")

            # Capturamos errores durante el intento de reserva.
            except Exception as e:

                # Mostramos el error producido.
                print("RESULTADO: Reserva rechazada.")
                print("DETALLE:", e)

                # Registramos el error en el archivo de eventos.
                logger.exception("Operación 10: servicio no disponible.")

            # Restauramos la disponibilidad original de la sala.
            finally:

                # Devolvemos el servicio a su estado anterior.
                sala.disponible = disponibilidad_original

                # Registramos la restauración del servicio.
                logger.info("Disponibilidad de la sala restaurada.")

    # Capturamos cualquier error inesperado de la operación.
    except Exception as e:

        # Mostramos el error producido.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 10.")

    # --------------------------------------------------------
    # OPERACIÓN 11: RESERVA CON DURACIÓN NEGATIVA
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Reserva con duración negativa")

    # Intentamos crear una reserva con una duración incorrecta.
    try:

        # Intentamos crear una reserva con duración de -3 horas.
        reserva_invalida = sistema.crear_reserva(
            cliente1,
            equipo,
            duracion_horas=-3
        )

        # Comprobamos si la reserva fue rechazada.
        if reserva_invalida is None:

            # Informamos que la duración fue rechazada.
            print("RESULTADO: Reserva rechazada por duración negativa.")

        # Comprobamos si la reserva fue aceptada.
        else:

            # Mostramos el resultado obtenido.
            print("RESULTADO: Reserva creada.")

    # Capturamos el error generado por la duración incorrecta.
    except Exception as e:

        # Mostramos el mensaje del error.
        print("RESULTADO: Duración inválida detectada.")
        print("DETALLE:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Operación 11: duración negativa.")

    # --------------------------------------------------------
    # OPERACIÓN 12: CREACIÓN Y CANCELACIÓN DE UNA RESERVA
    # --------------------------------------------------------

    # Incrementamos el contador de operaciones.
    operaciones += 1

    # Mostramos el número y la descripción de la operación.
    print(f"\n[OPERACIÓN {operaciones}/12] Cancelación de una reserva")

    # Intentamos crear y cancelar una reserva.
    try:

        # Creamos una reserva válida para el segundo cliente.
        reserva_cancelada = sistema.crear_reserva(
            cliente2,
            asesoria,
            duracion_horas=1
        )

        # Comprobamos que la reserva haya sido creada.
        if reserva_cancelada is not None:

            # Cancelamos la reserva antes de procesar el pago.
            resultado = reserva_cancelada.cancelar()

            # Comprobamos si la cancelación fue exitosa.
            if resultado:

                # Informamos que la reserva fue cancelada.
                print("RESULTADO: Reserva cancelada correctamente.")

                # Mostramos el estado final de la reserva.
                print("ESTADO FINAL:", reserva_cancelada.estado)

            # Informamos si la cancelación fue rechazada.
            else:

                # Mostramos el resultado de la operación.
                print("RESULTADO: No se pudo cancelar la reserva.")

        # Informamos si no se pudo crear la reserva.
        else:

            # Mostramos el resultado de la creación fallida.
            print("RESULTADO: No se pudo crear la reserva para cancelar.")

    # Capturamos cualquier error durante la operación.
    except Exception as e:

        # Mostramos el mensaje del error.
        print("ERROR:", e)

        # Registramos el error en el archivo de eventos.
        logger.exception("Error en la operación 12.")

    # ========================================================
    # RESUMEN FINAL DE LA SIMULACIÓN
    # ========================================================

    # Mostramos una línea de separación.
    print("\n" + "=" * 60)

    # Mostramos el título del resumen.
    print("             RESUMEN FINAL DEL SISTEMA")

    # Mostramos una línea de separación.
    print("=" * 60)

    # Mostramos el total de operaciones ejecutadas.
    print("Operaciones ejecutadas:", operaciones)

    # Mostramos el resumen de clientes, servicios y reservas.
    print(sistema.obtener_resumen_sistema())

    # Mostramos los clientes registrados.
    print("\nCLIENTES REGISTRADOS:")

    # Recorremos la lista de clientes del controlador.
    for cliente in sistema.obtener_clientes():

        # Mostramos el nombre de cada cliente.
        print("-", cliente.nombre)

    # Mostramos los servicios registrados.
    print("\nSERVICIOS REGISTRADOS:")

    # Recorremos la lista de servicios del controlador.
    for servicio in sistema.obtener_servicios():

        # Mostramos el nombre de cada servicio.
        print("-", servicio.nombre)

    # Mostramos las reservas registradas.
    print("\nRESERVAS REGISTRADAS:")

    # Recorremos todas las reservas almacenadas.
    for reserva in sistema.obtener_reservas():

        # Mostramos el resumen de cada reserva.
        print("-", reserva.obtener_resumen())

    # Registramos la finalización de la simulación.
    logger.info(
        "Simulación finalizada. Total de operaciones ejecutadas: %s",
        operaciones
    )

    # Mostramos el mensaje de finalización.
    print("\nSIMULACIÓN FINALIZADA CORRECTAMENTE.")

    # Informamos dónde quedaron almacenados los eventos.
    print("Los eventos y errores están registrados en sistema_eventos.log")

    # Mostramos la última línea de separación.
    print("=" * 60)


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================

# Comprobamos que el archivo se ejecute directamente.
if __name__ == "__main__":

    # Ejecutamos la simulación principal del sistema.
    ejecutar_sistema()
