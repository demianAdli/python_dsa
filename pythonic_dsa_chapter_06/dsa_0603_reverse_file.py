from pythonic_dsa_chapter_06.dsa_0602 import Stack as ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    stack = ArrayStack()
    original = open(filename)
    for line in original:
        stack.push(line.rstrip("\n"))       # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')        # reopening file overwrites original
    while not stack.is_empty():
        output.write(stack.pop() + "\n")    # re-insert newline characters
    output.close()


reverse_file("text.txt")

with open("text.txt", "r") as file:
    for a_line in file:
        print(a_line)
