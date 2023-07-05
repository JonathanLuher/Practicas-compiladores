from PIL import Image
import os

def img_to_mat(image_path):
    image = Image.open(image_path).convert("L")
    width, height = image.size
    binary_matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel = image.getpixel((x, y))
            value = 1 if pixel == 0 else 0
            row.append(value)
        binary_matrix.append(row)
    return binary_matrix

def read_weight_matrix(file_path):
    with open(file_path, "r") as file:
        weight_matrix = [[int(value) for value in line.split()] for line in file]
    return weight_matrix

def compare_matrices(input_matrix, weight_matrices):
    results = []
    max_match = float('-inf')
    max_match_file = ""
    for file_index, weight_matrix in enumerate(weight_matrices):
        total = 0
        for i in range(len(input_matrix)):
            for j in range(len(input_matrix[0])):
                if input_matrix[i][j] == 1:
                    total += input_matrix[i][j] * weight_matrix[i][j]
        results.append(total)
        if total > max_match:
            max_match = total
            max_match_file = f"El numero {file_index}"
    return results, max_match_file

def main():
    image_path = "img_in.png"
    weight_directory = "pesos"
    weight_matrices = []

    input_matrix = img_to_mat(image_path)

    for file_name in os.listdir(weight_directory):
        if file_name.endswith(".txt"):
            file_path = os.path.join(weight_directory, file_name)
            weight_matrix = read_weight_matrix(file_path)
            weight_matrices.append(weight_matrix)

    results, max_match_file = compare_matrices(input_matrix, weight_matrices)

    for i, result in enumerate(results):
        print(f"Numero {i}: {result}")

    print(f"El archivo con más coincidencias es: {max_match_file}")

if __name__ == "__main__":
    main()
