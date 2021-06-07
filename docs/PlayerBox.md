<!-- markdownlint-disable -->

<a href="..\blackJack\PlayerBox.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `PlayerBox`






---

<a href="..\blackJack\PlayerBox.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PlayerBox`
PlayerBox Subclass of QGroupBox. 

Returns GroupBoxWidget data and cards for each player. 

<a href="..\blackJack\PlayerBox.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(title, parent=None, player=None)
```

Construct a PlayerBox Widget. 



**Args:**
  parent (QWidget, optional) Parent widget object. Defaults to None.  player (Player) The player this box will be assigned to. 


---

#### <kbd>property</kbd> cardCount

Count cards in players hand. 



**Returns:**
 
 - <b>`int`</b>:  Total number of cards in players hand. 

---

#### <kbd>property</kbd> cards

Shortcut method accessing players cards property. 



**Returns:**
 
 - <b>`list`</b>:  A list of cards stored in players hand. 



---

<a href="..\blackJack\PlayerBox.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `addCard`

```python
addCard(card)
```

Shortcut for adding card widget to players list of cards. 

---

<a href="..\blackJack\PlayerBox.py#L151"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `addWidget`

```python
addWidget(card)
```

Add another card to Window. 

---

<a href="..\blackJack\PlayerBox.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `deleteCard`

```python
deleteCard()
```

Remove card from Players list of cards property. 

---

<a href="..\blackJack\PlayerBox.py#L161"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `isTurn`

```python
isTurn()
```

Return True if currently players turn. 



**Returns:**
 
 - <b>`bool`</b>:  True if it's players turn else false. 

---

<a href="..\blackJack\PlayerBox.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset()
```

Clear PlayerBox of all widgets. 

Called when current round ends and new deal begins. 

---

<a href="..\blackJack\PlayerBox.py#L169"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `turn`

```python
turn()
```

Flip `self.turn` property False or True. 

Changes the style of PlayerBox to indicate if it is or isn't currently players turn. 


---

<a href="..\blackJack\PlayerBox.py#L183"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CardWidget`
Store the image of the card it represents for GUI display. 

QLabel (QPixmap) Either a specific card or back of card if it is facedown. 

<a href="..\blackJack\PlayerBox.py#L196"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, card=None, cover=True, path=None)
```

Construct new CardWidget instance. 

parent (QWidget, optional): parent widget for CardWidget. card (Card, optional): Card object. Defaults to None. cover (bool, optional): If True use Cardcoverpath else use give path. path (str, optional): path to Pixmap Image. Defaults to CARDCOVER. 




---

<a href="..\blackJack\PlayerBox.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `faceDown`

```python
faceDown()
```

Call to hide value of dealers facedown card. 

---

<a href="..\blackJack\PlayerBox.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `faceUp`

```python
faceUp()
```

Flip a facedown card to up position. 

---

<a href="..\blackJack\PlayerBox.py#L222"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setCard`

```python
setCard(card)
```

Assign Card objrct to a CardWidget. 

Args: card (Card object) 

---

<a href="..\blackJack\PlayerBox.py#L232"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setImage`

```python
setImage()
```

Assign image path as pixmap. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
