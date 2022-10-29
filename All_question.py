#question 1
def getPairsCount(arr, n, sum):
 
    count = 0  
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
arr = [1,2,5,6,9,7,3,8]
n = len(arr)
sum = 9
print("Count of pairs is",
      getPairsCount(arr, n, sum))


#question 2
arr = [1, 2, 3, 4, 5,9,7,23];     
print("Original array: ");    
for i in range(0, len(arr)):    
    print(arr[i]),     
print("Array in reverse order: ");    
for i in range(len(arr)-1, -1, -1):     
    print(arr[i])


#question 3
str1 = "abcde";  
str2 = "deabc";  
   
if(len(str1) != len(str2)):  
    print("Second string is not a rotation of first string");  
else:  
    try:  
       
        str1 = str1 + str1;  
          
       
        if(str1.index(str2)):  
            print("Second string is a rotation of first string");  
    except ValueError:  
            print("Second string is not a rotation of first string")


#question4 
string = "tisisitinsne"
index = -1
fnc = ""
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", fnc)


# question 5
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
 

N = 3
 
TowerOfHanoi(N, 'A', 'C', 'B')
 

# question 6

def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False


def postToPre(post_exp):

	s = []


	length = len(post_exp)

	for i in range(length):

		if (isOperator(post_exp[i])):

			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

		
			temp = post_exp[i] + op2 + op1

			s.append(temp)

		
		else:

			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans


if __name__ == "__main__":
  
	post_exp = "AB+CD-"
	
	print("Prefix : ", postToPre(post_exp))


# question 7
def prefixToInfix(prefix):
	stack = []
	
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			
			stack.append(prefix[i])
			i -= 1
		else:
		
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

if __name__=="__main__":
	str = "*-A/BC-/vdv"
	print(prefixToInfix(str))


#question 8    
def areBracketsBalanced(expr):
	stack = []

	for char in expr:
		if char in ["(", "{", "["]:

	
			stack.append(char)
		else:

			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	
	if stack:
		return False
	return True

if __name__ == "__main__":
	expr = "{()}[]"

	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")



# question 9        
class Stack:
	def __init__(self):
		self.Elements = []
		
	def push(self, value):
		self.Elements.append(value)
	
	def pop(self):
		return self.Elements.pop()

	def empty(self):
		return self.Elements == []

	def show(self):
		for value in reversed(self.Elements):
			print(value)

def BottomInsert(s, value):

	if s.empty():
		

		s.push(value)

	else:
		popped = s.pop()
		BottomInsert(s, value)
		s.push(popped)

def Reverse(s):
	if s.empty():
		pass
	else:
		popped = s.pop()
		Reverse(s)
		BottomInsert(s, popped)


stk = Stack()

stk.push(616)
stk.push(25)
stk.push(65)
stk.push(4)
stk.push(7)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()


# question 10
class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
m = MinStack()
m.push(-2)
m.push(3)
m.push(-3)
m.push(-99)
print(m.getMin())



