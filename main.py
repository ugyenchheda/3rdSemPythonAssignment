import os
altitude_file_path = os.path.join(os.getcwd(), 'fileOne.asc')

try:
    with open(altitude_file_path, 'r') as altitude:
        for _ in range(30):
            line = altitude.readline().strip()
            if not line:
                break  # End of file reached
            columns = line.split()

            for i, column in enumerate(columns):
                if i < 30:
                    print(column, end='\t')

except FileNotFoundError:
    print(f"The file '{altitude_file_path}' does not exist.")

except IOError:
    print(f"An error occurred while reading the file '{altitude_file_path}'.")
