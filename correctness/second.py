# Assigning a lambda expression to a variable

# anti-patterns or No

f = lambda x:2*x
print(f(2))

# best practice
def f(x): return 2*x
print(f(3))