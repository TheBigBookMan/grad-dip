class ScoreEntry:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(score_entry):
        return score_entry.score


class Scoreboard:
    def __init__(self):
        self.scores = [] # each element is a score entry object

    # Write your add_score and print_leaderboard methods here
    def add_score(self, player_name, player_score):
        new_score_entry = ScoreEntry(player_name, player_score)
        
        print(new_score_entry.score)
        
        # self.scores.append(new_score_entry)
        # print(self.scores)

    # def print_leaderboard():
        

scoreboard = Scoreboard()

scoreboard.add_score('Alice', 7821)
scoreboard.add_score('Bob', 12103)
scoreboard.add_score('Charlie', 8762)
scoreboard.add_score('Denise', 6573)

# scoreboard.print_leaderboard()