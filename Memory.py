'''
Este juego es una implementacion del juego clasico de memorias en Python 3.3.2, donde se tiene que encontrar
todos los pares de cartas con el mismo numero para ganar el juego.

MEMORY GAME
Created by: Jassael Ruiz
Version: 1.0
'''

import sys
sys.path.append("..")
import simplegui
import random as rand

WIDTH = 800
HEIGHT = 100
#numbers in range [0,8)
deck_part1 = ['0', '1', '2', '3', '4', '5', '6', '7']
deck_part2 = ['0', '1', '2', '3', '4', '5', '6', '7']
deck_cards = deck_part1 + deck_part2
card_color = ["white" for card in deck_cards]
card_size = [50, 100]
exposed = [False for card in deck_cards]
state = 0
turn = 0
index_card1 = 0
index_card2 = 0

# helper function to initialize globals

def shuffle_deck():
    rand.shuffle(deck_cards)
    
def new_game():
    global exposed, state, turn, card_color
    shuffle_deck()
    exposed = [False for card in deck_cards]
    state = 0
    turn = 0
    l_turn.set_text("Turns = " + str(turn))
    card_color = ["white" for card in deck_cards]

def is_exposed(index):
    return exposed[index]

def expose_card(index):
    exposed[index] = True

def hide_card(index):
    exposed[index] = False

def get_card(index):
    return deck_cards[index]

def change_color(index):
    card_color[index] = "green"
     
# define event handlers
def mouseclick(pos):
    global state, turn, index_card1, index_card2
    # add game state logic here
    index = 0
    minx = 0
    maxx = card_size[0]
    posx = pos[0]
    
    while(maxx < WIDTH):
        if(minx < posx < maxx):
            break   
        index += 1
        minx, maxx = maxx, maxx + card_size[0]
   
    if(not is_exposed(index)):
        expose_card(index)
        if state == 0:
            #firt flipped card
            index_card1 = index
            state = 1
        elif state == 1:
            #second flipped card
            index_card2 = index
            state = 2
            turn += 1
            l_turn.set_text("Turns = " + str(turn))
        else:
            #state 2, we have two fliped cards
            card1 = get_card(index_card1)
            card2 = get_card(index_card2)
            if(card1 != card2):
                hide_card(index_card1)
                hide_card(index_card2)
            else:
                #the cards are equals
                change_color(index_card1)
                change_color(index_card2)
            index_card1 = index
            state = 1
    
# cards are logically 50x100 pixels in size    
def draw(c):
    cordx = 10
    cardx = 0
    if(False in exposed):
        for ind in range(len(deck_cards)):
            card = deck_cards[ind]
            if(is_exposed(ind)):
                c.draw_text(card, [cordx, card_size[1]], 60, card_color[ind])
            cordx += card_size[0]
            cardx += card_size[0]
            c.draw_line([cardx, 0], [cardx, card_size[1]], 1, "white")
    else:
        c.draw_text("Congratulations you win !!, click reset to play again", [0, 50], 20, "white")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
l_turn = frame.add_label("Turns = " + str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
