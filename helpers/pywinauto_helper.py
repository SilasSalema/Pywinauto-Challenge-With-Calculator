# pywinauto_helper.py


def click_button(calc_window, name):
    """
    Clica em um botão da calculadora.
    :param calc_window: janela da calculadora (UIAWrapper)
    :param name: nome do botão (ex: '1', 'Plus', 'Equals')
    """
    for btn in calc_window.descendants(control_type="Button"):
        if name.lower() in btn.window_text().lower():
            btn.invoke()
            return
    print(f"Botão '{name}' não encontrado!")


def get_result(calc_window):
    """
    Retorna o resultado atual da calculadora.
    :param calc_window: janela da calculadora (UIAWrapper)
    """
    for txt in calc_window.descendants(control_type="Text"):
        if (
            "display" in txt.window_text().lower()
            or "a exibição é" in txt.window_text().lower()
        ):
            result_text = txt.window_text()
            return result_text.replace("Display is ", "").replace("A exibição é ", "")
    return None
