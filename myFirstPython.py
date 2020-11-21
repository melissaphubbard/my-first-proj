# <= this symbol means comment so the code wont' include it to run
# below is a print out of 'hello world'
print("Hello World!")
# here is a function that prints something and waits for user response
ans = input("Give me a number: ")

# here i take the response, 
# and then convert to integer and see if it is divisble by 2
# if it is I print even
if((int(ans) % 2) == 0):
    print("EVEN!")
# if it is not, I print odd
else:
    print("ODD!")
