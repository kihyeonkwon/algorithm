def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            #continue statemen returns the control to the beginning of the while loop
            continue
        #else is executed only if no exceptions were raised in the try block.
        else:
            return userInput
            break


intNum = inputNumber("")
if intNum <0:
    print("%d \nminus"%(intNum))
else:
    print("%d"%(intNum))

