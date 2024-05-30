# 0x07. Rotate 2D Matrix
<table>
<td>Algorithm</td>
<td>Python</td>
</table>

This project contains interview coding challenges.

## Tasks To Complete

+ [x] 0. **Rotate 2D Matrix**<br/>[0-rotate_2d_matrix.py](0-rotate_2d_matrix.py) contains a module with a function that rotates an `n` x `n` 2D matrix 90 degrees clockwise with the following requirements:
  + Prototype: `def rotate_2d_matrix(matrix):`.
  + Do not return anything. The matrix must be edited **in-place**.
  + You can assume the matrix will have 2 dimensions and will not be empty.

```
jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$
```
