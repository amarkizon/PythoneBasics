# 1. Functios , logical units of the code with certain purpose
# unique name with lower case (not shadowing built-in function)
# def name_of_the_function():
# indentation that shows function block,
import builting_def
# 2. execute the function:
builting_def.addition(40, 60)
builting_def.hello()
builting_def.hello_name("jane")
builting_def.hello_name("tonny")
print(builting_def.hello_return())
print(f"addition: {builting_def.addition(45, 65)}")
print("Unit testing : executing the functions with various arguments and check with expected result")
print(builting_def.addition(2, None))