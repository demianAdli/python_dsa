"""
15 August, 2020
I have upgraded the book code and eliminate an eror which was
giving a too big of range for negative steps.
I have solved this problem by returning absolute values of step
and 'stop - start' clause of the book's code line 16 formula.
(Range class is in the page 81 code fragment 2.6)
"""


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('Step cannot be equal to zero')

        if stop is None:
            start, stop = 0, start

        self.__length = max(0, (abs(stop - start)
                                + abs(step) - 1) // abs(step))

        self.start = start
        self.stop = step

    def __len__(self):
        return self.__length

    def __getitem__(self, ind):
        if ind < 0:
            ind += len(self)

        if not 0 <= ind < self.__length:
            raise IndexError('Out of Range')

        return self.start + ind * self.stop


if __name__ == '__main__':
    my_range = Range(1, 10, 2)
    print(list(my_range))
