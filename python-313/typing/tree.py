from typing import TypeGuard

type Tree = list[Tree | int]


def is_tree(obj: object) -> TypeGuard[Tree]:
    return isinstance(obj, list) and all(
        is_tree(elem) or isinstance(elem, int) for elem in obj
    )


def get_left_leaf_value(tree_or_leaf: Tree | int) -> int:
    if is_tree(tree_or_leaf):
        return get_left_leaf_value(tree_or_leaf[0])
    else:
        return tree_or_leaf


# %% Python 3.13
#
# from typing import TypeIs
#
# type Tree = list[Tree | int]
#
# def is_tree(obj: object) -> TypeIs[Tree]:
#     return isinstance(obj, list) and all(
#         is_tree(elem) or isinstance(elem, int) for elem in obj
#     )
#
# def get_left_leaf_value(tree_or_leaf: Tree | int) -> int:
#     if is_tree(tree_or_leaf):
#         return get_left_leaf_value(tree_or_leaf[0])
#     else:
#         return tree_or_leaf

# %% Use the tree
#
print(get_left_leaf_value([[[[3, 13], 12], 11], 10]))
