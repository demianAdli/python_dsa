"""
July 14, 2020
eval_equation() evaluates if both sides of the equation are equal based
on the sum of each side characters' indices of one indexes each charater
beginning from left side between zero and nine.
eg. dog+cat=pig each side characters' indices sum is equal to 15

eq_dict() just defines the needed dictionary for theeval equation()
"""


def eq_dict(equation):
    no_duplicate = {"+": 0, "=": 0}
    ind = 0
    for letter in equation:
        if letter not in no_duplicate and letter not in '+=':
            no_duplicate[letter] = ind
            ind += 1
    return no_duplicate


def eval_equation(equation):
    chars_dict = eq_dict(equation)
    hint_chars = 0
    answer_chars = 0
    for each in equation:
        hint_chars += chars_dict[each]
        answer_chars += chars_dict[each]
        if each == "=":
            answer_chars = 0
    hint_chars -= answer_chars
    return hint_chars, answer_chars, hint_chars == answer_chars


if __name__ == "__main__":
    print(eval_equation("dog+cat=pig"))
    print(eval_equation("pot+pan=bib")[2])
    print(eval_equation("boy+girl=baby")[2])







