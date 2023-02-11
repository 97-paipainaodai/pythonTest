#get():  when the value get do not exist, return a new value
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups',0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs',0)) + ' eggs.')
