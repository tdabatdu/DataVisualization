'''
@author: Tyler Dabat
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import path
import yfinance as yf


#have to make this global to be accessible to calculate absolute value
atomicWeights = np.array([1, 4, 6, 9, 10, 12])


def absolute_value(val):
    a = np.round(val/100.*atomicWeights.sum(), 0)
    return a

def checkFile(file):
    # happy path
    if path.exists(file):
        print(file,'exists')
        return True

    # error path
    else:
        print('It appears the file does not exists.  Please inspect and try again')
        return False


def partOne():
    labels = ['Hydrogen' , 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon']
    explode = (0,0,.1,0,0,0)
    explode2 = (0,0,0,.1,0,0)
    #print(atomicWeights)

    #pieCharts
    fig1, (ax1, ax2) = plt.subplots(2)
    ax1.pie(atomicWeights, labels = labels, explode=explode, autopct='%1.1f%%')
    ax2.pie(atomicWeights, labels = labels, explode=explode2, autopct=absolute_value)
    ax1.title.set_text('Atomic Weight Percentages')
    ax2.title.set_text('Atomic Weight as amu')
    plt.show()

def partTwo():

    if checkFile('py_ide2.csv'):
        p2_df = pd.read_csv('py_ide2.csv')

        #vertical bar chart
        fig1, ax1 = plt.subplots()
        ax1.bar(p2_df['IDE'], p2_df['Adoption'])
        ax1.set_ylabel('Adoption')
        plt.xticks(rotation=70)
        plt.title('Vertical Bar Chart of IDE Adoption')
        fig1.tight_layout()

        plt.show()


        #horizontal bar chart
        fig1, ax1 = plt.subplots()
        ax1.barh(p2_df['IDE'], p2_df['Adoption'])
        ax1.set_xlabel('Adoption')
        #plt.xticks(rotation=70)
        plt.title('Horizontal Bar Chart of IDE Adoption')
        fig1.tight_layout()

        plt.show()

    else:
        print('Part 2 needs the file py_ide2.csv in the same folder to complete')


def partThree():

    #daylist
    days = ['01/01/2020', '01/02/2020', '01/03/2020', '01/04/2020', '01/05/2020', '01/06/2020', '01/07/2020', '01/08/2020']
    values = np.random.uniform(100,200,8)

    p3_df = pd.DataFrame(data={'date':days, 'values':values})
    p3_df['date'] = pd.to_datetime(p3_df['date'])
    p3_df.set_index(keys='date', drop=True, append=False, inplace=True)

    fig1, (ax1, ax2) = plt.subplots(2)

    ax1.plot(p3_df.index.values, p3_df['values'])
    ax1.tick_params('x',labelrotation=70)
    ax1.title.set_text('Line Chart in Same Window')
    ax2.bar(p3_df.index.values, p3_df['values'])
    ax2.title.set_text('Bar Chart in Same Window')
    plt.xticks(rotation=70)

    fig1.tight_layout()

    plt.show()


def partFour():
    hbro = yf.Ticker("HAS")
    p4_df = pd.DataFrame(hbro.history(period='1mo'))

    #hopefully line charts are what is desired
    fig1, (ax1, ax2) = plt.subplots(2,sharex=True)
    ax1.plot(p4_df.index.values, p4_df['Volume'])
    ax1.tick_params('x',labelrotation=70)
    ax1.title.set_text('Hasbro Volume')
    ax2.plot(p4_df.index.values, p4_df['Close'])
    ax2.title.set_text('Hasbro Closing Prices')
    ax2.tick_params('x',labelrotation=70)

    fig1.tight_layout()

    print("Hopefully, line charts are what is desired.  It didn't specify in the prompt, so I took a best guess.")
    plt.show()



if __name__ == "__main__":
    # Part1
    print('part 1')
    partOne()

    #part2
    print('part 2')
    partTwo()

    #part3
    print('part 3')
    partThree()

    #part4
    print('part 4')
    partFour()
