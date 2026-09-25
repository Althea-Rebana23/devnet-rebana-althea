"""
=================================================
WHAT IS THIS TOPIC?
=================================================
 
Functions are reusable blocks of code that perform a specific task.
Instead of writing the same code multiple times, I can place it
inside a function and call it whenever I need it.
I think of a function like ordering food at a restaurant. You tell
the staff what you want, they process your request, and then they
give you the result. In Python, functions can receive information,
perform a task, and return a result.
 
=================================================
KEY VOCABULARY
=================================================
 
- function: A reusable block of code that performs a specific task.
 
- parameter: A variable inside a function that receives a value.
 
- argument: The actual value passed into a function.
 
- return value: The result sent back by a function.
 
- function call: Running or using a function.
 
=================================================
MY EXAMPLE
=================================================
"""
 
def greet(name):
return f"Hello, {name}!"
 
message = greet("Althea")
print(message)
 
"""

=================================================
A MISTAKE I MADE
=================================================
 
I was a little confused about the difference between parameters and
arguments. At first, I thought they meant the same thing. After
reading and searching it, I learned that a parameter is written in the function
definition, while an argument is the actual value passed when the
function is called.
 
=================================================
HOW THIS CONNECTS TO SOMETHING ELSE
=================================================
 
Functions connect to the previous lessons because they can contain
variables, conditions, and loops. Using functions also helps make
programs more organized by grouping related code into a reusable
block instead of rewriting the same code multiple times.
"""
