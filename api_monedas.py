import requests


def obtener_valor_indicador():
    url = f"https://mindicador.cl/api/dolar"

    try:
        respuesta = requests.get(url, timeout=10)

        if respuesta.status_code != 200:
            print(f"Error HTTP: {respuesta.status_code}")
            return None

        datos = respuesta.json()
        valor = datos["serie"][0]["valor"]
        return valor

    except requests.RequestException as error:
        print(f"Error de conexión: {error}")
        return None

    except (KeyError, IndexError):
        print("La API respondió con un formato inesperado.")
        return None


def convertir_clp_a_usd(monto_clp):
    valor_dolar = obtener_valor_indicador()

    if valor_dolar is None:
        return None

    return monto_clp / valor_dolar
