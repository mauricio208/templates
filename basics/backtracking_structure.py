def caso_base_se_cumple(estado):
    return 0
def tratar_solucion(estado):
    return 0

estados_posibles = []

def es_valido(estado):
    return 0
def hacer_operacion_x(estado):
    return 0
def deshacer_nuevo_estado(estado):
    return 0


def back_tracking(estado):
    if caso_base_se_cumple(estado):
        tratar_solucion(estado)
    else:
        for nestado in estados_posibles_nuevos(estado):
            if es_valido(nestado):
                hacer_operacion_x(nestado)
                back_tracking(nestado)
                estado = deshacer_nuevo_estado(nestado)
