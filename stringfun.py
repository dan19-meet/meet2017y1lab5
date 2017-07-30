def stringTest(s):
    return (len(s) > 2 and s[0] == s[-1]) 

def addX(s):
    s = 'x' + s + 'x'
    return s

a = 'a'
a = addX(a)
c = stringTest('a')
print(c)

'''
class Monster:
    __init__(self):
        pass
    
    def growl(self):
        print("The monster is growling")

monster = MOnster()
'''
