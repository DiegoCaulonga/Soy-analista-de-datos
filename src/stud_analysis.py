
import pandas as pd

MBA = pd.read_csv("MBA.csv")

def workexp(a):
    """With this function, introducing his Student ID, we can know if the student had Working Experience before the MBA """
    return pd.DataFrame(MBA[MBA["Student ID"]==a]["Work Experience"])    


def sMBA(a):
    """With this function, introducing his Student ID, we can know the MBA he has studied"""
    return pd.DataFrame(MBA[MBA["Student ID"]==a]["MBA"])   


def sMBAavg(a):
    """With this funcion, introducing his Student ID, we can know the average MBA grades of the student"""
    return pd.DataFrame(MBA[MBA["Student ID"]==a]["MBA avg"])  


def sstatus(a):
    """With this function, introducing his student ID, we can know if the student is currently working"""
    return pd.DataFrame(MBA[MBA["Student ID"]==a]["Status"])


def studinfo(a,b):
    """With this function, we can know any other available information about the student, 
    introducing his Student ID as {a}, and the number of the other column as {b}"""
    return pd.DataFrame(MBA[MBA["Student ID"]==a][MBA.columns[b]])
