HORARIO = 0
ANTIHORARIO = 1

SENTIDO_HORARIO = "Horario"
SENTIDO_ANTIHORARIO = "Antihorario"
SENTIDOS = [SENTIDO_HORARIO, SENTIDO_ANTIHORARIO]


class Tablero(object):
    """Representa un tablero circular de un juego con casilleros, en los cuales
    pueden haber espacios vacios, o con lugares."""

    def __init__(self, casilleros, posiciones):
        """Recibe una lista de casilleros. Cada casillero debe contener una cadena
        con el contenido del casillero, en la posicion indicada, o None si no hay nada."""
        if len(casilleros) != len(posiciones):
            raise ValueError("La longitud de casilleros y posiciones no son iguales")

        self.casilleros = casilleros[:]
        self.posiciones = posiciones[:]
    
    def siguiente_sentido_horario(self, pos, movimiento):
        """Devuelve la siguiente posicion en sentido horario.
        Parametros:
            - pos: numero de posicion actual
            - movimiento: cantidad de casilleros a desplazarse.
        Salida: nueva posicion, resultante de moverse en sentido horario
        una cantidad "movimiento" de casilleros"""
        suma = pos + movimiento
        return suma if suma < len(self.casilleros) else int(suma+1 - len(self.casilleros))

    def siguiente_sentido_antihorario(self, pos, movimiento):
        """Devuelve la siguiente posicion en sentido antihorario.
        Parametros:
            - pos: numero de posicion actual
            - movimiento: cantidad de casilleros a desplazarse.
        Salida: nueva posicion, resultante de moverse en sentido antihorario
        una cantidad "movimiento" de casilleros"""
        resta = pos - movimiento
        return resta if resta >= 0 else int(len(self.casilleros) + resta-1)

    def siguiente(self, pos, movimiento, sentido):
        """Devuelve la posicion siguiente en el sentido indicado.
        Parametro:
            - pos: numero de posicion actual.
            - moviemiento: cantidad de casilleros a desplazarse.
            - sentido: HORARIO o ANTIHORARIO, para indicar el sentido deseado.
        Salida: nueva posicion, resultante de moverse en el sentido indicado,
        una cantidad "moviemiento" de casilleros"""
        return self.siguiente_sentido_antihorario(pos, movimiento) if sentido == ANTIHORARIO else self.siguiente_sentido_horario(pos, movimiento)

    def __getitem__(self, pos):
        """Obtiene el contenido del casillero indicado.
        Parametros:
            - pos: numero de casillero del cual se quiere obtener.
        Salida: el lugar que representa a tal casillero, o None si no hay nada."""
        return self.casilleros[pos]

    def __len__(self):
        """Obtiene la cantidad de casilleros del tablero."""
        return len(self.casilleros)

    def posicion_de_casillero(self, casillero):
        """Devuelve una tupla (posicion X, posicion Y) con las posiciones en el mapa
        del casillero recibido por parametro."""
        return self.posiciones[casillero]
