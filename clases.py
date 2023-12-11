tipos_posibles = ["organo", "virus", "medicina", "transplante", "ladron", "infectar", "cambiaCuerpos", "errorMedico"]
colores_posibles = ["rojo", "azul", "verde", "amarillo"]


class Cartas():
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color

    def __str__(self):
        return f'Carta: {self.tipo} Color: {self.color}'


class Organo(Cartas):

    def __init__(self, tipo, color, vidas):
        super().__init__(tipo, color)
        self.vidas = vidas

    def __str__(self):
        return f'{super().__str__()} Vidas: {self.vidas}'

    def estaVivo(self):
        if self.vidas > -2:
            return True
        else:
            return False

    def esInmune(self):
        if self.vidas == 2:
            return True
        else:
            return False


def matarOrgano(organo):
    if organo.estaVivo() == False:
        organo.organoVivo = False


class Virus(Cartas):
    def __init__(self, tipo, color):
        super().__init__(tipo, color)

    def __str__(self):
        return f'{super().__str__()}'


def atacarOrgano(organo):
    organo.vidas = organo.vidas- 1

def curarOrgano(organo):
    organo.vidas = organo.vidas+ 1

class Medicina(Cartas):
    def __init__(self, tipo, color):
        super().__init__(tipo, color)

    def __str__(self):
        return f'{super().__str__()}'

    def curar(self, organo):
        if self.color == organo.color and organo.organoInmune == False:
            organo.vidas = + 1
        else:
            print("no puedes curar a ese organo")


class Transplante(Cartas):
    def __init__(self, tipo):
        super().__init__(tipo)

    def transplantar_organo(self, organoJugador, organoRival):
        pass

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'


class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.mesa = []
        self.victoria = False
        self.turno = False
    def verMano(self):
        print(f'Mano del Jugador {self.nombre}')
        for carta in self.mano:
            print(f'\t{carta}')
    def verMesa(self):
        print(f'Mesa del Jugador {self.nombre}')
        for carta in self.mesa:
            print(f'\t{carta}')


def repartirManos(jugadores,mazo):
    for jugador in jugadores:
        jugador.mano.append(mazo.pop())
        jugador.mano.append(mazo.pop())
        jugador.mano.append(mazo.pop())
        jugador.verMano()


def verManoJugador(jugador):
    manoJugador = jugador.mano
    print(f'Mano del Jugador {jugador.nombre}')
    for organo in manoJugador:
        print(f'\t{organo}')






