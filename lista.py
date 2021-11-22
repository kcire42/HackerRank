def main():
    numero_instrucciones = int(input())
    lista = []
    for instruccion in range(numero_instrucciones):
        instruccion_a_ejecutar = list(input().split())
        #instruccion_a_ejecutar = input().strip().split("")
        cmd = instruccion_a_ejecutar[0]

        if cmd == "insert":
            #[1]posicion [2]objeto
            posicion = int(instruccion_a_ejecutar[1])
            objeto = int(instruccion_a_ejecutar[2])
            lista.insert(posicion,objeto)
            

            
        elif cmd == "print":
            print(lista)
        elif cmd == "remove":
            objeto = int(instruccion_a_ejecutar[1])
            lista.remove(objeto)
        elif cmd == "append":
            objeto = int(instruccion_a_ejecutar[1])
            lista.append(objeto)
        elif cmd == "sort":
            lista.sort()
        elif cmd == "pop":
            
            lista.pop()
        elif cmd == "reverse":
            
            lista.reverse()


if __name__=='__main__':
    main()
