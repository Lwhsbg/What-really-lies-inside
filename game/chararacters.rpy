define m = Character("[player_name]", color="#c9c9c9")
define e = Character("???", color="#8b0000", what_italic=True)
define fa = Character("A woman's voice", color="#c9a9a9", what_italic=True)
define fb = Character("A man's voice", color="#a9b9c9", what_italic=True)
define fc = Character("A boy's voice", color="#b9c9a9", what_italic=True)
define fd = Character("A small voice", color="#e0d9a9", what_italic=True)
define mira = Character("Mira", color="#e0b0b0")

define flicker = Fade(0.05, 0.05, 0.05, color="#000000")
define slow_fade = Fade(1.0, 0.5, 2.0, color="#000000")
define fade_black = Fade(0.5, 0.3, 1.2, color="#000000")

default player_name = "Byayaya"
default suspicion = 0
default clues = set()
default lore = set()
default tokens = set()
default done = set()
default memories = set()
default rooms_visited = set()
default hub_visits = 0
default door_gone = False
default lock_attempts = 0
default pins = []
default pin_slot = 1
default caught_reason = "lock"
default phone_checks = 0
default tc = 0
default enc1 = False
default enc2 = False
default enc3 = False
default enc4 = False

init python:
    def symbols_found():
        return len([s for s in ("wolf", "stag", "owl", "moth") if s in clues])

    def orders_found():
        return len([s for s in ("o_moth", "o_owl", "o_stag", "o_wolf") if s in clues])