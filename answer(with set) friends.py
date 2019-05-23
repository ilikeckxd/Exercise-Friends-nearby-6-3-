# 從user得到一串string以空格分離
# 拿去跟people.txt比對 重複的放到near_by_friends.txt

friends_list = input('enter 3 friends, split by space: ').split(' ')
# split() 把string轉成list。也可用[letter for letter in str]
# list() set() list跟set可互相轉換


def write_list_into_file(a_list, file_name_str):
    file = open(file_name_str, 'w')
    for people in a_list:
        file.write(f'{people}\n')
    file.close()


# 決定nearby有誰 也就是people.txt裡有誰
people_nearby_list = ['a', 'c', 'd', 'e']
write_list_into_file(people_nearby_list, 'people.txt')


file_nearby = open('people.txt', 'r')
nearby_list = [line.strip() for line in file_nearby.readlines()]
# 每個尾巴都有\n=>用strip()把string前後的空格、換行strip掉
# readlines()把檔案中的每行轉換成list

nearby_set = set(nearby_list)
friends_set = set(friends_list)
nearby_friends_set = friends_set.intersection(nearby_set)
# 轉換成set是因為要利用set的交集功能
# 或是用list的.count

nearby_friends_list = list(nearby_friends_set)
for friend in nearby_friends_list:
    print(f'{friend} is nearby, meet up with them!')


''' 使用list的.count功能

nearby_f_list = [friend for friend in friends_list if nearby_list.count(friend.strip()) != 0]
write_list_into_file(nearby_f_list, 'near_by_friends.txt')
for friend in nearby_f_list:
    print(f'{friend} is nearby, meet up with them!')
    



# 使用enumerate函數 讓每行都有\n 除了最後一行
def write_list_into_file(a_list, file_name_str):
    with open(file_name_str, 'w') as file:
        for i, people in enumerate(a_list):
            if i != len(a_list)-1:
                file.write(f'{people}\n')
            else:
                file.write(f'{people}.')

'''
