def convert_array_to_dict_tree(tree):
    tree_dict = {}
    for row in tree:
        tree_dict[row.id] = row.pid

    return tree_dict


def rec_get_tree(tree_dict, node=1, branch=[]):
    branch = branch + [str(node)]
    parent = tree_dict.get(node, 0)
    if parent == 0:
        return " -> ".join(branch[::-1])
    else:
        return rec_get_tree(tree_dict, parent, branch)
