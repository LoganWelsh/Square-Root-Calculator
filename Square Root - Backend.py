# This program calculates the square root of a number

input('This program finds the square root of your inputted number to an accuracy of 0.001,\n'
      'and shows how many iterations of guessing it took to reach the answer.\n'
      'Press enter to begin!')

number=float(input("Enter a number: "))
guess=number/2
accuracy=0.001
iteration=0
while abs(number-(guess**2)) > accuracy :
    print("Iteration",iteration, "Guessed square root is: ",guess)
    guess = (guess+(number/guess))/2
    iteration += 1
print('---------------------------------------------------------------------------------------------------------------')
print("Original number is: ",number)
print("Square root of the number is: ",guess,'\n')
input('Finished! Click close to exit or press enter.')
