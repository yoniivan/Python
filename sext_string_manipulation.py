str_good = "[(hjgfhjgdfhgf)]{}{[(lkjhkjggf)()](hgfdghdfh)}"
str_not_good = "[(cgfjhgkjh]kjgkjhg)"


def brackets_to_arr(str_not_good): # (n) notation
    arr = []
    for i in str_not_good:
        if i == '[' or i == ']' or i == '{' or i == '}' or i == '(' or i == ')':
            arr.append(i)
    return arr


def logic(arr_brackets): # (n) notation
    queue = []
    cnt = 0
    for i in arr_brackets:
        if i == '[' or i == '(' or i == '{':
            cnt = cnt + 1
            queue.append(i)
        if i == ']' or i == ')' or i == '}':
            if i == queue[cnt -1]:
                queue.pop(cnt -1)
            else:
                return False
    return True




def check_equal(dict, i):
    if dict["open"][i]["cnt"] == dict["close"][i]["cnt"]:
        bracket_equal = {"bracket": dict["open"][i]["bracket"], "status": True}
        dict["equal"].append(bracket_equal)
    else:
        bracket_equal = {"bracket": dict["open"][i]["bracket"], "status": False}
        dict["equal"].append(bracket_equal)


def string_maniplation(str): # (2n) notation
    count_of_brackets = 3
    cnt = 0
    brackets = {
        "open": [
            {"bracket": "{", "cnt": 0},
            {"bracket": "[", "cnt": 0},
            {"bracket": "(", "cnt": 0}],
        "close": [
            {"bracket": "}", "cnt": 0},
            {"bracket": "]", "cnt": 0},
            {"bracket": ")", "cnt": 0}
        ],
        "equal": []
    }
    # CHECK BY ASCII VALUE
    for i in str:
        x = ord(i)
        if x == 123:
            brackets["open"][0]["cnt"] = brackets["open"][0]["cnt"] + 1
            continue
        if x == 91:
            brackets["open"][1]["cnt"] = brackets["open"][1]["cnt"] + 1
            continue
        if x == 40:
            brackets["open"][2]["cnt"] = brackets["open"][2]["cnt"] + 1
            continue

        if x == 125:
            brackets["close"][0]["cnt"] = brackets["close"][0]["cnt"] + 1
            continue
        if x == 93:
            brackets["close"][1]["cnt"] = brackets["close"][1]["cnt"] + 1
            continue
        if x == 41:
            brackets["close"][2]["cnt"] = brackets["close"][2]["cnt"] + 1
            continue

    check_equal(brackets, 0)
    check_equal(brackets, 1)
    check_equal(brackets, 2)

    for i in brackets["equal"]:
        if i["status"]:
            cnt = cnt + 1

    if cnt == count_of_brackets:
        return True
    else:
        return False


def check_start_with(str): # (n) notation
    if not string_maniplation(str) or not logic(brackets_to_arr(str_not_good)):
        print("Text not valid")
        exit()
    bracket_1 = False # '{'
    bracket_2 = False # '['
    bracket_3 = False # '('
    for i in str:
        if i == '{':
            bracket_1 = not bracket_1
            continue
        if i == '[':
            bracket_2 = not bracket_2
            continue
        if i == '(':
            bracket_3 = not bracket_3
            continue

        if i == '}' and bracket_1:
            bracket_1 = not bracket_1
            continue
        if i == ']' and bracket_2:
            bracket_2 = not bracket_2
            continue
        if i == ')' and bracket_3:
            bracket_3 = not bracket_3
            continue

        if i == '}' and not bracket_1:
            print("Text not valid")
            exit()
        if i == ']' and not bracket_2:
            print("Text not valid")
            exit()
        if i == ')' and not bracket_3:
            print("Text not valid")
            exit()

    print("Text is not valid")


check_start_with(str_not_good) # SUM BIG O NOTATION  (5n)




