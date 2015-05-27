# pedidos = Conexion con Interfaz Jugador
# Dados = Conexion con Dados
# listado_inicial conexion con ListadoCartas

class Jugador(object):
    """Representa a un jugador manejado por un usuario.
    Todo el manejo para pedirle y mostrarle cosas al usuario se hace utilizando su atributo "pedidos"
    que se encarga de dichas tareas.
    En este modulo no puede haber ninguna funcion raw_input ni print, ni ninguna semejante."""

    def __init__(self, nombre, posicion_inicial, listado_inicial, dados, pedidos):
        """Recibe su nombre, una posicion inicial, un listado ya inicializado, los dados a usar
        y alguien que le permita hacerle pedidos al usuario, de la manera que corresponda."""
	#Notes : Nombre = String ; posicion_inicial integer, listado_inicial = lista, dados = lista de objetos
	self.nombre = nombre
	self.pos = posicion_inicial
	self.lista_cartas = listado_inicial
	self.dados = dados[:]
	self.pedidos = pedidos # Referencia a interfaz_jugador de cada jugador!
	
    def get_nombre(self):
        """Devuelve el nombre del jugador"""
        return self.nombre

    def __eq___(self, otro):
        """Verifica si un jugador es igual a otro jugador.
        Dos jugadores son iguales cuando tienen el mismo nombre"""
        return (self.nombre == otro.nombre)

    def asignar_carta(self, carta):
        """Se le asigna una carta a la mano del jugador. Este la marca como vista en su listado
        de cartas."""
	self.lista_cartas.sacar_carta(carta)
    
    def get_posicion(self):
        """Obtiene la posicion del jugador."""
	return self.pos

    def alguna_carta(self, jugada):
        """Se fija si el jugador tiene alguna de las cartas indicadas en la jugada.
        Parametros:
            - jugada: iterable con cartas.
        Salida: si tiene al menos una de las cartas, debe preguntarle al usuario cual
        prefiere mostrarle. Si no tiene ninguna, devuelve None."""
	cartas_a_mostrar = list( set(str(self.lista_cartas).split(",")) & set(jugada) )
		
	return self.pedidos.pedir_carta_a_mostrar(self, cartas_a_mostrar) if cartas_a_mostrar else None
		
    def arriesgar(self):
        """Devuelve arriesgo del usuario (personaje, arma, jugador), o None si no desea arriesgarse."""
        return self.pedidos.preguntar_arriesgo()

    def mover(self, tablero):
        """Lanza los dados y se mueve en algun sentido por el tablero. Le muestra al usuario el resultado de
        haber lanzado los dados, y le pide el sentido en el que debe moverse."""
	lista_de_dados = [ dados_user.lanzar() for dados_user in self.dados ]
	self.pedidos.mostrar_dados(lista_de_dados)
	self.pedidos.pedir_sentido()
	self.pos = sum(lista_de_dados)

    def sugerir(self, tablero, otros_jugadores):
        """Si esta en algun lugar para hacer sugerencias, le pregunta al usuario si desea hacer una.
        En caso afirmativo, le muestra la mano al jugador, le muestra el listado de cartas que aun no vio, 
        le pide la jugada, y le consulta al resto de los jugadores si tiene alguna
        de las cartas.
        Parametros:
            - tablero: tablero del juego.
            - otros_jugadores: un iterable con los demas jugadores, en el orden en el que se les debe consultar."""
        if tablero[self.pos] == None:
		return

	respuesta = self.pedidos.quiere_consultar(tablero[self.pos])

	if not respuesta:
		return

	self.pedidos.mostrar_mano(str(self.lista_cartas).split(","))
	self.pedidos.mostrar_listado(self.lista_cartas.obtener_no_vistas())

	posible_pj = self.pedidos.pedir_personaje()
	posible_arma = self.pedidos.pedir_arma()
	posible_lugar = self.pedidos.pedir_lugar()
	jugada_final = [posible_pj, posible_arma, posible_lugar]

	for jugadores_en_partida in otros_jugadores:
		carta = jugadores_en_partida.alguna_carta(jugada_final)
		if carta != None:
			self.pedidos.mostrar_carta(jugadores_en_partida, carta)
			return

	self.pedidos.mostrar_no_hay_cartas()
