from collections import Counter


def word_order(quantity_of_words:int):

    list_of_words = []
    for word in range(quantity_of_words):
        list_of_words.append(input())
    variant_of_words = Counter(list_of_words)
    print(len(variant_of_words))
    print(variant_of_words.values())
    for element in variant_of_words.values():
        print(str(element)+ " ",end ="")


if __name__ == '__main__':
    quantity_of_words = int(input())

    word_order(quantity_of_words)