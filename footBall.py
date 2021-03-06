""""
CODEFORCE 43-A
======================

One day Vasya decided to have a look at the results of Berland 1910 Football Championship’s finals. 
Unfortunately he didn't find the overall score of the match; however, he got hold of a profound description of the match's process. 
On the whole there are n lines in that description each of which described one goal. 
Every goal was marked with the name of the team that had scored it. Help Vasya, learn the name of the team that won the finals. 
It is guaranteed that the match did not end in a tie.

Input
The first line contains an integer n (1 ≤ n ≤ 100) — the number of lines in the description. 
Then follow n lines — for each goal the names of the teams that scored it. 
The names are non-empty lines consisting of uppercase Latin letters whose lengths do not exceed 10 symbols. 
It is guaranteed that the match did not end in a tie and the description contains no more than two different teams.

Output
Print the name of the winning team. We remind you that in football the team that scores more goals is considered the winner.

-----------------------------------------------------------------------------------------------------------------------------
"""


test = int(input())
t1 = ''
t2 = ''
teamList = []
t1Count = 0
t2Count = 0
while (test != 0):
    string = input()
    teamList.append(string)
    test -= 1
if len(teamList) > 1 and len(set(teamList)) == 1:
    t1 = sorted(set(teamList))[0]
elif len(teamList) > 1:
    t1 = sorted(set(teamList))[0]
    t2 = sorted(set(teamList))[1]
 
if len(teamList) == 1:
    print(string)
for i in teamList:
    if t1 == i:
        t1Count += 1
    elif t2 == i:
        t2Count += 1
if t1Count > t2Count:
    print(t1)
else:
    print(t2)