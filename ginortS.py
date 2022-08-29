def sorting(text):
    text_list = list(text.strip())
    lower_letters = []
    upper_letters = []
    even_numbers = []
    odd_numbers = []
    for character in text_list:
        if (character.islower()):
            lower_letters.append(character)
        elif (character.isupper()):
            upper_letters.append(character)
        elif (character.isnumeric()):
            if int(character) % 2 == 0:
                even_numbers.append(character)
            else: 
                odd_numbers.append(character)
    
    lower_letters = "".join(sorted(lower_letters))
    upper_letters = "".join(sorted(upper_letters))
    even_numbers = "".join(sorted(even_numbers))
    odd_numbers = "".join(sorted(odd_numbers))
    print(lower_letters+upper_letters+odd_numbers+even_numbers)
    

    


if __name__ == '__main__':
    text = input()
    sorted_text = sorting(text)
    #print(sorted_text)
    