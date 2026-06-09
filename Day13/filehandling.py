
# ############################################################################## File Handling #############################################################################

# # file handling
# # important part for any web application.

# # python has several function for creating updating deleting and reading files.

# # Need for File Handling
# # 1. Store data permanently, even after the program ends.
# # 2. Access external files like .txt, .csv, .json, etc.
# # 3. Process large files efficiently without using much memory.
# # 4. Automate tasks like reading configs or saving outputs.

# #########################################################################################################################################################################
# # opening a file 

# # syntax -> takes two parameter filename and mode 
# # eg. f = open("filehandle.txt") or f = open("filehandle.txt", rt) here r -> read t-> text is default value we dont need to specify them.

# f = open("filehandle.txt") 
# print(f)        # prints -> <_io.TextIOWrapper name='filehandle.txt' mode='r' encoding='UTF-8'> It's not the file content — it's just info about the file handle itself.
# print(f.read()) # prints -> Hello, /n I am under water. /n Please help me 



# f = open("/Users/dharmeshchaudhary/Material/Python/Day11/demofilehandle/demofile.txt")
# print(f.read())


# # with
# # we can also use with to open a file.
# with open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt") as f:
#     print(f.read())


# #########################################################################################################################################################################

# # ******* we need to close the file if not using with statement to open the file. ******
# f = open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt")
# print(f.read())
# f.close()
# print(f.closed)  # prints -> true :         (if closed)

# #########################################################################################################################################################################

# # by default read() -> returns the whole text/content but we can specify how many character we want to return

# f = open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt")
# print(f.read(11))       # prints -> Hello, how

# # reading in some different line and text from some index.

# lines = f.readlines()
# print(lines[3])

# print(lines[2][5:16])

# #########################################################################################################################################################################

# # writing a existing file 

# # To write to an existing file, you must add a parameter to the open() function:
# # "a" - Append - will append to the end of the file
# # "w" - Write - will overwrite any existing content

# with open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt", "a") as f:   # "a" writes at end of text file
#     f.write("\n Instagram meme, Hehe ")  
# with open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt") as f:        # open after writing it.
#     print(f.read())


# # overwrite the textfile

# with open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt", "w") as f:   # "w" overwrites at end of text file
#     f.write("delete under water guy, hehe")  
# with open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt") as f:        # open after writing it.
#     print(f.read())          


# #########################################################################################################################################################################

# # create a new file 
# # gives error if file existed 
# f = open("/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt", "x")  # print File exists: '/Users/dharmeshchaudhary/Material/Python/Day11/filehandle.txt'

# f = open("/Users/dharmeshchaudhary/Material/Python/Day11/filecreate.txt", "x")    # creates a file named as filecreate.txt

# #########################################################################################################################################################################

# # Handling Exceptions When Closing a File
# It's important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations. 
# Here, the finally block ensures the file is closed even if an error occurs.

# try:
#     file = open("/Users/dharmeshchaudhary/Material/Python/Day11/filecreate.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError as e:
#     print("Error:", e)
# finally:
#     file.close()
#     print(file.closed)

# #########################################################################################################################################################################