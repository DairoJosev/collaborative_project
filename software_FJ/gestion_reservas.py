# ============================================================
# MÓDULO: gestion_reservas.py
# DESCRIPCIÓN: Administra clientes, servicios y reservas,
# incluyendo validaciones, confirmaciones y procesamiento de pagos.
# ============================================================

# Importamos la clase Entidad para heredar su estructura.
from modelos_base import Entidad

# Importamos la clase Cliente para gestionar los clientes.
from modelos_base import Cliente

# Importamos la clase Servicio para gestionar los servicios.
from servicios import Servicio

# Importamos el logger y las excepciones personalizadas del sistema.
from excepciones_y_logs import (
    logger,
    ErrorSistemaFJ,
    DatosInvalidosError,
    ParametroFaltanteError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    CalculoInconsistenteError
)

# Importamos isfinite para comprobar que la duración sea un número válido.
from math import isfinite

# ============================================================
# CLASE: RESERVA
# ============================================================

# Definimos Reserva como una clase que hereda de Entidad.
class Reserva(Entidad):

    # Definimos los estados permitidos para las reservas.
    ESTADOS_VALIDOS = ("Pendiente", "Confirmada", "Cancelada")

    # Constructor de la clase Reserva.
    def __init__(self, cliente, servicio, duracion_horas, identificador=None):

        # Inicializamos los atributos heredados de Entidad.
        super().__init__(identificador)

        # Creamos el atributo privado para almacenar el cliente.
        self.__cliente = None

        # Creamos el atributo privado para almacenar el servicio.
        self.__servicio = None

        # Creamos el atributo privado para almacenar la duración.
        self.__duracion_horas = None

        # Inicializamos el estado de la reserva como Pendiente.
        self.__estado = "Pendiente"

        # Inicializamos el indicador de pago como falso.
        self.__pago_procesado = False

        # Asignamos el cliente mediante su propiedad y setter.
        self.cliente = cliente

        # Asignamos el servicio mediante su propiedad y setter.
        self.servicio = servicio

        # Asignamos la duración mediante su propiedad y setter.
        self.duracion_horas = duracion_horas

        # Validamos todos los datos de la reserva.
        self.validar()

        # Registramos la creación exitosa de la reserva.
        logger.info("Reserva creada correctamente. ID: %s", self._id)

    # ========================================================
    # PROPIEDAD: CLIENTE
    # ========================================================

    # Creamos una propiedad para consultar el cliente.
    @property
    def cliente(self):

        # Devolvemos el objeto Cliente asociado a la reserva.
        return self.__cliente

    # Creamos el setter para asignar y validar el cliente.
    @cliente.setter
    def cliente(self, valor):

        # Comprobamos si no se proporcionó ningún cliente.
        if valor is None:

            # Lanzamos una excepción cuando falta el cliente.
            raise ParametroFaltanteError("La reserva requiere un cliente.")

        # Comprobamos que el objeto pertenezca a la clase Cliente.
        if not isinstance(valor, Cliente):

            # Lanzamos una excepción si el objeto no es un cliente.
            raise DatosInvalidosError("El cliente debe ser un objeto de tipo Cliente.")

        # Guardamos el cliente validado.
        self.__cliente = valor

    # ========================================================
    # PROPIEDAD: SERVICIO
    # ========================================================

    # Creamos una propiedad para consultar el servicio.
    @property
    def servicio(self):

        # Devolvemos el objeto Servicio asociado a la reserva.
        return self.__servicio

    # Creamos el setter para asignar y validar el servicio.
    @servicio.setter
    def servicio(self, valor):

        # Comprobamos si no se proporcionó ningún servicio.
        if valor is None:

            # Lanzamos una excepción cuando falta el servicio.
            raise ParametroFaltanteError("La reserva requiere un servicio.")

        # Comprobamos que el objeto pertenezca a Servicio o una clase derivada.
        if not isinstance(valor, Servicio):

            # Lanzamos una excepción si el objeto no es un servicio válido.
            raise DatosInvalidosError("El servicio debe ser un objeto de tipo Servicio.")

        # Guardamos el servicio validado.
        self.__servicio = valor

    # ========================================================
    # PROPIEDAD: DURACION_HORAS
    # ========================================================

    # Creamos una propiedad para consultar la duración.
    @property
    def duracion_horas(self):

        # Devolvemos la duración almacenada.
        return self.__duracion_horas

    # Creamos el setter para asignar y validar la duración.
    @duracion_horas.setter
    def duracion_horas(self, valor):

        # Comprobamos si la duración no fue proporcionada.
        if valor is None:

            # Lanzamos una excepción cuando falta la duración.
            raise ParametroFaltanteError("La duración de la reserva es obligatoria.")

        # Comprobamos que la duración sea un número y no un valor booleano.
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):

            # Lanzamos una excepción si el tipo de dato es incorrecto.
            raise DatosInvalidosError("La duración debe ser un valor numérico.")

        # Comprobamos que la duración sea finita y mayor que cero.
        if not isfinite(valor) or valor <= 0:

            # Lanzamos una excepción si la duración no es válida.
            raise DatosInvalidosError("La duración debe ser mayor que cero y finita.")

        # Guardamos la duración validada como número decimal.
        self.__duracion_horas = float(valor)

    # ========================================================
    # PROPIEDAD: ESTADO
    # ========================================================

    # Creamos una propiedad para consultar el estado de la reserva.
    @property
    def estado(self):

        # Devolvemos el estado actual.
        return self.__estado

    # Creamos una propiedad para consultar si el pago fue procesado.
    @property
    def pago_procesado(self):

        # Devolvemos el indicador de procesamiento del pago.
        return self.__pago_procesado

    # ========================================================
    # MÉTODO: VALIDAR
    # ========================================================

    # Implementamos el método abstracto heredado de Entidad.
    def validar(self):

        # Comprobamos que exista un objeto Cliente válido.
        if not isinstance(self.__cliente, Cliente):

            # Lanzamos una excepción si falta un cliente válido.
            raise ParametroFaltanteError("La reserva debe tener un cliente válido.")

        # Comprobamos que exista un objeto Servicio válido.
        if not isinstance(self.__servicio, Servicio):

            # Lanzamos una excepción si falta un servicio válido.
            raise ParametroFaltanteError("La reserva debe tener un servicio válido.")

        # Validamos los datos internos del cliente.
        try:

            # Ejecutamos la validación del cliente.
            self.__cliente.validar()

        # Capturamos cualquier error personalizado del cliente.
        except ErrorSistemaFJ as e:

            # Encadenamos el error original con una excepción de reserva.
            raise ReservaInvalidaError(
                "No se puede crear la reserva porque el cliente no es válido."
            ) from e

        # Validamos los datos internos del servicio.
        try:

            # Ejecutamos la validación del servicio.
            self.__servicio.validar()

        # Capturamos errores de disponibilidad del servicio.
        except ServicioNoDisponibleError as e:

            # Encadenamos el error original con la excepción de reserva.
            raise ReservaInvalidaError(
                "No se puede reservar porque el servicio no está disponible."
            ) from e

        # Capturamos otros errores de validación del servicio.
        except ErrorSistemaFJ as e:

            # Conservamos el error original mediante encadenamiento.
            raise ReservaInvalidaError(
                "Los datos del servicio no permiten crear la reserva."
            ) from e

        # Comprobamos que el servicio esté disponible.
        if not self.__servicio.disponible:

            # Generamos primero el error específico de disponibilidad.
            try:

                # Lanzamos la excepción que identifica el servicio no disponible.
                raise ServicioNoDisponibleError(
                    "El servicio seleccionado no está disponible."
                )

            # Capturamos el error para encadenarlo con la reserva.
            except ServicioNoDisponibleError as e:

                # Lanzamos la excepción de reserva conservando el error original.
                raise ReservaInvalidaError(
                    "No es posible crear una reserva con un servicio no disponible."
                ) from e

        # Validamos la duración de la reserva.
        try:

            # Comprobamos que la duración sea numérica y positiva.
            if (
                isinstance(self.__duracion_horas, bool)
                or not isinstance(self.__duracion_horas, (int, float))
                or not isfinite(self.__duracion_horas)
                or self.__duracion_horas <= 0
            ):

                # Generamos el error original de duración inválida.
                raise DatosInvalidosError("La duración de la reserva no es válida.")

        # Capturamos el error de duración para encadenarlo.
        except DatosInvalidosError as e:

            # Lanzamos la excepción de reserva conservando la causa original.
            raise ReservaInvalidaError(
                "La reserva contiene una duración inválida."
            ) from e

        # Comprobamos que el estado pertenezca a los estados permitidos.
        if self.__estado not in self.ESTADOS_VALIDOS:

            # Lanzamos una excepción si el estado no es reconocido.
            raise ReservaInvalidaError("El estado de la reserva no es válido.")

        # Registramos que la validación general fue exitosa.
        logger.info("Validación exitosa de la reserva: %s", self._id)

        # Devolvemos verdadero cuando todos los datos son correctos.
        return True

    # ========================================================
    # MÉTODO: CONFIRMAR
    # ========================================================

    # Creamos el método encargado de confirmar una reserva.
    def confirmar(self):

        # Utilizamos try para controlar errores durante la confirmación.
        try:

            # Validamos nuevamente todos los datos de la reserva.
            self.validar()

            # Comprobamos que la reserva esté pendiente.
            if self.__estado != "Pendiente":

                # Lanzamos una excepción si no se puede confirmar.
                raise ReservaInvalidaError(
                    "Solamente se pueden confirmar reservas pendientes."
                )

            # Cambiamos el estado de la reserva a Confirmada.
            self.__estado = "Confirmada"

        # Capturamos los errores personalizados que puedan producirse.
        except ErrorSistemaFJ as e:

            # Registramos el error de confirmación en el sistema.
            logger.exception("Error al confirmar la reserva %s: %s", self._id, e)

            # Propagamos la excepción para que el controlador pueda gestionarla.
            raise

        # Ejecutamos este bloque cuando la confirmación termina correctamente.
        else:

            # Registramos la confirmación exitosa.
            logger.info("Reserva confirmada correctamente: %s", self._id)

            # Devolvemos verdadero como resultado de la operación.
            return True

        # Ejecutamos finally tanto si ocurre un error como si todo sale bien.
        finally:

            # Registramos la finalización del intento de confirmación.
            logger.info("Finalizó el proceso de confirmación: %s", self._id)

    # ========================================================
    # MÉTODO: CANCELAR
    # ========================================================

    # Creamos el método encargado de cancelar una reserva.
    def cancelar(self):

        # Utilizamos try para controlar errores durante la cancelación.
        try:

            # Comprobamos que la reserva no esté cancelada.
            if self.__estado == "Cancelada":

                # Lanzamos una excepción si ya estaba cancelada.
                raise ReservaInvalidaError("La reserva ya se encuentra cancelada.")

            # Comprobamos que no se haya procesado previamente el pago.
            if self.__pago_procesado:

                # Lanzamos una excepción porque no se implementan reembolsos.
                raise ReservaInvalidaError(
                    "No se puede cancelar una reserva con pago procesado sin gestionar un reembolso."
                )

            # Cambiamos el estado de la reserva a Cancelada.
            self.__estado = "Cancelada"

        # Capturamos los errores personalizados de la cancelación.
        except ErrorSistemaFJ as e:

            # Registramos el error producido durante la cancelación.
            logger.exception("Error al cancelar la reserva %s: %s", self._id, e)

            # Propagamos el error para que el controlador lo capture.
            raise

        # Ejecutamos este bloque cuando la cancelación es exitosa.
        else:

            # Registramos la cancelación en el sistema.
            logger.info("Reserva cancelada correctamente: %s", self._id)

            # Devolvemos verdadero para indicar que se completó la operación.
            return True

        # Ejecutamos finally independientemente del resultado.
        finally:

            # Registramos que terminó el intento de cancelación.
            logger.info("Finalizó el proceso de cancelación: %s", self._id)

    # ========================================================
    # MÉTODO: PROCESAR PAGO
    # ========================================================

    # Creamos el método encargado de simular el procesamiento del pago.
    def procesar_pago(self, descuento=0.0, impuesto=0.19):

        # Utilizamos try para controlar el cálculo y el procesamiento del pago.
        try:

            # Comprobamos que la reserva esté confirmada.
            if self.__estado != "Confirmada":

                # Lanzamos una excepción si la reserva no está confirmada.
                raise ReservaInvalidaError(
                    "El pago solamente puede procesarse para reservas confirmadas."
                )

            # Comprobamos que el pago no se haya procesado anteriormente.
            if self.__pago_procesado:

                # Lanzamos una excepción para evitar pagos duplicados.
                raise ReservaInvalidaError("El pago de esta reserva ya fue procesado.")

            # Obtenemos el costo unitario del servicio.
            costo_servicio = self.__servicio.calcular_costo(
                descuento=descuento,
                impuesto=impuesto
            )

            # Multiplicamos el costo del servicio por la duración reservada.
            costo_total = costo_servicio * self.__duracion_horas

            # Comprobamos que el resultado sea finito y no negativo.
            if not isfinite(costo_total) or costo_total < 0:

                # Lanzamos una excepción si el cálculo presenta inconsistencias.
                raise CalculoInconsistenteError(
                    "El costo total de la reserva no es válido."
                )

        # Capturamos cualquier error personalizado durante el procesamiento.
        except ErrorSistemaFJ as e:

            # Registramos el error ocurrido durante el procesamiento del pago.
            logger.exception("Error al procesar el pago de la reserva %s: %s", self._id, e)

            # Propagamos el error para que el controlador pueda capturarlo.
            raise

        # Ejecutamos este bloque cuando el cálculo termina correctamente.
        else:

            # Marcamos el pago como procesado mediante la simulación del sistema.
            self.__pago_procesado = True

            # Registramos el resultado del pago simulado.
            logger.info(
                "Pago simulado correctamente. Reserva: %s | Total: %.2f",
                self._id,
                costo_total
            )

            # Devolvemos el valor calculado del pago.
            return round(costo_total, 2)

        # Ejecutamos finally independientemente del resultado del proceso.
        finally:

            # Registramos la finalización del intento de procesamiento del pago.
            logger.info("Finalizó el procesamiento del pago: %s", self._id)

    # ========================================================
    # MÉTODO: OBTENER RESUMEN
    # ========================================================

    # Implementamos el método abstracto heredado de Entidad.
    def obtener_resumen(self):

        # Construimos un resumen con los datos principales de la reserva.
        return (
            f"ID: {self._id} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duración: {self.__duracion_horas} horas | "
            f"Estado: {self.__estado} | "
            f"Pago procesado: {self.__pago_procesado} | "
            f"Fecha de creación: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"
        )


# ============================================================
# CLASE: SISTEMAGESTIONFJ
# ============================================================

# Definimos el controlador principal del sistema.
class SistemaGestionFJ:

    # Constructor del controlador del sistema.
    def __init__(self):

        # Creamos una lista interna para almacenar los clientes.
        self.__clientes = []

        # Creamos una lista interna para almacenar los servicios.
        self.__servicios = []

        # Creamos una lista interna para almacenar las reservas.
        self.__reservas = []

        # Registramos el inicio del controlador.
        logger.info("Sistema de gestión FJ inicializado correctamente.")

    # ========================================================
    # MÉTODO: REGISTRAR CLIENTE
    # ========================================================

    # Creamos el método para registrar clientes en el sistema.
    def registrar_cliente(self, cliente):

        # Utilizamos try para controlar los errores de registro.
        try:

            # Comprobamos que el objeto recibido sea un Cliente.
            if not isinstance(cliente, Cliente):

                # Lanzamos una excepción si el objeto no es un cliente.
                raise DatosInvalidosError("El objeto proporcionado no es un cliente válido.")

            # Validamos los datos internos del cliente.
            cliente.validar()

            # Comprobamos que el cliente no esté registrado previamente.
            if any(c._id == cliente._id for c in self.__clientes):

                # Lanzamos una excepción si el cliente ya existe.
                raise DatosInvalidosError("El cliente ya se encuentra registrado.")

            # Agregamos el cliente a la lista interna.
            self.__clientes.append(cliente)

        # Capturamos cualquier excepción personalizada.
        except ErrorSistemaFJ as e:

            # Registramos el error de registro del cliente.
            logger.exception("No se pudo registrar el cliente: %s", e)

            # Devolvemos falso para indicar que el registro falló.
            return False

        # Ejecutamos este bloque si el registro fue exitoso.
        else:

            # Registramos la operación exitosa.
            logger.info("Cliente registrado en el sistema: %s", cliente.nombre)

            # Devolvemos verdadero para confirmar el registro.
            return True

    # ========================================================
    # MÉTODO: AGREGAR SERVICIO
    # ========================================================

    # Creamos el método para agregar servicios al sistema.
    def agregar_servicio(self, servicio):

        # Utilizamos try para controlar los errores del registro.
        try:

            # Comprobamos que el objeto sea un Servicio o una clase derivada.
            if not isinstance(servicio, Servicio):

                # Lanzamos una excepción si el objeto no es un servicio.
                raise DatosInvalidosError("El objeto proporcionado no es un servicio válido.")

            # Validamos los datos del servicio.
            servicio.validar()

            # Comprobamos que el servicio no esté registrado previamente.
            if any(s._id == servicio._id for s in self.__servicios):

                # Lanzamos una excepción si el servicio ya existe.
                raise DatosInvalidosError("El servicio ya se encuentra registrado.")

            # Agregamos el servicio a la lista interna.
            self.__servicios.append(servicio)

        # Capturamos cualquier excepción personalizada.
        except ErrorSistemaFJ as e:

            # Registramos el error al agregar el servicio.
            logger.exception("No se pudo agregar el servicio: %s", e)

            # Devolvemos falso para indicar que la operación falló.
            return False

        # Ejecutamos este bloque cuando el servicio fue agregado.
        else:

            # Registramos el servicio agregado correctamente.
            logger.info("Servicio agregado al sistema: %s", servicio.nombre)

            # Devolvemos verdadero para confirmar la operación.
            return True

    # ========================================================
    # MÉTODO: CREAR RESERVA
    # ========================================================

    # Creamos el método para generar nuevas reservas.
    def crear_reserva(self, cliente, servicio, duracion_horas):

        # Utilizamos try para controlar los posibles errores de creación.
        try:

            # Comprobamos que el cliente esté registrado en el sistema.
            if not any(c._id == cliente._id for c in self.__clientes):

                # Lanzamos una excepción si el cliente no está registrado.
                raise ReservaInvalidaError("El cliente no está registrado en el sistema.")

            # Comprobamos que el servicio esté registrado en el sistema.
            if not any(s._id == servicio._id for s in self.__servicios):

                # Lanzamos una excepción si el servicio no está registrado.
                raise ReservaInvalidaError("El servicio no está registrado en el sistema.")

            # Creamos el objeto Reserva con los datos proporcionados.
            reserva = Reserva(cliente, servicio, duracion_horas)

            # Validamos nuevamente la reserva creada.
            reserva.validar()

            # Agregamos la reserva a la lista interna.
            self.__reservas.append(reserva)

        # Capturamos cualquier error personalizado durante la creación.
        except ErrorSistemaFJ as e:

            # Registramos el error de creación en el archivo de eventos.
            logger.exception("No se pudo crear la reserva: %s", e)

            # Devolvemos None para indicar que no se creó la reserva.
            return None

        # Ejecutamos este bloque cuando la reserva se crea correctamente.
        else:

            # Registramos la creación exitosa de la reserva.
            logger.info("Reserva agregada al sistema: %s", reserva._id)

            # Devolvemos el objeto creado para utilizarlo posteriormente.
            return reserva

    # ========================================================
    # MÉTODO: PROCESAR RESERVA
    # ========================================================

    # Creamos el método para confirmar y procesar una reserva.
    def procesar_reserva(self, reserva, descuento=0.0, impuesto=0.19):

        # Utilizamos try para controlar los errores del procesamiento.
        try:

            # Comprobamos que el objeto sea una Reserva.
            if not isinstance(reserva, Reserva):

                # Lanzamos una excepción si el objeto no es una reserva.
                raise DatosInvalidosError("El objeto proporcionado no es una reserva válida.")

            # Comprobamos que la reserva pertenezca al sistema.
            if not any(r._id == reserva._id for r in self.__reservas):

                # Lanzamos una excepción si la reserva no está registrada.
                raise ReservaInvalidaError("La reserva no pertenece a este sistema.")

            # Confirmamos la reserva antes de procesar el pago.
            reserva.confirmar()

            # Procesamos el pago de la reserva confirmada.
            total = reserva.procesar_pago(descuento, impuesto)

        # Capturamos los errores personalizados del procesamiento.
        except ErrorSistemaFJ as e:

            # Registramos el error sin detener el controlador.
            logger.exception("No se pudo procesar la reserva: %s", e)

            # Devolvemos None para indicar que el procesamiento falló.
            return None

        # Ejecutamos este bloque cuando el procesamiento fue exitoso.
        else:

            # Registramos el resultado final de la operación.
            logger.info("Reserva procesada exitosamente. Total: %.2f", total)

            # Devolvemos el valor del pago calculado.
            return total

    # ========================================================
    # MÉTODOS DE CONSULTA
    # ========================================================

    # Creamos un método para obtener una copia de los clientes.
    def obtener_clientes(self):

        # Devolvemos una copia para evitar modificar la lista interna.
        return self.__clientes.copy()

    # Creamos un método para obtener una copia de los servicios.
    def obtener_servicios(self):

        # Devolvemos una copia para proteger la lista interna.
        return self.__servicios.copy()

    # Creamos un método para obtener una copia de las reservas.
    def obtener_reservas(self):

        # Devolvemos una copia para proteger la lista interna.
        return self.__reservas.copy()

    # ========================================================
    # MÉTODO: MOSTRAR RESUMEN DEL SISTEMA
    # ========================================================

    # Creamos un método para consultar las cantidades registradas.
    def obtener_resumen_sistema(self):

        # Construimos un resumen general de los registros.
        return (
            f"Clientes registrados: {len(self.__clientes)} | "
            f"Servicios registrados: {len(self.__servicios)} | "
            f"Reservas registradas: {len(self.__reservas)}"
        )
