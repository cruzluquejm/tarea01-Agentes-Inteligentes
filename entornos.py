#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Entorno(object):

    def sensores(self, estado):
        pass

    def accion_legal(self, estado, accion):
       return True

    def transicion(self, estado, accion):
        pass

    def sensores(self, estado):
        pass

class Agente(object):

    def programa(self, percepcion):
        pass

def simulador(entorno, agente, estado_inicial, pasos=10, verbose=True):
    """
    Realiza la simulación de un agente actuando en un entorno de forma genérica

    """
    estado = estado_inicial
    performance = 0
    performances = [performance]
    estados = [estado]
    acciones = [None]

    for paso in range(pasos):
        percepcion = entorno.sensores(estado)
        accion = agente.programa(percepcion)
        estado_n = entorno.transicion(estado, accion)
        performance += entorno.desempeno_local(estado, accion)

        performances.append(performance)
        estados.append(estado_n)
        acciones.append(accion)
        estado = estado_n

    if verbose:
        print "\n\nSimulacion de entorno tipo " + \
              str(type(entorno)) + \
              " con el agente tipo " + \
              str(type(agente)) + "\n"

        print 'Paso'.center(10) + \
              'Estado'.center(40) + \
              'Accion'.center(25) + \
              u'Desempeño'.center(15)

        print '_' * (10 + 40 + 25 + 15)

        for i in range(pasos):
            print (str(i).center(10) +
                   str(estados[i]).center(40) +
                   str(acciones[i]).center(25) +
                   str(performances[i]).rjust(12))

        print '_' * (10 + 40 + 25 + 15) + '\n\n'

    return estados, acciones, performances


