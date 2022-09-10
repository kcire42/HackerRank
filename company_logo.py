from collections import Counter

import math
import os
import random
import re
import sys

#programa que va a contar cuantas letras iguales aparecen en un palabra y ordenarlas de mayor a menor


def company_logo(company_name:str):
    company_name = sorted(company_name)
    
    count_letter = Counter(company_name).most_common(3)
    # list_of_data =  list(count_letter)
    # print(list_of_data)

    for valor in  count_letter:
        print(valor[0]+" "+str(valor[1]))
    #print(count_letter)
   


if __name__ == '__main__':
    company_name = input()
    company_logo(company_name)