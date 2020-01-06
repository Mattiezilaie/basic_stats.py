# Author: Mahtab Zilaie
# Date: January 6, 2020
# Description: class called Person containing two data members called name and age. A function outside
# of class is made called basic_stats that has one parameter called person_list. This function contains
# a for loop that goes through each person in the person_list and adds all the ages to a new list called
# age. The age list is used in order to find the mean, median, and mode of all the ages. The fucntion then
# returns the mean, median, and mode in the form of a tuple.

from statistics import mean, median, mode

class Person:
    """Class named Person that contains two data members name and age"""
    def __init__(self, name, age):
        """init function that initializes the two data members (in the Person class) name and age"""
        self.name = name
        self.age = age

def basic_stats(person_list):
    """function called basic_stats with parameter person_list that adds all the ages into a list
    then uses the mean, median, and mode that were imported from the statistics library and returns those
     values in a form of a tuple"""
    age = []
    for person in person_list: # loops through each person in list
        age.append(person.age) # every age goes into list
    mean_age = mean(age)
    median_age = median(age)
    mode_age = mode(age)
    return mean_age, median_age, mode_age


