# TODO решите задачу
import json
from pprint import pprint

def task() -> float:
    file_path = "input.json"
    with open(file_path, 'r') as fh:
        data = json.load(fh)
        sum = 0
        for dict in data:
            sum += (dict['score'] * dict['weight'])
        sum = round(sum, 3)
    return sum


print(task())
