# ============================================================
# MÓDULO: servicios.py
# DESCRIPCIÓN: Define los servicios disponibles en el sistema,
# sus características y los métodos para calcular sus costos.
# ============================================================

# Importamos ABC y abstractmethod para definir clases abstractas.
from abc import ABC, abstractmethod

# Importamos isfinite para comprobar que los números sean válidos.
from math import isfinite

# Importamos la clase Entidad desde el segundo módulo.
from modelos_base import Entidad

# Importamos el logger y las excepciones personalizadas del sistema.
from excepciones_y_logs import (
    logger,
    DatosInvalidosError,
    ParametroFaltanteError,
    CalculoInconsistenteError,
    ServicioNoDisponibleError
)

# ============================================================
# CLASE ABSTRACTA: SERVICIO
# ============================================================

# Definimos Servicio como una clase abstracta que hereda de Entidad.
class Servicio(Entidad):

    # Constructor de la clase Servicio.
    def __init__(self, nombre, tarifa_base, disponible=True, identificador=None):

        # Inicializamos los atributos heredados de Entidad.
        super().__init__(identificador)

        # Inicializamos los atributos privados del servicio.
        self.__nombre = None
        self.__tarifa_base = None
        self.__disponible = None

        # Asignamos el nombre utilizando su propiedad y setter.
        self.nombre = nombre

        # Asignamos la tarifa base utilizando su propiedad y setter.
        self.tarifa_base = tarifa_base

        # Asignamos la disponibilidad utilizando su propiedad y setter.
        self.disponible = disponible

    # ========================================================
    # PROPIEDAD: NOMBRE
    # ========================================================

    # Creamos una propiedad para consultar el nombre del servicio.
    @property
    def nombre(self):

        # Devolvemos el nombre almacenado en el atributo privado.
        return self.__nombre

    # Creamos el setter para modificar y validar el nombre.
    @nombre.setter
    def nombre(self, valor):

        # Comprobamos si el nombre está ausente o vacío.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción si falta el nombre.
            raise ParametroFaltanteError("El nombre del servicio es obligatorio.")

        # Comprobamos que el nombre sea una cadena de texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción si el tipo de dato es incorrecto.
            raise DatosInvalidosError("El nombre del servicio debe ser texto.")

        # Eliminamos los espacios innecesarios del nombre.
        valor = valor.strip()

        # Guardamos el nombre validado en el atributo privado.
        self.__nombre = valor

    # ========================================================
    # PROPIEDAD: TARIFA BASE
    # ========================================================

    # Creamos una propiedad para consultar la tarifa base.
    @property
    def tarifa_base(self):

        # Devolvemos el valor almacenado en el atributo privado.
        return self.__tarifa_base

    # Creamos el setter para modificar y validar la tarifa base.
    @tarifa_base.setter
    def tarifa_base(self, valor):

        # Comprobamos si la tarifa no fue proporcionada.
        if valor is None:

            # Lanzamos una excepción cuando falta la tarifa.
            raise ParametroFaltanteError("La tarifa base es obligatoria.")

        # Comprobamos que la tarifa sea un número válido.
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):

            # Lanzamos una excepción si la tarifa no es numérica.
            raise DatosInvalidosError("La tarifa base debe ser numérica.")

        # Comprobamos que la tarifa no sea infinita ni NaN.
        if not isfinite(valor):

            # Lanzamos una excepción si el valor no es finito.
            raise DatosInvalidosError("La tarifa base debe ser un número finito.")

        # Comprobamos que la tarifa no sea negativa.
        if valor < 0:

            # Lanzamos una excepción si la tarifa es negativa.
            raise DatosInvalidosError("La tarifa base no puede ser negativa.")

        # Guardamos la tarifa validada en el atributo privado.
        self.__tarifa_base = float(valor)

    # ========================================================
    # PROPIEDAD: DISPONIBILIDAD
    # ========================================================

    # Creamos una propiedad para consultar la disponibilidad.
    @property
    def disponible(self):

        # Devolvemos el estado de disponibilidad del servicio.
        return self.__disponible

    # Creamos el setter para modificar y validar la disponibilidad.
    @disponible.setter
    def disponible(self, valor):

        # Comprobamos que el valor sea verdadero o falso.
        if not isinstance(valor, bool):

            # Lanzamos una excepción si el valor no es booleano.
            raise DatosInvalidosError("La disponibilidad debe ser True o False.")

        # Guardamos el estado de disponibilidad.
        self.__disponible = valor

    # ========================================================
    # MÉTODO: VALIDAR
    # ========================================================

    # Implementamos el método abstracto heredado de Entidad.
    def validar(self):

        # Comprobamos que el nombre del servicio tenga contenido.
        if not self.__nombre:

            # Lanzamos una excepción cuando falta el nombre.
            raise ParametroFaltanteError("El nombre del servicio es obligatorio.")

        # Comprobamos que la tarifa base exista.
        if self.__tarifa_base is None:

            # Lanzamos una excepción cuando falta la tarifa.
            raise ParametroFaltanteError("La tarifa base es obligatoria.")

        # Comprobamos que la tarifa sea un valor numérico no negativo.
        if not isfinite(self.__tarifa_base) or self.__tarifa_base < 0:

            # Lanzamos una excepción cuando la tarifa no es válida.
            raise DatosInvalidosError("La tarifa base no es válida.")

        # Comprobamos que la disponibilidad sea de tipo booleano.
        if not isinstance(self.__disponible, bool):

            # Lanzamos una excepción si la disponibilidad es incorrecta.
            raise DatosInvalidosError("El estado de disponibilidad no es válido.")

        # Indicamos que las validaciones generales fueron exitosas.
        return True

    # ========================================================
    # MÉTODO AUXILIAR: CALCULAR TOTAL
    # ========================================================

    # Creamos un método protegido para calcular el costo final.
    def _calcular_total(self, subtotal, descuento=0.0, impuesto=0.19):

        # Comprobamos que el descuento sea un número válido.
        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):

            # Lanzamos una excepción si el descuento no es numérico.
            raise DatosInvalidosError("El descuento debe ser numérico.")

        # Comprobamos que el impuesto sea un número válido.
        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):

            # Lanzamos una excepción si el impuesto no es numérico.
            raise DatosInvalidosError("El impuesto debe ser numérico.")

        # Comprobamos que el subtotal sea un número finito.
        if not isinstance(subtotal, (int, float)) or isinstance(subtotal, bool) or not isfinite(subtotal):

            # Lanzamos una excepción si el subtotal no es válido.
            raise CalculoInconsistenteError("El subtotal del servicio no es válido.")

        # Comprobamos que el descuento esté entre cero y uno.
        if not isfinite(descuento) or descuento < 0 or descuento > 1:

            # Lanzamos una excepción si el descuento está fuera del rango permitido.
            raise DatosInvalidosError("El descuento debe estar entre 0.0 y 1.0.")

        # Comprobamos que el impuesto no sea negativo ni infinito.
        if not isfinite(impuesto) or impuesto < 0:

            # Lanzamos una excepción si el impuesto no es válido.
            raise DatosInvalidosError("El impuesto no puede ser negativo.")

        # Aplicamos el descuento al subtotal del servicio.
        subtotal_descuento = subtotal * (1 - descuento)

        # Aplicamos el impuesto al subtotal después del descuento.
        costo_final = subtotal_descuento * (1 + impuesto)

        # Comprobamos que el resultado no sea negativo ni infinito.
        if not isfinite(costo_final) or costo_final < 0:

            # Lanzamos la excepción personalizada de cálculo inconsistente.
            raise CalculoInconsistenteError("El costo calculado no puede ser negativo o inválido.")

        # Registramos el cálculo realizado en el sistema de logs.
        logger.info("Costo calculado para %s: %.2f", self.__nombre, costo_final)

        # Devolvemos el costo final del servicio.
        return round(costo_final, 2)

    # ========================================================
    # MÉTODO ABSTRACTO: CALCULAR COSTO
    # ========================================================

    # Declaramos el método abstracto para calcular el costo del servicio.
    @abstractmethod
    def calcular_costo(self, descuento=0.0, impuesto=0.19):

        # Obligamos a las clases hijas a implementar su propio cálculo.
        pass

    # ========================================================
    # MÉTODO ABSTRACTO: DESCRIBIR SERVICIO
    # ========================================================

    # Declaramos el método abstracto para describir el servicio.
    @abstractmethod
    def describir_servicio(self):

        # Obligamos a las clases hijas a implementar su descripción.
        pass

    # ========================================================
    # MÉTODO: OBTENER RESUMEN
    # ========================================================

    # Implementamos el método abstracto heredado de Entidad.
    def obtener_resumen(self):

        # Devolvemos un resumen general del servicio.
        return (
            f"ID: {self._id} | "
            f"Nombre: {self.__nombre} | "
            f"Tarifa base: {self.__tarifa_base:.2f} | "
            f"Disponible: {self.__disponible} | "
            f"Fecha de creación: {self._fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Descripción: {self.describir_servicio()}"
        )


# ============================================================
# CLASE: RESERVASALA
# ============================================================

# Definimos ReservaSala como una clase que hereda de Servicio.
class ReservaSala(Servicio):

    # Constructor de la clase ReservaSala.
    def __init__(self, nombre, tarifa_base, capacidad, tiene_proyector, disponible=True, identificador=None):

        # Inicializamos los atributos generales de la clase Servicio.
        super().__init__(nombre, tarifa_base, disponible, identificador)

        # Inicializamos los atributos privados de la sala.
        self.__capacidad = None
        self.__tiene_proyector = None

        # Asignamos la capacidad mediante su setter.
        self.capacidad = capacidad

        # Asignamos la disponibilidad del proyector mediante su setter.
        self.tiene_proyector = tiene_proyector

        # Validamos todos los datos de la reserva de sala.
        self.validar()

        # Registramos la creación exitosa de la reserva de sala.
        logger.info("Servicio de reserva de sala creado: %s", self.nombre)

    # Creamos una propiedad para consultar la capacidad de la sala.
    @property
    def capacidad(self):

        # Devolvemos la capacidad almacenada.
        return self.__capacidad

    # Creamos el setter para validar la capacidad.
    @capacidad.setter
    def capacidad(self, valor):

        # Comprobamos que la capacidad haya sido proporcionada.
        if valor is None:

            # Lanzamos una excepción cuando falta la capacidad.
            raise ParametroFaltanteError("La capacidad de la sala es obligatoria.")

        # Comprobamos que la capacidad sea un entero positivo.
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:

            # Lanzamos una excepción si la capacidad no es válida.
            raise DatosInvalidosError("La capacidad debe ser un entero mayor que cero.")

        # Guardamos la capacidad validada.
        self.__capacidad = valor

    # Creamos una propiedad para consultar si tiene proyector.
    @property
    def tiene_proyector(self):

        # Devolvemos el estado del proyector.
        return self.__tiene_proyector

    # Creamos el setter para validar el proyector.
    @tiene_proyector.setter
    def tiene_proyector(self, valor):

        # Comprobamos que el valor sea booleano.
        if not isinstance(valor, bool):

            # Lanzamos una excepción si el dato no es válido.
            raise DatosInvalidosError("El proyector debe indicarse con True o False.")

        # Guardamos el estado del proyector.
        self.__tiene_proyector = valor

    # Sobrescribimos el método validar de la clase Servicio.
    def validar(self):

        # Ejecutamos primero las validaciones generales del servicio.
        super().validar()

        # Comprobamos que la capacidad sea válida.
        if self.__capacidad is None or self.__capacidad <= 0:

            # Lanzamos una excepción si la capacidad es incorrecta.
            raise DatosInvalidosError("La capacidad de la sala no es válida.")

        # Comprobamos que el proyector tenga un valor booleano.
        if not isinstance(self.__tiene_proyector, bool):

            # Lanzamos una excepción si el proyector no tiene un estado válido.
            raise DatosInvalidosError("El estado del proyector no es válido.")

        # Confirmamos que los datos de la sala son correctos.
        return True

    # Sobrescribimos el método calcular_costo para las salas.
    def calcular_costo(self, descuento=0.0, impuesto=0.19):

        # Comprobamos que el servicio esté disponible.
        if not self.disponible:

            # Lanzamos una excepción si la sala no está disponible.
            raise ServicioNoDisponibleError("La sala solicitada no está disponible.")

        # Validamos los atributos propios de la sala.
        self.validar()

        # Partimos de la tarifa base de la reserva.
        subtotal = self.tarifa_base

        # Aplicamos un recargo del 10% si la sala tiene proyector.
        if self.__tiene_proyector:

            # Incrementamos el subtotal por el uso del proyector.
            subtotal *= 1.10

        # Calculamos el costo final aplicando descuento e impuesto.
        return self._calcular_total(subtotal, descuento, impuesto)

    # Sobrescribimos el método describir_servicio para las salas.
    def describir_servicio(self):

        # Construimos una descripción con las características de la sala.
        return (
            f"Reserva de sala con capacidad para {self.__capacidad} personas. "
            f"Proyector: {'Sí' if self.__tiene_proyector else 'No'}."
        )


# ============================================================
# CLASE: ALQUILEREQUIPO
# ============================================================

# Definimos AlquilerEquipo como una clase que hereda de Servicio.
class AlquilerEquipo(Servicio):

    # Constructor de la clase AlquilerEquipo.
    def __init__(self, nombre, tarifa_base, tipo_equipo, cantidad_equipos, disponible=True, identificador=None):

        # Inicializamos los atributos generales de Servicio.
        super().__init__(nombre, tarifa_base, disponible, identificador)

        # Inicializamos los atributos privados del equipo.
        self.__tipo_equipo = None
        self.__cantidad_equipos = None

        # Asignamos el tipo de equipo mediante su setter.
        self.tipo_equipo = tipo_equipo

        # Asignamos la cantidad de equipos mediante su setter.
        self.cantidad_equipos = cantidad_equipos

        # Validamos todos los datos del alquiler.
        self.validar()

        # Registramos la creación exitosa del alquiler.
        logger.info("Servicio de alquiler de equipo creado: %s", self.nombre)

    # Creamos una propiedad para consultar el tipo de equipo.
    @property
    def tipo_equipo(self):

        # Devolvemos el tipo de equipo almacenado.
        return self.__tipo_equipo

    # Creamos el setter para validar el tipo de equipo.
    @tipo_equipo.setter
    def tipo_equipo(self, valor):

        # Comprobamos si falta el tipo de equipo.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción si falta el parámetro.
            raise ParametroFaltanteError("El tipo de equipo es obligatorio.")

        # Comprobamos que el tipo de equipo sea texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción si el dato no es una cadena.
            raise DatosInvalidosError("El tipo de equipo debe ser texto.")

        # Guardamos el tipo de equipo eliminando espacios externos.
        self.__tipo_equipo = valor.strip()

    # Creamos una propiedad para consultar la cantidad de equipos.
    @property
    def cantidad_equipos(self):

        # Devolvemos la cantidad de equipos almacenada.
        return self.__cantidad_equipos

    # Creamos el setter para validar la cantidad de equipos.
    @cantidad_equipos.setter
    def cantidad_equipos(self, valor):

        # Comprobamos si falta la cantidad de equipos.
        if valor is None:

            # Lanzamos una excepción si falta el parámetro.
            raise ParametroFaltanteError("La cantidad de equipos es obligatoria.")

        # Comprobamos que la cantidad sea un entero positivo.
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:

            # Lanzamos una excepción si la cantidad no es válida.
            raise DatosInvalidosError("La cantidad de equipos debe ser un entero positivo.")

        # Guardamos la cantidad validada.
        self.__cantidad_equipos = valor

    # Sobrescribimos el método validar de la clase Servicio.
    def validar(self):

        # Ejecutamos las validaciones generales del servicio.
        super().validar()

        # Comprobamos que el tipo de equipo tenga contenido.
        if not self.__tipo_equipo:

            # Lanzamos una excepción si falta el tipo de equipo.
            raise ParametroFaltanteError("El tipo de equipo es obligatorio.")

        # Comprobamos que la cantidad sea un entero positivo.
        if self.__cantidad_equipos is None or self.__cantidad_equipos <= 0:

            # Lanzamos una excepción si la cantidad es incorrecta.
            raise DatosInvalidosError("La cantidad de equipos no es válida.")

        # Confirmamos que los datos del alquiler son correctos.
        return True

    # Sobrescribimos el método calcular_costo para los equipos.
    def calcular_costo(self, descuento=0.0, impuesto=0.19):

        # Comprobamos que el servicio esté disponible.
        if not self.disponible:

            # Lanzamos una excepción si el equipo no está disponible.
            raise ServicioNoDisponibleError("El equipo solicitado no está disponible.")

        # Validamos los atributos propios del alquiler.
        self.validar()

        # Multiplicamos la tarifa base por la cantidad de equipos.
        subtotal = self.tarifa_base * self.__cantidad_equipos

        # Calculamos el costo final aplicando descuento e impuesto.
        return self._calcular_total(subtotal, descuento, impuesto)

    # Sobrescribimos el método describir_servicio para los equipos.
    def describir_servicio(self):

        # Construimos una descripción del alquiler de equipos.
        return (
            f"Alquiler de {self.__cantidad_equipos} unidades "
            f"del equipo: {self.__tipo_equipo}."
        )


# ============================================================
# CLASE: ASESORIAESPECIALIZADA
# ============================================================

# Definimos AsesoriaEspecializada como una clase que hereda de Servicio.
class AsesoriaEspecializada(Servicio):

    # Definimos los multiplicadores según el nivel de complejidad.
    MULTIPLICADORES = {

        # Nivel básico: no aplica recargo adicional.
        "basico": 1.0,

        # Nivel intermedio: aplica un incremento del 50%.
        "intermedio": 1.5,

        # Nivel avanzado: aplica un incremento del 100%.
        "avanzado": 2.0
    }

    # Constructor de la clase AsesoriaEspecializada.
    def __init__(self, nombre, tarifa_base, especialidad, nivel_complejidad, disponible=True, identificador=None):

        # Inicializamos los atributos generales de Servicio.
        super().__init__(nombre, tarifa_base, disponible, identificador)

        # Inicializamos los atributos privados de la asesoría.
        self.__especialidad = None
        self.__nivel_complejidad = None

        # Asignamos la especialidad mediante su setter.
        self.especialidad = especialidad

        # Asignamos el nivel de complejidad mediante su setter.
        self.nivel_complejidad = nivel_complejidad

        # Validamos todos los datos de la asesoría.
        self.validar()

        # Registramos la creación exitosa de la asesoría.
        logger.info("Asesoría especializada creada: %s", self.nombre)

    # Creamos una propiedad para consultar la especialidad.
    @property
    def especialidad(self):

        # Devolvemos la especialidad almacenada.
        return self.__especialidad

    # Creamos el setter para validar la especialidad.
    @especialidad.setter
    def especialidad(self, valor):

        # Comprobamos si falta la especialidad.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción cuando falta el parámetro.
            raise ParametroFaltanteError("La especialidad de la asesoría es obligatoria.")

        # Comprobamos que la especialidad sea texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción si el tipo de dato es incorrecto.
            raise DatosInvalidosError("La especialidad debe ser una cadena de texto.")

        # Guardamos la especialidad eliminando espacios externos.
        self.__especialidad = valor.strip()

    # Creamos una propiedad para consultar el nivel de complejidad.
    @property
    def nivel_complejidad(self):

        # Devolvemos el nivel de complejidad almacenado.
        return self.__nivel_complejidad

    # Creamos el setter para validar el nivel de complejidad.
    @nivel_complejidad.setter
    def nivel_complejidad(self, valor):

        # Comprobamos si falta el nivel de complejidad.
        if valor is None or (isinstance(valor, str) and not valor.strip()):

            # Lanzamos una excepción cuando falta el parámetro.
            raise ParametroFaltanteError("El nivel de complejidad es obligatorio.")

        # Comprobamos que el nivel sea una cadena de texto.
        if not isinstance(valor, str):

            # Lanzamos una excepción si el tipo de dato es incorrecto.
            raise DatosInvalidosError("El nivel de complejidad debe ser texto.")

        # Normalizamos el texto para evitar diferencias por mayúsculas.
        valor = valor.strip().lower()

        # Comprobamos que el nivel esté dentro de las opciones permitidas.
        if valor not in self.MULTIPLICADORES:

            # Lanzamos una excepción si el nivel no está reconocido.
            raise DatosInvalidosError(
                "El nivel debe ser basico, intermedio o avanzado."
            )

        # Guardamos el nivel de complejidad validado.
        self.__nivel_complejidad = valor

    # Sobrescribimos el método validar de la clase Servicio.
    def validar(self):

        # Ejecutamos las validaciones generales del servicio.
        super().validar()

        # Comprobamos que la especialidad tenga contenido.
        if not self.__especialidad:

            # Lanzamos una excepción si falta la especialidad.
            raise ParametroFaltanteError("La especialidad es obligatoria.")

        # Comprobamos que el nivel de complejidad sea válido.
        if self.__nivel_complejidad not in self.MULTIPLICADORES:

            # Lanzamos una excepción si el nivel no está permitido.
            raise DatosInvalidosError("El nivel de complejidad no es válido.")

        # Confirmamos que los datos de la asesoría son correctos.
        return True

    # Sobrescribimos el método calcular_costo para las asesorías.
    def calcular_costo(self, descuento=0.0, impuesto=0.19):

        # Comprobamos que el servicio esté disponible.
        if not self.disponible:

            # Lanzamos una excepción si la asesoría no está disponible.
            raise ServicioNoDisponibleError("La asesoría solicitada no está disponible.")

        # Validamos los atributos propios de la asesoría.
        self.validar()

        # Obtenemos el multiplicador correspondiente al nivel elegido.
        multiplicador = self.MULTIPLICADORES[self.__nivel_complejidad]

        # Calculamos el subtotal según la complejidad de la asesoría.
        subtotal = self.tarifa_base * multiplicador

        # Calculamos el costo final aplicando descuento e impuesto.
        return self._calcular_total(subtotal, descuento, impuesto)

    # Sobrescribimos el método describir_servicio para las asesorías.
    def describir_servicio(self):

        # Construimos una descripción de la asesoría especializada.
        return (
            f"Asesoría en {self.__especialidad} "
            f"con nivel de complejidad {self.__nivel_complejidad}."
        )
