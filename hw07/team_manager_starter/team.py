from player import Player
import re


class Team:
    """
    A class representing a dodgeball team
    """
    def __init__(self):
        self.name = "Anonymous Team"
        # List of all players
        self.players = []

    def set_team_name(self, name):
        # Set the team name
        bad_name_char = r"[^\w\s]"
        if len(re.findall(bad_name_char, name)) == 0:
            self.name = name
        else:
            print("Name entered is not alphanumeric.")

    def add_player(self, player_name, player_number, player_position):
        # Create and call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        player_object = Player(player_name, player_number, player_position)
        self.players.append(player_object)

    def cut_player(self, player_name):
        # Remove the player with the name player_name
        # from the players list.
        for i in self.players:
            if player_name == i.player_name:
                self.players.remove(i)
                return
        print("Player is not on the roster.")

    def is_position_filled(self, position):
        # Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        for i in self.players:
            if position == i.player_position:
                print("Yes, the", position, "is filled.")
                return
        print("No, the", position, "position is not filled")

    def show_team_roster(self):
        # Show roster method
        # Print is left indented to create columnar format
        if len(self.players) > 0:
            print("The lineup for", self.name, "is:")
            for i in self.players:
                print('{:<5} {:<14} {:<8}'.format
                      (i.player_number, i.player_name, i.player_position))
        elif len(self.players) == 0:
            print("The lineup for", self.name, "is currently empty.")
