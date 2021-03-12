#1. take input
a,b = input().split()

#2. Convert them into integers
a = int(a)
b = int(b)

#It has N height and M breadth
#so loop is to be run "loop_for_height" times leaving the center piece
loop_for_height = int(((a-1)/2))


#3. make the upper cone
#easy take odd number of ".|." in center 
for i in range(loop_for_height):
    print((".|."*(2*i+1)).center(b,"-"))

#4. Center Piece
print("WELCOME".center(b,"-"))

#5. bottom Piece
#loop can be run backward or forward 
for i in range(loop_for_height-1,-1,-1):
    print((".|."*(2*i+1)).center(b,"-"))



'''
range(start, stop, step)
When you call range() with three arguments, you can choose not only where the series of numbers will start and stop but also how big the difference will be between one number and the next. If you don’t provide a step, then range() will automatically behave as if the step is 1.

Note: step can be a positive number or a negative number, but it can’t be 0:

>>> for i in range(10,0,-2):
	print(i)


10
8
6
4
2




>>> for i in range(0,10,2):
	print(i)

	
0
2
4
6
8	'''
