import re
import math
import pprint

def getwords(doc):
    splitter = re.compile('\\W*') #ens ha de partir les paraules que no son numeros i lletres
    words = [word.lower() for word in splitter.split(doc)]
    words = [word for word in words if len(word) > 2 and len(word) < 20]
    
    return {word: 1 for word in words}

class Classifier:
    def __init__(self, get_features, filename=None):
        self.fc = dict()#contador per cada paraula
        self.cc = dict()#contador per cada categoria
        self.get_features = get_features#
    
    def incf(self,f,cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat] += 1
    
    def incc(self,cat):
        self.cc[f].setdefault(cat,0)
        self.cc[f] += 1
    def fcount(self,f,cat):
        if f in self.fc and cat in self.fc[f]:
            return self.fc[f][cat]
    def catcount(self,cat):
        if cat in self.cc:
            return self.cc[cat]
        return 0.0
    def totalcount(self,cat):
        return sum(self.cc.values())
    def categories(self):
        return self.cc.keys()
    def train(self,item,cat):
        #1.Extract feature
        features = self.get_features(item)
        #features = {gos:1, cat:1, animal:1}
        #2. Increment features/category counter
        for word in features.keys():
            self.incf(feat,cat)
        #3. Increment category counter
        self.incc(cat)

        Classifier.incf = incf
        Classifier.incc = incc
        Classifier.fcount = fcount
        Classifier.catcount = catcount
        Classifier.totalcount = totalcount
        Classifier.categories = categories


    

c1 = Classifier(getwords)
c1.train("the quick brown fox jumps over the lazy dog", "good")
c1.train("make quick money in the online casino","bad")

print c1.catcount("quick","good")
print getwords("quick money at Cayman-Casino")