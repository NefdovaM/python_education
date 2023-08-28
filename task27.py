"""Задача No27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных слов содержится в этом тексте.`"""

user_input = "She sells sea shells on the sea shore. The shells that she sells are sea shells I'm sure.\
So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
list_input = user_input.split()
for i in range(len(list_input)):
    list_input[i] = list_input[i].lower()
    if list_input[i][-1] in [".", ",", "!", "?"]:
        list_input[i] = list_input[i][:len(list_input[i])-1]
unique_words = set(list_input)
print(len(unique_words))