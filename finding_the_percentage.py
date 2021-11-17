def main():
    numero_estudiantes = int(input())
    calificacion_estudiantes = {}
    for _ in range(numero_estudiantes):
        name, *line = input().split()
        scores = list(map(float, line))
        calificacion_estudiantes[name] = scores
    verificicaion_estudiante = input()
    for i in calificacion_estudiantes:
        if i == verificicaion_estudiante:
            #calificacion_estudiantes[i]
            promedio(calificacion_estudiantes[i])
            #print(calificacion_estudiantes[i])

    #print(calificacion_estudiantes)
def promedio(calificaciones):
    suma_calificaciones = 0
    #print(calificaciones)
    for j in calificaciones:
        suma_calificaciones += j
    promedio = suma_calificaciones/len(calificaciones)
    print("{:.2f}".format(promedio))


if __name__ == '__main__':
    main()