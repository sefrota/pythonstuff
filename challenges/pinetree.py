# How tall is the tree: 5

     #
    ###
   #####
  #######
 #########
     #

height = input("How tal is the tree: ")
height = int(height)

spaces = height - 1
hashes = 1

stump_spaces = height - 1

while height != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    height -= 1

for i in range(stump_spaces):
    print(" ", end="")
print("#")
