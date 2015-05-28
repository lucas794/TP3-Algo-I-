import random

TIPO_DADO_ESTANDAR = "Estandar (todas las caras equiprobables)"
TIPO_DADO_CRECIENTE = "Creciente"
TIPO_DADO_DECRECIENTE = "Decreciente"
TIPO_DADO_TRIANGULAR = "Triangular"
TIPOS_DADOS = [TIPO_DADO_ESTANDAR, TIPO_DADO_CRECIENTE, TIPO_DADO_DECRECIENTE, TIPO_DADO_TRIANGULAR]


class Dado(object):
    """Clase que representa un dado cargado para obtener un numero aleatorio,
    con una probabilidad diferente por cada cara."""

    def __init__(self, prob_dados):
        """Recibe un iterable con las probabilidades de cada resultado del dado (empezando por 1).
        Parametros:
            - prob_dados: un iterable con tantos elementos como dados se quieran tener.
            Cada elemento de prob_dados debe ser un iterable, con tantos elementos como caras se deseen,
            con la probabilidad de aparicion de cada cara. La suma de las probabilidades debe ser 1 (o
            muy similar), sino lanzara una excepcion de tipo ValueError."""
        raise NotImplementedError()

    def obtener_probabilidades(self):
        """Devuelve una copia de las probabilidades de ocurrencia de cada cara del dado."""
        return self.probabilidades[:]

    def lanzar(self):
        """Lanza todos los dados que tiene, con sus probabilidades asignadas, y devuelve la suma de todos
        los resultados de lanzadas"""

        rand = random.random()
        index = 0
        while True:
            probabilidad = self.probabilidades[index]
            if rand < probabilidad :
                return self.probabilidades.index(probabilidad)+1 #Empiezan de 0 los indices
            else:
                rand -= probabilidad

            if index+1 < len(self.probabilidades):
                index += 1
            else:
                index = 0


class DadoEstandar(Dado):
    """Clase que representa un dado con una distribucion de probabilidades estandar."""

    def __init__(self, caras):
    	self.caras = caras
    	self.probabilidades = [1.0/caras for x in xrange(caras)]


class DadoCreciente(Dado):
    """Clase que representa un dado con una distribucion de probabilidades creciente."""
    def __init__(self, caras):
        self.caras = caras
        suma = (caras*(caras+1))/2
        self.probabilidades = [x/float(suma) for x in xrange(1,caras+1)]


class DadoDecreciente(Dado):
    """Clase que representa un dado con una distribucion de probabilidades decreciente."""
    def __init__(self, caras):
        self.caras = caras
        suma = (caras*(caras+1))/2
        self.probabilidades = [x/float(suma) for x in xrange(1,caras+1)]
        self.probabilidades = self.probabilidades[::-1]


class DadoTriangular(Dado):
    """Clase que representa un dado con una distribucion de probabilidades triangular:
    las caras cercanas al valor medio tienen mayor probabilidad, y a medida que nos alejamos
    de dicho valor la probabilidad va disminuyendo."""
    def __init__(self, caras):
        self.caras = caras
        # Si len() es impar meto probabilidades del 1 al len()/2
        # Meto el valor maximo a la posicion del medio
        # Agrego la inversa de lo que tenia hasta antes del medio

        # Si el hdp es par, los dos numeros mas cercanos al medio
        # son los mayores, el resto se repite

        suma = float( (caras*(caras+1))/2 )
        if caras%2 != 0:
            self.probabilidades = [x/suma for x in xrange(1, (caras+1)/2) ]
            self.probabilidades += [(len(self.probabilidades)+1)/suma] + self.probabilidades[::-1]
        else:
            self.probabilidades = [x/suma for x in xrange(1, (caras+1)/2) ] # Redondea para abajo en la division
            val = (len(self.probabilidades)+1)/suma
            self.probabilidades += [val,val] + self.probabilidades[::-1]

GENERADORES = [DadoEstandar, DadoCreciente, DadoDecreciente, DadoTriangular]