<<<<<<< HEAD
import math
def find_angle_mbc(co: int , ca:int)-> str:
    teta_mbc = str(round(math.degrees(math.atan2(co,ca))))
    return teta_mbc


if __name__ == "__main__":
    co = int(input())
    ca = int(input())
    teta_mbc= find_angle_mbc(co,ca)
=======
import math
def find_angle_mbc(co: int , ca:int)-> str:
    teta_mbc = str(round(math.degrees(math.atan2(co,ca))))
    return teta_mbc


if __name__ == "__main__":
    co = int(input())
    ca = int(input())
    teta_mbc= find_angle_mbc(co,ca)
>>>>>>> 8432214d2306260373a48679c395bcacf06772c3
    print(teta_mbc,chr(176),sep= '')