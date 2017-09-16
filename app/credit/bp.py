# -*- coding:utf-8 -*-

import cPickle as pickle


def dump_data():
    d = [0, 1, 2, 3, 4]
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()


def load_data():
    f = open('dump.txt', 'rb')
    d = pickle.load(f)
    f.close()
    print d


