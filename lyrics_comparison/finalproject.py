#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:44:42 2021

@author: polinapetrova
"""

# Name: Polina Petrova
# E-mail: 
# finalproject.py (Final Project)


import math

def clean_text(txt):
    """ 
    txt: string
    returns a list of words in txt 'cleaned' of punctuation
    """
    words = txt.split()
    lower = [x.lower() for x in words]
    clean = []
    
    for x in lower:
        if x[-1] == '.':
            clean += [x[:-1]]
        elif x[-1] == ',':
            clean += [x[:-1]]
        elif x[-1] == '?':
            clean += [x[:-1]]
        elif x[-1] == '!':
            clean += [x[:-1]]
        elif x[-1] == ';':
            clean += [x[:-1]]
        elif x[-1] == ':':
            clean += [x[:-1]]
        elif x[-1] == '"':
            clean += [x[:-1]]
        else:
            clean += [x]
    
    return clean


def stem(s):
    """ 
    s: string
    returns returns the stem of s
    """
    if s[-1] == 's':
        w = s[:-1]
    else: 
        w = s
    
    if len(w) <= 3:
        return w
    
    stem_rest = w
    
    if w[-3:] == 'ing':
        stem_rest = w[:-3]
    elif w[-2:] == 'er' or w[-2:] == 'or':
        stem_rest = w[:-2]
    elif w[-2:] == 'ed':
        stem_rest == w[:-2]
    elif w[-3:] == 'ise' or w[-3:] == 'ize':
        stem_rest = w[:-3]
    elif w[-4:] == 'ance' or w[-4:] == 'ence':
        stem_rest = w[:-4]
    elif w[-3:] == 'ion':
        stem_rest = w[:-3]
    elif w[-3:] == 'ity':
        stem_rest = w[:-3]
    elif w[-4:] == 'ment':
        stem_rest = w[:-4]
    elif w[-4:] == 'ness':
        stem_rest = w[:-4]
    elif w[-4:] == 'ship':
        stem_rest = w[:-4]
    elif w[-3:] == 'ate':
        stem_rest = w[:-3]
    elif w[-2:] == 'en':
        stem_rest = w[:-2]
    elif w[-3:] == 'ify':
        stem_rest = w[:-3]
    elif w[-4:] == 'able':
        stem_rest = w[:-4]
    elif w[-2:] == 'al':
        stem_rest = w[:-2]
    elif w[-3:] == 'ant' or w[-3:] == 'ent':
        stem_rest = w[:-3]
    elif w[-3:] == 'ful':
        stem_rest = w[:-3]
    elif w[-2:] == 'ry':
        stem_rest = w[:-2]
    elif w[-4:] == 'ible':
        stem_rest = w[:-4]
    elif w[-3:] == 'ive':
        stem_rest = w[:-3]
    elif w[-4:] == 'less':
        stem_rest = w[:-4]
    elif w[-3:] == 'ous':
        stem_rest = w[:-3]
    elif w[-1] == 'y':
        stem_rest = w[:-1] + 'i'
    elif w[-2:] == 'ly':
        stem_rest = w[:-2]
    elif w[-2:] == 'ie':
        stem_rest = w[:-1]
    elif w[-1] == 'e':
        stem_rest = w[:-1]
        
    return stem_rest
    
    
def compare_dictionaries(d1, d2):
    """ 
    d1, d2: dictionaries
    returns the log similarity score of d1 and d2
    """   
    score = 0
    total = 0
    
    for k in d1:
        total += d1[k]
    
    for k in d2:
        if k in d1:
            score += (math.log(d1[k] / total) * d2[k])
        else: 
            score += (math.log(0.5 / total) * d2[k])
    
    return score
    
    


class TextModel:
    """ 
    data type
    """
    def __init__(self, model_name):
        """
        TextModel constructor
        model_name: string
        initialises name, words, word_lengths
        name: string that is a label for the text model (ex. author name), taken from model_name
        words: dictionary that records the number of times each words appears
        word_lengths: a dictionary that records the number of times each word length appears
        stems: records how many times a word's stem appears in text
        sentence_lengths: records how many times a sentence length appears 
        punctuation: counts punctuation in each sentence
        """
        assert(type(model_name) == str)
        
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        
        
    def __repr__(self):
        """ 
        returns a string including name of model and size of dictionaries
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of sentence punctuation: ' + str(len(self.punctuation)) + '\n'
        
        return s
        
        
    def add_string(self, s):
        """ 
        s: string of text
        adds s to model by changing the dictionaries in the contructor
        """
        words = s.split()
        
        sent_count = 0
        
        for w in words:
            sent_count += 1
            if '.' in w or '?' in w or '!' in w:
                if sent_count not in self.sentence_lengths:
                    self.sentence_lengths[sent_count] = 1
                else: 
                    self.sentence_lengths[sent_count] += 1
                sent_count = 0
                
        pun_count = 0
        
        for w in words:
            if ':' in w or '-' in w or ',' in w or ';' in w or '"' in w:
                pun_count += 1
            elif '.' in w or '?' in w or '!' in w:
                pun_count += 1
                if pun_count not in self.punctuation:
                    self.punctuation[pun_count] = 1
                else:
                    self.punctuation[pun_count] += 1
            pun_count = 0
        
        word_list = clean_text(s)
        
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        
        for w in word_list:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
                
        for w in word_list:
            if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
            else:
                self.stems[stem(w)] += 1
        
            
    
    def add_file(self, filename):
        """ 
        adds all the text from filename to the model
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        s = f.read()
        self.add_string(s)
            
          
    def save_model(self):
        """ 
        saves TextModel by writing its dictionaries into files
        """
        d1 = self.words
        filename1 = self.name + '_words'
        f1 = open(filename1, 'w')
        f1.write(str(d1))
        f1.close()
        
        d2 = self.word_lengths
        filename2 = self.name + '_word_lengths'
        f2 = open(filename2, 'w')
        f2.write(str(d2))
        f2.close()
        
        d3 = self.stems
        filename3 = self.name + '_stems'
        f3 = open(filename3, 'w')
        f3.write(str(d3))
        f3.close()
        
        d4 = self.sentence_lengths
        filename4 = self.name + '_sentence_lengths'
        f4 = open(filename4, 'w')
        f4.write(str(d4))
        f4.close()
        
        d5 = self.punctuation
        filename5 = self.name + '_punctuation'
        f5 = open(filename5, 'w')
        f5.write(str(d5))
        f5.close()
        
        
        
    def read_model(self):
        """ 
        reads the stored dictionaries for TextModel and assigns them to attributes in TextModel
        """
        filename1 = self.name + '_words'
        f1 = open(filename1, 'r')
        d_str1 = f1.read()
        f1.close()
        
        d1 = dict(eval(d_str1))
        
        
        filename2 = self.name + '_word_lengths'
        f2 = open(filename2, 'r')
        d_str2 = f2.read()
        f2.close()
        
        d2 = dict(eval(d_str2))
        
        filename3 = self.name + '_stems'
        f3 = open(filename3, 'r')
        d_str3 = f3.read()
        f3.close()
        
        d3 = dict(eval(d_str3))
        
        filename4 = self.name + '_sentence_lengths'
        f4 = open(filename4, 'r')
        d_str4 = f4.read()
        f4.close()
        
        d4 = dict(eval(d_str4))
        
        filename5 = self.name + '_punctuation'
        f5 = open(filename5, 'r')
        d_str5 = f5.read()
        f5.close()
        
        d5 = dict(eval(d_str5))
        
        self.words = d1
        self.word_lengths = d2
        self.stems = d3
        self.sentence_lengths = d4
        self.punctuation = d5
        
        
    def similarity_scores(self, other):
        """ 
        returns a list of log similarity scores for each sict attribute of self and other
        """
        score = []
        score += [compare_dictionaries(other.words, self.words)]
        score += [compare_dictionaries(other.word_lengths, self.word_lengths)]
        score += [compare_dictionaries(other.stems, self.stems)]
        score += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        score += [compare_dictionaries(other.punctuation, self.punctuation)]
        
        return score
    
    
    def classify(self, source1, source2):
        """ 
        source1, source2: other TextModel objects
        compares self, source1 and source2 to determine with source self comes from
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print('scores for', source1.name, ':', scores1)
        print('scores for', source2.name, ':', scores2)
        
        compare1 = 0
        compare2 = 0
        
        for x in range(len(scores1)):
            if scores1[x] > scores2[x]:
                compare1 += 1
            else:
                compare2 += 1
                
        if compare1 > compare2:
            print(self.name, 'is more likely to have come from', source1.name)
        elif compare2 > compare1:
            print(self.name, 'is more likely to have come from', source2.name)
        else:
            print('the source of', self.name, 'cannot be determined')
            
            
def test():
    """ 
    testing TextModel class
    """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
        

def run_tests():
    """
    testing TextModel class
    source1: Lauv songs
    source2: Billie Eilish songs
    comparing a Troye Sivan song to sources
    comparing an Ariana Grande song to sources
    mystery_song1: comparing a Lauv song to sources
    mystery_song2: comparing a Billie Eilish song to sources
    """
    source1 = TextModel('Lauv')
    source1.add_file('lauv.txt')

    source2 = TextModel('Billie Eilish')
    source2.add_file('billie_eilish.txt')

    new1 = TextModel('Troye Sivan')
    new1.add_file('troye_sivan_class.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('Ariana Grande')
    new2.add_file('ariana_grande_class.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('Mystery Song 1')
    new3.add_file('lauv_class.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('Mystery Song 2')
    new4.add_file('billie_eilish_class.txt')
    new4.classify(source1, source2)

    
