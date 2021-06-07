<!-- markdownlint-disable -->

<a href="..\blackJack\Deck.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Deck`






---

<a href="..\blackJack\Deck.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `InvalidType`
Exception Class for Invalid type comparison. 

<a href="..\blackJack\Deck.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(other)
```

Initialize Exception. 





---

<a href="..\blackJack\Deck.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DeckEmpty`
Deck Empty when no more cards in deck to deal. 





---

<a href="..\blackJack\Deck.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Deck`
Deck of cards. 

Subclass of list object representing a deck of cards. 

<a href="..\blackJack\Deck.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(cls, *args, **kwargs)
```

Create Deck Object. 

List of 52 Card objects based on deck of playing cards. 




---

<a href="..\blackJack\Deck.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `pop`

```python
pop(x=0)
```

Remove 1 card from deck at index `x`. 


- Args: x (int, optional): index. Defaults to 0. 
- Raises: DeckEmpty: when no cards left 
- Returns: Card object: removed card. 

---

<a href="..\blackJack\Deck.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `shuffle`

```python
shuffle(t=8)
```

Shuffle Cards in deck. 

Args: t (int, optional): number of times to shuffle the deck 

---

<a href="..\blackJack\Deck.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `swap`

```python
swap(i1, i2)
```

Swap utility for shuffling deck. 



**Args:**
 
 - <b>`i1`</b> (Card):  first card for swapping 
 - <b>`i2`</b> (Card):  next card to be swapped with first 

---

<a href="..\blackJack\Deck.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `times`

```python
times(num)
```

Class method constructor for creating multiple decks. 

Returns: Deck object * number of decks. 


---

<a href="..\blackJack\Deck.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Card`
Card Object == contents of Deck Object. 

<a href="..\blackJack\Deck.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(suit, name, value)
```

Construct instance of Card Objects. 

suit (str): name of suit e.g. Diamonds Hearts name (str): name of card e.g. King 7 Ace value (int): Point value in blackjackicon 




---

<a href="..\blackJack\Deck.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `getPath`

```python
getPath()
```

Get path retreives filesystem location for card. 

str: absolute path to image file 

---

<a href="..\blackJack\Deck.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ismatch`

```python
ismatch(other)
```

Suit matches other suit. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
