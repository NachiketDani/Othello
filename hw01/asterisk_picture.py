def make_tree(height):
    print("    **    ")
    while height>0:
        print ("   ****   ")
        print ("  ******  ")
        print (" ******** ")
        print ("**********")
        height -=1
    print ("____||____")
make_tree(4)