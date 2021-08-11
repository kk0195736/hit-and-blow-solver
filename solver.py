import copy

def same_number_check(lst):
    for i in lst:
        if lst.count(i) >= 2:
            return True
    return False

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

def answer_check(n_lst, h, b): 
    for i in range(len(answer)):
        if flag[i]:
            x, y = h_and_b_check(answer[i], n_lst)
            if h == x and b == y:
                pass
            else:
                flag[i] = False

answer = []

for i in range(5556):
    t = list(str('{0:04d}'.format(i)))
    t_int = [int(s) for s in t]
    if 6 in t_int or 7 in t_int or 8 in t_int or 9 in t_int:
        pass
    else:
        answer.append(t_int)

flag = [True]*len(answer)

# 同色なしの場合
for i in range(len(answer)):
    if same_number_check(answer[i]):
        flag[i] = False

while True:
    numbers = list(map(int, input().split()))
    h, b = list(map(int, input().split()))
    plus_numbers = list(map(lambda x: x-1, numbers))
    answer_check(plus_numbers, h, b)
    for i in range(len(answer)):
        if flag[i]:
            plus_answer = list(map(lambda x: x+1, answer[i]))
            print(plus_answer)