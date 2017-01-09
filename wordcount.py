# put your code here.
# import time
import string
import sys
import collections


def stripped_word(word):
    """strips word of punctuation (every non alphabetic character but '-') and changes it to lowercase
    """

    return ''.join([letter for letter in word.lower() if letter in string.ascii_lowercase+"-"])


with open(sys.argv[1]) as word_file:
    text = word_file.read().split()

clean_text = [stripped_word(word) for word in text]

    # words = []
    # for line in word_file:
    #     for word in line.split():
    #         word = ''.join([letter for letter in word.lower() if letter in string.ascii_lowercase])
    #         words.append(word)


word_count = collections.Counter(clean_text)


def negative_reverse(tup):

    return (-tup[1], tup[0])


# start_1 = time.time()
for key, value in sorted(word_count.iteritems(), key=lambda tup: (-tup[1], tup[0])):
    print key, value
# end_1 = time.time()


# start_2 = time.time()
# for key, value in words.items():
    # print key, value
# end_2 = time.time()

# print "Time elapsed with iteritems: %f seconds" % (end_1 - start_1)
#
# print "Time elapsed with items: %f seconds" % (end_2 - start_2)

#Code review comments: COULD break this up into many small funtions, one for each piece of the algorithm