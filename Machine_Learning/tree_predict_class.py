def read_file(file_path, data_sep="," , ignore_first_line=False):
    prototypes = []
    #open file
    with open(file_path, "r") as fh:

        #strip_lines. Borrar espacios y craemos un generador
        strip_reader= (line.strip() for line in fh)
        #print(strip_reader) #si no se le pide, devolvera nada
        #print("strip_reader", list(strip_reader)) #consumismo la lista. Vaciamos memoria. Ya no mostrara nada despues si lo volvemos a llamar.

        #Filter empty lines
        filtered_reader = (line for line in strip_reader if line)#anyadir linias de caracter
        # en python: not "a" es False. not"" es True.
        #print("filtered_reader", list(filtered_read))
        #fh.readlines guarda en memoria la lista. No es eficiente.
        
        #Skip first line if needed. Lo ponemos despues del filtered porque la
        #primeria linea es de caracateres vacios
        
        if ignore_first_line:
            next(filtered_reader)
        
        #print(list(filtered_reader))
        
        # #Split line, parse token and append to prototypes
        for line in filtered_reader:
            prototypes.append([filter_token(token) for token in line.split(data_sep)])

    return prototypes

def filter_token(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token

#-----------t4------------------
def unique_counts(part):
    #import collections
    #return dict(collections.Counter(row[-1] for row in part))
    results={}
    for row in part:
        results[row[-1]] = results.get(row[-1],0)+1
        print(row)    
    return results

#-----------t5-------------
def gini_impurity(part):
    total = float(len(part))
    results = unique_counts(part)
    print (results.values())

    return 1 - sum((count/total)**2 for count in results.values())

#-----------t6-------------------
def entropy(part):
    from math import log
    log2 = lambda x: log(x) / log(2)
    results = unique_counts(part)
    total = float(len(part))
    return - sum((count/total) * log2(count/total) for count in results.values())

#------------t7-------------
def divideset(part,column,value):
    split_function = None

    if isinstance(value, int) or isinstance(value,float):
        split_function = lambda row: row[column] >= value
    else:
        split_function = lambda row: row[column] == value
    
    #split "part" according "split_function"
    set1 = []
    set2 = []

    for row in part:
        if split_function(row):
            set1.append(row)
        else:
            set2.append(row)

    return set1, set2

#--------------t8-----------
class decisionode:
    def __init__(self,col=-1, value=None, results=None, tb= None, fb=None):
        self.col = col
        self.value= value
        self.reslts = results
        self.tb = tb
        self.fb = fb





prototypes = read_file("decision_tree_example.txt", data_sep=",", ignore_first_line=True)

print(prototypes[0][2])
print (prototypes)

print (unique_counts(prototypes))

print (gini_impurity(prototypes))
print(entropy(prototypes))
set1, set2 = divideset(prototypes, column=3, value=20)

print(set1)
print ("\n")
print(set2)