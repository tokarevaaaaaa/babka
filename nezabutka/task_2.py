# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    dict_res = []
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]
        for line in lines:
            dict_res.append(line)

    res = json.dumps(dict_res, indent=4)

    print(res, end="")

    with open(OUTPUT_FILENAME, "w") as f:
        json.dump(res, f)

if __name__ == '__main__':
    # Нужно для проверки
    task()
