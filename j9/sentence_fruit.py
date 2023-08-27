sentence_fruit = str(input('enter a sentence about fruits = '))
sentence_fruit_2 = sentence_fruit.split()

my_fruit = {'grape':'🍇',
            'orange':'🍊',
            'pineapple':'🍍',
            'apple':'🍏',
            'cherry':'🍒',
            'strawberry':'🍓',
            'pear':'🍐',
            'lemon':'🍋',
            'kiwi':'🥝',
            'avocado':'🥑',
            'cucumber':'🥒',
            'banana':'🍌',
            'coconut':'🥥',
            'tomato':'🍅'}

update_sentence_fruit_2 = []

for word in sentence_fruit_2 :

    if word in my_fruit :
        update_sentence_fruit_2.append(my_fruit[word])
    else :
        update_sentence_fruit_2.append(word)

print('update_sentence_fruit_2 = ' , ''.join(update_sentence_fruit_2))