def create_test_file():
    """Creates a test file with sample text for processing"""
    filename = "test.txt"
    content = """Hello, File Processor!
    
This is a test file with multiple lines.
It contains:
- Numbers like 12345
- Special characters: !@#$%^&*
- Mixed CASE ExAmPlEs

The quick brown fox jumps over the lazy dog.
Python is fun! 🐍
"""

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully created test file: '{filename}'")
        print("You can now use this with the file processing program.")
    except Exception as e:
        print(f"Error creating test file: {e}")

if __name__ == "__main__":
    print("=== Test File Creator ===")
    create_test_file()
    print("\nFile content preview:")
    print("-" * 40)
    with open("test.txt", 'r', encoding='utf-8') as f:
        print(f.read())
    print("-" * 40)