'''
@author: Tyler Dabat
'''
import csv
import random
from os import path
from math import pi, cos
import numpy as np
import pandas as pd

######### Part 1
# static elements
elements = [['name', 'symbol', 'atomic number'],
            ['Hydrogen', 'H', 1],
            ['Helium', 'He', 2],
            ['Lithium', 'Li', 3],
            ['Beryllium', 'Be', 4],
            ['Boron', 'B', 5],
            ['Carbon', 'C', 6],
            ['Nitrogen', 'N', 7],
            ['Oxeygen', 'O', 8]]
more_elements = np.array([['fluorine', 'F', 9], ['Neon', 'Ne', 10]])
weights = [1, 4, 6, 9, 10, 12, 14, 15, 18, 20]


# writing to csv within this .py as I am not sure if we were supposed to do it externally or not,
# but this option seems safer
def writeElements(file):
    with open(file, 'w', newline='') as outFile:
        elementWriter = csv.writer(outFile)

        elementWriter.writerows(elements)


# confirming the file is there/makes sure there wasn't write permission errors or anything
def checkFile(file):
    # happy path
    if path.exists(file):
        print('Elements csv exists')
        return True

    # error path
    else:
        print('It appears the file does not exists.  Please inspect and try again')
        return False


def setupDf(file):
    if checkFile(file):
        elements_df = pd.read_csv(file)
        elements_df.loc[len(elements_df)] = more_elements[0]
        elements_df.loc[len(elements_df)] = more_elements[1]
        elements_df['weight'] = weights
        print(elements_df)
    return elements_df

############# Part 2
greek = ['delta', 'beta', 'ets', 'zeta', 'pi', 'phi', 'alpha', 'epsilon', 'lambda']
rand_dist_one = np.random.normal(10,1.5,9)
rand_dist_two = np.random.normal(10,1.5,9)
angle = np.array([random.uniform(0,2*pi) for x in range(0,9)])
cosine = np.array([cos(x) for x in angle])
part2_dict = {'letter': greek, 'Dist 1': rand_dist_one, 'Dist 2': rand_dist_two, 'angle': angle, 'cosine':cosine}

def p2_createDF(dict):
    p2_df = pd.DataFrame(dict)
    print(p2_df)

    return p2_df

def trim(df):
    df = df.sort_values('letter')
    df = df.drop(['Dist 1', 'cosine'], axis = 1)
    df = df.drop(index=1)
    print(df)

    return df



############# Part 3
def createFibonacci(length):
    a = 0
    b = 1
    fib_seq = [1]

    if length <= b:
        print('Sorry wrong input')
        return None

    for i in range(1,length):
        c = a + b
        fib_seq.append(c)
        a = b
        b = c

    print(fib_seq)
    return fib_seq

def lastFibRatio(fib_seq, scope):
    ratios = []
    n = -1

    for i in range(0,scope):
        ratios.append(fib_seq[n]/fib_seq[n-1])
        n = n - 1
    print(ratios)



############# Part 4

def kelvinToRankine(temp):
    rankine = temp * (9/5)

    #print(rankine)
    return rankine

kelvin_temps = [10,100,300,900,1000]

rankine = [(lambda x: kelvinToRankine(x))(x) for x in kelvin_temps]



if __name__ == "__main__":
    # Part1
    print('part 1')
    writeElements('elements.csv')
    elements_df = setupDf('elements.csv')
    print('')

    # Part2
    print('part 2')
    df_2 = p2_createDF(part2_dict)
    trim(df_2)
    print('')

    # Part3
    print('part 3')
    fib = createFibonacci(12)
    lastFibRatio(fib, 5)
    # The observations on the ratios is quite interesting.  They always seem to be an approximate ratio of 1.6
    print('')

    # part4
    print('part 4')
    print(kelvin_temps)
    print(rankine)







