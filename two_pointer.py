def reverseWorld(word):
    res = ""
    l = 0
    r = 0
    while r < len(word):
        if r != "":
         r = r +1
        else:
            res = word[l:r+1][::-1]
            r = r + 1
            l = r
    res = res + " "
    res = res + word[l:r+2][::-1]
    return res[1:]

print(reverseWorld("Leandro De Melo"))
