#8/11/24
#Author: Abo_Hashem
#this problem from Turing.com Challenges 
#This code tries to count operations to restrict the array elements from 1 to N(size of array)
#by one use increment by one or decrement by one 
#algorithm with cases:
#case 1 : [3,2,1,4] #no needed operation, it's from 1 to 4
#case 2 : [2,3, 4,5]  # so we need to convert '5' to '1' by 4 decrement operations =>(5-1) 
#case 3 : [4, 2,4 ,1] # so we need to decrement duplicated element (4) by one to become 3

# so we need to find outRange elements ]1,N[, and repleced with the restricted range [1,N] which isn't found in acutal array
#and also replaced duplicated element with diserd elements if not found.

def OutRangeElements(arr):
    arr1 = arr.copy()
    #check by len if return is zero, so not numbers outside range
    #else , there are numbers outside range
    first_len = len(arr1)
    outRange = []
 
    #idea: we walk all numbers greater than length of array and store then delete from array
    maximum = max(arr1)
    while (maximum > first_len):
            outRange.append(maximum)
            print(maximum)
            arr1.remove(maximum)
            maximum = max(arr1)
        #now store numbers smaller than 1 and then delete them
    minimum = min(arr1)
    while (minimum < 1):
        outRange.append(minimum)
        print(minimum)
        arr1.remove(minimum)
        minimum = min(arr1)
    return outRange

def count_op(arr):
    operations = 0
    #Check the numbers outside of the range array
    outsiderange = OutRangeElements(arr)#found the outrange and their duplicated
    print("outsiderange:", outsiderange)
    for i in range( 1, len(arr)+1 ):
        countt = arr.count(i)
        if ( countt ==0):
            #check duplicated in the disred range:
            #Check the numbers outside 
            if(len(outsiderange ) > 0):
                element = outsiderange.pop()
                print("element:",element)
                ind = arr.index(element)
                operations += arr[ind] - i
                print("operations:")
                arr[ind] = i
                
    return operations
                    

#challenge 1:
'''
how solve this error
ValueError: min() arg is an empty sequence
a = [-1,8]
'''
a = [2,3,4,5]
#print(len(OutRangeElements(a)))
print("count_op(a):", count_op(a))

