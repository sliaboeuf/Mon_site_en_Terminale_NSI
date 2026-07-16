---
password: "corr_Présentation_projet"
---

# <center><div class = "titre3"> Correction du mini-projet </div></center>
<div class = "list2_1" markdown="1">

1. Une proposition de code :
```python
def type_parametre(text):
    return str(type(text))

def presence_3_chiffres_min(text):
    lst = [str(i) for i in range(10)]
    nb = 0
    for elt in text:
        if elt in lst:
            nb += 1
    return nb >= 3

def presence_maj(text):
    nb = 0
    for elt in text:
        if elt == elt.upper():
            nb += 1
    return nb > 0

def nb_caract_speciaux(text):
    lst = ['#', '@', '|', '~', '§']
    nb = 0
    for elt in text:
        if elt in lst:
            nb += 1
    return nb

def presence_8_caract_min(text):
    return len(text) >= 8
```

</div>
<div class = "list2_2" markdown="1">

2. Avec le jeu de tests suivant :
```python
import unittest
class TestFonctions(unittest.TestCase):
    
    def test_type_parametre(self):
        self.assertEqual(type_parametre("123"),"<class 'str'>")
        self.assertEqual(type_parametre(123),"<class 'int'>")
        self.assertEqual(type_parametre(12.3),"<class 'float'>")
        self.assertEqual(type_parametre(1==2),"<class 'bool'>")
    
    def test_presence_3_chiffres_min(self):
        self.assertTrue(presence_3_chiffres_min("1234"))
        self.assertTrue(presence_3_chiffres_min("123"))
        self.assertFalse(presence_3_chiffres_min("12a"))
        self.assertFalse(presence_3_chiffres_min(""))
        self.assertTrue(presence_3_chiffres_min("a234"))
    
    def test_presence_maj(self):
        self.assertTrue(presence_maj("A"))
        self.assertFalse(presence_maj("a"))
        self.assertFalse(presence_maj("1"))
        self.assertFalse(presence_maj("@"))
    
    def test_nb_caract_speciaux(self):
        self.assertEqual(nb_caract_speciaux("12-"),0)
        self.assertEqual(nb_caract_speciaux("#a"),1)
        self.assertEqual(nb_caract_speciaux("#@|~§"),5)
    
    def testpresence8CaractMin(self):
        self.assertTrue(presence_8_caract_min("12345678"))
        self.assertFalse(presence_8_caract_min("#a"))
    

unittest.main()
```
... on obtient 2 erreurs qui concernent la fonction `#!python presence_maj`.
```pycon
...F.
======================================================================
FAIL: test_presence_maj(__main__.TestFonctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<tmp 1>", line 49, in test_presence_maj
    self.assertFalse(presence_maj("1"))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 5 tests in 0.085s

FAILED (failures=1)
```
Et celle-ci :
```pycon
...F.
======================================================================
FAIL: test_presence_maj(__main__.TestFonctions)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "<tmp 1>", line 50, in test_presence_maj
    self.assertFalse(presence_maj("@"))
AssertionError: True is not false

----------------------------------------------------------------------
Ran 5 tests in 0.148s

FAILED (failures=1)
```
3. On peut proposer cette solution :
```python
def presence_maj(text):
    nb = 0
    maj_autorisees = [chr(i) for i in range(65, 91)]  + ['À', 'Â', 'Ä', 'Ç', 'É', 'È', 'Ê', 'Ë', 'Î', 'Ï', 'Ô', 'Ö', 'Ù', 'Û','Ü', 'Æ', 'Œ']
    for elt in text:
        if elt in maj_autorisees:
            nb += 1
    return nb > 0
```
4.  
```python
def test_MDP(text):
    return type_parametre(text) == "<class 'str'>" and presence_3_chiffres_min(text) and presence_maj(text) and nb_caract_speciaux(text) >= 2 and presence_8_caract_min(text)
```

</div>
