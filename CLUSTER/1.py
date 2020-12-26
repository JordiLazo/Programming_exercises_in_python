import os
import sys

def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()

    colnames = lines[0].strip().split("\t")[1:]
    rownames = list()
    data = list()

    for line in lines[1:]:
        p = line.strip().split("\t")
        rownames.append(p[0])
        data.append(list(map(float, p[1:])))
    return rownames,colnames,data
     
blognames,words,data = readfile(os.path.abspath(sys.argv[1]))

print (blognames)
print (words)
print (data)