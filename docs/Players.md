<!-- markdownlint-disable -->

<a href="..\blackJack\Players.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Players`






---

<a href="..\blackJack\Players.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Player`
Object representing a player playing against the dealer. 

Player(pos=None: int, window=None: widget, **kwargs) 

<a href="..\blackJack\Players.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(pos=None, window=None, **kwargs)
```

Player Constructor Function. 



**Args:**
 
 - <b>`pos`</b> (int):  players position at table. 
 - <b>`window`</b> (Window):  The program's main window. 
 - <b>`**kwargs`</b>:  arbitrary keyword arguements. 


---

#### <kbd>property</kbd> score

Total points from sum of card values in hand. 



**Returns:**
 
 - <b>`int`</b>:  sum of the cards in players hand. 



---

<a href="..\blackJack\Players.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_card`

```python
add_card(card)
```

Add a Card object to Players hand. 

Takes a card just poped off Deck by dealer and includes it in hand. 



**Args:**
 
 - <b>`card`</b> (Card):  Card object popped off deck 

---

<a href="..\blackJack\Players.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `isturn`

```python
isturn()
```

Return True or False. 

Called by dealer and Window Buttons to check who's turn it is. 



**Returns:**
 
 - <b>`bool`</b>:  true if it is players turn else false. 

---

<a href="..\blackJack\Players.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `output`

```python
output(line)
```

Write output to QTextBrowserWidgit. 

Simple way to keep track of previous hands and cards already dealt by dealer. 



**Args:**
 
 - <b>`line`</b> (str):  Content to print to window. 

---

<a href="..\blackJack\Players.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_hand`

```python
show_hand()
```

Wtites logs details about the score and cards in players hand. 

---

<a href="..\blackJack\Players.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_score`

```python
show_score(score)
```

Write players score to the QTextBrowser Widgit. 



**Args:**
 
 - <b>`score`</b> (int):  self.score 

---

<a href="..\blackJack\Players.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `turn`

```python
turn()
```

Call at the beginning and end of players turn. 


---

<a href="..\blackJack\Players.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Dealer`
Dealer Object. Controls most aspects of the game. 

Subclass of Player but requires a few extra keyword args 

<a href="..\blackJack\Players.py#L134"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(decks=1, players=2, driver=None, **kwargs)
```

Dealer constructor. 



**Args:**
 
 - <b>`decks`</b> (int, optional):  Number of decks to use. 
 - <b>`players`</b> (int, optional):  Total players in game. 


---

#### <kbd>property</kbd> decksize

Count of cards in the current deck. 



**Returns:**
 
 - <b>`int`</b>:  Total number of cards in the deck. 

---

#### <kbd>property</kbd> score

Score overloaded function from Player Class. 



**Returns:**
 
 - <b>`int`</b>:  Dealers score 



---

<a href="..\blackJack\Players.py#L189"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_card`

```python
add_card(card)
```

Overload method from player class. 



**Args:**
 
 - <b>`card`</b> (Card):  adds card just pooped from deck to hand. 

---

<a href="..\blackJack\Players.py#L272"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `add_players`

```python
add_players()
```

Part of the constructor. 

Initializes a new players according to num_players attribute and creates their GUI representation. 

---

<a href="..\blackJack\Players.py#L206"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deal_card`

```python
deal_card(player)
```

Retreive card from top of deck and deals to player. 



**Args:**
 
 - <b>`player`</b> (Player):  instance of Player in game 

---

<a href="..\blackJack\Players.py#L226"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `dealer_round`

```python
dealer_round()
```

Call when all other players have had their turn betting. 

---

<a href="..\blackJack\Players.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `isturn`

```python
isturn()
```

Return True or False. 

Called by dealer and Window Buttons to check who's turn it is. 



**Returns:**
 
 - <b>`bool`</b>:  true if it is players turn else false. 

---

<a href="..\blackJack\Players.py#L262"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `new_game`

```python
new_game()
```

Call after dealer has played their turn. 

---

<a href="..\blackJack\Players.py#L253"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `next_player`

```python
next_player()
```

Call when previous players turn ended. 

---

<a href="..\blackJack\Players.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `output`

```python
output(line)
```

Write output to QTextBrowserWidgit. 

Simple way to keep track of previous hands and cards already dealt by dealer. 



**Args:**
 
 - <b>`line`</b> (str):  Content to print to window. 

---

<a href="..\blackJack\Players.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `player_hit`

```python
player_hit(player)
```

Call when Player asks dealer to "hit". 



**Args:**
  Player (Player) the player whos turn it is. 

---

<a href="..\blackJack\Players.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `round`

```python
round()
```

Begin new players turn for betting, hitting or staying. 

---

<a href="..\blackJack\Players.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setPreferences`

```python
setPreferences(decks=None, players=None)
```

Set preferences for the next game. 



**Args:**
 
 - <b>`decks`</b> (int, optional):  Number of decks. Defaults to None. 
 - <b>`players`</b> (int, optional):  Number of players. Defaults to None. 

---

<a href="..\blackJack\Players.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_hand`

```python
show_hand()
```

Wtites logs details about the score and cards in players hand. 

---

<a href="..\blackJack\Players.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show_score`

```python
show_score(score)
```

Write players score to the QTextBrowser Widgit. 



**Args:**
 
 - <b>`score`</b> (int):  self.score 

---

<a href="..\blackJack\Players.py#L199"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start_deal`

```python
start_deal()
```

Initialize deal sequence of 2 cards to each player. 

---

<a href="..\blackJack\Players.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `turn`

```python
turn()
```

Call at the beginning and end of players turn. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
