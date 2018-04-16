__author__ = "Brandon Hardesty"
from InfixPostfix import  infixToPostfix
import DoublyLinkedList
import cStack
import MixedFraction

postfixExpressions = ['4.4 4.6 + 2 1 3 + / ^', '2 20 ^ 2 1 3 + / ^', '2 20 + 2 1 3 + + *', '2 -1 3 + -']
infixExpressions = ["7 + 9 * 8 - 4 ^ 2", "7 + 9 * 8 / 4 ^ 2", "( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4", "7.5 + 9 - 1.8 / 4 ^ 2.5"]
def evaluatePost(exp):
    stack = cStack.Stack()
    tokenList = exp.split(" ")
    for i in tokenList:
        try:
            if(i.count("/") == 1 and len(i) > 1):
                stack.push(float(MixedFraction.MixedFraction.from_string(i)))
            else:
                i = float(i)
                stack.push(i)
        except:
            if (i in "*/+-^"):
                b = stack.pop()
                a = stack.pop()
                if (i == "*"):
                    stack.push(a * b)
                elif (i == "/"):
                    stack.push(a / b)

                elif (i == "+"):
                    stack.push(a + b)
                elif (i == "-"):
                    stack.push(a - b)
                elif (i == "^"):
                    stack.push(a ** b)



    return stack.peek()

def main():
    for i in postfixExpressions:
        result = evaluatePost(i)
        out = "{} = {}".format(i,result)
        print(out)
    for i in infixExpressions:
        c = infixToPostfix(i)
        result = evaluatePost(c)
        out = "{} = {}".format(i, result)
        print(out)
if __name__ == "__main__":
    main()






