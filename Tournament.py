
#Tornament Class
class Tournament:
    
    self.teams = []
    self.game_started = False
    self.current_game = None
    self.rounds = [
        [[0,0, ()]]
        ]
    
    self.winner = ""

    def Tournament(self):
        pass

    #add a team
    def add_team(self, name):
        if not self.game_started:
            self.teams.append(name)
        else:
            raise Exception("Game Already Started")

    #start a game
    def start(self):
        bckt_generated = False

        round_num = 0
        while not bckt_generated:
            self.rounds.append([])
            nxt_round = round_num +1
            #loop through each game in each round, and add two games to the next round
            for game in self.rounds[round_num]:
                game_index = list(self.rounds[round_num]).index(game)

                self.rounds[nxt_round].append(["null", "null", (round_num, game_index, 0)])
                self.rounds[nxt_round].append(["null", "null", (round_num, game_index, 1)])

            bckt_generated = len(self.rounds[nxt_round]*2) >= len(self.teams)
            round_num += 1
        
        self.current_game = (round_num-1, 0)
        self.game_started = True
    
    #have a team win the current game
    #team should be an int that is either 0 or 1
    def win(self, team):
        if team not in (0,1):
            raise Exception("Error, winning team in improper format, please give a 1 or a 0")

        rd_num = self.current_game[0]
        gm_num = self.current_game[1]

        game = self.rounds[rd_num][gm_num]

        winner = game[team]

        #if the game is the last one
        if self.current_game == (0,0):
            self.winner = winner
            return

        nxt_round, nxt_game, nxt_pos = game[2]
        self.rounds[nxt_round][nxt_game][nxt_pos] = winner

        if gm_num >= len(self.rounds[rd_num]):
            self.current_game = (rd_num-1, 0)
        else:
            self.current_game = (rd_num, gm_num+1)


    def get_full_bracket(self):
        return self.rounds


    def get_current_game(self):
        return self.rounds[self.current_game[0], self.current_game[1]]