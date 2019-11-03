from ..desks import DefaultDesk
from argparse import _SubParsersAction

class DefaultCommandHandler:

    def __init__(self, desk: DefaultDesk):
        self.desk = desk

    def init(self, parser: _SubParsersAction):

        move_up_parser = parser.add_parser("up")
        move_up_parser.set_defaults(action="up")

        move_down_parser = parser.add_parser("down")
        move_down_parser.set_defaults(action="down")

        move_parser = parser.add_parser("move")
        move_parser.set_defaults(action="move")
        move_to_parser = move_parser.add_argument('--to')

    def handle(self, args):

        if args.action == "up":
            self.desk.up()
        elif args.action == "down":
            self.desk.down()
        elif args.action == "move":
            self.desk.move_to(int(args.to))
        else:
            pass # allow overrides / extends