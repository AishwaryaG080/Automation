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
            {'point' : 'D', 'X' : 6, 'Y' : 5, 'label' : 'Blue'}

            ]

    print(Border)
    print("Marvellous UserDefined KNN")
    print(Border)

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)

    print(Border)

    new_point = {'X' : 2, 'Y' : 2}
    
    # Calculate all distances 

    for d in data:
        d['distance'] = EucDistance(d, new_point)
    
    print(Border)
    print("Calculated distances are :")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key= lambda item : item['distance'])

    print(Border)
    print("Sorted data is :")
    print(Border)
    
    for d in sorted_data:
        print(d)

    k=3
    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 elements are :")
    print(Border)

    for d in nearest:
        print(d)

    # Voting
    votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        votes[label] = votes.get(label,0) + 1

    print(Border)
    print("Voting result is :")
    print(Border)

    for d in votes:
        print("Name :", d, "No of votes :", votes[d])

    print(Border)

    pedicted_class = max(votes, key=votes.get)

    print("Predicted class of (3,3) is :", pedicted_class)

def main():

    MarvellousKNeighbourClassifier()

if __name__ == "__main__":


    main()