import numpy as np

class Generate_new_string():

    def fit(input_txt):
        # считываем текст
        with open(input_txt, 'r', encoding='utf-8') as file:
            text = file.read()

        # разбиваем текст на отдельные слова, сохранив при этом знаки препинания ->
        # -> чтобы сгенерированный текст был со знаками препинания
        splited_text = text.split()
        return splited_text


    # функция-генератор, создающая пары слов
    def make_pairs(splited_text):
        # перебираем все слова в подготовленном тексте, кроме последнего
        for i in range(len(splited_text) - 1):
            # генерируем новую пару и возвращаем её как результат работы функции
            yield (splited_text[i], splited_text[i + 1])

    def generate(splited_text, lenght):
        # вызываем генератор и получаем все пары слов
        pairs = Generate_new_string.make_pairs(splited_text)

        # словарь, который будет содержать слова и их продолжения ->
        # -> в качестве ключа - слово, в качестве значения - список возможных продолжений
        word_dict = {}

        # перебираем все пары слов из списка пар
        for word_1, word_2 in pairs:
            # если первое слово уже было добавлено в словарь
            if word_1 in word_dict.keys():
                # тогда второе слово добавим как возможное продолжение первого
                word_dict[word_1].append(word_2)
            else:
                # если первого слова ещё не было в словаре, ->
                # -> создаём новую запись в словаре и указываем второе слово как продолжение первого
                word_dict[word_1] = [word_2]

        # выбираем первое слово(случайно) для генерации новой последовательности
        first_word = np.random.choice(splited_text)

        # Для красоты вывода, мы хотим начинать нашу новую последовательность с большой буквы ->
        # -> поэтому если в нашем первом слове нет заглавных букв, то будем искать до тех пор, пока не найдём
        while first_word.islower():
            first_word = np.random.choice(splited_text)

        # новая последовательность
        sequence = [first_word]

        # количество слов в новой последовательности
        number_of_words = lenght

        # цикл заполняющий последовательность
        for i in range(number_of_words):
            # на каждой итерации добавляем одно из прололжений для слова - случайно
            sequence.append(np.random.choice(word_dict[sequence[-1]]))


        # выводим нашу последовательность в файл generated.txt
        with open('generated.txt', 'w') as file2:
            file2.write(' '.join(sequence))

    # блок, обрабатывающий ввод и запускающий обучение, а затем и генерацию
    def Main(input_txt, lenght):
        sp_txt = Generate_new_string.fit(input_txt)
        Generate_new_string.generate(sp_txt, lenght)

Generate_new_string.Main(input("Write filename of text with filename extension\n"), int(input("Enter number of words in the new sequence\n")))
