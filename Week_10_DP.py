# This creates a class called ChelseaPlayer (Based on my favourite soccer team Chelsea FC)
class ChelseaPlayer:
    # Initializes the class with 4 attributes: Player name, jersey number, goals, and assists
    def __init__(self, name, jersey_number, goals_scored, assists):
        self.name = name
        self.jersey_number = jersey_number
        self.goals_scored = int(goals_scored)
        self.assists = int(assists)
        self.total_contributions = self.goals_scored + self.assists

    # Creates a method to display player statistics
    def show_stats(self):
        print(f"{self.name} plays for Chelsea FC, he wears number {self.jersey_number}, "
              f"in the 2024-2025 premier league season so far he has {self.goals_scored} goals and "
              f"{self.assists} assists for a total of {self.total_contributions} total contributions!")

    # Creates a method to increase player goal count by 1 each time this method is called upon
    def score_goal(self):
        self.goals_scored += 1
        print(f"{self.name} has scored another goal!!! GO BLUES!!! "
              f"{self.name} now has {self.goals_scored} goals scored.")

# Creates 3 players within the ChelseaPlayer and adds information for their attributes
# These are real players from Chelsea FC with current stats from the 2024-2025 season of the premier league!
player1 = ChelseaPlayer("Cole Palmer", "20", "7", "5")
player2 = ChelseaPlayer("Nicolas Jackson", "15", "6", "4")
player3 = ChelseaPlayer("Pedro Neto", "7", "1", "2")


# Displays stats from players 1, 2, and 3 while also adding a goal to both players 1 and 3
player1.show_stats()
player1.score_goal()
player2.show_stats()
player3.show_stats()
player3.score_goal()