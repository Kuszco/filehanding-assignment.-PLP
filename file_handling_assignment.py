try:
    with open("my_file,txt", 'w') as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("text and numbers: 4561\n")

    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        print(file.read())

    with open("my_file.txt" 'a') as file:
        file.write("This is an appended line\n")
        file.write("98765\n")
        file.write("appended line with text and numbers: 84568\n")

    with open("my_file.txt, 'r") as file:
        print("\nContents of my_file.txt after appending:")
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("\nEnd of program.")