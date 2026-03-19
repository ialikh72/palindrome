list=[1,2,3,2,1]
copy_list=list.copy()
list.reverse()
if(copy_list==list):
    print("The list is a palindrome")
else:
    print("the list is not palindrome")