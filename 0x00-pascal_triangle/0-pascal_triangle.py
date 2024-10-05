def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Every row starts with a 1
        prev_row = triangle[i - 1]
        # Generate the middle values of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Every row ends with a 1
        triangle.append(row)

    return triangle

