from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "veinticinco": 25, "treinta": 30, "cuarenta": 40, "cincuenta": 50, 
            "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90, "media": 0.5
        }
        numero = numeros.get(palabra.lower())
        if numero is not None:
            return numero
        else:
            # Aseguramos que el mensaje sea claro
            raise ValueError(f"No se pudo convertir la palabra '{palabra}' a un número válido.")

@given('que he comido {cantidad_pepinos} pepinos')
def step_given_eaten_varios_cukes(context, cantidad_pepinos):
    try:
        cantidad_pepinos = cantidad_pepinos.strip('"')  # Elimina las comillas si las hay
        if cantidad_pepinos == 'un montón':
            context.belly.comer(20)  # Si dice "un montón", comemos 20 pepinos
        else:
            try:
                pepinos = int(cantidad_pepinos)
            except ValueError:
                # Convertimos la palabra numérica a un número
                pepinos = convertir_palabra_a_numero(cantidad_pepinos)
        
        # Validamos la cantidad de pepinos y alimentamos al estómago
        if pepinos > 50:
            raise ValueError(f"Cantidad no válida de pepinos: {pepinos} excede el límite permitido.")
        elif pepinos <= 0:
            raise ValueError(f"Cantidad no válida de pepinos: {pepinos} debe ser mayor que cero.")
        
        context.belly.comer(pepinos)  # Comemos los pepinos
    except Exception as e:
        context.exception = e  # Capturamos la excepción en el contexto

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    try:
        time_description = time_description.strip('"').lower()
        time_description = time_description.replace('y', ' ')
        time_description = time_description.strip()

        # Manejar casos especiales como 'media hora'
        if time_description == 'media hora':
            total_time_in_hours = 0.5
        else:
            # Expresión regular para extraer horas y minutos
            pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?')
            match = pattern.match(time_description)

            if match:
                hours_word = match.group(1) or "0"
                minutes_word = match.group(2) or "0"

                hours = convertir_palabra_a_numero(hours_word)
                minutes = convertir_palabra_a_numero(minutes_word)

                total_time_in_hours = hours + (minutes / 60)
            else:
                raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")
        
        context.belly.esperar(total_time_in_hours)  # Usamos el método esperar de Belly
    except Exception as e:
        context.exception = e  # Capturamos la excepción en el contexto

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('el sistema debería arrojar un error de cantidad no válida')
def step_then_should_raise_invalid_quantity_error(context):
    assert hasattr(context, 'exception'), "No se produjo un error cuando se esperaba uno."
    assert isinstance(context.exception, ValueError), f"Se esperaba ValueError, pero se obtuvo {type(context.exception)}."
    assert "Cantidad no válida de pepinos" in str(context.exception) or "No se pudo convertir la palabra" in str(context.exception), f"El mensaje de error no es el esperado: {context.exception}"


