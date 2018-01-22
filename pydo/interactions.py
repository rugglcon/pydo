"""
Copyright (C) 2018 Connor Ruggles

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import curses
from . import Task
from . import utils

NUM_KEYS = {
    '48' : '0',
    '49' : '1',
    '50' : '2',
    '51' : '3',
    '52' : '4',
    '53' : '5',
    '54' : '6',
    '55' : '7',
    '56' : '8',
    '57' : '9'
}

def get_intent(screen):
    """gets the intent of the user"""
    print_help(screen)
    return screen.getkey()

def print_help(screen):
    """prints the standard help message"""
    screen.addstr(curses.LINES - 1, 0, "(l)ist tasks; (c)reate task; (d)elete task; (f)inish task; (q)uit")
    screen.addstr(curses.LINES - 2, 0, "Help:")
    screen.refresh()

def print_all_tasks(list_object, screen):
    """
    calls a function to retrieve all
    tasks, then prints them
    """
    screen.addstr(0, 0, "All tasks")
    screen.addstr(1, 0, "---------")
    list_object.print_tasks(screen)
    print_help(screen)

def create_task(list_object, screen):
    """
    creates a task with user input of
    title and description
    """
    screen.addstr(0, 0, "New task")
    screen.addstr(1, 0, "--------")
    screen.addstr(3, 0, "Title of new task: ")
    curses.echo()
    screen.refresh()
    title = screen.getstr(3, 19)
    desc_str = "Description of new task (leave blank for no description): "
    desc_len = len(desc_str)
    screen.addstr(4, 0, desc_str)
    desc = screen.getstr(4, desc_len)
    curses.noecho()
    new_task = Task.Task(title.decode("utf-8"), desc.decode("utf-8"))
    list_object.add_task(new_task)
    screen.clear()
    print_all_tasks(list_object, screen)
    print_help(screen)

def delete_task(list_object, screen):
    """deletes the selected task"""
    screen.addstr(0, 0, "Deleting task")
    screen.addstr(1, 0, "-------------")
    cur_line = list_object.print_tasks(screen)
    screen.addstr(cur_line + 1, 0, "Which task to delete? > ")
    index = screen.getch()
    screen.refresh()
    list_object.delete_task(int(NUM_KEYS[str(index)]))
    screen.clear()
    print_all_tasks(list_object, screen)
    print_help(screen)

def finish_task(list_object, screen):
    """finishes the selected task"""
    screen.addstr(0, 0, "Finishing task")
    screen.addstr(1, 0, "--------------")
    cur_line = list_object.print_tasks(screen)
    screen.addstr(cur_line + 1, 0, "Which task to finish? > ")
    index = screen.getch()
    screen.refresh()
    list_object.finish_task(int(index) - 1)
    print_help(screen)
