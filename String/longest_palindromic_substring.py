
def lps(string, result=[]):
    if len(string) > 0:
        end = 0
        for i in range(1, len(string)):
            if string[i] == string[0] and i > end:
                end = i
        if not result:
            result.append(string[0: end + 1])
        elif len(string[0: end+1]) > len(result[0]):
            result.pop()
            result.append(string[0: end + 1])
        lps(string[1:], result)


if __name__ == "__main__":
    string = "bananas"
    result = []
    lps(string, result)
    print(result[0])
