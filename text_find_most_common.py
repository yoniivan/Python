# Text / words file needs to be inside the same folder as the "words_text.txt" file.

file = 'words_text_file.txt'


def word_to_arr_from_file(file_path):
    arr = []
    with open(file_path, "r") as f:
        for line in f:
            arr = [word for word in line.split()]
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
        if len(json_obj["words"]) < 1:
            word = {"word": i, "cnt": 1}
            json_obj["words"].append(word)
        else:
            for j in json_obj["words"]:
                if j.get("word") == i:
                    j.get("cnt") == j.get("cnt") + 1
                    flag = True
                    break
            if flag is not False:
                word = {"word": i, "cnt": 1}
                json_obj.get("words").append(word)


def find_max():
    unique()

    max_item = 0
    word = {}
    for i in json_obj["words"]:
        if i.get("cnt") > max_item:
            max_item, word = i["cnt"], i
    return word


print(find_max())
