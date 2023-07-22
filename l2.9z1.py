import numpy as np
import pandas as pd
import random
import json




def generate(name, num):
    
    data = {
        'Number1': [random.random() for _ in range(num)],
        'Number2': [random.random() for _ in range(num)],
        'Number3': [random.random() for _ in range(num)],
    }

    df = pd.DataFrame(data)
    df.to_csv(name, index=False)


generate('random_numbers.csv', num=1000)

def roots(func):
    def csv(name):
        df = pd.read_csv(name)
        results = []

        for index, row in df.iterrows():
            a, b, c = row['Number1'], row['Number2'], row['Number3']
            result = func(a, b, c)
            results.append(result)

        return results

    return csv

def roots(func):
    def csv(name):
        df = pd.read_csv(name)
        results = []

        for index, row in df.iterrows():
            a, b, c = row['Number1'], row['Number2'], row['Number3']
            result = func(a, b, c)
            results.append(result)

        return results

    return csv



def decorator(func):
    def wrapper(*args):
        result = func(*args)

        data = {
            'input_parameters': args,
            'result': result
        }

        with open('output.json', 'w') as json_file:
            json.dump(data, json_file)

        return result

    return wrapper


generate('random_numbers.csv', 500)
@roots
@decorator

def roots(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + np.sqrt(d)) / (2*a)
        root2 = (-b - np.sqrt(d)) / (2*a)
        return root1, root2
    elif d == 0:
        root = -b / (2*a)
        return root, root
    else:
        return None

results = roots('random_numbers.csv')
print(results)

