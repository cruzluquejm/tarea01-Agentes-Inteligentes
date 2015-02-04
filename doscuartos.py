#!/usr/bin/env python
# -*- coding: utf-8 -*-

import entornos
from random import choice

class DosCuartos(entornos.Entorno):

    def sensores(self, estado):

        robot, A, B, C, D, E, F = estado

        if robot == 'A':
            result = A

        if robot == 'B':
            result = B

        if robot == 'C':
            result = C

        if robot == 'D':
            result = D

        if robot == 'E':
            result = E

        if robot == 'F':
            result = F

        return robot,result

    def accion_legal(self, estado, accion):

        robot = estado[0]

        if robot == 'A':
            return accion in ('irDerecha','bajar','limpiar','noOp')

        if robot == 'B':
            return accion in ('irIzquierda','irDerecha','bajar','limpiar','noOp')

        if robot == 'C':
            return accion in ('irIzquierda','bajar','limpiar','noOp')

        if robot == 'D':
            return accion in ('irDerecha','subir','limpiar','noOp')

        if robot == 'E':
            return accion in ('irIzquierda','irDerecha','subir','limpiar','noOp')

        if robot == 'F':
            return accion in ('irIzquierda','subir','limpiar','noOp')

    def transicion(self, estado, accion):

        if not self.accion_legal(estado, accion):
            raise ValueError("La accion no es legal para este estado")

        robot, A, B, C, D, E, F = estado

        if robot == 'A':
            return (('B', A, B, C, D, E, F) if accion == 'irDerecha' else
                    ('D', A, B, C, D, E, F) if accion == 'bajar' else
                    ('A', 'limpio', B, C, D, E, F) if accion == 'limpiar' else
                    (robot, A, B, C, D, E, F))

        if robot == 'B':
            return (('A', A, B, C, D, E, F) if accion == 'irIzquierda' else
                    ('C', A, B, C, D, E, F) if accion == 'irDerecha' else
                    ('E', A, B, C, D, E, F) if accion == 'bajar' else
                    ('B', A, 'limpio', C, D, E, F) if accion == 'limpiar' else
                    (robot, A, B, C, D, E, F))

        if robot == 'C':
            return (('B', A, B, C, D, E, F) if accion == 'irIzquierda' else
                    ('F', A, B, C, D, E, F) if accion == 'bajar' else
                    ('C', A, B, 'limpio', D, E, F) if accion == 'limpiar' else
                    (robot, A, B, C, D, E, F))

        if robot == 'D':
            return (('E', A, B, C, D, E, F) if accion == 'irDerecha' else
                    ('A', A, B, C, D, E, F) if accion == 'subir' else
                    ('D', A, B, C, 'limpio', E, F) if accion == 'limpiar' else
                    (robot, A, B, C, D, E, F))

        if robot == 'E':
            return (('D', A, B, C, D, E, F) if accion == 'irIzquierda' else
                    ('F', A, B, C, D, E, F) if accion == 'irDerecha' else
                    ('B', A, B, C, D, E, F) if accion == 'subir' else
                    ('E', A, B, C, D, 'limpio', F) if accion == 'limpiar' else
                    (robot, A, B, C, D, E, F))

        if robot == 'F':
            return (('E', A, B, C, D, E, F) if accion == 'irIzquierda' else
                    ('C', A, B, C, D, E, F) if accion == 'subir' else
                    ('F', A, B, C, D, E, 'limpio') if accion == 'limpiar' else
                    (robot, A, B, C, D, E, F))

    def desempeno_local(self, estado, accion):
        robot, A, B, C, D, E, F = estado
        return 0 if accion == 'noOp' and A == B == 'limpio' else -1


class AgenteAleatorio(entornos.Agente):

    def programa(self, percepcion):

        robot = percepcion[0]

        if robot == 'A':
            return choice(['irDerecha','bajar','limpiar','noOp'])

        if robot == 'B':
            return choice(['irIzquierda','irDerecha','bajar','limpiar','noOp'])

        if robot == 'C':
            return choice(['irIzquierda','bajar','limpiar','noOp'])

        if robot == 'D':
            return choice(['irDerecha','subir','limpiar','noOp'])

        if robot == 'E':
            return choice(['irIzquierda','irDerecha','subir','limpiar','noOp'])

        if robot == 'F':
            return choice(['irIzquierda','subir','limpiar','noOp'])

def test():

    print "Prueba del entorno de dos cuartos con un agente aleatorio"
    entornos.simulador(DosCuartos(),AgenteAleatorio(),('A', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio', 'sucio'), 10)

if __name__ == '__main__':
    test()
