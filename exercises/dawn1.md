

# OOP exercise 1: add eval history to oop_dawn.Collaborator

oop_dawn.Collaborator stores the evaluation points in an attribute "evaluation". 

But two consecutive calls of Boss.evaluate(c) result in the first value to be overwritten.

Create  a new class MyCollaborator(Collaborator)
which has an attribute "evaluations" that stores ALL the evaluations (a list)

The following code must work:


```
c = MyCollaborator("pepe")
boss = Boss()
boss.evaluate(c)
print c.evaluations
boss.evaluate(c)
print c.evaluations
assert(len(c.evaluations) == 2)
assert(c.evaluations[-1] == c.evaluation)
```
