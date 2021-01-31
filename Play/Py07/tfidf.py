# -*- coding: utf-8 -*-
"""
Google or any other text-based search engine must have efficient ways of finding the relevant documents in a large corpus. To weight the importance of words in documents for search a numerical statistic, called tf-idf may be used. Typically, for each document, a vector is used. You will need to implement the following steps:

    Build a vocabulary: create a list with all words in all documents, as lower-case
    Build the text frequency vector (TF): create a dictionary where, for each word, specify a list of how many times it occurs for each document
    Multiply each value in the dictionary by a factor known as the inverse document frequency (IDF): log(N/n), where N is the total number of documents and n is the number of documents where the word appears. Round the result to 3 digits.

The reason for the IDF step is to scale the vector so that words that appear often (like "the" or "and") are given a lower value because they are frequent not only in that document, but in all documents. The resulting element of each vector is its tf*idf.

Write a function called tfidf(documents) that receives a list of documents (as its string content) and returns a list of a dictionary for each document associating each word to its tf-idf vector.

For example:

    tfidf(["To be or not to be", "Impossible is a word to be found only in the dictionary of fools", "There is nothing impossible to him who will try"]) returns the list of tf-idf dictionaries: {'to': [0.0, 0.0, 0.0], 'be': [0.811, 0.405, 0.0], 'or': [1.099, 0.0, 0.0], 'not': [1.099, 0.0, 0.0], 'impossible': [0.0, 0.405, 0.405], 'is': [0.0, 0.405, 0.405], 'a': [0.0, 1.099, 0.0], 'word': [0.0, 1.099, 0.0], 'found': [0.0, 1.099, 0.0], 'only': [0.0, 1.099, 0.0], 'in': [0.0, 1.099, 0.0], 'the': [0.0, 1.099, 0.0], 'dictionary': [0.0, 1.099, 0.0], 'of': [0.0, 1.099, 0.0], 'fools': [0.0, 1.099, 0.0], 'there': [0.0, 0.0, 1.099], 'nothing': [0.0, 0.0, 1.099], 'him': [0.0, 0.0, 1.099], 'who': [0.0, 0.0, 1.099], 'will': [0.0, 0.0, 1.099], 'try': [0.0, 0.0, 1.099]}

"""

import math

def tfidf(documents):
    # build a vocabulary
    vocabulary = []
    for document in documents:
        words = document.split(" ")
        for word in words:
            if word.lower() not in vocabulary:
                vocabulary.append(word.lower())

    # build text frequency vector
    tf_idf = {}
    for word in vocabulary:
        for document in documents:
            occurrences = 0
            for doc_word in document.split(" "):
                if word == doc_word.lower():
                    occurrences += 1
            tf_idf[word] = tf_idf.get(word, []) + [occurrences]
    
    # implementind idf
    N = len(documents)
    for word, alist in tf_idf.items():
        frequency = 0
        for elem in alist:
            if elem != 0:
                frequency += 1
        for idx, num in enumerate(alist):
            alist[idx] = round(num * math.log(N/frequency, math.exp(1)), 3)
    return tf_idf