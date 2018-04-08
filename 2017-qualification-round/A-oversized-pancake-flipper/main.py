import os


def solve(line):
    [pancakes, pan] = line.split()

    pancakes = [pancake == "+" for pancake in pancakes]
    pan = int(pan)
    flips = 0
    i = 0
    while i < (len(pancakes) - pan + 1):
        if not pancakes[i]:
            for j in range(i, i + pan):
                pancakes[j] = not pancakes[j]
            flips += 1
        i += 1
    return str(flips) if all(pancakes) else "IMPOSSIBLE"



def main():
    with open("A-large-practice.in", "r") as f:
        data = f.readlines()
    for i in range(1, len(data)):
        result = solve(data[i])
        print("Case #%d: %s" % (i, result))
    


if __name__ == "__main__":
    main()