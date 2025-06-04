class ConversorTemperatura:
    @staticmethod
    def celsius_para_fahrenheit(c):
        return (c * 1.8) + 32

    @staticmethod
    def fahrenheit_para_celsius(f):
        if not ConversorTemperatura.__validar(f):
            raise ValueError("O valor deve ser numérico.")
        return (f - 32) / 1.8

    @staticmethod
    def __validar_minimo(valor,minimo):
        return valor >= minimo
