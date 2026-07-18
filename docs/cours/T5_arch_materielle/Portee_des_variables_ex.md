# <center><div class = "titre2"> Exercices sur la portée des variables</div></center>

### <div class = "encadré_exo"> __Exercice 1__ </div>
On considère le script Python suivant : 

```python
def f():
    global a
    a = a + 1
    c = 2 * a
    return a + b + c

a = 3
b = 4
c = 5
print(f())
print(a)
print(b)
print(c)

```

- [ ] Quelles sont les variables locales et globales de la fonction `f` ?
- [ ] Qu’affiche ce programme ?

<center markdown="1">
[Correction de l'exercice 1 :material-cursor-default-click:](Portee_des_variables_corr_ex.md#correction-de-lexercice-1){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 2__ </div>
On considère les deux scripts Python suivants : 

=== "Script 1"
	```python
	def f(x):
	    global b
	    b = 10
	    return x + 1

	a = 3
	b = 4
	print(b + f(a) + b)

	```

=== "Script 2"
	```python
	def f(x):
	    b = 10
	    return x + 1

	a = 3
	b = 4
	print(b + f(a) + b)

	```

- [ ] Vont-ils afficher le même résultat ? Pourquoi ?

<center markdown="1">
[Correction de l'exercice 2 :material-cursor-default-click:](Portee_des_variables_corr_ex.md#correction-de-lexercice-2){:target="_blank" .md-button}
</center>

### <div class = "encadré_exo"> __Exercice 3__ </div>
On considère le script Python suivant : 

```python
def g(x):
    global v 
    v = 1000
    return 2 * x

def f(x):
    v = 1
    return g(x) + v 

a = 3
print(f(6) + v + a)

```

- [ ] Qu’affiche ce programme ? Pourquoi ?

<center markdown="1">
[Correction de l'exercice 3 :material-cursor-default-click:](Portee_des_variables_corr_ex.md#correction-de-lexercice-3){:target="_blank" .md-button}
</center>
