import math

# for nth line of the triangle
ExcpectedLine = int(input("Please Enter the Expected Line Number:"))

final = ''

for choise in range(0,ExcpectedLine+1):
    final += ' ' + str(int(math.factorial(ExcpectedLine)/(math.factorial(choise)*(math.factorial(ExcpectedLine - choise)))))
    
print(final)