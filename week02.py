# WRITE YOUR CODE HERE
## Function to Greet a Person
def greet(name):
    """
    Gives someone a greeting given a name
    Input
    -----
    name : string
    """
    print("Hello " + name +". How are you?")
    print()
greet("Dr. Leo")
## Greeting Multiple People
friend_list = ["Anakin","Obi Wan","Padme"]
for name in friend_list:
    greet(name)
## Solve an equation
def solve_quadratic(a,b,c):
    """
    Gives solution to a quadratic equation ax^2+bx+c: 
    Inputs
    ------
    a : int
        The coefficient of x^2
    b : int
        The coefficient of x
    c : int
        The constant
    """
    if ((b**2)-(4*a*c)) > 0:
        x1= (-b+((b**2-(4*a*c))**0.5)/(2*a)
        x2= (-b-((b**2-(4*a*c))**0.5)/(2*a)
        print(x1, x2)
    elif ((b**2)-(4*a*c)) == 0:
        x= (-b+((b*b-4*(a*c))**0.5)/(2*a)
        print(x)
    else:
        print("No real solutions")
solve_quadratic(1,2,4)