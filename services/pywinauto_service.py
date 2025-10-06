# pywinauto_service.py
from pywinauto import Desktop
import subprocess
import time


class CalculatorService:
    def __init__(self):
        self.calc_window = None

    def start_calculator(self):
        """Inicia a Calculadora e conecta à janela principal"""
        subprocess.Popen("calc.exe")
        time.sleep(2)  # espera abrir

        # Localizar a janela da calculadora
        for w in Desktop(backend="uia").windows():
            if (
                "calculadora" in w.window_text().lower()
                or "calculator" in w.window_text().lower()
            ):
                self.calc_window = w
                break

        if not self.calc_window:
            raise Exception("Calculadora não encontrada!")

    def close_calculator(self):
        """Fecha a calculadora"""
        if self.calc_window:
            self.calc_window.close()
            self.calc_window = None
