import sys
import heapq


class Node(object):
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(data):
    if data:
        freq_list = get_char_freq(data)
        tree = get_tree(freq_list)
        encode = get_encodings(tree)
        encoded_data = ''
        for i in data:
            encoded_data += ''.join(encode[i])
        return encoded_data, tree
    else:
        print('Invalid Input, size of string should be greater than 0')
        return None, None


def huffman_decoding(data, tree):
    if data:
        if tree.left_child is None and tree.right_child is None:
            decoded_data = ''
            for i in data:
                decoded_data += tree.char
            return decoded_data
        decoded_data = ''
        node = tree
        for i in data:
            if i == '0':
                node = node.left_child
                if node.char:
                    decoded_data += node.char
                    node = tree
            elif i == '1':
                node = node.right_child
                if node.char:
                    decoded_data += node.char
                    node = tree
        return decoded_data
    else:
        print('Invalid Data, to encoder')


def get_char_freq(data):
    freq_dict = {}
    for ch in data:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    freq_list = [Node(i, j) for i, j in freq_dict.items()]
    heapq.heapify(freq_list)
    return freq_list


def get_tree(_list):
    while len(_list) > 1:
        s = heapq.heappop(_list)
        l = heapq.heappop(_list)
        m = merge_node(s, l)
        heapq.heappush(_list, m)
    return _list[0]


def merge_node(n1, n2):
    node = Node(None, n1.freq + n2.freq)
    node.left_child = n1
    node.right_child = n2
    return node


def get_encodings(tree):
    en_dict = {}
    en_list = []
    encodings(tree, en_dict, en_list)
    return en_dict


def encodings(tree, en_dict, en_list):
    if tree.left_child is None and tree.right_child is None:
        en_dict[tree.char] = en_list + ['0']
        return en_dict
    else:
        if tree.left_child.char:
            en_dict[tree.left_child.char] = en_list + ['0']
        elif tree.left_child.freq:
            en_list.append('0')
            encodings(tree.left_child, en_dict, en_list)
            en_list.pop()
        if tree.right_child.char:
            en_dict[tree.right_child.char] = en_list + ['1']
        elif tree.right_child.freq:
            en_list.append('1')
            encodings(tree.right_child, en_dict, en_list)
            en_list.pop()
        return en_dict


if __name__ == "__main__":
    # test 1
    a_great_sentence = "The bird is the word"
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Test 1 Passed: {}".format(a_great_sentence == decoded_data))
    print('\n--------------------------------------------------------')

    # test 2
    a_great_sentence = ""
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Test 2 Passed: {}".format(
        decoded_data is None and encoded_data is None))
    print('\n--------------------------------------------------------')

    # test 3
    a_great_sentence = "AAA"
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Test 3 Passed: {}".format(a_great_sentence == decoded_data))
