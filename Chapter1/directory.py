import os

def print_directory_contents(directory):
    try:
        # Print the contents of the directory
        print(f"Contents of {directory}:")
        for item in os.listdir(directory):
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access directory '{directory}'.")
    except OSError as e:
        print(f"Error accessing directory '{directory}': {e}")

# Example usage:
directory_path = 'D:/'  # Replace with your directory path
print_directory_contents(directory_path)
