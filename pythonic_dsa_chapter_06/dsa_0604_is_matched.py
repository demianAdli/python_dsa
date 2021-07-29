from pythonic_dsa_chapter_06.dsa_0602 import Stack as ArrayStack


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = "({["           # opening delimiters
    righty = ")}]"          # respective closing delims
    stack = ArrayStack()
    for c in expr:
        if c in lefty:
            stack.push(c)       # push left delimiter on stack
        elif c in righty:
            if stack.is_empty():
                return False    # nothing to match with
            if righty.index(c) != lefty.index(stack.pop()):
                return False        # mismatched
    return stack.is_empty()


if __name__ == "__main__":
    print(is_matched("[(5 * 2)][][]"))
    print(is_matched("[(5 * 2)][)[]"))