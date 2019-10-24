
class Bench:
    """
    A class representing a sidelines bench
    """
    def __init__(self):
        # Initialize the bench object
        self.benched_players = []

    def send_to_bench(self, player_name):
        # Move the specific player "onto the bench"
        self.benched_players.append(player_name)

    def get_from_bench(self):
        # Return the name of the player who has
        # been on the bench longest.
        unbenched_player = self.benched_players.pop(0)
        return unbenched_player

    def cut_player(self, player_name):
        # Remove player from bench if the player
        # has been cut from the team
        if player_name in self.benched_players:
            self.benched_players.remove(player_name)

    def show_bench(self):
        # Function that will display the
        # current list of players on the bench
        if len(self.benched_players) == 0:
            print("The bench is currently empty.")
        elif len(self.benched_players) > 0:
            for i in self.benched_players:
                print(i)
