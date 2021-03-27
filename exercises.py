import time
import random


def measure_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} with parameters: -- took: {time.time() - start_time} seconds')
        return result
    return inner

# @measure_time
# def get_common_elements(list1, list2):
#     return set(list1).intersection(set(list2))
#
# list1 = [random.randint(0,100) for _ in range(0,1000) ]
# list2 = [random.randint(0,100) for _ in range(0,1000) ]
#
# print(get_common_elements(list1,list2))


def remove_duplicates(text):
    return "".join(dict.fromkeys(text))


def word_with_most_occurrences(text_input):
    split_text = text_input.split(' ')
    return max(split_text, key=lambda x: split_text.count(x))


# print(remove_duplicates("Alabala adsffad"))
print(word_with_most_occurrences("Ana Ana are mere mere mere "))
