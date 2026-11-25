class Libro:
    def __init__(self, titulo, autor, paginas, leidas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self._progreso = leidas

    def leer(self, cantidad):
        if cantidad > 0 and self._progreso + cantidad <= self.paginas:
            self._progreso += cantidad
        else:
            print("Cantidad inválida")

    def progreso(self):
        if self.paginas == 0:
            return 0
        return round((self._progreso / self.paginas) * 100)

    def resumen(self):
        porcentaje = self.progreso()
        return (
            f"{self.titulo} - {self.autor} ({porcentaje}%): "
            f"{self._progreso} páginas leídas de {self.paginas}"
        )