def transpose_text_file(input_file, output_file):
    try:
        # Read the data from the input text file
        with open(input_file, 'r') as f:
            data = [line.strip().split('\t') for line in f]

        # Transpose the data
        transposed_data = list(map(list, zip(*data)))

        # Save the transposed data to a new text file
        with open(output_file, 'w') as f:
            for row in transposed_data:
                f.write('\t'.join(row) + '\n')

        print("Data transposed successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    input_file = 'GSE174302_all-reads-available-samples.txt'
    output_file = 'output_file.txt'

    transpose_text_file(input_file, output_file)




