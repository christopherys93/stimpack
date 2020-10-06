print('Would you like to see if you qualify for a stimulus check? (YES/NO)')
answer = input().upper()
if answer == 'NO':
    exit()

print('Are you an American citizen or U.S. Resident? (YES/NO)')
citizen = input().upper()
if citizen == 'NO':
    print('You do not qualify for a stimulus check')
    exit()

print('What is your age?')
age = input()
if age <= str(16):
    print('Sorry, you are a minor and do not qualify for a check')
    exit()

print('Did you file your taxes in 2018 or 2019? (YES/NO)')
taxes = input().upper()
if taxes == 'NO':
    print('Sorry, you do not qualify for a stimulus check.')
    exit()

print('Did you file your taxes as independent or dependent?'
      '\nType 1 for independent or 2 for dependent')
status = input()
if status == '2':
    print('You do not qualify for a stimulus check')
elif status == '1':
    print('Good! you may qualify for a stimulus check!')

print('What is your yearly income as stated in your taxes?'
      '\nType your income without any commas')






