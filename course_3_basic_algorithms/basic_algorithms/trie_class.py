'''I want to create a class using which I can save word
and check if I have saved it later on.
I can use set but add and addition and adopt have
very similar startings, I can instead have a class
which uses nested dictionary and have different levels
for each word.
For example:
{
    a: {
        is_word: False,
        d: {
            is_word: False,
            d: {
                is_word = True
                }
            }
    
        }
}

This class will have a dictionary.

'''


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        dict_ = self.root
        for ch in word:
            if dict_.get(ch):
                dict_ = dict_[ch]
            else:
                dict_[ch] = {}
                dict_ = dict_[ch]
        dict_['is_word'] = True

    def exists(self, word):
        dict_ = self.root
        for ch in word:
            if dict_.get(ch) is None:
                return False
            else:
                dict_ = dict_[ch]
        return dict_.get('is_word') is not None

## solution given by udacity
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                current_node.children[ch] = TrieNode()
            current_node = current_node.children[ch]
        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root
        for ch in word:
            if ch not in current_node.children:
                return False
            else:
                current_node = current_node.children[ch]
        return current_node.is_word
