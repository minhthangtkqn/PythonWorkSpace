import numpy
import math
from collections import Counter

def tf_idf(document_1, document_2):
    x = document_1.lower().split().__len__()
    y = document_2.lower().split().__len__()

    # convert Counter object to list
    counter_1 = Counter(document_1.lower().split())
    words_count_1 = counter_1.most_common(Counter(document_1.lower().split()).__len__())

    # convert Counter object to list
    counter_2 = Counter(document_2.lower().split())
    words_count_2 = counter_2.most_common(Counter(document_2.lower().split()).__len__())

    # tao 2 mang chua tf
    tf_1 = []
    tf_2 = []

    for word in words_count_1:
        tf_1.append([word[0], (word[1]*1.0/document_1.lower().split().__len__())])
    for word in words_count_2:
        tf_2.append([word[0], (word[1]*1.0/document_2.lower().split().__len__())])
    print tf_1
    print tf_2

    # tao 1 mang chua idf
    idf = []
    # list storage checked words
    checked = []

    for word in words_count_1:
        if word[0] in checked:
            pass
        else:
            if word[0] in document_2.lower().split():
                value = math.log(1,10)
            else:
                value = math.log(2,10)
            idf.append([word[0], value])
            checked.append(word[0])

    for word in words_count_2:
        if word[0] in checked:
            pass
        else:
            if word[0] in document_1.lower().split():
                value = math.log(1,10)
            else:
                value = math.log(2,10)
            idf.append([word[0], value])
            checked.append(word[0])

    print idf
    print checked

    tf_idf_1 = []
    tf_idf_2 = []

    max_1_1 = ['',0]
    max_1_2 = ['',0]
    max_1_3 = ['',0]
    max_2_1 = ['',0]
    max_2_2 = ['',0]
    max_2_3 = ['',0]

    for tf_value_1 in tf_1:
        for idf_value in idf:
            if tf_value_1[0] == idf_value[0]:
                tf_idf_1.append([tf_value_1[0], tf_value_1[1]*idf_value[1]])

    for tf_value_2 in tf_2:
        for idf_value in idf:
            if tf_value_2[0] == idf_value[0]:
                tf_idf_2.append([tf_value_2[0], tf_value_2[1]*idf_value[1]])

    #-----------------------

    for tf_idf_value in tf_idf_1:
        if max_1_1[1] < tf_idf_value[1]:
            max_1_1 = tf_idf_value

    for tf_idf_value in tf_idf_1:
        if max_1_2[1] < tf_idf_value[1] and tf_idf_value[0] != max_1_1[0]:
            max_1_2 = tf_idf_value

    for tf_idf_value in tf_idf_1:
        if max_1_3[1] < tf_idf_value[1] and tf_idf_value[0] != max_1_1[0] and tf_idf_value[0] != max_1_2[0]:
            max_1_3 = tf_idf_value

    for tf_idf_value in tf_idf_2:
        if max_2_1[1] < tf_idf_value[1]:
            max_2_1 = tf_idf_value

    for tf_idf_value in tf_idf_2:
        if max_2_2[1] < tf_idf_value[1] and tf_idf_value[0] != max_2_1[0]:
            max_2_2 = tf_idf_value

    for tf_idf_value in tf_idf_2:
        if max_2_3[1] < tf_idf_value[1] and tf_idf_value[0] != max_2_1[0] and tf_idf_value[0] != max_2_2[0]:
            max_2_3 = tf_idf_value

    print '-----------------------'
    print '-----------------------'
    print '-----------------------'

    print 'CAC TU CO TF-IDF CAO TRONG DOCUMENT 1'
    print max_1_1
    print max_1_2
    print max_1_3

    print '------------------------'
    print 'CAC TU CO TF-IDF CAO TRONG DOCUMENT 2'

    print max_2_1
    print max_2_2
    print max_2_3

    return


if __name__ == '__main__':
    document_a = "Flywheels allow the engine to run more smoothly by creating a more constant load, and they convert the conventional back-and-forth power stroke into a circular (rotary) motion that can be adapted more readily to power machinery. By 1790, Watt's improved steam engine offered a powerful, reliable power source that could be located almost anywhere. It was used to pump bellows for blast furnaces, to power huge hammers for shaping and strengthening forged metals, and to turn machinery at textile mills. More than anything, it was Watt's steam engine that speeded up the Industrial Revolution both in England and the rest of the world."
    document_b = "Once the dominant power source, steam engines eventually declined in popularity as other power sources became available. Although there were more than 60,000 steam cars made in the United States between 1897 and 1927, the steam engine eventually gave way to the internal combustion engine as a power source for vehicles."

    documents = [document_a, document_b]

    tf_idf(document_a, document_b)
