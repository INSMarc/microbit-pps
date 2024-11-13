def on_button_pressed_a():
    global Eleccion_Jugador
    if Eleccion_Jugador > 0:
        Eleccion_Jugador += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

# No Presentar En Clase

def on_gesture_shake():
    global Eleccion_Ordenador
    basic.show_string("IA Eligiendo")
    Eleccion_Ordenador = randint(0, 2)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global Decision_Definitiva
    Decision_Definitiva += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Eleccion_Jugador
    if Eleccion_Jugador < 2:
        Eleccion_Jugador += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

Decision_Definitiva = 0
Eleccion_Jugador = 0
Eleccion_Ordenador = 0
Eleccion_Ordenador = randint(0, 2)
Eleccion_Jugador = 0

def on_forever():
    if Decision_Definitiva == 1:
        if Eleccion_Jugador == 0 and Eleccion_Ordenador == 2:
            basic.show_icon(IconNames.YES)
        elif Eleccion_Jugador == 0 and Eleccion_Ordenador == 1:
            basic.show_icon(IconNames.NO)
        elif Eleccion_Jugador == 0 and Eleccion_Ordenador == 0:
            basic.show_icon(IconNames.DIAMOND)
        elif Eleccion_Jugador == 1 and Eleccion_Ordenador == 2:
            basic.show_icon(IconNames.NO)
        elif Eleccion_Jugador == 1 and Eleccion_Ordenador == 1:
            basic.show_icon(IconNames.DIAMOND)
        elif Eleccion_Jugador == 1 and Eleccion_Ordenador == 0:
            basic.show_icon(IconNames.YES)
        elif Eleccion_Jugador == 2 and Eleccion_Ordenador == 2:
            basic.show_icon(IconNames.DIAMOND)
        elif Eleccion_Jugador == 2 and Eleccion_Ordenador == 1:
            basic.show_icon(IconNames.YES)
        else:
            basic.show_icon(IconNames.NO)
basic.forever(on_forever)

def on_forever2():
    while Decision_Definitiva == 0:
        if Eleccion_Jugador == 0:
            basic.show_leds("""
                . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
                """)
        elif Eleccion_Jugador == 1:
            basic.show_leds("""
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                """)
        else:
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
                """)
basic.forever(on_forever2)