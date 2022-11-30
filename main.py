from matplotlib import pyplot as plt
import numpy as np
import sympy as sym

x = np.arange(1,1000) # 그래프를 그리기 위한 x값 배열 [1,2,3, ~1000]
y = input("수식을 입력하시오 : ") # 함수 수식 입력 받아와 y라는 변수에 저장

xWillClosed = input("x는 어떤 값에 한 없이 가까워 집니까? 만약 무한 이면 oo(소문자 영어) 입력 : ")
# x가 한 없이 가까워 지는 값에 대한 입력을 받은 후 변수에 저장

if xWillClosed == "oo": # 만약 무한이면 sympy 라이브러리에 내장된 무한 값 으로 변수 치환
    xWillClosed = "sym.oo"

limit = sym.limit(y, sym.Symbol('x'), eval(xWillClosed)) # 실질적으로 limit 값을 구하는 로직
print("limit 값은 : ", limit) # 구해진 limit 값을 출력

plt.plot(x, eval(y)) # 수식에 대한 그래프를 그림
plt.show() # 나타난 그래프를 화면에 표시
