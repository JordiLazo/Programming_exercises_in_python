import re
import csv
import math
import csv
import random
import seaborn
import pandas

def load_dataset(filename):
    dataset = list()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile,delimiter=",")
        header = False
        for row in reader:
            if not reader:
                header = True
                continue
            label = row[0]
            message = row[1]
            dataset.append((message,label))
    return dataset
dataset = load_dataset("spam.csv")
for i in range(5):
    print(dataset[i][0] + "==> " + dataset[i][1])


def getwords(doc):
    splitter = re.compile("\\W+") #ens ha de partir les paraules que no son numeros i lletres
    words = [word.lower() for word in splitter.split(doc)]
    words = [word for word in words if len(word) > 2 and len(word) < 20]
    
    return {word: 1 for word in words}
print(getwords("quick money at Cayman-Casino"))

class Classifier:
    def __init__(self, get_features, filename=None):
        self.fc = dict()#contador per cada paraula
        self.cc = dict()#contador per cada categoria
        self.getfeatures = get_features#
    
    def incf(self,f,cat):#increment the count of a feature/category pair
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat] += 1
    
    def incc(self,cat):#increment de count of a category
        self.cc.setdefault(cat,0)
        self.cc[cat] += 1
    def fcount(self,f,cat):#the number of times a features is in a category
        if f in self.fc and cat in self.fc[f]:
            return self.fc[f][cat]
    def catcount(self,cat):#number of items in a category
        if cat in self.cc:
            return self.cc[cat]
        return 0.0
    def totalcount(self): #total number of items
        return sum(self.cc.values())
    def categories(self): #the list of all categories
        return self.cc.keys()

    def fprob(self, f, cat):
        if self.catcount(cat) == 0:
            return 0.0
        total_count = float(self.totalcount())
        p_feat_category = float(self.fcount(f, cat)/total_count)
        p_category = float(self.catcount(cat)/total_count)
        return float(p_feat_category/p_category)

    def weightedprob(self,f,cat,prf,weight = 1.0, ap = 0.5):
        fprob = prf(f,cat)
        for cat in self.categories():
            self.fcount(f,cat)
        count = sum([self.fcount(f,cat) for cat in self.categories()])
        return ((weight * ap * count * fprob) / (count * weight))

    def train(self,item,cat):#train a classifier given an intem and its category
        #1.Extract feature
        features = self.getfeatures(item)
        #features = {gos:1, cat:1, animal:1}
        #2. Increment features/category counter
        for feat in features.keys():
            self.incf(feat,cat)
        #3. Increment category counter
        self.incc(cat)
        """
        Classifier.incf = incf
        Classifier.incc = incc
        Classifier.fcount = fcount
        Classifier.catcount = catcount
        Classifier.totalcount = totalcount
        Classifier.categories = categories
        """





c1 = Classifier(getwords)
c1.train("the quick brown fox jumps over the lazy dog and he quick quick quick", "good")
c1.train("the quick brown quick quick", "good")
c1.train("make quick money in the online casino","bad")

print(c1.fcount(f="quick",cat="good"))
print(c1.fcount(f="money",cat="good"))
#print(c1.cc)
print(c1.catcount("good"))

def sampletrain(classifier):
    documents = {
        ("Nobody quick owns the water", "good"),
        ("the quick rabbit jumps fences", "good"),
        ("buy pharmaceuticals now", "bad"),
        ("make quick money at the online casino", "bad"),
        ("the quick bron fox jumps", "good")
    }
    for item, category in documents:
        classifier.train(item,category)
c2 = Classifier(getwords)
sampletrain(c2)

print("quick in good:", c2.fcount("quick","good"))
print("quick in bad:", c2.fcount("quick","bad"))
sampletrain(c1)
print(c2.fprob("quick","good"))
print(c1.fprob("quick","good"))
c1.train("money","bad")
c1.train("money","bad")
#print(c1.weightedprob("money","bad",c1.fprob()))
#print(c1.weightedprob("money","good",c1.fprob))
