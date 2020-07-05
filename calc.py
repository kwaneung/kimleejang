#테스트트트트
def Dsum(x, y):
    hap = x + y
    print(str(x)+" + "+str(y)+" = "+str(round(hap, 2)))
    
def Dsub(x, y):
    hap = x - y
    print(str(x)+" - "+str(y)+" = "+str(round(hap, 2)))

def Ddiv(x, y):
    hap = x / y
    print(str(x)+" / "+str(y)+" = "+str(round(hap, 2)))

def Dmul(x,y):
    hap = x * y
    print(str(x) + "*" + str(y) + " = " + str(round(hap,2)))



if __name__ == "__main__":
    print("계산기 시작")
    a = float(input("계산을 위한 첫 번째 숫자를 입력하시오 "))
    b = float(input("계산을 위한 두 번째 숫자를 입력하시오 "))
    p = input("수식을 입력하시오(+, -, *, /) ")
    if p == '+':
        print("덧셈 연산을 실행합니다.")
        Dsum(a, b)
    elif p == '-':
        print("뺄셈 연산을 실행합니다.")
        Dsub(a, b)
    elif p == '*':
        print("곱셈 연산을 실행합니다.")
        Dmul(a,b)
    elif p == '/':
        print("나눗셈 연산을 실행합니다.")
        Ddiv(a, b)
    else:
        print("정상적인 값을 입력하시오")
