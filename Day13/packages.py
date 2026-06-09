
########################################################################## Packages ##############################################################################

# packages 
# Python packages are a way to organize and structure code by grouping related modules into directories.

# A package is essentially a folder that contains an __init__.py file and one or more Python files (modules).
# Allows modules to be easily shared and distributed across different applications.

#################################################################################################################################################################

# package folder structure:
# my_project/                    # project folder 
# │
# ├── main.py                    # main script 
# │
# └── mypackage/                 # package, just a folder
#     ├── __init__.py            # makes it a package can be empty
#     ├── calculator.py          # module 1
#     └── converter.py          # module 2


################################################################################################################################################################

# __init__.py
# Its just a file that tells Python:
# this folder is a package, not just a random folder".

# Sub-Packages: Packages nested within other packages for deeper organization with their own __init__.py

################################################################################################################################################################

# Example # #

# create a package called math to organize. The package contains two sub-packages:
# basic: add and sub
# advanced: multiply and divide
# Each operation is stored in its own module, which makes the code modular, reusable and easier to maintain.


from math_package import calculate, add, subtract, multiply, divide

# Using the placeholder calculate function
calculate()

# Perform basic operations
print("Addition:", add(5, 3))
print("Subtraction:", subtract(10, 4))

# Perform advanced operations
print("Multiplication:", multiply(4, 2))
print("Division:", divide(10, 2))


################################################################################################################################################################

# Importing from Packages
# There are 3 ways to import from a package:

# Style                                             Example
# Full package                                 import math_package
# Specific function                         from math_package import add
# From subpackage                        from math_package.basic import add

# in the above example we were able to use "" from math_package import calculate, add, subtract, multiply, divide "" directly because 
# because math_package/__init__.py was exposing everything at the top level by importing from all the subpackages inside it! 
# if math_package/__init__.py is emplty then we need to use deeper imports like from math_package.basic import add, subtract to access the functions.


################################################################################################################################################################

# pip

# pip install
# pip is Python's package manager — it lets you download and install packages that other people have written.
 
################################################################################################################################################################

# virtual environment 

# python -m venv myenv        # 1. create
# source myenv/bin/activate   # 2. activate
# pip install requests        # 3. install packages
# python app.py               # 4. run your code
# deactivate                  # 5. exit when done
