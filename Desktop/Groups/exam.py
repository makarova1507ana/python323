# import functools
# """
# 5 13
# 3 10 300 15 3
# """
# n, money = map(int, input().split())
# guns = []
# guns= list(map(int, input().split()))
# guns = list (filter(lambda x: x<=money, guns))
# if len(guns) == 0:
#     print(0)
# else:
#     print(max(guns))



# #-----------------------------------------------#
# string = input("")  #sheriff
# s = string.count("s")
# h = string.count("h")
# e = string.count("e")
# r = string.count("r")
# i = string.count("i")
# f = string.count("f") #в слове 2 буквы должно быть использовано
# count_words = 0
# while s > 0 and h > 0 and e > 0 and r > 0 and i > 0 and f >= 2:
#     s -= 1
#     h -= 1
#     e -= 1
#     r -= 1
#     i -= 1
#     f -= 2
#     count_words += 1
# print(count_words)

# #-----------------------------------------------#
# import functools
# money, n = map(int, input().split())
# nominals = list(map(int, input().split()*2)) #каждой по 2
# nominals.sort()
# nominals = list(filter(lambda x: x<=money, nominals))
# s = []
# for i in range(len(nominals)):
#     f = False
#     for j in range(i+1, len(nominals)):
#         if sum(nominals[i:j+1]) == money:
#             s = nominals[i:j+1]
#             f =True
#             break
#         elif sum(nominals[i:j+1]) > money:
#             break
#     if f:
#         break
# if len(s)==0:
#     print(-1)
# else:
#     print(len(s))
#     for i in s:
#         print(i, end=' ')

# # #-----------------------------------------------#
# # import functools
# cities, rides = map(int, input().split())
# states = {}
# d = {}
# state = 0
# max_num = 0
# list_city_with_1_ride = []
# for ride in range(rides):
#     city1, city2, len_ride = list(map(int, input().split()))
#     if (city1 in d) == False and (city2 in d) == False:
#         state += 1
#         d = {}
#
#     if (city1 in d) == False:
#         d[city1] = []
#
#     if (city2 in d) == False:
#         d[city2] = []
#
#     if city1 != city2:
#         d[city1].append(len_ride)
#         d[city2].append(len_ride)
#         states[state] = d
#     else:
#         d[city1].append(len_ride)
#         states[state] = d
#
#     max_num = max(max_num,len_ride)
#
# print(d)
# print(states)
# l = []
# t = 0
# for x in range(max_num):
#     for state in states:
#         for city in states[state]:
#             for ride in states[state][city]:
#                 if len(states[state][city]) == 1:
#                     t = states[state][city] - 1
#                 else:
#                     if (max(states[state][city]) in l) == False:
#                         l.append(max(states[state][city]))
# if t!=0:
#     print(t)
# else:
#     print(min(l)-1)


# #-----------------------------------------------#
spirites, questions = map(int, input().split())
q = []
for i in range(questions):
    q.append(list(map(int, input().split())))

d = {}
teams = []
for i in range(1, spirites+1):
    d[i] = 1
    teams.append([i])

answer = ""

for i in range(questions):
    question = q[i]

    if question[0] == 1:
        for team in teams:
            if question[1] in team and question[2] in team:
                break
            elif question[1] in  team:
                for el in team:
                    d[el] += 1
                d[question[1]]-=1
                team.pop(team.index(question[1]))

            if question[2] in team:
                team.append(question[1])
                for el in team:
                    d[el] += 1

        for team in teams:
            if len(team) == 0:
                teams.pop(teams.index(team))


    if question[0] == 2:
        for team in teams:
            if question[1] in team and question[2] in team:
                answer += "YES\n"
                break
        else:
            answer += "NO\n"

    if question[0] == 3:
        answer = answer +  str(d[question[1]]) + '\n'
print(answer)



# # # #-----------------------------------------------#
# def check(a, b):
#
#     if a == b:
#         return True
#     for l in range(len(a)):
#         for r in range(l+1,len(a)):
#             res = a
#             part2 = a[l:r+1]
#             part2.sort()
#             res = a[:l] + part2 + a[r+1:]
#             if res == b:
#                 return True
#
#     return False
#
#
#
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# # Проверяем, может ли Джо получить выигрышную последовательность.
#
# if check(a, b):
#     print("YES")
# else:
#    print("NO")

# # # #-----------------------------------------------#
#
#
