def no_boring_zeros(n):
    if n == 0:
        return n
    res = []
    string = str(n)
    for i in range(len(string)-1):
        if string[i] != "0":
            res.append(string[i])
        elif string[i+1] != "0":
            res.append("0")
    if res.append(string[len(string)-1]) != "0":
        res.append(string[len(string)-1])
    result = "".join(res)
    return int(result)

print(no_boring_zeros(183005))

def spin_words(a):
    b = a.split(' ')
    res = []
    if len(b) == 1:
        return ''.join(list(reversed(a)))
    else:
        for i in range(len(b)):
            if len(b[i]) >= 5:
                res.append(''.join(list(reversed(b[i]))))
            else:
                res.append(b[i])
    return ' '.join(res)


print(spin_words("ot"))