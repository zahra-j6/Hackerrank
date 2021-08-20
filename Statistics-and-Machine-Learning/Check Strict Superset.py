# Enter your code here. Read input from STDIN. Print output to STDOUT

# A strict superset has at least one element that does not exist in its subset.

set_a = set( input().split()) #Set A
no = int(input()) # no of sets
list=[]
final_op = True
for i in range(no):
    list =  input().split() # set to check
    for i in list:
        if i not in set_a: # check if element is not in set a
            print(False) # if not print false and exit code
            exit()
print(True)

#    if list in set_a: print(True)
 #   else: print(False)
    #    print("New set created is ",set_i)
    #set_n = set_i.difference(set_a)
    #    print("New set is ",set_n)
#    if len(set_n) > 0 and final_op == True:
 #       final_op = True
 #   else:
       # final_op = False
#print(final_op)




