import math
def find_angle_mbc(co: int , ca:int)-> str:
    teta_mbc = str(round(math.degrees(math.atan2(co,ca))))
    return teta_mbc


if __name__ == "__main__":
    co = int(input())
    ca = int(input())
    teta_mbc= find_angle_mbc(co,ca)
    print(teta_mbc,chr(176),sep= '')