def draw_line() :
    print("=======================")

def switch(input, x, y):
    x = int(x)
    y = int(y)
    {1:plus(x,y), 2:minus(x,y), 3:multiply(x,y), 4:division(x,y), 5:exit()}.get(x, "default")

def plus(x,y): print(x+y)
def minus(x,y): print(x-y)
def multiply(x,y): print(x*y)
def division(x,y): print(x/y)

while(1):
    draw_line()
    select_method = int(input("원하는 방법을 골라주세요 \n"))
    if(select_method == 5):
        print("bye")
        draw_line()
        break
 
    draw_line()

    x,y = input("두 숫자를 입력하시오\n").split()

    switch(select_method, x, y)
