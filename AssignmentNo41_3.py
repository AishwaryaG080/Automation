#  [A,B,C,D]
# X[1,2,3,6]
# Y[2,3,1,5]
#  [R,R,B,B]    

import numpy as np
import math

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans

def MarvellousKNeighbourClassifier():
    
    Border = "-"*40

    data = [
            {'point' : 'A', 'X' : 2, 'Y' : 60, 'label' : 'fail'},
            {'point' : 'B', 'X' : 5, 'Y' : 80, 'label' : 'pass'},
            {'point' : 'C', 'X' : 6, 'Y' : 85, 'label' : 'pass'},
            {'point' : 'D', 'X' : 1, 'Y' : 50, 'label' : 'fail'}
            ]

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)

    new_point = {'X':4,'Y':70}

    # Calculate distances
    for d in data:
        d['distance'] = EucDistance(d,new_point)

    sorted_data = sorted(data,key=lambda item:item['distance'])

    k_values = [1,3,5]

    for k in k_values:

        nearest = sorted_data[:k]

        votes = {}

        for n in nearest:
            label = n['label']
            votes[label] = votes.get(label,0)+1

        predicted_class = max(votes,key=votes.get)

        print("k =",k,"->",predicted_class)

def main():

    MarvellousKNeighbourClassifier()

if __name__ == "__main__":
    main()