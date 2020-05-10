# put your python code here
n = int(input())
table = [[0, ]]
teams = []
match = []
game = 0
win = 0
lose = 0
nn = 0
point = 0
p = 0
for i in range(n):
    match = input().split(';')
    team1 = match[0]
    team2 = match[2]
    sc1 = int(match[1])
    sc2 = int(match[3])
    # print(match)
    if team1 not in teams:
        teams.append(team1)
        table.append([team1, game, win, nn, lose, point])
    if team2 not in teams:
        teams.append(team2)
        table.append([team2, game, win, nn, lose, point])
    if sc1 > sc2:
        for i in range(len(table)):
            if team1 == table[i][0]:
                table[i][1] += 1
                table[i][2] += 1
                table[i][5] += 3
        for i in range(len(table)):
            if team2 == table[i][0]:
                table[i][1] += 1
                table[i][4] += 1

    if sc1 < sc2:
        for i in range(len(table)):
            if team2 == table[i][0]:
                table[i][1] += 1
                table[i][2] += 1
                table[i][5] += 3
        for i in range(len(table)):
            if team1 == table[i][0]:
                table[i][1] += 1
                table[i][4] += 1
    if sc1 == sc2:
        for i in range(len(table)):
            if team2 == table[i][0]:
                table[i][1] += 1
                table[i][3] += 1
                table[i][5] += 1
        for i in range(len(table)):
            if team1 == table[i][0]:
                table[i][1] += 1
                table[i][3] += 1
                table[i][5] += 1

del table[0]
for i in range(len(table)):
    print(table[i][0] + ':', table[i][1], table[i][2], table[i][3], table[i][4], table[i][5])