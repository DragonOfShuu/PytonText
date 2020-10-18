#Created by MushroomEnder, 1:31am, October 17, 2020
"""
This code is used to edit already printed statements;
if you want to edit a print statement that has already
been printed to the screen, this program will allow such things.
You can do things like glitch the already printed text, and much more. 
"""

import time 
import os 
import sys 
import platform

p = print 
def s(amount): time.sleep(amount)
clear = os.system("clear")


def Typed(text: str, timeBetween: float):
  """
  This function is used to print a string character by character.

  ***

  text: This is what you want to be printed to the screen.
  
  timeBetween: This is the time that the console waits in-between characters

  ***
  """
  for i in text:
    p(i, end="", flush="false")
    s(0.08)
  s(0.3)
  print("")

def Question(text: str, AnswerType: type, clr: bool, InputPrompt: str):
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
    Typed(text, 0.3)
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
        Typed("That was not an integer")
      else:
        break
    
    elif AnswerType == float:
      try:
        float(Answer)
      except ValueError:
        Typed("That was not a float")
      else:
        break
    elif AnswerType == bool:
      try:
        bool(Answer)
      except ValueError:
        Typed("That was not a true or false statement")
      else:
        break

    else:
      TypeError("That was not an accepted Value")
  
  if clr: 
    clear
  return Answer;
    
def Continue(text: str, clr: bool) -> str:
  """
  This function is used to ask the user to press enter to continue the code

  ***

  text: The text that is printed when they are prompted to press Enter. This
  is normally "<Press Enter to Continue>"(type in "normal" for this argument if you want to use that)

  clr: If true, the screen will be cleared after the enter key has been pressed
  
  ***

  This function will also return anything that they typed.
  """
  if text.upper() == "NORMAL":
    Continue1 = input("<Press Enter to Continue>")
  else:
    Continue1 = input("<" + text + ">")

  if clr:
    clear

  return Continue1;
