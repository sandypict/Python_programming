from pprint import pprint as pp

def get_word_count(txt_file):
    word_count = dict()

    for line in open(txt_file):
        for word in line.rstrip().split():
            word_count[word] = word_count.get(word,0)+1
    return word_count



def group_words_by_count(wc):
    group_by = dict()
    for word, count in wc.iteritms():
        group_by.setdefault(count,list()).append(word)
    return group_by

wc=get_word_count('c:/textfile.txt')
pp(wc)
grp_by= group_words_by_count(wc)
pp(grp_by)

for count, words_list in grp_by.iteritems():
    print count
    for word in words_list:
        print "\t", word
    print