#"""task 1"""

def num_translate():
    number = input('Введите число на английском: ')
    print(number.get(number.lower()))


numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}

num_translate()


# """task 2"""

def num_translate_adv():
    number = input('Введите число на английском: ')
    if number.istitle():
        print(number.get(number.lower()).title())
    else:
        print(numbers.get(number))


numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}

num_translate_adv()


# """task 3"""

def thesaurus(*args):  #conver name list to dictionary like {А: [Артём..] , И:[Иван..]}
    out_dict = {}
    for name in args:
        first_letter = name[0]
        out_dict[first_letter] = out_dict.get(first_letter, []) + [name]    # в словаре ищет ключ
    return out_dict


print(thesaurus("Артур", "Артём", "Иван", "Мария", "Пётр", "Илья", "Михаил", "Григорий", "Георгий"))

#"""task 4"""

def thesaurus_adv(*names):
    """
    Возвращает словарь, где ключ - первая буква имени, значение - лист ФИ
    :param names: лист ФИ
    :return: словарь ФИ
    """
    result_names = {}
    for item in names:
        if result_names.get(item[0][0]):
            result_names[item[0][0]].append(item)
        else:
             result_names[item[0][0]] = [item]
    return(result_names)


def thesaurus_adv(*names):
    result_full_names = {}
    for item in names:
        full_name = item.split()
        full_name.reverse()
        if result_full_names.get(full_name[0][0]):
            result_full_names[full_name[0][0]].append(item)
        else:
            result_full_names[full_name[0][0]] = [item]
    for key in result_full_names:
        result_full_names[key] = thesaurus(*result_full_names[key])
    print(result_full_names)


thesaurus_adv("Иван Сергеев", "Инна Серова", "Пётр Алексеев", "Илья Иванов", "Анна Савельева")

"""task 5"""

from random import randrange

def get_jokes(n):
    joke_list = []
    for _ in range(n):
        joke = ' '.join[nouns[randrange(len(nouns))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
        joke_list.append(joke)
    print(joke_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

get_jokes()