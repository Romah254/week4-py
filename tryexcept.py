"""
File Processing Program with Error Handling
------------------------------------------
1. Reads a file specified by the user
2. Modifies the content (converts to uppercase)
3. Writes the modified version to a new file
4. Handles all common file-related errors
"""

def main():
    print("\n=== File Processing Program ===")
    print("This program will read a file, modify its content,")
    print("and save the modified version as a new file.\n")
    
    # Step 1: Get input filename from user
    while True:
        input_filename = input("Enter the name of the file to read (e.g., 'example.txt'): ").strip()
        if input_filename:  # Ensure user didn't just press Enter
            break
        print("Error: Please enter a valid filename.")

    # Step 2: Generate output filename
    if '.' in input_filename:
        name, ext = input_filename.rsplit('.', 1)
        output_filename = f"{name}_modified.{ext}"
    else:
        output_filename = f"{input_filename}_modified"

    # Step 3: File processing with error handling
    try:
        # Read the input file
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            original_content = input_file.read()
        
        # Display file info to user
        print(f"\nSuccessfully read: '{input_filename}'")
        print(f"File size: {len(original_content)} characters")
        
        # Step 4: Modify the content
        modified_content = original_content.upper()
        
        # Step 5: Write to output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)
        
        # Success message
        print(f"\nSuccessfully created modified file: '{output_filename}'")
        print(f"Modified content preview:\n{modified_content[:200]}...")  # Show first 200 chars

    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' does not exist in the current directory.")
        print("Please check the filename and try again.")
    except PermissionError:
        print(f"\nError: Permission denied when trying to read '{input_filename}'.")
        print("You may need to run the program as administrator or choose a different file.")
    except IsADirectoryError:
        print(f"\nError: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"\nError: Could not read '{input_filename}' as a text file.")
        print("The file may be a binary file (like an image or PDF).")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("Please check the file and try again.")

    # Final message
    print("\nProgram completed. Press Enter to exit...")
    input()  # Keeps the window open in some environments

if __name__ == "__main__":
    main()