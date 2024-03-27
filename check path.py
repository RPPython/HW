try:
    # Open a file for reading
    with open("filename.txt", "r") as file:
        # Perform operations on the file
        pass  # Placeholder for file operations
except FileNotFoundError:
    print("File not found! Check the file path.")
except IOError as e:
    print(f"Error: {e}")

# Replace "filename.txt" with the actual file path you are trying to access.
    
