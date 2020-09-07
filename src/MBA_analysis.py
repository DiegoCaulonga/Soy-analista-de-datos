
import pandas as pd

MBA = pd.read_csv("MBA.csv")

def genderMBA(a):
    """With this function, we can know the number of people from each gender who have studied the introduced MBA type"""
    return pd.DataFrame(MBA[MBA["MBA"]== a]["Gender"].value_counts()) 


def statusMBA(a):
    """With this function, we can know the status of the MBA type students of that promotion"""
    return pd.DataFrame(MBA[MBA["MBA"]== a]["Status"].value_counts()) 


def degreeMBA(a):
    """With this function, we can know the degree students of this MBA type studied in University"""
    return pd.DataFrame(MBA[MBA["MBA"]== a]["Degree"].value_counts()) 


def avgMBA(a):
    """With this function, we can know the average qualification of the whole group of students of one MBA type"""
    return MBA[MBA["MBA"]== a]["MBA avg"].mean()




