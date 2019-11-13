import ToyData as td
import ID3
import math
import numpy as np
from sklearn import tree, metrics, datasets
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
def entropy(target,classes):
  if(len(target) == 0):
    return 0
  else:
    counts = [0]*len(classes)
    for i,cl in enumerate(classes):
      for tar in target:
        if(cl == tar):
            counts[i] += 1
    probs = counts/np.sum(counts)
    entropy = 0
    for prob in probs:
      entropy-= prob*math.log2(prob)
    return entropy

def information_gain(target,classes,data,attributes):
  entr = entropy(target,classes)

  attr_entrop = [0]*len(attributes)
  for i,attr in enumerate(attributes):
    curr_sum = 0
    for val in attr:
      target_idxs = [ i for i in range(len(data)) if val in data[i] ]
      print(target_idxs)
      tar = np.array(list(target))
      curr_sum+= entropy(tuple(tar[target_idxs]),classes)
    attr_entrop[i] = curr_sum
    curr_sum = 0
  return attr_entrop

      
def main():

    attributes, classes, data, target, data2, target2 = td.ToyData().get_data()

    id3 = ID3.ID3DecisionTreeClassifier()

    #myTree = id3.fit(data, target, attributes, classes)
    print(information_gain(target,classes,data,attributes))


if __name__ == "__main__": main()