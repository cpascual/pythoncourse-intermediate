# Course Summary

## Day 1:
- We looked at the [Basic OOP Tutorial] examplesto introduce basic concepts such as:
  - classes, objects, instances
  - initialization, `self`
  - static methods
- We wrote [oop_inheritance](class_examples/oop_inheritance.py) to play with inheritance (and multiple inheritance)
  - inheritance

- We used [oop_dawn.py] to dive deeper all previous OOP concepts and to introduce setter/getters and properties.
We created [class_examples/oop_dawn2.py](class_examples/oop_dawn2.py) to understand the properties.

- I proposed exercise 1 of [exercises/oop_dawn_exercises.md](/exercises/oop_dawn_exercises.md)

## Day 2

- We finish exercise 1 of [oop_dawn_exercises.md](/exercises/oop_dawn_exercises.md)
- We introduce ["special methods"](https://docs.python.org/2/reference/datamodel.html#special-method-names)
  and do exercise2 of [exercises/oop_dawn_exercises.md](/exercises/oop_dawn_exercises.md)
- We work on exercise3 [exercises/oop_dawn_exercises.md](/exercises/oop_dawn_exercises.md) and discuss the
  [Inheritance vs composition patterns in OOP](https://en.wikipedia.org/wiki/Composition_over_inheritance)
- We introduce concepts such as [Duck Typing](https://en.wikipedia.org/wiki/Duck_typing#In_Python) and
  [Monkey Patching](http://stackoverflow.com/a/5626250) and then sum up OOP concepts by studying the full
  implementation of [oop_dawn_cheat](/exercises/cheat/oop_dawn_cheat.py).
- We introduce Qt and PyQt, and, specifically, we discuss:
  - how to use the PyQt4 and Qt documentation
  - Relations vs Qt, PyQt and PySide
  - PyQt4 architecture overview (submodules and class organization)
  - Qt parenting relations
  - Qt signals (mentioning old-style signals and focusing on new-style signals)
  - Qt Event loop
  - Work on understanding the simplest PyQt4 examples [qtexample01](qtexample01.py) and [qtexample02](qtexample02.py)

## Day 3

(TODO)
- Introduce Layouts
- Do qtexercise01
- Introduce Qt Designer
- Mention PyUic and Introduce [uiload](/exercises/uiload.py) module
- Do qtexercise02
- Mention various Qt widgets/mechanism:
  - QTimer and QTimer.singleShot
  - Qt's Model-View mechanism
  - discuss QThread, QFile, VS their python standard library alternatives

## Day 4
- Introduce Taurus
- Explain Taurus Model-View architecture (schemes, ...)
- Do taurusexercise01 (Create a new compsite widget that uses uses Taurus)
- Introduce TaurusBaseComponent as a way to create new Taurus widgets/objects (handleEvent, etc)


# Resources

## Basic OOP

- [Basic OOP Tutorial]

## Basic Qt

Useful resources:

- [Tutorial](http://zetcode.com/gui/pyqt4/)
- PyQt4 Docs:
  - http://pyqt.sourceforge.net/Docs/PyQt4/introduction.html
  - http://pyqt.sourceforge.net/Docs/PyQt4/classes.html
- Note: the C++ Qt class reference can be more usable than the PyQt4 one:
  - http://doc.qt.io/qt-4.8/classes.html



[Basic OOP Tutorial]: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
