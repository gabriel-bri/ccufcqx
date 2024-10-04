def count_words_with_3_different_letters():
    total_letters = 26
    valid_letters_count = total_letters * (total_letters - 1) * (total_letters - 2)
    return valid_letters_count

result = count_words_with_3_different_letters()
print("Número de palavras com 3 letras diferentes:", result)
