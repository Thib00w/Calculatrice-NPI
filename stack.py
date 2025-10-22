class Stack:
    def __init__(self, stack = []):
        self.stack = stack
    
    def is_empty(self):
        return self.stack == []
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            tmp = self.stack[-1]
            self.stack = self.stack[0:-1]
            return tmp
    
    def push(self, element):
        self.stack.append(element)

    def size(self):     
        return int(len(self.stack))  
    
    def copy(self): 
        copy_stack = Stack(list(self.stack))
        return copy_stack
        
    def __repr__(self):
        affichage = "---\n"
        size_stack = self.size()
        for i in range(0, size_stack, 1):
            affichage += f"|{self.stack[size_stack-i-1]}|\n"
        affichage += "---"
        return affichage

#TODO: Finir ex 7 et mettre verification

if __name__ == "__main__":
    # Création première pile
    stack1 = Stack([1,2,3])
    stack2 = stack1.copy()
    print(stack1)
    # Test methode pop
    print(f"Test methode pop -> Valeur retourné par la methode == {stack1.pop()}")
    print(stack1)
    # Test methode push
    print(f"Test methode push")
    stack1.push(3)
    print(stack1)
    # Test methode size
    print(f"Test methode size -> {stack1.size()} == 3")
    # Test methode copy
    print("Test methode copy:")
    print(f"stack1 : \n{stack1}")
    print(f"stack2 : \n{stack2}")
    stack2.push(7)
    print(f"stack1 : \n{stack1}")
    print(f"stack2 : \n{stack2}")
