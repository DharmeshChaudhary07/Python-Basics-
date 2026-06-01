################################################ Advance for loops ########################################################

#Pass. continue, break.

# break : in for loop
# break stops the loop immediately : it jumps out and end the loop right away

names = [ 'Ram', 'sam', '' ,'ayushi' ] 
for name in names:
    if name == "":
        print(f'Name: empty')
        break
    print(f'names: {name}')


# continue : in for loop
# it skips one loop cycle without stopping the loop
# use continue to skip or empty data without stopping the whole loop

names = ['Ram' ,'sham' ,'' ,'ayushi' ] 
for name in names:
    if name == "":
        print(f'Name: empty')
        continue
    print(f'Names: {name}')


# pass in for loop
# it is a placeholder where nothing happens for now :just keep going do nothing 

names = ['Ram' ,'sham' ,'' ,'ayushi' ] 
for name in names:
    if name == '':
        pass
    print(f'Names: {name}')

names = ['Ram' ,'sham' ,'' ,'ayushi' ] 
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f'Names: {name}')


# else in for loops
# runs the block of code only if the loop is finished naturally - completed withoud a break 

for i in (1, 2, 3, 4):
    print(i)
else:
    print("end")

items = [1, 3, 6, 7]
for item in items:
    print(item)
else:              # here the else is pointess, we could directy use print.
    print("loop is completed")

for item in items:
    print(item)
                # here the else is pointess, we could directy use print.
print("loop is completed")

# use else only if with break statement:

items = [1, 3, 6, 7]
for item in items:
    if item == 6:
        print("item:", item)
        break
else:              # here the else is pointess, we could directy use print.
    print("loop is completed")


# if the no is even is
items = [1, 3, 6, 7]
for item in items:
    if item % 2 == 0:
        print("item:", item)
        break
else:              # here the else is pointess, we could directy use print.
    print("loop is completed")

