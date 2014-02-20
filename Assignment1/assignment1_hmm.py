# solution for Assignment 1
# Trigram Hidden Markov Model

from collections import defaultdict

def emission_counts(counts_file):
    """ This function reads the counts files generated by the helper file count_freqs.py and calculates the emission parameters """
    word_tag_counts = {}
    tag_counts = defaultdict(int) # This will store the cumulative tag counts
    for line in counts_file:
        parts = line.strip()
        if parts[1] == 'WORDTAG':
            word_tag_count = parts[0]
            tag = parts[2]
            word = parts[3]
            tag_counts[tag] += int(word_tag_count)
            if word_tag_counts.get(word):
               word_tag_counts[word][tag] = int(word_tag_count)
            else:
                word_tag_counts[word] = {tag : int(word_tag_count)}
    return word_tag_counts, tag_counts

def get_emission(word, tag, word_tag_counts, tag_counts):
    word_tag_count = word_tag_counts[word][tag] # assumes word exists and has been seen
    total_tag_count = tag_counts[tag]
    return word_tag_count * 1.0 / total_tag_count



if __name___ == '__main__':
    counts_file = sys.argv[1]
    emission_counts, tag_counts = emission_counts(sys.argv[1])

