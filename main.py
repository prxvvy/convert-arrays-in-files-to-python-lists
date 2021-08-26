def read_file(file_name, mode="r"):
    with open(f"{file_name}.txt", mode, encoding="UTF8") as file:
        return [i.strip("\n") for i in file]


def convert_to_matrix(matrix):
    matrix_ = []
    for item in matrix:
        list_ = []
        for element in item:
            if element != ' ':
                list_.append(int(element))
        matrix_.append(list_)
    return matrix_


def main():
    matrix = []
    for row_matrix_one, row_matrix_two in zip(convert_to_matrix(read_file("matrix1")), convert_to_matrix(read_file("matrix2"))):
        list_ = []
        for col_matrix_one, col_matrix_two in zip(row_matrix_one, row_matrix_two):
            item = "x"
            if col_matrix_one == col_matrix_two:
                item = "o"
            list_.append(item)
        matrix.append(list_)
    with open("matrix_result.txt", "w", encoding="UTF8") as file:
        for rows in range(5):
            for cols in range(5):
                file.write(f"{matrix[rows][cols]} ")
            file.write("\n")


if __name__ == "__main__":
    main()
