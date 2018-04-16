__author__ = "Brandon Hardesty"
import cStack
import DoublyLinkedList
import MixedFraction



def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = cStack.Stack()
    postfixList = []
    tokenList = infixexpr.split(" ")

    for token in tokenList:
        if token.isnumeric() or token.isalpha() or token.count(".") == 1 or (token.count("/") == 1 and len(token) > 1):
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                try:
                    postfixList.append(topToken)
                    topToken = opStack.pop()
                except Exception:
                    print("Bad expession: {}".format(infixexpr))
                    break
        else:
            try:
                while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            except KeyError:
                print("Key Error: {}".format(infixexpr))
                break
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def main():
    print(infixToPostfix("A * B + C ^ D"))
    print(infixToPostfix("( 4.4 + 4.6 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infixToPostfix("( 2 ^ 20 ) ^ ( 2 / ( 1 + 3 ) )"))
    print(infixToPostfix("A * B ) + ( C ^ D )"))
    print(infixToPostfix("( A * B ) + (C ^ D )"))
    print(infixToPostfix("7 + 9 * 8 / 4 ^ 2"))
    print(infixToPostfix("( 17 + 9 ) * 3 / ( 5 - 3 ) ^ 4"))
if __name__ == "__main__":
    main()




