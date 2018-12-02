
def choose_numbers():
    try:

        amount = int(input("How many numbers?: "))
        numbers = []
        for i in range(0,amount):
            numbers.append(str(int(input("number "+str(i+1)+": ")))) #ensure it can be an int and then convert back to string
        return numbers
    except:
        print("Please only input integers!")
        choose_numbers()

def multiply(numbers):
    try:
        print("Calculating... (this may take some time)")
        total = int(numbers[0])
        for counter in range(0,len(numbers)-1):
            if int(numbers[counter+1]) == 0:
                total = 0
            total_partial = total
            for i in range(0,int(numbers[counter+1])-1):
                total += total_partial
        return total
    except:
        print("Error Multiplying!")



while True:
    numbers = choose_numbers()
    str_expression = " x ".join(numbers)+" ="
    answer = multiply(numbers)
    print(str_expression,answer)
    
