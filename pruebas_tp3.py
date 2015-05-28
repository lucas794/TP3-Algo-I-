
# Importa el paquete para realizar pruebas automatizadas de Python.
import unittest
from unittest import TestCase

# Importa las clases que se van a probar
from dados import *
from tablero import Tablero
from listado_cartas import ListadoCartas

# Definimos una clase que hereda de TestCase por cada Clase que queremos probar.
# Esta clase esta dedicada a probar la clase de DadoEstandar.
class TestDadoEstandar(TestCase):

    # Cada metodo debe probar una funcionalidad de la clase.
    # Este, por ejemplo, verifica que las probabilidades de cada cara son iguales.
    def test_probabilidades_son_equiprobables(self):
        # Dentro de un metodo realizo la prueba:

        # Creo un dado estandar de seis caras.
        dado = DadoEstandar(6)

        # Obtengo sus probabilidades.
        # Este metodo no se usa en el juego pero se agrego para poder correr la prueba.
        probabilidades = dado.obtener_probabilidades()

        prob = probabilidades[0]
        for i in range(1, len(probabilidades)):
            # Se usan los metodos de unittest para hacer verificaciones.
            self.assertEqual(prob, probabilidades[i])

    # Este otro metodo, por ejemplo, verifica que las probabilidades de ocurrencia de
    # cada cara no se puedan modificar.
    def test_probabilidades_no_se_deben_modificar(self):
        dado = DadoEstandar(6)
        probabilidades = dado.obtener_probabilidades()

        # Modifico el resultado devuelto.
        probabilidad_anterior = probabilidades[0]
        probabilidades[0] = probabilidad_anterior + 1

        # Verifico que no se haya modificado su probabilidad dentro del dado.
        self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])


class TestDadoCreciente(TestCase):

    def test_probabilidades_son_crecientes(self):

        dado = DadoCreciente(6)

        probabilidades = dado.obtener_probabilidades()

        prob = probabilidades[0]
        for i in range(1, len(probabilidades)):
            self.assertLess(prob, probabilidades[i])
            prob = probabilidades[i]

    def test_probabilidades_no_se_deben_modificar(self):
        dado = DadoCreciente(6)
        probabilidades = dado.obtener_probabilidades()

        # Modifico el resultado devuelto.
        probabilidad_anterior = probabilidades[0]
        probabilidades[0] = probabilidad_anterior + 1

        # Verifico que no se haya modificado su probabilidad dentro del dado.
        self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])


class TestDadoDecreciente(TestCase):

    def test_probabilidades_son_decrecientes(self):

        dado = DadoDecreciente(6)

        probabilidades = dado.obtener_probabilidades()

        prob = probabilidades[0]
        for i in range(1, len(probabilidades)):
            self.assertGreater(prob, probabilidades[i])
            prob = probabilidades[i]

    def test_probabilidades_no_se_deben_modificar(self):
        dado = DadoDecreciente(6)
        probabilidades = dado.obtener_probabilidades()

        # Modifico el resultado devuelto.
        probabilidad_anterior = probabilidades[0]
        probabilidades[0] = probabilidad_anterior + 1

        # Verifico que no se haya modificado su probabilidad dentro del dado.
        self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])


class TestDadoTriangular(TestCase):

    def test_probabilidades_son_triangular(self):
        """Se realizan dos pruebas, para una cantidad de caras par y para otra impar, ya que sus probabilidades se generan distinto."""
        # Dentro de un metodo realizo la prueba:

        # Creo un dado triangular de siete caras para tener un valor medio mayor y no dos. (Ver explicacion en el constructor)
        dado = DadoTriangular(7)

        # Obtengo sus probabilidades.
        # Este metodo no se usa en el juego pero se agrego para poder correr la prueba.
        probabilidades = dado.obtener_probabilidades()
        
        prob = probabilidades[0]
        midValue = 4 # Si, es magico, como el 7 de arriba; pero estamos hablando de clase de pruebas.

        for i in range(1, len(probabilidades)):
            if i < midValue:
                self.assertLess(prob, probabilidades[i])
            elif i > midValue:
                self.assertGreater(prob, probabilidades[i])
            elif i == midValue:
                self.assertLess(probabilidades[i], prob)
                self.assertGreater(prob, probabilidades[i])
            prob = probabilidades[i]

        # Creo un dado triangular de seis caras para tener dos valores medios. (Ver explicacion en el constructor)
        dado = DadoTriangular(6)

        # Obtengo sus probabilidades.
        # Este metodo no se usa en el juego pero se agrego para poder correr la prueba.
        probabilidades = dado.obtener_probabilidades()
        
        prob = probabilidades[0]
        midValue = (2,3)
        for i in range(1, len(probabilidades)):
            if i < midValue[0]:
                self.assertLess(prob, probabilidades[i])
            elif i > midValue[1]:
                self.assertGreater(prob, probabilidades[i])
            elif i in midValue:
                self.assertEqual(probabilidades[midValue[0]], probabilidades[midValue[1]])
            prob = probabilidades[i]



    # Este otro metodo, por ejemplo, verifica que las probabilidades de ocurrencia de
    # cada cara no se puedan modificar.
    def test_probabilidades_no_se_deben_modificar(self):
        dado = DadoTriangular(6)
        probabilidades = dado.obtener_probabilidades()

        # Modifico el resultado devuelto.
        probabilidad_anterior = probabilidades[0]
        probabilidades[0] = probabilidad_anterior + 1

        # Verifico que no se haya modificado su probabilidad dentro del dado.
        self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])


class TestTablero(TestCase):

    # Prueba que la creacion usando listas de diferentes largos levante una excepcion.
    def test_inicializacion_con_distintos_largos_invalida(self):
        casilleros = ['1', None, '3']
        posiciones = ['1', '2']

        # Estructura que verifica que se levante una excepcion de tipo ValueError
        # dentro del bloque with.
        with self.assertRaises(ValueError):
            Tablero(casilleros, posiciones)

    # Prueba que los casilleros no se puedan modificar desde afuera.
    def test_casilleros_no_se_deben_modificar(self):
        casilleros = ['1', None, '3']
        posiciones = ['1', '2', '3']

        tablero = Tablero(casilleros, posiciones)

        # Modifico un casillero
        casilleros[1]='2'

        # Verifico que no se haya modificado el tablero
        self.assertNotEqual(tablero[1],casilleros[1])


class TestListadoCartas(TestCase):

    # # Prueba que la creacion usando listas de diferentes largos levante una excepcion.
    # def test_inicializacion_con_distintos_largos_invalida(self):
    #     personajes = ['Psj1', 'Psj2', 'Psj3'] #Anarchy!
    #     armas      = ['Gun1', 'Gun2', 'Gun3']
    #     lugares    = ['Lgr1', 'Lgr2', 'Lgr3']

    #     # Estructura que verifica que se levante una excepcion de tipo ValueError
    #     # dentro del bloque with.
    #     with self.assertRaises(ValueError):
    #         listado_cartas = ListadoCartas(personajes, armas, lugares)

    # Prueba que las cartas no se puedan modificar desde afuera.
    def test_cartas_no_se_deben_modificar(self):
        personajes = ['Psj1', 'Psj2', 'Psj3'] #Anarchy!
        armas      = ['Gun1', 'Gun2', 'Gun3']
        lugares    = ['Lgr1', 'Lgr2', 'Lgr3']

        listado_cartas = ListadoCartas(personajes, armas, lugares)

        # Modifico una carta
        personajes[0]='Mostaza'
        # Verifico que no se haya modificado el tablero
        self.assertNotIn(personajes[0],str(listado_cartas))
        

# Si este archivo crece mucho quizas sea necesario dividirlo...


# Ejecuta todas las pruebas cuando se ejecute este archivo.
if __name__ == "__main__":
    unittest.main()
