# Course Summary


## Day 1:

### Environment preparation
- We assume that you already did the [pre-course installation](https://git.cells.es/cpascual/pythoncourse-intro/blob/master/pre-course.md)
- Connect to your machine
- Check that the environment is working.
  - windows: Anaconda prompt -> `conda activate course`
  - linux: `source ~/miniconda/bin/activate course`
- Fork the [official repo](https://git.cells.es/<YOURUSERNAME>/pythoncourse-intermediate)
- Clone from fork  `git clone https://git.cells.es/<YOURUSERNAME>/pythoncourse-intermediate.git`
- Add official remote: `git remote add official https://git.cells.es/cpascual/pythoncourse-intermediate.git`
- PyCharm: create a PyCharm project from the local repo
  - use conda course environment as the interpreter for the project
  - check that the `Settings-> editor-> inspections-> code compatibility inspections` is set to 2.7, 3.5 and 3.6
- PyCharm quick demo and configuration:
  - Show the Structure view (`View menu -> toolWindows-> Structure`). Suggest: `gear icon -> move -> right`
  - Scratch files: `File -> New Scratch File`
  - Double click on tab to disable/reenable docked panels
  - Live templates: e.g. create main section with `CTRL+J` + "ma..." 
  - Autocompletion: type `im`...`ENTER`...`pyqt`...`ENTER` to get `import pyqtgraph`
  - Check git menu (bottom right). It should show the origin and official 
    remotes and their branches
  - ...

### lessons start
- [Basic OOP Tutorial] examples to introduce basic concepts such as:
  - classes, objects, instances
  - initialization, `self`
  - static methods
- Write [oop_inheritance](class_examples/oop_inheritance.py) to play with inheritance (and multiple inheritance)
  - inheritance

- Use [oop_dawn.py](oop_dawn.py) to introduce:
  - setter/getters 
  - properties in function and simple decorator mode (play with[class_examples/oop_dawn2.py](class_examples/oop_dawn2.py))

- Homework: [exercise](/exercises/) OOP-1

## Day 2

- Finish [exercise](/exercises) OOP-1
- Introduce ["special methods"](https://docs.python.org/2/reference/datamodel.html#special-method-names). 
  - as an example,implement a Vector (TODO ... inherit from list, reimplement add and sub)
  - [exercise](/exercises) OOP-2
- Look at [exercise](/exercises) OOP-3
- Introduce [Inheritance vs composition patterns in OOP](https://en.wikipedia.org/wiki/Composition_over_inheritance)
- Introduce [Duck Typing](https://en.wikipedia.org/wiki/Duck_typing#In_Python)
- Introduce [Monkey Patching](http://stackoverflow.com/a/5626250) 
- OOP concepts by studying the full implementation of [oop_dawn_cheat](/exercises/cheat/oop_dawn_cheat.py).
- Introduce Qt and PyQt, and, specifically, we discuss:
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
