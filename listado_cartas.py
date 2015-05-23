
class ListadoCartas(object):
    """Representa el listado de cartas que un jugador aun no visualizo. Permite llevar cuenta de las cartas
    que ya se vieron, para saber cuales conviene consultar."""

    def __init__(self, personajes_inicial, armas_inicial, lugares_inicial):
        """Recibe un iterable para las cartas de personajes, armas y lugares."""
        listado_inicial = personajes_inicial + armas_inicial + lugares_inicial
        self.listado = {carta: False for carta in listado_inicial}

    def __str__(self):
        """Convierte el listado en una cadena"""
        return ",".join(self.listado.keys())

    def obtener_no_vistas(self):
    	"""Devuelve las cartas aun no vistas"""
    	return [carta for carta in self.listado.keys() if self.listado[carta] == False]

    def sacar_carta(self, carta):
        """Saca una determinada carta de los listados de personajes, armas y lugares (los marca como "vistos")"""
        self.listado[carta] = False
