from num2words import num2words


def obter_numero_por_extenso(valor: str) -> str:
    numero_por_extenso = num2words(valor, lang="pt_BR").capitalize()
    return numero_por_extenso


def obter_sinal_por_extenso(sinal: str) -> str:
    sinais = {
        "+": "Mais",
        "-": "Menos",
        "*": "Multiplicar por",
        "x": "Multiplicar por",
        "/": "Dividir por",
        "^": "Elevado a",
        "%": "Por cento",
        "=": "Igual a",
        "C": "Limpar",
    }
    return sinais.get(sinal, "sinal desconhecido")
