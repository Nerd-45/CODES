# def main():
#     colours = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#     colours = [colour for (index, colour) in enumerate(colours) if index not in (0,4,5)]
#     print(colours)
# if __name__ == '__main__':
#     main()
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Original list elements:")
print(color)
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print("After removing the 0th, 4th, 5th element:")
print(color)