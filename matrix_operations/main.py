#/usr/bin/env python3
"""
This script reads the matrices and the operations from 'input.txt' and
prints out the results of the operations.

Usage: main.py

Author: TheKitsuneDev (Kis Vilmos Bendegúz)
Date: 2024.05
Event: nokia-hackathon
"""
import numpy as np

OPCHARS: set = {"+", "-", "*"}
matrices: dict = {}

with open("./input.txt") as f:
    line: str = f.readline().strip()
    while line != "operations":
        if line == "matrices":
            line = f.readline().strip() 
            continue

        if line == "":
            name: str = f.readline().strip()
            if name == "operations":
                line = name
                break

            line = f.readline().strip()
            rows: list = []
            while line != "":
                rows.append([int(i) for i in line.split(" ") if i != ''])
                line = f.readline().strip()
            matrices[name] = np.array(rows)
    

    while True:
        if line == "operations":
          f.readline()

        line = f.readline().strip()
        if line == "":
            break
        operations: list = line.split(" ")
        for i, operation in enumerate(operations):
            if operation not in OPCHARS:
                operations[i] = matrices[operation]
        
        while len(operations) > 1:
            for i, operation in enumerate(operations):
                if type(operation) != str:
                    continue
                if operation == "*":
                    operations[i] = np.dot(operations[i-1], operations[i+1])
                    operations.pop(i-1)
                    operations.pop(i)
                    continue
                if operation == "+":
                    operations[i] = np.add(operations[i-1], operations[i+1])
                    operations.pop(i-1)
                    operations.pop(i)
                if operation == "-":
                    operations[i] = np.subtract(operations[i-1], operations[i+1])
                    operations.pop(i-1)
                    operations.pop(i)

        print(line)
        for ro in operations[0]:
            print(" ".join([str(i) for i in ro]))
        print()