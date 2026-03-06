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
            {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
            {'point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
            {'point' : 'C', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
            {'point' : 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'},
            {'point' : 'E', 'X' : 4, 'Y' : 4, 'label' : 'Blue'}
            ]

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)

    new_point = {'X':2,'Y':2}

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