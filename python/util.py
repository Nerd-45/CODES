#1
# import os

# cwd = os.getcwd()

# for i in range(ord('A'), ord('Z') + 1):

#     f = open(f"{cwd}/Test_dir/{chr(i)}.txt", "x")

#     print(f"Generated Empty file {chr(i)}.txt")

# f.close()

#2
# def Alphabet_lines(n):
    
#     with open("alphabets_lines.txt", "w") as fw:

#         for i in range(ord('A'), ord('Z') + 1):

#             if(ord('A') - i) % n == 0 and i != ord('A'):

#                 fw.write("\n")

#                 fw.write(chr(i))

# print("File is Successfully Written!!")

# num = int(input("Enter the letters to be in each line: "))

# Alphabet_lines(num)

#3
# with open("hello_world.txt", 'r') as f:

#     print("Reading file 'hello_world.txt'")

#     print()

#     print(f.read())

#4
# frequency = {}
# with open("hello_world.txt", 'r') as f:
#     for word in f.read().split():
#         if word in frequency.keys():
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
# print(frequency)

#5
with open("hello_world.txt", "r") as first_f:
    with open("other_file.txt", "w") as second_f:
        second_f.write(first_f.read())   
        print("Content from hello_world.txt is copied Successfully to other_file.txt")


