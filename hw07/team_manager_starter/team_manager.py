from team import Team
from bench import Bench


def main():
    print("Welcome to the team manager.")
    # Create objects for the team and the bench
    # Objects used to run all functions required
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower()
        command = (input("What do you want to do?\n")).lower()

        # Inputting "done" exits main, ending the session.
        if command == "done":
            print("Shutting down team manager\n")
            return
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


# Function to set team name
def do_set_team_name(team):
    name = input("What do you want to name the team?\n")
    team.set_team_name(name)


# Function to show current team roster
def do_show_team_roster(team):
    # TODO: call the method on the team object that
    # displays the roster
    team.show_team_roster()


# Function to check if a position is filled
def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    team.is_position_filled(position)


# Function to add a new player to the team
def do_add_player_to_team(team):
    player_name = input("What's the player's name?\n")
    player_number = input("What's " + player_name + "'s number?\n")
    # Check if number entered is an integer
    try:
        player_number = int(player_number)
    except ValueError:
        print("Player number needs to be an integer."
              "Try adding the player again!")
        return
    player_position = input("What's " + player_name + "'s position?\n")
    if player_position not in ("catcher", "corner", "sniper", "thrower"):
        print("That position does not seem right."
              "Try adding a player again!")
        return

    team.add_player(player_name, player_number, player_position)
    # TODO: call the method on team that creates a new player and
    # adds the player to the team.
    print("Added", player_name, "to", team.name)


# Function to send a player to the bench
def do_send_player_to_bench(team, bench):
    name = input("Who do you want to send to the bench?\n")
    for player in team.players:
        if name == player.player_name:
            bench.send_to_bench(name)
            print("Sent", name, "to bench")
            return
    print(name, "isn't on the team.")


# Function to get the player who has been on the bench longest
def do_get_player_from_bench(bench):
    if len(bench.benched_players) > 0:
        unbenched_player = bench.get_from_bench()
        print("Got", unbenched_player, "from bench")
    else:
        print("The bench is empty.")


# Function to cut a player from the team & bench
def do_cut_player(team, bench):
    player_name = input("Who do you want to cut?\n")
    team.cut_player(player_name)
    bench.cut_player(player_name)


# Function to show current bench
def do_show_bench(bench):
    bench.show_bench()


# Code to handle unknown commands
def do_not_understand():
    print("I didn't understand that command")


main()
