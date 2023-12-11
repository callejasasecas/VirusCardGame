from clases import *
import random
mazo=[
    Organo("organo", "azul", 0),
    Organo("organo", "azul", 0),
    Organo("organo", "azul", 0),
    Organo("organo", "azul", 0),
    Organo("organo", "azul", 0),
    Virus("virus", "azul"),
    Virus("virus", "azul"),
    Virus("virus", "azul"),
    Virus("virus", "azul"),
    Medicina("medicina", "azul"),
    Medicina("medicina", "azul"),
    Medicina("medicina", "azul"),
    Medicina("medicina", "azul"),
    Organo("organo", "rojo", 0),
    Organo("organo", "rojo", 0),
    Organo("organo", "rojo", 0),
    Organo("organo", "rojo", 0),
    Organo("organo", "rojo", 0),
    Virus("virus", "rojo"),
    Virus("virus", "rojo"),
    Virus("virus", "rojo"),
    Virus("virus", "rojo"),
    Medicina("medicina", "rojo"),
    Medicina("medicina", "rojo"),
    Medicina("medicina", "rojo"),
    Medicina("medicina", "rojo"),
    Organo("organo", "verde", 0),
    Organo("organo", "verde", 0),
    Organo("organo", "verde", 0),
    Organo("organo", "verde", 0),
    Organo("organo", "verde", 0),
    Virus("virus", "verde"),
    Virus("virus", "verde"),
    Virus("virus", "verde"),
    Virus("virus", "verde"),
    Medicina("medicina", "verde"),
    Medicina("medicina", "verde"),
    Medicina("medicina", "verde"),
    Medicina("medicina", "verde")
]


def cambiarTurno(players):
    numeroJugadores = len(players)
    for i in range(numeroJugadores):
        if i == numeroJugadores-1:
            players[i].turno = False
            players[0].turno = True
        elif players[i].turno==True:
            players[i].turno = False
            players[i+1].turno = True
            break
def sePuedeJugarOrgano(organo,mesa):
    colorOrgano = organo.color
    for carta in mesa:
        if carta.color == colorOrgano:
            return False
    return True

def sePuedeJugarVirus(virus,players):
    colorOrgano = virus.color
    organosAtacables = []
    for jugador in players:
        for carta in jugador.mesa:
            if carta.tipo == "organo" and carta.color==colorOrgano and carta.vidas<2:
                organosAtacables.append([jugador,carta])

    if len(organosAtacables) > 0:
        return True
    else:
        print("no se puede jugar este virus")
        return False
def seleccionarOrganoVirus(virus,players):
    colorOrgano = virus.color
    organosAtacables = []
    organoElegido = None
    for jugador in players:
        for carta in jugador.mesa:
            if carta.tipo == "organo" and carta.color==colorOrgano and carta.vidas<2:
                organosAtacables.append([jugador,carta])
    print("Organos atacables:")
    for carta in organosAtacables:
        organoElegido=input(f'atacar Organo {carta[1]} del jugador {carta[0].nombre} y/n')
        if organoElegido == 'y':
            return (carta[0],carta[1])
        elif organoElegido =='n':
            pass
        else:
            print("respuesta no valida, se tomará como un no")
            pass

def sePuedeJugarMedicina(virus,players):
    colorOrgano = virus.color
    organosAtacables = []
    for jugador in players:
        for carta in jugador.mesa:
            if carta.tipo == "organo" and carta.color==colorOrgano and carta.vidas<2:
                organosAtacables.append([jugador,carta])

    if len(organosAtacables) > 0:
        return True
    else:
        print("no se puede jugar esta medicina")
        return False

def seleccionarOrganoMedicina(virus,players):
    colorOrgano = virus.color
    organosAtacables = []
    organoElegido = None
    for jugador in players:
        for carta in jugador.mesa:
            if carta.tipo == "organo" and carta.color==colorOrgano and carta.vidas<2:
                organosAtacables.append([jugador,carta])
    print("Organos curables:")
    for carta in organosAtacables:
        organoElegido=input(f'curar Organo {carta[1]} del jugador {carta[0].nombre} y/n')
        if organoElegido == 'y':
            return (carta[0],carta[1])
        elif organoElegido =='n':
            pass
        else:
            print("respuesta no valida, se tomará como un no")
            pass

def robar(jugador):
    while len(jugador.mano) < 3:
        print(f'jugador {jugador.nombre} robando carta')
        jugador.mano.append(mazo.pop())
    jugador.verMano()


jugando = True
descartes = []
random.shuffle(mazo)
jugador1 = Jugador("Alejandro")
jugador2 = Jugador("Marywach")

players = [jugador1, jugador2]
repartirManos(players,mazo)
jugador1.turno = True


while jugando:
    for jugador in players:
        if jugador.turno == True:
            accion = int(input(f'Hola {jugador.nombre} que deseas hacer? 1) Jugar una Carta 2)Descartarte'))
            if accion == 1:
                jugador.verMano()
                carta = int(input("Elige una carta 0) 1) o 2)"))
                cartaValida = True
                while cartaValida:
                    if 0 <= carta <= 2:
                        cartaJugada = jugador.mano[carta]
                        print(f'Carta jugada = {cartaJugada}')
                        if cartaJugada.tipo == "organo" and sePuedeJugarOrgano(cartaJugada,jugador.mesa):
                            jugador.mesa.append(jugador.mano.pop(carta))
                            robar(jugador)
                            cartaValida = False
                        elif cartaJugada.tipo == "virus" and sePuedeJugarVirus(cartaJugada,players):
                            jugadorelegido,organoElegido = seleccionarOrganoVirus(cartaJugada,players)
                            atacarOrgano(organoElegido)
                            if not organoElegido.estaVivo():
                                print("Organo eliminado!")
                                index = jugadorelegido.mesa.index(organoElegido)
                                descartes.append(jugadorelegido.mesa.pop(index))

                            robar(jugador)
                            cartaValida = False
                        elif cartaJugada.tipo == "medicina" and sePuedeJugarMedicina(cartaJugada,players):
                            jugadorelegido, organoElegido = seleccionarOrganoMedicina(cartaJugada, players)
                            curarOrgano(organoElegido)
                            print("Medicina jugada")
                            cartaValida = False
                        else:
                            print("vuelve a elegir una carta")
                            jugador.verMano()
                            carta = int(input("Elige una carta 0) 1) o 2)"))
                    else:
                        print("numero no válido prueba otra vez")
                        jugador.verMano()
                        carta = int(input("Elige una carta 0) 1) o 2)"))
                print(f'\t{jugador.verMesa()}')
                cambiarTurno(players)
                break
            elif accion == 2:
                print("hora de descartar cartas")
                cambiarTurno(players)
                break
            else:
                print("respuesta no válida")


    jugando = jugador1.victoria == False and jugador2.victoria == False


