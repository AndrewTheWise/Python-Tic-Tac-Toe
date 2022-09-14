from os import system, name
def clear():
  if name == 'nt':
    _=system('cls')
  else:
    _=system('clear')

from sys import stdout

import time
def write(print):
  for i in print:
    stdout.write(i)
    stdout.flush()
    time.sleep(.040)

i=1

player="player1"

one="   │"
two="   "
three="│   "
four="   │"
five="   "
six="│   "
seven="   │"
eight="   "
nine="│   "
def tictactoe():
  print("\033[1;37;40m")
  print(one, end=' ')
  print(two, end=' ')
  print(three)
  print("―――――――――――――")
  print(four, end=' ')
  print(five, end=' ')
  print(six)
  print("―――――――――――――")
  print(seven, end=' ')
  print(eight, end=' ')
  print(nine)

write("\033[1;37;40mHow to play:\nEnter the number (1 through 9) of the space you want to mark it.\nMatch 3 spaces in a row to win!")
time.sleep(3)

while i==1:
  clear()
  print("\033[1;37;40mTic Tac Toe\nBy Andrew Wise")
  tictactoe()
  
  if (one==" \033[1;36;40mX\033[1;37;40m │") and (two==" \033[1;36;40mX\033[1;37;40m ") and (three=="│ \033[1;36;40mX\033[1;37;40m ") or (four==" \033[1;36;40mX\033[1;37;40m │") and (five==" \033[1;36;40mX\033[1;37;40m ") and (six=="│ \033[1;36;40mX\033[1;37;40m ") or (seven==" \033[1;36;40mX\033[1;37;40m │") and (eight==" \033[1;36;40mX\033[1;37;40m ") and (nine=="│ \033[1;36;40mX\033[1;37;40m ") or (one==" \033[1;36;40mX\033[1;37;40m │") and (four==" \033[1;36;40mX\033[1;37;40m │") and (seven==" \033[1;36;40mX\033[1;37;40m │") or (two==" \033[1;36;40mX\033[1;37;40m ") and (five==" \033[1;36;40mX\033[1;37;40m ") and (eight==" \033[1;36;40mX\033[1;37;40m ") or (three=="│ \033[1;36;40mX\033[1;37;40m ") and (six=="│ \033[1;36;40mX\033[1;37;40m ") and (nine=="│ \033[1;36;40mX\033[1;37;40m ") or (one==" \033[1;36;40mX\033[1;37;40m │") and (five==" \033[1;36;40mX\033[1;37;40m ") and (nine=="│ \033[1;36;40mX\033[1;37;40m ") or (three=="│ \033[1;36;40mX\033[1;37;40m ") and (five==" \033[1;36;40mX\033[1;37;40m ") and (seven==" \033[1;36;40mX\033[1;37;40m │"):
    while i==1:
      clear()
      print("\033[1;37;40mTic Tac Toe\nBy Andrew Wise")
      tictactoe()
      print("\033[1;36;40m\nPlayer 1 Wins!")
      time.sleep(1)
      clear()
      print("\033[1;37;40mTic Tac Toe\nBy Andrew Wise")
      tictactoe()
      print("\033[1;37;40m\nPlayer 1 Wins!")
      time.sleep(1)
      
  elif (one==" \033[1;31;40mO\033[1;37;40m │") and (two==" \033[1;31;40mO\033[1;37;40m ") and (three=="│ \033[1;31;40mO\033[1;37;40m ") or (four==" \033[1;31;40mO\033[1;37;40m │") and (five==" \033[1;31;40mO\033[1;37;40m ") and (six=="│ \033[1;31;40mO\033[1;37;40m ") or (seven==" \033[1;31;40mO\033[1;37;40m │") and (eight==" \033[1;31;40mO\033[1;37;40m ") and (nine=="│ \033[1;31;40mO\033[1;37;40m ") or (one==" \033[1;31;40mO\033[1;37;40m │") and (four==" \033[1;31;40mO\033[1;37;40m │") and (seven==" \033[1;31;40mO\033[1;37;40m │") or (two==" \033[1;31;40mO\033[1;37;40m ") and (five==" \033[1;31;40mO\033[1;37;40m ") and (eight==" \033[1;31;40mO\033[1;37;40m ") or (three=="│ \033[1;31;40mO\033[1;37;40m ") and (six=="│ \033[1;31;40mO\033[1;37;40m ") and (nine=="│ \033[1;31;40mO\033[1;37;40m ") or (one==" \033[1;31;40mO\033[1;37;40m │") and (five==" \033[1;31;40mO\033[1;37;40m ") and (nine=="│ \033[1;31;40mO\033[1;37;40m ") or (three=="│ \033[1;31;40mO\033[1;37;40m ") and (five==" \033[1;31;40mO\033[1;37;40m ") and (seven==" \033[1;31;40mO\033[1;37;40m │"):
    while i==1:
      clear()
      print("\033[1;37;40mTic Tac Toe\nBy Andrew Wise")
      tictactoe()
      print("\033[1;31;40m\nPlayer 2 Wins!")
      time.sleep(1)
      clear()
      print("\033[1;37;40mTic Tac Toe\nBy Andrew Wise")
      tictactoe()
      print("\033[1;37;40m\nPlayer 2 Wins!")
      time.sleep(1)

  elif player=="player1":
    player="player2"
    player1=input("\033[1;36;40m\nPlayer 1 > ")
    if player1=="1":
      if one=="   │":
        one=" \033[1;36;40mX\033[1;37;40m │"
    elif player1=="2":
      if two=="   ":
        two=" \033[1;36;40mX\033[1;37;40m "
    elif player1=="3":
      if three=="│   ":
        three="│ \033[1;36;40mX\033[1;37;40m "
    elif player1=="4":
      if four=="   │":
        four=" \033[1;36;40mX\033[1;37;40m │"
    elif player1=="5":
      if five=="   ":
        five=" \033[1;36;40mX\033[1;37;40m "
    elif player1=="6":
      if six=="│   ":
        six="│ \033[1;36;40mX\033[1;37;40m "
    elif player1=="7":
      if seven=="   │":
        seven=" \033[1;36;40mX\033[1;37;40m │"
    elif player1=="8":
      if eight=="   ":
        eight=" \033[1;36;40mX\033[1;37;40m "
    elif player1=="9":
      if nine=="│   ":
        nine="│ \033[1;36;40mX\033[1;37;40m "
    elif player1=="andrew made this":
      print("8==>")
      time.sleep(1)

  elif player=="player2":
    player="player1"
    player2=input("\033[1;31;40m\nPlayer 2 > ")
    if player2=="1":
      if one=="   │":
        one=" \033[1;31;40mO\033[1;37;40m │"
    elif player2=="2":
      if two=="   ":
        two=" \033[1;31;40mO\033[1;37;40m "
    elif player2=="3":
      if three=="│   ":
        three="│ \033[1;31;40mO\033[1;37;40m "
    elif player2=="4":
      if four=="   │":
        four=" \033[1;31;40mO\033[1;37;40m │"
    elif player2=="5":
      if five=="   ":
        five=" \033[1;31;40mO\033[1;37;40m "
    elif player2=="6":
      if six=="│   ":
        six="│ \033[1;31;40mO\033[1;37;40m "
    elif player2=="7":
      if seven=="   │":
        seven=" \033[1;31;40mO\033[1;37;40m │"
    elif player2=="8":
      if eight=="   ":
        eight=" \033[1;31;40mO\033[1;37;40m "
    elif player2=="9":
      if nine=="│   ":
        nine="│ \033[1;31;40mO\033[1;37;40m "
    elif player2=="andrew made this":
      print("8==>")
      time.sleep(1)