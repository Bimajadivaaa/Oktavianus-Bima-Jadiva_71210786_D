class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']
    # method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)
    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"
    # method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"

def cekValidExpression(self,expression):
    # tuliskan code anda disini
    if expression in "+-":
        return 1
    elif expression in "*/":
        return 2
    elif expression in "^":
        return 3
    return 0

def infixToPrefix(self,expression):
    # Tuliskan code anda disini
    # Test Case
    stack = PrefixConverter()
    expression = '(' + expression + ')'
    output = ""
    for c in expression[::-1]:
        print(c)
        if c.isnumeric():
            output+=c
        elif c == ")":
            stack.push(c)
        elif c in "+-*/^":
            if c == "^":
                while cekValidExpression(c) <= cekValidExpression(stack.top()):
                    output += stack.pop()
            else:
                while cekValidExpression(c) < cekValidExpression(stack.top()):
                    output += stack.pop()
            stack.push(c)
        elif c == "(":
            while not stack.is_empty():
                c1 = stack.pop()
                if c1 == ')':
                    break
                output += c1
    while not stack.is_empty():
        output+=stack.pop()
    return output

expresi1 = PrefixConverter()
print(expresi1.infixToPrefix("1+2+3*4/2-1"))
print(expresi1.infixToPrefix("A * (B + C) / D"))
print(expresi1.infixToPrefix("(1+2)*3"))
print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))