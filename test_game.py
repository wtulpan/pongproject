
teams = [
    "chimichangas",
    "pizzas",
    "gnocchi fritti",
    "team2",
    "team4",
    "team6",
    "team8",
    "that fucking guy"
]

d = {
    0: [('x','y')],
    1: [('x','a',(0,0)), ('y','b', (0,0))],
    2: [('x','c',(1,0)), ('a','d',(1,0))]
}

bracket_gen = False

d = [
    [[0,0, ()]]
    ]

d_index = 0
while not bracket_gen:
    d.append([])
    new_d_index = d_index+1
    for game in d[d_index]:
        game_index = list(d[d_index]).index(game)
        d[new_d_index].append([0,0,(d_index, game_index, 0)])
        d[new_d_index].append([0,0,(d_index, game_index, 1)])
    
    bracket_gen = len(d[d_index+1]*2) >= len(teams)
    d_index += 1

for game in d[len(d)-1]:
    if len(teams) == 0:
        break
    game[0] = teams.pop(0)
    if len(teams) == 0:
        break
    game[1] = teams.pop(0)


for rd in d:
    print(rd)

for rd in d[::-1]:
    for game in rd:
        winner = game[int(input("Who won? 0. {} or 1. {} :".format(game[0], game[1])))]
        if len(rd) > 1:
            roud, game, pos = game[2]
            d[roud][game][pos] = winner
        else:
            print("{} won!".format(winner))
            break
            
    print()
    for rd in d:
        print(rd)
    print()

