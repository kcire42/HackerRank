
def minion_game(palabra):
    palabra = palabra.upper()
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    
    for i in range(len(palabra)):
        if palabra[i] in vowels:
            kevin_score += (len(palabra)-i)
        else:
            stuart_score +=  (len(palabra)-i)
    # print(f"Kevin {kevin_score}")
    # print(f"Stuart {stuart_score}")
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")
    

    
        

    
   


if __name__ == "__main__":
    palabra = input()
    minion_game(palabra)

