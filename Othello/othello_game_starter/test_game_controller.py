from game_controller import GameController


def test_constructor():
    """
    Test the Game Controller constructor
    """
    g = GameController(800, 8)
    assert g.WINDOW_SIZE == 800
    assert g.BOARD_SIZE == 8
    assert g.player_turn is True
    assert g.game_over is False
    assert g.game_scores is None
    assert g.name is None
    assert g.name_entered is False
    assert g.TURN_TEXT_TIMER == 60
    assert g.ASK_NAME_TIMER == 30
    assert g.ask_name_timer == 30
    assert g.turn_display_timer == 60
    assert g.TEXT_OFFSET == 100


def test_update():
    """
    Test game controller update function
    """
    g = GameController(800, 8)
    g.game_over = False
    g.player_turn = False
    g.turn_display_timer = 0
    g.update()
    assert g.player_turn is True
    assert g.turn_display_timer == 60


# def test_display_turn_text():
    # Unable to test method since it displays in processing


# def test_display_result():
    # Unable to test method since it displays in processing

# def test_input_name():
    # Unable to test java input function

def test_score_file():
    """
    Test if scores can be written correctly into the file
    """
    g = GameController(800, 8)
    # Test high score
    g.game_scores = (50, 100)
    g.name = "Alpha"
    g.score_file()
    with open("scores.txt", "r") as f:
        top_score_line = f.readline()
    assert top_score_line == "Alpha 100\n"

    # Test low score
    g.game_scores = (5, 10)
    g.name = "Beta"
    g.score_file()
    with open("scores.txt", "r") as f:
        file_contents = f.read().split("\n")
    assert file_contents[-2] == "Beta 10"


# def test_get_player_name():
    # Unable to test method that calls the java input function
