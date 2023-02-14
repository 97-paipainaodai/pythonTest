#isalpha() :string contains only alpha, and non-empty
#isalnum() :string contains only alpha and number, and non-empty
#isdecimal() :string contains only number, and non-empty
#isspace() :string contains only ' '(space) '\' '\n', and non-empty
#istitle() :string contains only words that begin with an uppercase letter and are followed by a lowercase letter
            #number and space.
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new passward (letters and numbers only):')
    passward = input()
    if passward.isalnum():
        break
    print('Passwards can only have letters and numbers.')