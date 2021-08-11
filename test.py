rng = {0,1,2,3,4,5}

t = [0,1,2,3]
s = t

for i in t:
    rng.remove(i)

print(rng)

for i in rng:
    print(i)

for i in range(4):
    s[i] = 7
    print(s)
print(t)

def h_and_b_check(a_lst, b_lst):
    x = 0
    y = 0
    for i in range(4):
        if a_lst[i] == b_lst[i]:
            x += 1
            y -= 1
    for i in a_lst:
        if i in b_lst:
            y += 1
    
    return x, y

a = [0,2,1,4]
b = [1,3,2,1]

print(h_and_b_check(a,b))