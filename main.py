import os

altitude_file_path = os.path.join(os.getcwd(), 'fileOne.asc')

try:
    with open(altitude_file_path, 'r') as altitude:
        # Read the first thirty rows
        for _ in range(3):
            line = altitude.readline().strip()
            if not line:
                break  # End of file reached
            columns = line.split()

            # Read the first thirty columns in each row
            for i, column in enumerate(columns):
                if i < 3:
                    print(column, end='\t')
            print()

except FileNotFoundError:
    print(f"The file '{altitude_file_path}' does not exist.")

except IOError:
    print(f"An error occurred while reading the file '{altitude_file_path}'.")
