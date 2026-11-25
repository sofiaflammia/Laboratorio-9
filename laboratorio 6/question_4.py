class Semaforo:
    _orden = ["rojo", "verde", "amarillo"]

    def __init__(self, color_inicial="rojo"):
        self._color = color_inicial

    def siguiente_estado(self):
        indice_actual = self._orden.index(self._color)
        siguiente_indice = (indice_actual + 1) % len(self._orden)
        self._color = self._orden[siguiente_indice]
        return self._color

    def puede_avanzar(self):
        return self._color == "verde"