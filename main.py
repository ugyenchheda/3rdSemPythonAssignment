import os

altitude = []
current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

altitude_file_path = os.path.join(current_directory, 'fileOne.asc')

directory_contents = os.listdir(os.getcwd())
print("Directory Contents:", directory_contents)
try:
    with open(altitude_file_path, 'r') as file:
        altitudes = file.read()
        print(altitudes)
        
except FileNotFoundError:
    print(f"The file '{altitude_file_path}' does not exist.")

except IOError:
    print(f"An error occurred while reading the file '{altitude_file_path}'.")