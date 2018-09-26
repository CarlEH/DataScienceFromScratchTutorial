from __future__ import division
from matplotlib import pyplot as plt 
import random as rnd

from collections import Counter

if __name__ == "__main__":
    # years = [1950,1960,1970,1980,1990,2000,2010]
    # gdp = [310.5,543.3, 1075.6, 2864.7, 5979.5, 10289.6, 14956.7]

    # plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    # plt.title("Nominal GDP")
    # plt.ylabel("Billions of $")
    # plt.show()

    # awards = [3,6,11,4,5,2]
    # movies = ["SW IV", "Train", "Snakes", "Muggles", "Gandalf","Ring"]

    # xs = [i + 0.5 for i,_ in enumerate(movies)]
    # plt.bar(xs, awards)
    # plt.ylabel("Nb of Awards")
    # plt.title("Best Movies")

    # plt.xticks([i + 0.5 for i,_ in enumerate(movies)], movies)
    # plt.show()

    # grades = [87,96,74,0,49,68,0,68,98,57,88,100]
    # decile = lambda grade: grade // 10 * 10
    # histogram = Counter(decile(grade) for grade in grades)


    # plt.bar([x for x in histogram.keys()], [x for x in histogram.values()], 8)
    # plt.axis([-5,105,0,5])
    # plt.xticks([10 * i for i in range(11)])
    # plt.xlabel("Decile")
    # plt.ylabel("Nb. of Students")
    # plt.title("Grades Distribution")
    # plt.show()

    # variance = [pow(2,x) for x in range(9)]
    # bias_squared = [pow(2,x) for x in range(8,-1,-1)]
    # total_error = [x + y for x,y in zip(variance,bias_squared)]
    # xs = [i for i,_ in enumerate(variance)]
    # print(variance, bias_squared, total_error, xs)
    # plt.plot(xs, variance, 'g-', label='variance')
    # plt.plot(xs, bias_squared, 'r-.', label='bias_sq')
    # plt.plot(xs, total_error, 'b:', label='tot error')

    # plt.legend(loc=9)
    # plt.xlabel('model complexity')
    # plt.title('Bias-Variance Tradeoff')
    # plt.show()


    friends = sorted([rnd.randrange(40,90) for _ in range(14)])
    minutes = sorted([rnd.randrange(110, 210) for _ in range(14)])
    labels = [chr(rnd.randrange(97,124)) for _ in range(14)]

    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                xy = (friend_count, minute_count),
                xytext = (5,-5),
                textcoords = 'offset points')
    plt.title("Daily Minutes by friend count")
    plt.xlabel("Nb. of Friends")
    plt.ylabel("Total minutes spent daily")
    plt.show()