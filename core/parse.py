def is_vowel(c):
    vowels = 'аеёиоуыэюя'
    if c in vowels:
        return(True)
    else:
        return(False)



def is_valid(line, s):
    vowels = 0

    for c in s:
        if is_vowel(c):
            vowels += 1

    if   line == 1 or line == 3:
        if vowels == 9:
            return(True)
        else:
            return(False)

    elif line == 2:
        if vowels == 8:
            return(True)
        else:
            return(False)

    elif line == 4:
        if vowels == 2:
            return(True)
        else:
            return(False)

    else:
        return(False)



def is_acceptable(s):
    letters = 'йцукенгшщзхъфывапролджэячсмитьбюё '
    for c in s:
        if c not in letters:
            return(False)
    return(True)



def parse(text):

    pre = list(
        map(
            lambda s: s.strip(),
            text.lower().replace('<br>','\n').splitlines()
        )
    )

    poroshki = []
    i = 0
    while i < len(pre) - 3:
        v1 = is_valid(1, pre[i])
        if v1:
            v2 = is_valid(2, pre[i+1])
            if v2:
                v3 = is_valid(3, pre[i+2])
                if v3:
                    v4 = is_valid(4, pre[i+3])
                    if v4:
                        poroshki.append(pre[i:i+4])
                        i += 4
                    else:
                        i += 2
                else:
                    i += 3
            else:
                i += 1
        else:
            i += 1

    return(poroshki)
