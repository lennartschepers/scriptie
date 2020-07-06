#!/usr/bin/python3

import nltk.classify
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from featx import bag_of_words, high_information_words
from classification import precision_recall
from nltk.classify import SklearnClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import SVC
import string

from random import shuffle
from os import listdir # to read files
from os.path import isfile, join # to read files
import sys





# reads all the files that correspond to the input list of categories and puts their contents in bags of words
def read_files(categories):
        feats = list () 
        print("\n##### Reading files...")
        csvfile = open('fries', 'r', encoding='UTF-8').readlines()
        feats=list()
        
        for line in csvfile:
                line = line.rstrip()
                line = line.split()
                data = " ".join(line[:-1])#.lower()
                print(data)
                category = line[-1]
                print(category)
                # 0=fries, 1=nederlands, 2=gronings
                if category == '0' or category == '1': # or category == '2':
                    tokens = word_tokenize(data)
                    feats.append((bag_of_words(tokens),category))


        print("  Total, %i files read" % (len(feats)))
        return feats



# splits a labelled dataset into two disjoint subsets train and test
def split_train_test(feats, split=0.5):
        train_feats = []
        test_feats = []
        #print (feats[0])

        shuffle(feats) # randomise dataset before splitting into train and test
        cutoff = int(len(feats) * split)
        train_feats, test_feats = feats[:cutoff], feats[cutoff:]        

        print("\n##### Splitting datasets...")
        print("  Training set: %i" % len(train_feats))
        print("  Test set: %i" % len(test_feats))
        return train_feats, test_feats



def split_folds(feats, folds=10):
        shuffle(feats) # randomise dataset before splitting into train and test

        # divide feats into n cross fold sections
        nfold_feats = []
        l = int(len(feats)/folds)
        for n in range(folds):

                test_feats = feats[int(n*l):][:int(n+1)*l]
                train_feats = feats[:int(n*l)] + feats[int((n+1)*l):]
                nfold_feats.append((train_feats, test_feats))
        
        print("\n##### Splitting datasets...")
        return nfold_feats



# trains a classifier
def train(train_feats):
        classifier = SklearnClassifier(SVC(kernel="rbf", C=1, gamma=0.01)).train(train_feats)
        # the following code uses the classifier with add-1 smoothing (Laplace)
        #from nltk.probability import LaplaceProbDist
        #classifier = nltk.classify.NaiveBayesClassifier.train(train_feats, estimator=LaplaceProbDist)
        return classifier



def calculate_f(precisions, recalls):
        f_measures = {}
        for key in precisions.keys():
                try:
                        f_measures[key] = 2*(precisions[key]*recalls[key])/(precisions[key]+recalls[key])
                except:
                        f_measures[key] = 0
        return f_measures



# prints accuracy, precision and recall
def evaluation(classifier, test_feats, categories):
        print ("\n##### Evaluation...")
        print("  Accuracy: %f" % nltk.classify.accuracy(classifier, test_feats))

        precisions, recalls = precision_recall(classifier, test_feats)

        f_measures = calculate_f(precisions, recalls)
        print(" |-----------|-----------|-----------|-----------|")
        print(" |%-11s|%-11s|%-11s|%-11s|" % ("category","precision","recall","F-measure"))
        print(" |-----------|-----------|-----------|-----------|")
        for category in categories:
                if precisions[category] is None:
                        print(" |%-11s|%-11s|%-11s|%-11s|" % (category, "NA", "NA", "NA"))

                else:

                        print(" |%-11s|%-11f|%-11f|%-11s|" % (
                                category, precisions[category], recalls[category], f_measures[category]))

        print(" |-----------|-----------|-----------|-----------|")
        return nltk.classify.accuracy(classifier, test_feats)


# show informative features
def analysis(classifier):
        print("\n##### Analysis...")
        #print(classifier.show_most_informative_features(10))




# obtain the high information words
def high_information(feats, categories):
        print("\n##### Obtaining high information words...")

        labelled_words = [(category, []) for category in categories]

        from collections import defaultdict
        words = defaultdict(list)
        all_words = list()
        for category in categories:
                words[category] = list()

        for feat in feats:
                category = feat[1]
                bag = feat[0]
                for w in bag.keys():
                        words[category].append(w)
                        all_words.append(w)
#               break

        labelled_words = [(category, words[category]) for category in categories]
        #print labelled_words

        high_info_words = set(high_information_words(labelled_words))
        #print(high_info_words)

        print("  Number of words in the data: %i" % len(all_words))
        print("  Number of distinct words in the data: %i" % len(set(all_words)))
        print("  Number of distinct 'high-information' words in the data: %i" % len(high_info_words))

        return high_info_words

# grid searcher
def gridsearch(X_train, y_train):
    param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['linear','rbf', 'poly', 'sigmoid']}
    grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
    grid.fit(X_train, y_train)
    return grid.best_estimator_


def main():
        # fri ned gro
        categories = ['0','1']#,'2']

        feats = read_files(categories)
        high_info_words = high_information(feats, categories)


        train_feats, test_feats = split_train_test(feats)

        nfold_feats = split_folds(feats)
        scorelist = []
        for train_feats, test_feats in nfold_feats:
                

                classifier = train(train_feats)
                scorelist.append(evaluation(classifier, test_feats, categories))
                analysis(classifier)
        scorelist.append(sum(scorelist)/len(scorelist))
        for score in scorelist:
                print(score)
        
        #grid search
        
        vectorizer = DictVectorizer()
        X_train, y_train = list(zip(*train_feats))
        X_train = vectorizer.fit_transform(X_train)
        best_param = gridsearch(X_train, y_train)
        print(best_param)



if __name__ == '__main__':
        main()


