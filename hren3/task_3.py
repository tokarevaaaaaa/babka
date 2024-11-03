# TODO  Напишите функцию count_letters

def count_letters ( sourse_text ):
    little_letters_dict = { }

    i = 0

    mas_letter = []

    len_sourse_text = len(sourse_text)
    while ( i < len_sourse_text):
        if ( ( sourse_text[i] >= 'А' and sourse_text[i] <= 'Я' )
        or ( sourse_text[i] >= 'а' and sourse_text[i] <= 'я' )
        or sourse_text[i] == 'ё' or sourse_text[i] == 'Ё'):

            tmp_letter = sourse_text[i]

            if ( tmp_letter >= 'А' and tmp_letter <= 'Я'):
                tmp_letter = chr (ord (tmp_letter) + 32)

            elif ( tmp_letter == 'Ё' ):
                tmp_letter = 'ё'

            if (tmp_letter not in mas_letter):
                mas_letter.append( tmp_letter )
                little_letters_dict[ tmp_letter ] = 1
            else:
                little_letters_dict[ tmp_letter ] += 1

        i += 1
    return little_letters_dict

def calculate_frequency ( dict_letter,  count_letters_in_text):

    distribution_letters_in_sourse_text_dict = {}

    temp_letter_rus = 'а'

    while (temp_letter_rus != 'я'):

        if temp_letter_rus in dict_letter:

             res = \
                dict_letter[temp_letter_rus] / count_letters_in_text

             distribution_letters_in_sourse_text_dict[temp_letter_rus] = res

        temp_letter_rus = chr (ord (temp_letter_rus) + 1)

    if 'ё' in dict_letter:

        res = \
            dict_letter['ё'] / count_letters_in_text

        distribution_letters_in_sourse_text_dict['ё'] = res

    res = \
        dict_letter[temp_letter_rus] / count_letters_in_text

    distribution_letters_in_sourse_text_dict[temp_letter_rus] = res


    return distribution_letters_in_sourse_text_dict


# TODO Напишите функцию calculate_frequency


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

dict_letter = count_letters (main_str)

count_letters_in_text = 0

len_text = len (main_str)

i = 0
while (i < len_text):

    if ( (main_str[i] >= 'А' and main_str[i] <= 'Я')
            or (main_str[i] >= 'а' and main_str[i] <= 'я')
            or main_str[i] == 'ё' or main_str[i] == 'Ё'):
        count_letters_in_text += 1

    i += 1

frequency_dict = calculate_frequency(dict_letter, count_letters_in_text)

i = 0
mas_letter = []
len_sourse_text = len(main_str)

while (i < len_sourse_text):

    if ((main_str[i] >= 'А' and main_str[i] <= 'Я')
            or (main_str[i] >= 'а' and main_str[i] <= 'я')
            or main_str[i] == 'ё' or main_str[i] == 'Ё'):

        tmp_letter = main_str[i]

        if (tmp_letter >= 'А' and tmp_letter <= 'Я'):
            tmp_letter = chr(ord(tmp_letter) + 32)

        elif (tmp_letter == 'Ё'):
            tmp_letter = 'ё'

        if (tmp_letter not in mas_letter):
            mas_letter.append(tmp_letter)

            print(tmp_letter + ':', "%.2f" % frequency_dict[tmp_letter] )

    i += 1

# TODO Распечатайте в столбик букву и её частоту в тексте
