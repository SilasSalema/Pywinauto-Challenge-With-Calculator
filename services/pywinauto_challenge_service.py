from concurrent.futures import *
from dotenv import load_dotenv


from services.pywinauto_service import CalculatorService
from helpers.pywinauto_helper import click_button, get_result
from helpers.excel_helper import *
from helpers.utils_helper import *
from helpers.criar_arquivo_log_helper import configurar_arquivo_log
from helpers.tratar_erro_helper import *


class PywinautoChallengeService:
    @tratar_erro
    def __init__(self) -> None:
        load_dotenv()
        self.logging = configurar_arquivo_log()
        self.logging.info("Iniciou Execução")
        self.execucao()
        self.logging.info("Terminou Execução")

    def execucao(self) -> None:
        data_frame = obter_data_frame_do_arquivo_excel()

        service = CalculatorService()
        service.start_calculator()
        calc = service.calc_window
        for numero_linha, dados_linha in data_frame.iterrows():
            valor_1 = str(dados_linha["Valor_1"])
            for caracter in valor_1:
                numero_por_extenso = obter_numero_por_extenso(caracter)
                click_button(calc, numero_por_extenso)
            valor_2 = str(dados_linha["Valor_2"])

            sinal = str(dados_linha["Sinal"])
            sinal_por_extenso = obter_sinal_por_extenso(sinal)
            click_button(calc, sinal_por_extenso)

            for caracter in valor_2:
                numero_por_extenso = obter_numero_por_extenso(caracter)
                click_button(calc, numero_por_extenso)

            sinal_por_extenso = obter_sinal_por_extenso("=")
            click_button(calc, sinal_por_extenso)

            # Obter resultado
            result = get_result(calc)
            self.logging.info(f"Resultado: {result}")

        # Fechar calculadora
        service.close_calculator()
