

# OOP exercise 1: add eval history to oop_dawn.Collaborator

oop_dawn.Collaborator stores the evaluation points in an attribute "evaluation". 

But two consecutive calls of Boss.evaluate(c) result in the first value to be overwritten.

Create  a new class MyCollaborator(Collaborator)
which has an attribute `evaluations` that stores ALL the evaluations (a list)

The following code must work:


```
c = MyCollaborator("pepe")
boss = Boss("Jefez")

assert(issubclass(MyCollaborator, Collaborator))

assert(c.evaluation == None)
assert(len(c.evaluations) == 0)

boss.evaluate(c)
print c.evaluations
assert(len(c.evaluations) == 1)
assert(c.evaluations[-1] == c.evaluation)

boss.evaluate(c)
print c.evaluations
assert(len(c.evaluations) == 2)
assert(c.evaluations[-1] == c.evaluation)
```

# OOP exercise 2: modify the `Collaborator` class to be print-friendly

Right now, a print on a collaborator is not very user-friendly:

```
In [1]: import oop_dawn

In [2]: c = oop_dawn.Collaborator('Mindundez')

In [3]: print c
<oop_dawn.Collaborator object at 0x7f3427601ed0>
```

Make make it so that the following test passes:

```
c1 = Collaborator('Mindundez')
c2 = Boss('Jefez')
c3 = SuperBoss('Juan Bueno')

assert(str(c1) == "Mindundez:Collaborator")
assert(str(c2) == "Jefez:Boss")
assert(str(c3) == "Juan Bueno:SuperBoss")
```

Note: you may find the [docs of the special methods](https://docs.python.org/2/reference/datamodel.html#special-method-names
) interesting:

# OOP exercise 3: Create a class `Staff`

Implement the `Staff` class missing in [staff.py]() so that it passes the tests and conforms to the docs

**Try not to look at the exercises.cheat.oop_dawn_cheat module!!**



