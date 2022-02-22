import sys
import re
from joblib import Parallel, delayed

lines = open('large_text.txt').read().split('\n')
num_threads = int(sys.argv[1])

word_count_dict = dict()

def word_count_line(line):
    for word in re.findall("[\\w]+", line):
        word_count_dict[word] = word_count_dict.get(word, 0)+1

Parallel(n_jobs=num_threads, backend='threading')(delayed(word_count_line)(line) for line in lines)

print(word_count_dict)
