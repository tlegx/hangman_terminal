from utils import utils
_BODY_PART_MAPPER = {'head':(0,2), 'left_arm':(1,3), 'right_arm':(2,3), 'left_leg':(4,5), 'right_leg':(5,5), 'body':(3,4)}
HANGMAN_SEQ = ['head', 'left_arm', 'right_arm', 'body', 'left_leg', 'right_leg']
BODY = ["     |      (_)", 
        "     |       |/" ,
        "     |      \|/",
        "     |       |",
        "     |      /  ",
        "     |      / \ ",
        ]
HANGER = [
        "      _______ ",
        "     |/      |",
        "     |        ",
        "     |        ",
        "     |        ",
        '     |        ',
        "     |        ",
        "    _|___     ",
        ]

class DrawHangMan:
    def __init__(self) -> None:
        self.curr_frame = HANGER
        self.curr_part = 0

    def hanger(self, pos=None, body_no=None):
        utils.clear_screen()
        if pos == None:
            self.draw_curr_hanger()
        else:
            frame = []
            for k, hanger_part in enumerate(self.curr_frame):
                if k == pos:
                    frame.append(BODY[body_no])
                    print(BODY[body_no])
                else:
                    frame.append(self.curr_frame[k])
                    print(self.curr_frame[k])
            self.curr_frame = frame

    def draw(self, part='head'):
        part_no, part_pos = _BODY_PART_MAPPER[part]
        self.hanger(part_pos, part_no)

    def draw_curr_hanger(self):
        utils.clear_screen()
        for frame in self.curr_frame:
            print(frame)

    def start(self):
        self.hanger()

    def next(self):
        if self.curr_part==len(HANGMAN_SEQ):
            print('GAME OVER!!!')
            exit()
        self.draw(part=HANGMAN_SEQ[self.curr_part])
        self.curr_part += 1

