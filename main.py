#Created by MushroomEnder, 1:31am, October 17, 2020
"""
This code is used to edit already printed statements;
if you want to edit a print statement that has already
been printed to the screen, this program will allow such things.
You can do things like glitch the already printed text, and much more. 
"""

import time
import os
from sys import exit
import platform
from colorama import init, Fore, Back, Style

framemode = True
flashLimiter = False


class Screen:
  Render = ""
  def __init__(self):
      self.Layer1 = []
      self.Layer2 = []
      self.Layer3 = []

  def Clear(self):
      self.Layer1 = []
      self.Layer2 = []
      self.Layer3 = []
      self.Update()

  def Update(self):
    clear()
    counter = 0
    Screen.Render = ""
    for q in self.Layer1:
      print(q, end="", flush="false")
      Screen.Render = Screen.Render + q

      counter = counter + 1
      if counter != len(self.Layer1):
        print("")
        Screen.Render = Screen.Render + "\n"


screen = Screen()

p = print


def s(amount):
    time.sleep(amount)


def clear():
    os.system("clear")


defaultTimeBetween = 0.08


def typed(text: str, timeBetween: float = 0.08, StopNull: list = []):
    """
  This function is used to print a string of characters, character by character.

  ***

  text: This is what you want to be printed to the screen.
  
  timeBetween: This is the time that the console waits in-between characters

  StopNull: These are the indexes of which the typed statement will not wait for them to be typed

  ***
  """
    Link = False
    if "http" in text:
        Link = True

    build = None
    counter = 0
    for i in text:
        counter = counter + 1

        if framemode:
            if build == None:
                screen.Layer1.append(str(i))
                build = i
            else:
                build = str(build) + str(i)

            screen.Layer1[-1] = build

            screen.Update()
        else:
            print(i, end="", flush="false")

        if not (counter in StopNull):
            if (i == ",") and not (Link == True):
                s(timeBetween * 6.25)
            elif (i == ".") or (i == "!") or (i == "?") and not (Link == True):
                s(timeBetween * 12.5)
            else:
                s(timeBetween)
    print("")
    s(0.3)


def question(text: str,
             clr: bool = False,
             AnswerType: type = str,
             InputPrompt: str = ">>> "):
    """
  This function is used to ask the user a question in any format you wish.
  
  ***
  text: this is the question that is being asked of the User. 

  AnswerType: This is the type of answer you want the user to input. This can be  
  a string(str), integer(int), float(float), or bool(bool). This is how the
  answer will be returned as well.

  Clr: True if you want the screen to be cleared after.

  InputPrompt: This is what will be printed as the input question. This is normally ">>> " (To use the default, type "normal" for this argument)
  but this can be changed to something like "$" so then the user knows they're entering
  a dollar amount. Ex -> Afterprint: "$ " When user has typed something: "$ 4.00" Then they can press enter, and the function will return: "4.00" as a float
  ***
  """
    while True:
        typed(text)
        if InputPrompt.upper() == "NORMAL":
            Answer = input(">>> ")
        else:
            Answer = input(InputPrompt)

        if AnswerType == str:
            str(Answer)
            break

        elif AnswerType == int:
            try:
                int(Answer)
            except ValueError:
                typed("That was not an integer")
            else:
                break

        elif AnswerType == float:
            try:
                float(Answer)
            except ValueError:
                typed("That was not a float")
            else:
                break
        elif AnswerType == bool:
            try:
                bool(Answer)
            except ValueError:
                typed("That was not a true or false statement")
            else:
                break

        else:
            TypeError("That was not an accepted Value")

    if clr:
        clear()
    return Answer


def Continue(text: str = "normal", clr: bool = True) -> str:
    """
  This function is used to ask the user to press enter to continue the code

  ***

  text: The text that is printed when they are prompted to press Enter. This
  is normally "<Press Enter to Continue>"

  clr: If true, the screen will be cleared after the enter key has been pressed
  
  ***

  This function will also return anything that they typed.
  """

    if text.upper() == "NORMAL":
        Continue1 = input("<Press Enter to Continue>")
    else:
        Continue1 = input("<" + text + ">")

    if clr:
        clear()

    return Continue1


#Functions so they do not have to create a whole new character
def deathhancox(text: str):
    """
  Talk as deathhancox 

  text: What they Say 
  """

    typed(text)
    screen.Layer1[-1] = "Deathhancox: " + screen.Layer1[-1]
    screen.Update()


#functions so they do not have to create a whole new character
def ender(text: str):
    """
  Talk as MushroomEnder 

  text: What they Say 
  """

    typed(text)
    screen.Layer1[-1] = "MushroomEnder: " + screen.Layer1[-1]
    screen.Update()

def stc(color):
  color = color.lower()
  if color == "red":
    NewColor = Fore.RED
  elif color == "orange":
    NewColor = Fore.ORANGE 
  elif color == "yellow":
    NewColor = Fore.Yellow 
  elif color == "green":
    NewColor = Fore.GREEN 
  elif color == "cyan":
    NewColor = Fore.CYAN 
  elif color == "blue":
    NewColor = Fore.BLUE 
  elif (color == "purple") or (color == "magenta"):
    NewColor = Fore.MAGENTA 
  elif color == "black":
    NewColor = Fore.BLACK 
  elif color == "white":
    NewColor = Fore.WHITE

  return NewColor;

class character:
    def __init__(self, name: str = "Somebody", color: str = "WHITE"):
        self.n = name
        self.c = stc(color)

    def Talk(self, text):
        BeginningText = self.n + ": "
        counter = 0
        AvoidList = [0]
        for i in BeginningText:
            counter = counter + 1

            AvoidList.append(counter)

        typed(self.c + BeginningText + text, 0.08, AvoidList)

    def Action(self, text):
      screen.Layer1.append(self.c + "*{} {}*".format(self.n, text))
      screen.Update()

