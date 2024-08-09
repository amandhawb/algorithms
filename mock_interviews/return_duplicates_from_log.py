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
from collections import defaultdict
def return_duplicates(input):
    unfiltered_result = defaultdict(list)

    for item in input:
        splitted = item.split(':')
        user_name = splitted[0]
        user_id = splitted[2]

        unfiltered_result[user_name].append(user_id)

    filtered_result = {}
    
    for key, value in unfiltered_result.items():
        if len(value) > 1:
            filtered_result[key] = value
    
    return filtered_result

input = [
    'index-server:x:233336:10558:index-server:/home/index-server:/sbin/nologin ##(Service Acct)',
    'bobbyd:x:12342:15050:J. Bobby Dorlus:/home/bobbyd:/bin/bash'
    'jdoe:x:34969:155500:John Doe:/home/jdoe:/bin/bash',
    'foobar:x:18836:150440:Mr. Foo Bar:/home/foobar:/bin/bash',
    'bobbyd:x:2333:150880:J. Bobby Dorlus:/home/foobar:/bin/bash', 
    'index-server:x:2336:105558:index-server:/home/index-server:/sbin/nologin',
    'index-server:x:236:105558:index-server:/home/index-server:/sbin/nologin'
]

# print(return_duplicates(input))

# follow up --> Can you do it without the second for loop?

def return_duplicates_follow_up(input):
    already_seen = defaultdict(list)
    filtered_result = defaultdict(list)

    for item in input:
        splitted = item.split(':')
        user_name = splitted[0]
        user_id = splitted[2]

        if user_name in already_seen:
            print('AQUI', already_seen[user_name])
            # already_seen[user_name].append(user_id)
            # prev_id = already_seen[user_name]
            # prev_id.extend(user_id)
            # filtered_result[user_name].append(prev_id)
        else:
            already_seen[user_name].append(user_id)

        # unfiltered_result[user_name].append(user_id)
    print('LISTA AQUI', already_seen)

    
    
    # for key, value in unfiltered_result.items():
    #     if len(value) > 1:
    #         filtered_result[key] = value
    
    return filtered_result

print(return_duplicates_follow_up(input))