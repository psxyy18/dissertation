import re

def modify_first_column(input_file, output_file):
    try:
        # Read the data from the input text file
        with open(input_file, 'r') as f:
            data = [line.strip().split('\t') for line in f]

        # Function to extract the desired value from the first column
        def extract_value(text):
            pattern = r'^(CRC|ESCA|HCC|LUAD|NC|STAD)'
            match = re.match(pattern, text)
            return match.group(0) if match else ""

        # Update the first column based on the specified criteria
        for row in data:
            row[0] = extract_value(row[0])

        # Save the modified data to a new text file
        with open(output_file, 'w') as f:
            for row in data:
                f.write('\t'.join(row) + '\n')

        print("Modifications completed successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    input_file = 'input_file.txt'
    output_file = 'output_file.txt'

    modify_first_column('output_file.txt', 'output_file2.txt')
