
class ListadoCartas(object):
    """Representa el listado de cartas que un jugador aun no visualizo. Permite llevar cuenta de las cartas
    que ya se vieron, para saber cuales conviene consultar."""

    def __init__(self, personajes_inicial, armas_inicial, lugares_inicial):
        """Recibe un iterable para las cartas de personajes, armas y lugares."""
        # En ningun lado se especifica que deba ser la misma longitud para los tres parametros.
        #if len(personajes_inicial) != len(armas_inicial) != len(lugares_inicial):
        #    raise ValueError("La de personajes, armas y lugares debe ser igual")

        listado_inicial = personajes_inicial + armas_inicial + lugares_inicial
        self.listado = {carta: False for carta in listado_inicial}
        self.mano = []

    def __str__(self):
        """Convierte el listado en una cadena"""
        return ",".join(self.listado.keys())

    def obtener_no_vistas(self):
    	"""Devuelve las cartas aun no vistas"""
    	return [carta for carta in self.listado.keys() if self.listado[carta] == False]

    def obtener_mano(self):
        """Devuelve la mano de cartas del jugador."""
        return self.mano[:]

    def asignar_carta(self, carta):
        """Agrega una determinada carta de los listados de personajes, armas y lugares a la mano del jugador."""
        self.mano.append(carta)
        # Marcarla como vista
        self.listado[carta] = True

    def sacar_carta(self, carta):
        """Saca una determinada carta de los listados de personajes, armas y lugares (los marca como "vistos")"""
        self.listado[carta] = True
