#                Introduction to lists
# string_list = ['1', '2', '3', '4', '5']
# int_list = [1, 2, 3, 4, 5]
# float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
# combo_list = [1, 2.2, 'string', 4, 5.5]
# multi_list = [int_list, float_list, string_list]
#
# print(int_list)
# print(float_list)
# print(string_list)
# print(combo_list)
# print(multi_list)
# print()
#
# print(int_list[0])
# print(float_list[1])
# print(string_list[2])
# print(combo_list[3])
# print(multi_list[1])
# print(multi_list[1][1])
#
# Manipulating Lists
# int_list = [34, 12, 19, 123, 987, 78, 98, 1, 4, 876, 1200, 1289]
# 12 items, 0 lowest index, 11 highest index
# print('intial list:', int_list)
# print()
#
# # Determining the length of the list (items in list)
# len() function
# print('length of list:', len(int_list))
# print()
#
# To add an item to the end of the list, you call the append() method
# int_list.append(' Justine new list')
# print('int_list with the append: ', int_list)
# print()
#
# # # To insert an item in a list, use the list's insert() method.
# # Insert method requires an index where value is to be inserted and a value
# # Insert does not overwrite the current value which is there, it just increases the index by 1
# int_list.insert(6, 100)
# print('insert 100 at index 6:', int_list)
# print('new length of list: ', len(int_list))
# print()
#
# Can also extend a list by adding the contents of an entire other list to the end of the list
# This is done using the extend() method
# another_list = [12, 13, 14]
# int_list.extend(another_list)
# print('int_list plus the new list at the end', int_list)
# print('new length of list: ', len(int_list))
# print()
#
# To remove an item from the list, simply call the method remove() and provide it with the value to remove
# int_list.remove(1200)
# print('print int_list with the removed value: ', int_list)
# print('new length of list: ', len(int_list))
# print()
# #
# #
# # # To a remove a specific item from the list, use the del() method and specify the index of the item you want to remove
# del(int_list[2])
# print('int_list with removed index: ',int_list)
# print('new length of list: ', len(int_list))
# print()
#
# To remove an item and return it's value, use the pop() method
# Once pop is provided with the index, it will return the value stored at the index and  remove the item from the list
# print('popped from index 1: ', int_list.pop(1))
# print('After pop index 1: ', int_list)
# print('new length of list: ', len(int_list))
# #
# More ways to manipulate a list and to gather info on the list
# int_list = [34, 12, 19, 123, 987, 78, 98, 12, 4, 876, 1200, 1289]
# print('intial list:', int_list)
# # print()
#
# # find the first occurence of a value in a list, use the index() method and provide it with the value to search for
# print('first index of the value 12: ', int_list.index(12))
# print()
#
# # To find the number of times the value appears in the list use count() method and provide it with the value to count
# print('how many times does the number 12 appear: ', int_list.count(12))
# print()
#
# string_list = ['white', 'yellow', 'red', 'gold', 'yellow', 'blue']
# print('How many times does the color yellow appear in the list: ', string_list.count('yellow'))
# print()
#
# #To sort items in a list , use the sort() method
# string_list.sort()
# int_list.sort()
# print('Sorted String list: ', string_list, '\n', 'Sorted integer list: ', int_list)
# print()
#
# # to reverse items in a list, use the reverse() method
# string_list.reverse()
# int_list.reverse()
# print('reverse String list: ', string_list)
# print('reverse integer list: ', int_list)
# print()
#
#                                     # Tuple (cannot change and uses (parenthesis)
# int_tuple = ('dress', 'pants', 'jacket')
# print('print tuple values: ', int_tuple)
# print('print tuple value at index 2: ', int_tuple[2])
# print()
# #
# # # assigning variables to tuples
# x, y, z = int_tuple
# print('x:', x, '\t' 'y: ',y, '\t' 'z: ', z)
# print()
#
# making sure tuples cannot be change
# int_tuple[2] = 'hoodie'
#
#                                     #Sets (needs to be unique)
# color_set = {'white', 'yellow', 'red', 'gold', 'blue'}
# print('Initial color set: ', color_set)
# print()
# #
# # # Use the add() method to add values to a set
# color_set.add('pink')
# print('color set with pink added: ', color_set)
# print()
# #
# # # Use the discard() method to discard a value
# color_set.discard('blue')
# print('print color set and see that blue is not there: ', color_set)
# print()
# #
# # # Use the intersection() method to determine which values appear between 2 sets
# new_color_set = {'pink', 'orange', 'yellow', 'purple'}
# print('new color set: ', new_color_set)
# print('Same colors in both color sets : ', color_set.intersection(new_color_set))
# print()
# #
# # # use difference to show the difference between 2 sets
# print('Different colors in the first color set that is not in the second set: ', color_set.difference(new_color_set))
# print()
#
#                                             Dictionary
students_noroff_campus = {'frontend': 219, 'IT': 190, 'Film': 42, 'UX': 10, 'Digital Marketing': 123}
# print('Dictionary list for courses', students_noroff_campus)
print()
print('Students for Front End: ', students_noroff_campus['frontend'])
print()
del(students_noroff_campus['UX'])
print('Students per program after deleting UX: ', students_noroff_campus)
print()
print('Only the keys: ', students_noroff_campus.keys())
print()

# In Keyword
print('Contains students for IT:', 'IT' in students_noroff_campus)
print()
print('Contains students for UX: ',  'UX' in students_noroff_campus)
print()

# Adding keys and values to dictionary (it is mutable)
students_noroff_campus['Music'] = 10
print('Newly added program: ', students_noroff_campus)
print()

print((students_noroff_campus)['frontend']-(students_noroff_campus['IT']))