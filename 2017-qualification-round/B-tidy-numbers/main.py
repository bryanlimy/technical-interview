import os


def solve(number):
    if len(number) <= 1:
        return number
    prev = "0"
    for i, digit in enumerate(number):
        if prev > digit:
            number = str(int(number[:i]) - 1) + "9" * (len(number) - i)
            if number[0] == "0":
                number = number[1:]
            return solve(number)
        prev = digit
    return number


def brute_force(number):
    number = int(number)
    while sorted(str(number)) != list(str(number)):
        number -= 1
    return str(number)


def main():
    with open("B-large-practice.in", "r") as f:
        data = f.read().splitlines()
    for i in range(1, len(data)):
        result = solve(data[i])
        print("Case #%d: %s" % (i, result))
    

if __name__ == "__main__":
    main()