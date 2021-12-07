from app import convert_array_to_dict_tree, rec_get_tree
from models import validate_tree

tree = [
    {"id": 1, "pid": 0},
    {"id": 2, "pid": 1},
    {"id": 3, "pid": 1},
    {"id": 4, "pid": 2},
    {"id": 5, "pid": 3},
    {"id": 6, "pid": 2},
    {"id": 7, "pid": 4},
    {"id": 8, "pid": 4},
    {"id": 9, "pid": 10},
]

if __name__ == "__main__":
    tree = validate_tree(tree)
    tree_dict = convert_array_to_dict_tree(tree)
    for node in tree_dict:
        print(rec_get_tree(tree_dict, node))
