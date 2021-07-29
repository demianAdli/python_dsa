from pythonic_dsa_chapter_08.dsa_0808_linked_binary import *


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.

        In a single parameter form, token should be a leaf value (e.g., 42 ),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator.
        """
        super().__init__()          # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self.add_root(token)        # use inherited, nonpublic method
        if left is not None:        # presumably three-parameter form
            if token not in "+-*x/":
                raise ValueError("token must be valid operator")
            self.attach(self.roots(), left, right)  # use inherited, nonpublic method

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []     # sequence of piecewise strings to compose
        self.parenthesize_recur(self.roots(), pieces)
        return "".join(pieces)

    def parenthesize_recur(self, p, result):
        """Append piecewise representation of p s subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))     # leaf value as a string
        else:
            result.append('(')      # opening parenthesis
            self.parenthesize_recur(self.left(p), result)      # left subtree
            result.append(p.element())          # operator
            self.parenthesize_recur(self.right(p), result)     # right subtree
            result.append(')')     # closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self.evaluate_recur(self.roots())

    def evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())    # we assume element is numeric
        else:
            op = p.element()
            left_val = self.evaluate_recur(self.left(p))
            right_val = self.evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val     # treat x or as multiplication


def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression.
       27 August, 2020
       It is vital to apply all the parentheses correctly, otherwise
       it returns a wrong answer (without any 'Exception's)
       e.g.
       build_expression_tree(((2*3)+6)/3) returns 3 which is the
       last digit in the input expression (missed last right parenthesis)
       build_expression_tree(((2*3)+6)/3) returns 4 which is the
       correct output.
    """
    result = []         # we use Python list as stack
    for t in tokens:
        if t in '+-x*/':        # t is an operator symbol
            result.append(t)         # push the operator symbol
        elif t not in '()':     # consider t to be a literal
            result.append(ExpressionTree(t))     # push trivial tree storing value
        elif t == ')':         # compose a new tree from three constituent parts
            right = result.pop()     # right subtree as per LIFO
            op = result.pop()        # operator symbol
            left = result.pop()      # left subtree
            result.append(ExpressionTree(op, left, right))   # repush tree
    # we ignore a left parenthesis
    return result.pop()


if __name__ == "__main__":
    calc_1 = ExpressionTree('+', ExpressionTree('42'), ExpressionTree('42'))
    calc_2 = ExpressionTree('*', ExpressionTree('2'), ExpressionTree('34'))
    calc = ExpressionTree('+', calc_1, calc_2)
    print(calc)
    print(calc.evaluate())

    print(build_expression_tree(['(', '(', '2', '*', '3', ')',
                                 '+', '6', ')', '/', '3', ')']))

    print(build_expression_tree('((2*3)+6)/3)'))
