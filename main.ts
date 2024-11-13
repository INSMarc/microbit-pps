input.onButtonPressed(Button.A, function () {
    if (Eleccion_Jugador > 0) {
        Eleccion_Jugador += -1
    }
})
// No Presentar En Clase
input.onGesture(Gesture.Shake, function () {
    basic.showString("IA Eligiendo")
    Eleccion_Ordenador = randint(0, 2)
})
input.onButtonPressed(Button.AB, function () {
    Decision_Definitiva += 1
})
input.onButtonPressed(Button.B, function () {
    if (Eleccion_Jugador < 2) {
        Eleccion_Jugador += 1
    }
})
let Decision_Definitiva = 0
let Eleccion_Jugador = 0
let Eleccion_Ordenador = 0
Eleccion_Ordenador = randint(0, 2)
Eleccion_Jugador = 0
basic.forever(function () {
    while (Decision_Definitiva == 0) {
        if (Eleccion_Jugador == 0) {
            basic.showLeds(`
                . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
                `)
        } else if (Eleccion_Jugador == 1) {
            basic.showLeds(`
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
                `)
        } else {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
                `)
        }
    }
})
basic.forever(function () {
    if (Decision_Definitiva == 1) {
        if (Eleccion_Jugador == 0 && Eleccion_Ordenador == 2) {
            basic.showIcon(IconNames.Yes)
        } else if (Eleccion_Jugador == 0 && Eleccion_Ordenador == 1) {
            basic.showIcon(IconNames.No)
        } else if (Eleccion_Jugador == 0 && Eleccion_Ordenador == 0) {
            basic.showIcon(IconNames.Diamond)
        } else if (Eleccion_Jugador == 1 && Eleccion_Ordenador == 2) {
            basic.showIcon(IconNames.No)
        } else if (Eleccion_Jugador == 1 && Eleccion_Ordenador == 1) {
            basic.showIcon(IconNames.Diamond)
        } else if (Eleccion_Jugador == 1 && Eleccion_Ordenador == 0) {
            basic.showIcon(IconNames.Yes)
        } else if (Eleccion_Jugador == 2 && Eleccion_Ordenador == 2) {
            basic.showIcon(IconNames.Diamond)
        } else if (Eleccion_Jugador == 2 && Eleccion_Ordenador == 1) {
            basic.showIcon(IconNames.Yes)
        } else {
            basic.showIcon(IconNames.No)
        }
    }
})
