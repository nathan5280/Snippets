from curses import wrapper
from typing import Dict, List


def open_file(*, stdscr) -> None:
    stdscr.clear()
    stdscr.addstr("Open File")
    stdscr.getch()


def save_file(*, stdscr) -> None:
    stdscr.clear()
    stdscr.addstr("Save File")
    stdscr.getch()


def menu(*, stdscr, title: str, cfg: List[Dict]) -> None:
    done = False

    def done_menu(*, stdscr):
        nonlocal done
        done = True

    action_lookup = {}
    while not done:
        stdscr.clear()

        stdscr.addstr("\t{}\n\n".format(title))
        for item in cfg:
            stdscr.addstr("\t{}\n".format(item["item"]))

            for key in item["select"]:
                action_lookup[key] = item["action"]

        stdscr.addstr("\n\tE(x)it\n\n")
        action_lookup[ord('X')] = done_menu
        action_lookup[ord('x')] = done_menu

        stdscr.addstr("Selection: ")

        stdscr.refresh()
        key = stdscr.getch()

        if key in action_lookup:
            action_lookup[key](stdscr=stdscr)


def select(*, stdscr, title: str, cfg=List[Dict]) -> int:
    done = False
    while not done:
        stdscr.clear()

        valid_selections = []
        stdscr.addstr("\t{}\n\n".format(title))
        for idx, item in enumerate(cfg):
            stdscr.addstr("\t{}: {}\n".format(chr(ord('a') + idx), item))
            valid_selections.append(ord('a') + idx)

        stdscr.addstr("\n\tE(x)it\n\n")
        stdscr.addstr("Selection: ")

        stdscr.refresh()
        key = stdscr.getch()

        if key in [ord('X'), ord('x')]:
            return None

        if key in valid_selections:
            return key - ord('a')


def file_menu(*, stdscr):
    menu_cfg = [
        {
            "item": "(O)pen",
            "select": [ord('O'), ord('o')],
            "action": open_file
        },
        {
            "item": "(S)ave",
            "select": [ord('S'), ord('s')],
            "action": save_file
        }
    ]

    menu(stdscr=stdscr, title="File Menu", cfg=menu_cfg)


def select_menu(*, stdscr):
    select_cfg = [
            "Item 1",
            "Item 2"
    ]
    selection = select(stdscr=stdscr, title="Selection Menu", cfg=select_cfg)


    stdscr.clear()
    stdscr.addstr("Selection: {}".format(selection))
    stdscr.getch()


def main_menu(stdscr):
    menu_cfg = [
        {
            "item": "(F)ile",
            "select": [ord('F'), ord('f')],
            "action": file_menu
        },
        {
            "item": "(S)elect",
            "select": [ord('S'), ord('s')],
            "action": select_menu
        }
    ]
    menu(stdscr=stdscr, title = "Main Menu", cfg=menu_cfg)


if __name__ == '__main__':
    wrapper(main_menu)
