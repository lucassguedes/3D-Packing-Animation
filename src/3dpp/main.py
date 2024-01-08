from mip import *
from itertools import permutations


def main():

    model = Model()

    W = 0
    H = 0
    D = 0

    w = list()
    h = list()
    d = list()

    m = list()

    numberOfVariables = -1
    # Reading the instance
    with open('instance.txt') as f:
        for index, line in enumerate(f.readlines()):
            separated_values = line.replace("\n", "").split(",")
            separated_values = [float(value) for value in separated_values]

            if len(separated_values) == 3:
                if index == 0:
                    W = float(separated_values[0])
                    H = float(separated_values[1])
                    D = float(separated_values[2])
                else:
                    possible_permutations = set(permutations(separated_values, 3))
                    m.append(len(possible_permutations))

                    w.append([value[0] for value in possible_permutations])
                    h.append([value[1] for value in possible_permutations])
                    d.append([value[2] for value in possible_permutations])

                numberOfVariables+=1
            else:
                unit = separated_values[0]
    # Creating the variables

    x = list()
    y = list()
    z = list()

    s = list()
    left = dict()
    right = dict()
    under = dict()
    over = dict()
    behind = dict()
    inFront = dict()

    for i in range(numberOfVariables):
        x.append(model.add_var(name=f'x_{i+1}', var_type=CONTINUOUS, lb=0))
        y.append(model.add_var(name=f'y_{i+1}', var_type=CONTINUOUS, lb=0))
        z.append(model.add_var(name=f'z_{i+1}', var_type=CONTINUOUS, lb=0))

        s.append(list())
        for k in range(m[i]):
            s[i].append(model.add_var(name=f's_{i+1}_{k+1}', var_type=BINARY))

        left[i] = dict()
        right[i] = dict()
        under[i] = dict()
        over[i] = dict()
        behind[i] = dict()
        inFront[i] = dict()

        for j in range(i+1, numberOfVariables):
            left[i][j] = model.add_var(name=f'l_{i+1}_{j+1}', var_type=BINARY)
            right[i][j] = model.add_var(name=f'r_{i+1}_{j+1}', var_type=BINARY)
            under[i][j] = model.add_var(name=f'u_{i+1}_{j+1}', var_type=BINARY)
            over[i][j] = model.add_var(name=f'o_{i+1}_{j+1}', var_type=BINARY)
            behind[i][j] = model.add_var(name=f'b_{i+1}_{j+1}', var_type=BINARY)
            inFront[i][j] = model.add_var(name=f'f_{i+1}_{j+1}', var_type=BINARY)

    # Creating the model

    model.objective = maximize(xsum(s[i][k] for i in range(numberOfVariables) for k in range(m[i])))

    for i in range(numberOfVariables):
        for j in range(i+1, numberOfVariables):
            model += left[i][j] + right[i][j] + under[i][j] + over[i][j] + behind[i][j] + inFront[i][j] >= xsum(s[i][k] for k in range(m[i])) + xsum(s[j][k] for k in range(m[j])) - 1

            model += left[i][j] + right[i][j] + under[i][j] + over[i][j] + behind[i][j] + inFront[i][j] <= xsum(s[i][k] for k in range(m[i]))
            model += left[i][j] + right[i][j] + under[i][j] + over[i][j] + behind[i][j] + inFront[i][j] <= xsum(s[j][k] for k in range(m[j]))


            model += x[i] - x[j] + W*left[i][j] <= W - \
                xsum(s[i][k]*w[i][k] for k in range(m[i]))
            model += x[j] - x[i] + W*right[i][j] <= W - \
                xsum(s[j][k]*w[j][k] for k in range(m[j]))
            model += y[i] - y[j] + H*under[i][j] <= H - \
                xsum(s[i][k]*h[i][k] for k in range(m[i]))
            model += y[j] - y[i] + H*over[i][j] <= H - \
                xsum(s[j][k]*h[j][k] for k in range(m[j]))
            model += z[i] - z[j] + D*behind[i][j] <= D - \
                xsum(s[i][k]*d[i][k] for k in range(m[i]))
            model += z[j] - z[i] + D*inFront[i][j] <= D - \
                xsum(s[j][k]*d[j][k] for k in range(m[j]))

        model += xsum(s[i][k] for k in range(m[i])) == 1

    for i in range(numberOfVariables):
        model += x[i] <= W - xsum(s[i][k]*w[i][k] for k in range(m[i]))
        model += y[i] <= H - xsum(s[i][k]*h[i][k] for k in range(m[i]))
        model += z[i] <= D - xsum(s[i][k]*d[i][k] for k in range(m[i]))

    # Solving the problem

    model.max_gap = 0.05
    status = model.optimize(max_seconds=10)

    positions = []
    orientations = []

    if status == OptimizationStatus.OPTIMAL:
        print(f'solution: {model.objective_value}')
        items_orientation = dict()
        for v in model.vars:
            if v.name[0] == "s" and v.x >= 0.98:
                sep_name = v.name.split("_")
                item_name = f"Item {sep_name[1]}"

                items_orientation[item_name] = list()
                # items_orientation[item_name].append(round(w[int(sep_name[1])-1][int(sep_name[2])-1]/unit))
                # items_orientation[item_name].append(round(h[int(sep_name[1])-1][int(sep_name[2])-1]/unit))
                # items_orientation[item_name].append(round(d[int(sep_name[1])-1][int(sep_name[2])-1]/unit))
                items_orientation[item_name].append(w[int(sep_name[1])-1][int(sep_name[2])-1])
                items_orientation[item_name].append(h[int(sep_name[1])-1][int(sep_name[2])-1])
                items_orientation[item_name].append(d[int(sep_name[1])-1][int(sep_name[2])-1])

        print("Items:")
        position = []
        for index, v in enumerate(model.vars):
            
            if v.name[0] == "x":
                sep_name = v.name.split("_")
                print(f"\tItem {sep_name[1]}:")
                # print(f"\t\tposition: [{round(v.x/unit)}, ", end="")
                print(f"\t\tposition: [{v.x}, ", end="")
                position.append(v.x)
            elif v.name[0] == "y":
                print(f"{v.x}, ", end="")
                position.append(v.x)
            elif v.name[0] == "z":
                print(f"{v.x}],")
                position.append(v.x)
                positions.append(position)
                position = []
                sep_name = v.name.split("_")
                print(f"\t\torientation: {items_orientation[f'Item {sep_name[1]}']}")
                orientations.append(items_orientation[f'Item {sep_name[1]}'])


        print("boxes_dimensions = ", end="")
        print(orientations)
        print("boxes_positions = ", end="")
        print(positions)

        model.write("3DPacking.lp")


if __name__ == "__main__":
    main()
