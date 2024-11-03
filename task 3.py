# TODO  Напишите функцию count_letters
def count_letters(text:str):
    form_text = text.lower()  # преобразование текста в нижний регистр и запись в переменную
    dict1={}
    for char in form_text:
        if char.isalpha():
            dict1[char] = form_text.count(char) # если char буква, то идет запись в словарь
    return dict1

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count: dict):
    total = sum(letter_count.values())
    result={}
    for char, counter in letter_count.items():
        result[char] = counter/total    # частота
    return result

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_counts = count_letters(main_str)
letter_frequencies = calculate_frequency(letter_counts)

for letter, frequency in letter_frequencies.items():
 print(f"{letter}: {frequency:.2f}")