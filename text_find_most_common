text_50_words = "aaa bbb ccc vvv bbb rrr yyy aaa vvv bbb www eee ttt uuu"

file = 'words_text_file'

def word_to_arr_from_file(file_path):
    arr = []
    with open(file_path, "r") as f:
        for line in f:
            for word in line.split():
                arr.append(word)
    return arr


arr_words = word_to_arr_from_file(file)

json_obj = {}
json_obj["words"] = []

arr_words_diff = []

def unique():
    for i in arr_words:
        flag = False
        length = len(json_obj["words"])
        if length < 1:
            word = {"word": i, "cnt": 1}
            json_obj["words"].append(word)
        else:
            for j in json_obj["words"]:
                if j["word"] == i:
                    j["cnt"] = j["cnt"] + 1
                    flag = True
                    break
            if flag == False:
                word = {"word": i, "cnt": 1}
                json_obj["words"].append(word)


def find_max():
    unique()
    max = 0
    word = {}
    for i in json_obj["words"]:
        if i["cnt"] > max:
            max = i["cnt"]
            word = i
    return word

print(find_max())
