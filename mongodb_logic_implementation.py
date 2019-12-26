# Takes a MongoDB query as a param and prints all rows (inventory) that are valid to the given query.
# Example: "{\"\$and\": [{\"name\": {\"\$eq\": \"ij\"}}, {\"\$or\": [{\"price\": {\"\$lt\": 2}}, {\"qty\": {\"\$gte\": 15}}]}]}"
# Will return [{'name': 'ij', 'qty': 3, 'price': 1.99}]

import sys
import json

inventory = [
    {"name": "xy", "qty": 2, "price": 0.99},
    {"name": "ab", "qty": 15, "price": 2.99},
    {"name": "ij", "qty": 3, "price": 1.99},
    {"name": "cd", "qty": 5, "price": 3.99},
]
operators_available = {"$and", "$or", "$eq", "$ne", "$in", "$nin", "$gt", "$gte", "$lt", "$lte"}


def outer(query, operator, db):
    arr = []

    def inner():
        for dict_row in db:
            if operator not in operators_available:
                if not_in_operators(dict_row.get(operator), query):
                    arr.append(dict_row)
                    continue
                else:
                    continue
            fn_name = "op_" + operator[1:]
            if eval(fn_name)(query, dict_row):
                arr.append(dict_row)
        return arr
    return inner()


def op_gt(db_value, wanted_value):
    return db_value < wanted_value


def op_lt(db_value, wanted_value):
    return db_value > wanted_value


def op_eq(db_value, value):
    return db_value == value


def op_ne(db_value, value):
    return db_value != value


def op_gte(db_value, value):
    return db_value == value or db_value > value


def op_lte(db_value, value):
    return db_value == value or db_value < value


def op_in(db_value, value_arr):
    return str(db_value) in value_arr


def op_nin(db_value, value_arr):
    return not (str(db_value) in value_arr)


def __and_or_logic(value, dict_row, key):
    value_operator, value_from_value = list(value.items())[0]
    db_value = dict_row.get(key)
    fn_name = "op_" + value_operator[1:]
    return eval(fn_name)(value_from_value, db_value)


def op_or(query, dict_row):
    for query_row in query:
        for key, value in query_row.items():
            return __and_or_logic(value, dict_row, key) and type(value) is not list
    return False


def op_and(query, dict_row):
    for query_row in query:
        for key, value in query_row.items():
            if type(value) is not list:
                if __and_or_logic(value, dict_row, key):
                    continue
                else:
                    return False
            else:
                fn_name = "op_" + key[1:]
                if eval(fn_name)(value, dict_row):
                    continue
                else:
                    return False
    return True


def not_in_operators(attr, query):
    operator, value = list(query.items())[0]
    fn_name = "op_" + operator[1:]
    return eval(fn_name)(attr, value)


def find(db, expression):
    return [outer(value, key, db) for key, value in expression.items()]


def main():
    if len(sys.argv) != 2:
        print("invalid number of arguments")
        return -1
    input_param = str(sys.argv[1]).replace('\\', '')
    results = find(inventory, json.loads(input_param))
    for record in results:
        print(record)


if __name__ == "__main__":
    main()
