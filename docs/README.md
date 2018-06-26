# Course Summary

## Day 1:
- We look at the [Basic OOP Tutorial] examples to introduce basic concepts such as:
  - classes, objects, instances
  - initialization, `self`
  - static methods
- We write [oop_inheritance](class_examples/oop_inheritance.py) to play with inheritance (and multiple inheritance)
  - inheritance

- We use [oop_dawn.py] to dive deeper at all previous OOP concepts and to introduce setter/getters and properties.
We create [class_examples/oop_dawn2.py](class_examples/oop_dawn2.py) to understand the properties.

- I propose [exercise](/exercises) OOP-1

## Day 2

- We finish [exercise](/exercises) OOP-1
- We introduce ["special methods"](https://docs.python.org/2/reference/datamodel.html#special-method-names)
  and do [exercise](/exercises) OOP-2
- We work on [exercise](/exercises) OOP-3 and discuss the
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
  - the simplest PyQt4 examples [qtexample01](qtexample01.py) and [qtexample02](qtexample02.py)

## Day 3

- We Introduce Layouts
- We Do [exercise](/exercises) Qt-1
- We Introduce [Qt Designer](http://doc.qt.io/qt-4.8/designer-manual.html) 
- We Mention PyUic and Introduce [`PyQt.uic.loadUi()`](http://pyqt.sourceforge.net/Docs/PyQt4/designer.html#the-uic-module) for dynamic UI loading.
- We Do [exercise](/exercises) Qt-2
- We Mention QTimer and QTimer.singleShot

We ran out of time for discussing:
  - Qt's Model-View mechanism
  - discuss QThread, QFile, VS their python standard library alternatives

## Day 4

- Introduce [Taurus](https://www.taurus-scada.org)
- Explain Taurus Model-View architecture (schemes, ...)
- Do taurusexercise01 (Create a new composite widget that uses Taurus)
- Introduce TaurusBaseComponent as a way to create new Taurus widgets/objects (handleEvent, etc)


# Resources

## Basic OOP

- [Basic OOP Tutorial]

## Basic Qt

Useful resources:

- [Qt Tutorial](http://zetcode.com/gui/pyqt4/)
- PyQt4 Docs:
  - http://pyqt.sourceforge.net/Docs/PyQt4/introduction.html
  - http://pyqt.sourceforge.net/Docs/PyQt4/classes.html
- Note: the C++ Qt class reference can be more usable than the PyQt4 one:
  - http://doc.qt.io/qt-4.8/classes.html
- [Qt Designer Manual](http://doc.qt.io/qt-4.8/designer-manual.html) 

## Taurus

- [Taurus main page](https://www.taurus-scada.org)
- [Slides of TangoMeeting2016](TaurusStatus-TangoMeeting201606-v7.pdf)
- [Slides of ICALEPCS2015](THHC3O03_talk.pdf)

[Basic OOP Tutorial]: https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
