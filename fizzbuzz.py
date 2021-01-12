
def do_fizzbuzz():
    """
    while the number starts with 1 and up to 100.
    print 'fizz' if the number is times of three.
    print 'buzz' if the number is times of five.
    print 'fizzbuzz' if the number is times of fifteen.
    else, print the number.
    """
    # Fizzbuzz with if and for
    for i in range(1,100+1):
        if i%15==0:
            print('fizzbuzz')
        elif i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else:
            print(i)
    # Fizzbuzz with list comprehension

    # Fizzbuzz in one line

    # Fizzbuzz with lambda function

if __name__=='__main__':
    do_fizzbuzz()
