# Blackjack Outline #

- Card class
    1 get image path function
    2 get value

--------------------

- Deck class
    1 number of decks * 52
    2 shuffle cards
    3 pop card off deck

--------------------

- Player class
    1 is turn function
    2 hand = list if card values
    3 score = sum of hand
    4 add card function
    5 set turn function

--------------------

- Window class
    1 Main window
    2 player groupboxes
    3 card images
    4 score box
    5 output window
    6 deck count
    7 card count
    8 hit, stand, new game buttons
    9 next round button

--------------------

- Dealer class
    1 Player subclass
    2 deal card to player
    3 deal card to self
    4 round table for hit or stay
    5 if hand > 15 deal self
    6 if player or self break = lose
    7 highest score under 22 wins
