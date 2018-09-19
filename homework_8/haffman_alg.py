# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

import operator

class MyNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_tree(freq, part_tree=None):

    if part_tree is None:
        tree = MyNode(freq[0][1] + freq[1][1])
        tree.left = MyNode(freq[0][0])
        tree.right = MyNode(freq[1][0])
        freq.pop(0)
        freq.pop(0)
        part_tree = get_tree(freq, tree)
    elif len(freq) != 0:
        if part_tree.value == freq[0][1]:
            tree = MyNode(part_tree.value + freq[0][1])
            tree.right = MyNode(freq[0][0])
            tree.left = part_tree
            freq.pop(0)
            part_tree = get_tree(freq, tree)
        elif part_tree.value > freq[0][1]:
            if len(freq) > 1:
                tree = MyNode(freq[0][1] + freq[1][1] + part_tree.value)
                tree.left = part_tree
                tree.right = MyNode(freq[0][1] + freq[1][1])
                tree.right.left = MyNode(freq[0][0])
                tree.right.right = MyNode(freq[1][0])
                freq.pop(0)
                freq.pop(0)
                part_tree = get_tree(freq, tree)
            else:
                tree = MyNode(freq[0][1] + part_tree.value)
                tree.left = part_tree
                tree.right = MyNode(freq[0][1])
                tree.right.left = MyNode(freq[0][0])
                freq.pop(0)
                part_tree = get_tree(freq, tree)
    return part_tree


def get_symbol_code(tree, symbol_d, code=''):

    if isinstance(tree.left.value, int):
        code += '0'
        get_symbol_code(tree.left, symbol_d, code)
        code = code[:len(code)-1]
    if isinstance(tree.right.value, int):
        code += '1'
        get_symbol_code(tree.right, symbol_d, code)
        code = code[:len(code) - 1]
    if isinstance(tree.left.value, str):
        symbol_d[tree.left.value] = code + '0'
    if isinstance(tree.right.value, str):
        symbol_d[tree.right.value] = code + '1'
    return symbol_d


def get_coded_str(string, codes):
    coded_str = ''
    for letter in string:
        for key in codes:
            if key == letter:
                coded_str += (codes[key] + ' ')
    return coded_str


def count_f(text):
    freq_dict = {}
    for i in text:
        if i not in freq_dict:
            freq_dict[i] = 1
        else:
            freq_dict[i] += 1
    return freq_dict


user_text = input('Введите вашу строку: ')

frequency_d = count_f(user_text)
sorted_d = sorted(frequency_d.items(), key=operator.itemgetter(1))

code_d = {}
print(sorted_d)
tree = get_tree(sorted_d)
coded_sym = get_symbol_code(tree, code_d)
coded_text = get_coded_str(user_text, coded_sym)

for key in coded_sym:
    print(f'Символ : {key} | {coded_sym[key]} : Код')
print(f'Закодированная строка будет такой: {coded_text}')

