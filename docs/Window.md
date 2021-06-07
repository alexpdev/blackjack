<!-- markdownlint-disable -->

<a href="..\blackJack\Window.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Window`






---

<a href="..\blackJack\Window.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Window`
Window MainWindow for Blackjack UI. 



**Args:**
 
 - <b>`QMainWindow`</b> (Qt Widget Window):  MainWindow 

<a href="..\blackJack\Window.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, players=None, decks=None, app=None)
```

Window Constructor. 



**Args:**
 
 - <b>`parent`</b> (QWidget, optional):  parent widget. Defaults to None. 
 - <b>`players`</b> (list, optional):  list of players. Defaults to None. 
 - <b>`decks`</b> (number of decks):  this number * 52 Cards. Defaults to None. 
 - <b>`app`</b> (QApplication, optional):  Main Application. Defaults to None. 




---

<a href="..\blackJack\Window.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `addPlayer`

```python
addPlayer(player)
```

Add Player construct groupbox for each player. 



**Args:**
 
 - <b>`Player`</b> (Player):  One of the Dealers challengers. 

---

<a href="..\blackJack\Window.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clearPlayers`

```python
clearPlayers()
```

Clear Players Clear out old players groupbox for new players. 

---

<a href="..\blackJack\Window.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `playerBroke`

```python
playerBroke(player, score)
```

Show and alert box to user when they break 21. 



**Args:**
 
 - <b>`player`</b> (Player):  The player who broke 21 
 - <b>`score`</b> (int):  The score. Will be over 21 

---

<a href="..\blackJack\Window.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setDealer`

```python
setDealer(dealer)
```

Set Dealer Assign a dealer to the window. 



**Args:**
 
 - <b>`dealer`</b> (Dealer):  Subclass of Player with more responsibility.  performs all dealing cards and shuffling. 


---

<a href="..\blackJack\Window.py#L179"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `HitButton`
Hit Button triggered by player wants to be dealt another card. 



**Args:**
 
 - <b>`QPushButton`</b> (ButtonWidget):  Ask dealer for one more card. 

<a href="..\blackJack\Window.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, window=None)
```

Construct HitButton Object. 



**Args:**
 
 - <b>`parent`</b> (Window, optional):  mainwindow. Defaults to None. 
 - <b>`window`</b> (Window, optional):  mainwindow. Defaults to None. 




---

<a href="..\blackJack\Window.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `hit`

```python
hit()
```

Ask dealer for another card. 


---

<a href="..\blackJack\Window.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `StandButton`
Stand Button is for players who want their turn to be over. 



**Args:**
  QPushButton (ButtonWidget)  Tell dealer no more cards and allow next player to take turn. 

<a href="..\blackJack\Window.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, window=None)
```

Construct Stay Button. 



**Args:**
 
 - <b>`parent`</b> (Window, optional):  mainwindow. Defaults to None. 
 - <b>`window`</b> (Window, optional):  mainwindow. Defaults to None. 




---

<a href="..\blackJack\Window.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `stay`

```python
stay()
```

Stay function. 


---

<a href="..\blackJack\Window.py#L256"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `NewGameButton`
New Game Button. 

<a href="..\blackJack\Window.py#L268"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, window=None)
```

Construct for NewGameButton. 



**Args:**
 
 - <b>`parent`</b> (Window, optional):  mainwindow. Defaults to None. 
 - <b>`window`</b> (Window, optional):  mainwindow. Defaults to None. 




---

<a href="..\blackJack\Window.py#L282"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `start_new_game`

```python
start_new_game()
```

Start new game function. 

Sets score to zero, and starts a new game. 


---

<a href="..\blackJack\Window.py#L301"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BrokeDialog`
BrokeDialog box to show player if their score is over 21. 



**Args:**
 
 - <b>`QMessageBox`</b> (Window):  Alerts the user they lost. 

<a href="..\blackJack\Window.py#L309"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, player=None, score=None)
```

Construct for the Alert box. 



**Args:**
 
 - <b>`parent`</b> (Widget, optional):  parent window. Defaults to None. 
 - <b>`player`</b> (player, optional):  players title. Defaults to None. 
 - <b>`score`</b> (int, optional):  players score. Defaults to None. 







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
