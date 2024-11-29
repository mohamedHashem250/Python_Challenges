class solution:
	def bruteForceSoln(self,nums:list[int])-> bool:
		#iterative method to search if the array has at least two duplicated numbers
		i = 1
		for element in nums:
			for element_i in nums[i:]:
				if element == element_i:#if the two elements are equal that the condition is validate
					return True
			i +=1
		return False

	def sort_soln(self, nums:list[int])-> bool:
		#this solution first sort the array then compare the neighbours if the same, the array has duplicated values:
		#nums.sort()##does not return anything but alters the original list 
		#sorted(nums)##return the new sorted verison:
		modifed_nums = sorted(nums)
		for i in range(len(modifed_nums)-1):
			if(modifed_nums[i] == modifed_nums[i+1]):
				return True
		return False

	def hashSet_soln(self, nums:list[int])-> bool:
		'''
		we create a set for sorting the elements and every time, we check if the element 
		in the set or not
		'''
		hashset = set()
		for ele in nums:
			if ele in hashset:
				return True
			hashset.add(ele)
		return False

#test bruteForceSoln:
arr = [1,2,3,4]
case1 = solution()
#select one method:
select_method = int(input("pleae press 1 for bruteForceSoln\n press 2 for sort_soln\n press 3 for hashSet_soln: "))
if select_method ==1:
	ans = case1.bruteForceSoln(arr)
elif select_method ==2:
	ans = case1.sort_soln(arr)
elif select_method ==3:
	ans = case1.hashSet_soln(arr)
if ans:
	print("the array has duplicated values")
else:
	print("the array has unqiue values")