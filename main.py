# Set  items are  enclosed in curly  brackets
# Set  is unordered
# Set  is mutable, can  contain only immutable items 
# Set  elements are unique 
# Set can  contain  only  immutable items 


'''
Python  Set  Attributes
'''
# print(dir(set))

'''
Creating  Python  Sets
'''

# set  = set()
# # print(type(set))
# set  =  {1,2,3}
# print(set)

'''
Modifying  a set in  Python  
'''

  # set_example =  {'hello', 'world'}
  # # set_example(0)
  # set_example.add('yay!')
  # # set_example.add(['hey'])
  # set_example.add('hey')
  # set_example.update([1,2,3])

  # print(help(set.update))
  # print(set_example)

'''
Removing  element from  a set   
'''
# set_example = {1,2,3,4,5,6,7,8}
# # set_example.discard(10)
# # set_example.remove(1)
# set_example.pop()
# print(help(set.pop))
# print(set_example)

# print({'hello', 'world', 'hello', 'hello'})

'''
Set Union  Operations  
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print (a | b)
# print(a.union(b))
# print(a.intersection(b))

'''
Set Difference Operations
'''
# a =  {1,2,3,4,5,6,7,9}
# b = {2,5,6,7,8,9}

# print(a-b)
# print(a.difference(b))
# print(b.difference(a))

'''
Set Symmetric  Difference
'''

# a =  {1,2,3,4,5,6,7,9}
# b = {2,5,6,7,8,9}


# print (a^b)
# print(a.symmetric_difference(b))

'''
Set Method
'''

print(dir(set))