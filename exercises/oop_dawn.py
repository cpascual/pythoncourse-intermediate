class MyCollaborator(......)
    ...



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
