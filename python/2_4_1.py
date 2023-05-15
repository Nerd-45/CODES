
# QUESTION 1
# l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print([t[:-1] + (100,) for t in l])

# QUESTION 2
# L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# L = [t for t in L if t]
# print(L)

# QUESTION 3
# def mutiple_tuple(nums):
#     temp = list(nums)
#     product = 1 
#     for x in temp:
#         product *= x
#     return product

# nums = (4, 3, 2, 2, -1, 18)
# print ("Original Tuple: ")
# print(nums)
# print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums))

# nums = (2, 4, 8, 8, 3, 2, 9)
# print ("\nOriginal Tuple: ")
# print(nums)
# print("Product - multiplying all the numbers of the said tuple:",mutiple_tuple(nums))

# QUESTION 4
# def tuple_int_str(tuple_str):
#     result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
#     return result

# tuple_str =  (('333', '33'), ('1416', '55'))
# print("Original tuple values:")
# print(tuple_str)
# print("\nNew tuple values:")
# print(tuple_int_str(tuple_str))

# QUESION 5

def check_in_tuples(colors, c):
    result = any(c in tu for tu in colors)
    return result

colors = (
    ('Red', 'White', 'Blue'),
    ('Green', 'Pink', 'Purple'),
    ('Orange', 'Yellow', 'Lime'),
)
print("Original list:")
print(colors)
c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'White'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))
c1 = 'Olive'
print("\nCheck if",c1,"presenet in said tuple of tuples!")
print(check_in_tuples(colors, c1))