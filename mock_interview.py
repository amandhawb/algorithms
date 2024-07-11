# Generate the below output that’ll provide the accounts with duplications in a list of UIDs of those accounts.

# user@localhost:~$ cat /etc/passwd
# index-server:x:233336:10558:index-server:/home/index-server:/sbin/nologin ##(Service Acct)
# bobbyd:x:12342:15050:J. Bobby Dorlus:/home/bobbyd:/bin/bash
# jdoe:x:34969:155500:John Doe:/home/jdoe:/bin/bash
# foobar:x:18836:150440:Mr. Foo Bar:/home/foobar:/bin/bash
# bobbyd:x:2333:150880:J. Bobby Dorlus:/home/foobar:/bin/bash
# index-server:x:2336:105558:index-server:/home/index-server:/sbin/nologin
# index-server:x:236:105558:index-server:/home/index-server:/sbin/nologin
# …

# Output:
# { 'bobbyd': ['12342', '2333'], 'index-server': ['2333336', '2336', '236'] }

# Doc my understading --> missed during the interview, improve it.
# I understood that my output will be a hashmap where the key is the user-name and the value will be an array with the passwords associated with this user.
# I will receive the input as an array, example gived by Bobby:
# input_array = [
#   ‘index-server:x:23333:…’, 
#   ‘bobbyd:x:12342:…’, 
#   …
# ]
# My output will contain only the duplicated values in the input_array

# Pseudocode --> wrote during the interview, keep doing it.

# Result --> done during the interview
from collections import defaultdict 

def remove_duplicated_users(input_array):
    # result = { ' ' : [] } --> wrote this, it generate a bug
    # [hint] use defaultdict
    result = defaultdict(list)

    for line in input_array:
    # [hint] string.split(‘...’) -> [‘index-server’, ‘x’, ‘23333’, ….]
        splitted_line = line.split(':') # --> put (:) on the interview, it was wrong
        user_name = splitted_line[0]
        user_id = splitted_line[2]
        result[user_name].append(user_id)

    new_result = {} # --> this idea came after the interview
    for key, value in result.items(): # --> put for key, value in result during the interview, it was wrong
        if len(value) > 1:
            new_result[key] = value

    return new_result

input = [
    'index-server:x:233336:10558:index-server:/home/index-server:/sbin/nologin ##(Service Acct)',
    'bobbyd:x:12342:15050:J. Bobby Dorlus:/home/bobbyd:/bin/bash'
    'jdoe:x:34969:155500:John Doe:/home/jdoe:/bin/bash',
    'foobar:x:18836:150440:Mr. Foo Bar:/home/foobar:/bin/bash',
    'bobbyd:x:2333:150880:J. Bobby Dorlus:/home/foobar:/bin/bash', 
    'index-server:x:2336:105558:index-server:/home/index-server:/sbin/nologin',
    'index-server:x:236:105558:index-server:/home/index-server:/sbin/nologin'
]

print(remove_duplicated_users(input))
