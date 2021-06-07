<!-- markdownlint-disable -->

<a href="..\blackJack\MenuBar.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `MenuBar`






---

<a href="..\blackJack\MenuBar.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MenuBar`
QMenuBar instance for main window menubar. 

Assigns object instance to as QMainWindow Menubar and creates File and Settings submenu. 

<a href="..\blackJack\MenuBar.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, window=None)
```

Construct MenuBar instance and create submenus. 



**Args:**
  parent (widget, optional) Objects parent widget. Defaults to None.  window (widget, optional) Program's main window. Defaults to None. 




---

<a href="..\blackJack\MenuBar.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `about`

```python
about()
```

Display Program Information. 

---

<a href="..\blackJack\MenuBar.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `aboutQtMenu`

```python
aboutQtMenu()
```

Display Qt Information. 

---

<a href="..\blackJack\MenuBar.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `exit_app`

```python
exit_app()
```

Quit program. 

---

<a href="..\blackJack\MenuBar.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `maxamizeWindow`

```python
maxamizeWindow()
```

Set Window to fill screen. 

---

<a href="..\blackJack\MenuBar.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `minimizeWindow`

```python
minimizeWindow()
```

Set window to hide. 

---

<a href="..\blackJack\MenuBar.py#L104"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `newGame`

```python
newGame()
```

Start New Game. 

Same as pressing NewGameButton. 

---

<a href="..\blackJack\MenuBar.py#L111"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `open_settings`

```python
open_settings()
```

Create a QDialog with editable options related to gameplay. 

Options include: Number of players, Number of Decks. 


---

<a href="..\blackJack\MenuBar.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `About`
Dialog with information about the Program. 

<a href="..\blackJack\MenuBar.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, window=None)
```

Construct Dialog Box. 



**Args:**
  parent (QWidget, optional) Parent widget object. Defaults to None.  window (QWidget, optional) Program's MainWindow. Defaults to None. 




---

<a href="..\blackJack\MenuBar.py#L173"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `okbutton`

```python
okbutton()
```

Close Window. 


---

<a href="..\blackJack\MenuBar.py#L178"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Settings`
Open new window with editable options that effect gameplay. 

<a href="..\blackJack\MenuBar.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(parent=None, window=None)
```

Construct Settings Dialog. 



**Args:**
  parent (QWidget, optional) Parent widget object. Defaults to None.  window (QWidget, optional) Program's MainWindow. Defaults to None. 




---

<a href="..\blackJack\MenuBar.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `accept`

```python
accept()
```

Close Window. 

---

<a href="..\blackJack\MenuBar.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `finishedSignal`

```python
finishedSignal()
```

When Settings Window returns accept or reject signals. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
