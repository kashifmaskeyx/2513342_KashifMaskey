def generate_permutations(s):
    if len(s) <= 1:
        return s
    
    perms = []

    for i in range(len(s)):
        a = s[i]
        rem = s[:i] + s[i+1:]

        for p in generate_permutations(rem):
            perms.append(a + p)

    return list(set(perms))

print(generate_permutations("abc"))


