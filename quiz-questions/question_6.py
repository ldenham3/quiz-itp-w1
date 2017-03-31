"""Intro to Python - Week 1 - Quiz."""


# Question 6
def matrix_sum(a_matrix):
    """Implement the code required to make this function work.

    Write a function `matrix_sum` that sums all the values in a square matrix.
    Example:

    m1 = [
        [2, 9, 1],
        [3, 1, 18],
        [22, 8, 16]
    ]
    m2 = [
      [81, 29],
      [31, 57]
    ]

    matrix_sum(m1)  #  80
    matrix_sum(m2)  # 198
    """
    m_sum = 0
    if type(a_matrix) == list:
        for a_list in a_matrix:
            for number in a_list:
                m_sum += number
        return m_sum
    else:
        return "matrix not given"
