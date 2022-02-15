'''
@author: Tyler Dabat
'''
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


######### Part 1
mpg = pd.DataFrame(sns.load_dataset('mpg'))
mpg_num = mpg[['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year']]
cor = mpg_num.corr()


def part1corr(cor):
    fig, ax = plt.subplots(figsize=(14, 7))
    mask = np.zeros_like(cor, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    ax = sns.heatmap(cor, mask=mask, ax=ax, annot=True, annot_kws={'fontsize':10}, cmap="viridis")
    ax.set_xticklabels(ax.xaxis.get_ticklabels(), fontsize=14)
    ax.set_yticklabels(ax.yaxis.get_ticklabels(), fontsize=14)
    plt.tight_layout()
    plt.show();

def part1pair(df):
    sns.pairplot(df)
    plt.show()


############################### Part 2
diamonds = pd.DataFrame(sns.load_dataset('diamonds'))
diamonds = diamonds[(~diamonds['color'].isin(['D','E'])) & (diamonds['cut'] != 'Fair')]
#diamonds = diamonds[diamonds['cut']!='Fair'].cat.remove_unused_categories()
diamonds['color'] = diamonds['color'].cat.remove_unused_categories()
diamonds['cut'] = diamonds['cut'].cat.remove_unused_categories()

def part2():
    grid = sns.FacetGrid(diamonds, col = 'cut', row='color')
    grid.map(sns.scatterplot, 'price', 'carat')

    plt.show()


############################## Part 3
crash = pd.DataFrame(sns.load_dataset('car_crashes'))

def part3():
    sns.regplot(data=crash, x='speeding', y='total')
    plt.show()
    sns.regplot(data=crash, x='alcohol', y='total')
    plt.show()


############################### Part 4
iris = pd.DataFrame(sns.load_dataset('iris'))

def part4():
    fig, axes = plt.subplots(1, 4)
    cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    ax_count = 0
    for col in cols:
        sns.boxplot(y=col, x="species", data=iris,  ax=axes[ax_count])
        ax_count += 1

    plt.show()



if __name__ == "__main__":
    # Part1
    print('part 1')
    part1corr(cor)
    part1pair(mpg_num)

    print('')

    # Part2
    print('part 2')
    part2()

    print('')

    # Part3
    print('part 3')
    print('The Syllabus says plot a "scattergram".  I took a best guess as a scatter plot with a trend line/regression.')
    part3()

    print('')

    # part4
    print('part 4')
    part4()








