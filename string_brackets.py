str_good = "[(hjgfhjgdfhgf)]{}{[(lkjhkjggf)()](hgfdghdfh)}"
str_not_good = "[(cgfjhgkjh]kjgkjhg)"

def brackets_to_arr(str):
    arr = []
    for i in str:
        if i == '[' or i == ']' or i == '{' or i == '}' or i == '(' or i == ')':
            arr.append(i)
    return arr


def logic(arr_brackets):
    queue = []
    cnt = 0
    for i in arr_brackets:
        if i == '[' or i == '(' or i == '{':
            cnt = cnt + 1
            queue.append(i)
            continue
        if i == ']' or i == ')' or i == '}':
            if len(queue) == 0:
                return False
            if i == ']' and queue[cnt -1] == '[' or i == '}' and queue[cnt -1] == '{' or i == ')' and queue[cnt -1] == '(':
                queue.pop(cnt -1)
                cnt = cnt - 1
                continue
    if len(queue) > 0:
        return False
    return True


if logic(brackets_to_arr(str_good)):
    print("String is Balanced")
else:
    print("String in not Balanced")
