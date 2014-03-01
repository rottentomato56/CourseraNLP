# Part 2 of Assignment 1

""" Find trigram parameters for q(y(i)|y(i-1), y(i-2)) 

the possible tags are *, STOP, I-GENE, O

"""
import unittest

tags = ['*', 'STOP', 'I-GENE', 'O'] # set of possible tags

def count_ngrams():
    ngram_counts = {}
    with open('gene.counts') as f:
        for line in f:
            parts = line.split()
            if parts[1] in ('1-GRAM', '2-GRAM', '3-GRAM'):

                count = int(parts[0])
                ngram_tag = ' '.join(parts[2:])
                ngram_counts[ngram_tag] = count
    return ngram_counts

class TestNgramCounter(unittest.TestCase):
    def test(self):
        ngram_counts = count_ngrams()
        self.assertEqual(ngram_counts['I-GENE'], 41072)
        self.assertEqual(ngram_counts['I-GENE I-GENE O'], 9622)

if __name__ == '__main__':
    unittest.main()
    




class Node(object):
    """ Node object stores reference to another node and a count relative to the parent node """
    def __init__(self, tag, count):
        self.count = count
        self.next_unigrams = {}
        self.tag = tag

def build_ngram_tree():
    with open('gene.counts') as f:
        for line in f:
            parts = line.split()
            if parts[1] == '1-GRAM':
                node = Node(parts[2], int(parts[0]))
                tree = {parts[2] : node}

class TrigramCounter(object):
    def __init__(self, dims):
        """ initializes an dict with the proper dimensions """
        self.trigram_counts = {}

    def add_trigram_counts(self, trigram, counts):
        third_word = {trigram[2] : counts} 
        second_word = {trigram[1] : unigram_count}
        if self.trigram_counts.get(trigram[0]):
            if self.trigram_counts[trigram[0]].get(trigram[1]):
                if self.trigram_counts[trigram[0]].get(trigram[1]).get(trigram[2]):
                    # add to dict if trigram doesn't exist
                    pass
        self.trigram_counts[trigram[0]] = second_word

    def get_count(self, trigram):
         
        first = self.trigram_counts.get(trigram[0])
        if not first:
            return 0
        second = first.get(trigram[1])
        if not second:
            return 0

        return second.get(trigram[2], 0)

def trigram_counts(trigram):
    """
    Parameters:

    trigram: list of three words in order
    Calculates and stores trigram counts and return a dict as:

        {word1 : {word2 : {word3 : count for (word1, word2, word3) trigram}}}

    """
    trigram_counts = {}
    with open('gene.counts') as f:
        for line in f:
            parts = line.split()
            if parts[1] == '3-GRAM':
                trigram = parts[2:]
                
                if trigram_counts.get(trigram[0]):
                    if trigram_counts.get(trigram[0]).get(trigram[1]):
                        if tigram_counts.get(trigram):
                            pass

