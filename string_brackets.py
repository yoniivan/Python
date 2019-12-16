# A program the check if bracket are valid in terms of math rules. 


str_good = "[(hjgfhjgdfhgf)]{}{[(lkjhkjggf)()](hgfdghdfh)}"
str_not_good = "[(cgfjhgkjh]kjgkjhg)"

def brackets_to_arr(str):
    arr = []
    for char in str:
        if char == '[' or char == ']' or char == '{' or char == '}' or char == '(' or char == ')':
            arr.append(char)
    return arr


def logic(arr_brackets):
    queue = []
    cnt = 0
    for i in arr_brackets:
        if i == '[' or i == '(' or i == '{':
            cnt += 1
            queue.append(i)
            continue
        if i == ']' or i == ')' or i == '}':
            if len(queue) == 0:
                return False
            if i == ']' and queue[cnt-1] == '[' or i == '}' and queue[cnt-1] == '{' or i == ')' and queue[cnt-1] == '(':
                queue.pop(cnt-1)
                cnt -= 1
                continue
    if len(queue) > 0:
        return False
    return True


if logic(brackets_to_arr(str_good)):
    print("String is Balanced")
else:
    print("String in not Balanced")
