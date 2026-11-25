class Tarea:
    def __init__(self, titulo, prioridad="baja", completada=False):
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = completada

    def marcar_completada(self):
        self.completada = True


class ListaTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self._tareas = []

    def agregar_tarea(self, tarea):
        self._tareas.append(tarea)

    def listar_pendientes(self):
        return [tarea for tarea in self._tareas if not tarea.completada]

    def contar_por_prioridad(self, prioridad):
        return sum(1 for tarea in self._tareas if tarea.prioridad == prioridad)