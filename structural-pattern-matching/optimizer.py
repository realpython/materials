import ast
import inspect
import textwrap


def main():
    source_code = inspect.getsource(sample_function)
    source_tree = ast.parse(source_code)
    target_tree = optimize(source_tree)
    target_code = ast.unparse(target_tree)

    print("Before:")
    print(ast.dump(source_tree))
    print(textwrap.indent(source_code, "| "))

    print("After:")
    print(ast.dump(target_tree))
    print(textwrap.indent(target_code, "| "))


def sample_function():
    return 40 + 2


def optimize(node):
    match node:
        case ast.Module(body, type_ignores):
            return ast.Module(
                [optimize(child) for child in body], type_ignores
            )
        case ast.FunctionDef():
            return ast.FunctionDef(
                name=node.name,
                args=node.args,
                body=[optimize(child) for child in node.body],
                decorator_list=node.decorator_list,
                returns=node.returns,
                type_comment=node.type_comment,
                type_params=node.type_params,
                lineno=node.lineno,
            )
        case ast.Return(value):
            return ast.Return(value=optimize(value))
        case ast.BinOp(ast.Constant(left), op, ast.Constant(right)):
            match op:
                case ast.Add():
                    return ast.Constant(left + right)
                case ast.Sub():
                    return ast.Constant(left - right)
                case _:
                    return node
        case _:
            return node


if __name__ == "__main__":
    main()
