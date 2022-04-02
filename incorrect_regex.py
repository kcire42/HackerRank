# def main(intentos : int):
#     lista_str = []
#     for intento in range(intentos):
#         cadena : str = input()
#         lista_str.append(cadena)
    
#     for elemento in lista_str:
#         if elemento == ".*\+":
#             print("True")
#         else:
#             print("False")
import re
def main():
    for _ in range(int(input())):
        ans = True
        try:
            reg = re.compile(input())
        except re.error:
            ans = False
        print(ans)
    
    


if __name__ == "__main__":
    # intentos = int(input())
    # main(intentos)
    main()