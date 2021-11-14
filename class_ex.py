>>> class student(object):
	name='Gopi Raj'
	pass

>>> s=student()

>>> s.name
'Gopi Raj'

>>> class student():
	def __init__(self):
		self.name=''
		self.age=0

		
>>> s=student()

>>> s.age
0

>>> s.name
''

>>> student()
<__main__.student object at 0x00000211F02EBB20>


>>> s.age=21

>>> s.name='sathish kumar'

>>> s.name
'sathish kumar'

>>> s.age
21

>>> d=student()

>>> d.name
''
>>> d.age
0
>>> #  passing instence attribute values in constructor

>>> class student():
	clsAttr='gugai hr sec school' #  this is class attribute
	name='gopiraj'
	def demo(self):
		print('hello world')

		
>>> s=student()

>>> s.name
'gopiraj'

>>> s.demo

<bound method student.demo of <__main__.student object at 0x00000211F02EBA90>>

>>> s.demo()
hello world

>>> class student():
	clsAttr='gugai hr sec school' #  this is class attribute
	name='gopiraj'
	def demo(self):
		print('hello world',self.name)

		
>>> s=student()

>>> s.demo
<bound method student.demo of <__main__.student object at 0x00000211F02EBD90>>

>>> s.demo()
hello world gopiraj

>>> s.clsAttr
'gugai hr sec school'

>>> s.name
'gopiraj'


>>> s.clsAttr='Gugai Hr Sec School'

>>> s.demo()
hello world gopiraj

>>> s.name
'gopiraj'

>>> s.clsAttr
'Gugai Hr Sec School'

>>> s.name='Sathish Kumar'

>>> s.clsAttr
'Gugai Hr Sec School'

>>> s.demo()
hello world Sathish Kumar

>>> d=student()

>>> d.clsAttr
'gugai hr sec school'


>>> d.demo()
hello world gopiraj

>>> d.name
'gopiraj'

>>> s.name
'Sathish Kumar'

>>> #-----------------------


>>> class student(object):
	school=''
	name=''
	age=0
	def pri(self):
		print('hellow ',self.school,'and his age ',self.age)

		
>>> s=student()

>>> s.age
0

>>> s.name
''

>>> s.school
''

>>> s.pri()
hellow   and his age  0

>>> s.name='gopiraj'

>>> s.age=21


>>> s.school='Gugai Hr Sec School'


>>> s.pri()
hellow  Gugai Hr Sec School and his age  21

>>> class student(object):
	school=''
	name=''
	age=0
	def pri(self):
		print('hellow ',self.name,'and his age ',self.age)

		

>>> s=student()

>>> s.name='Sathish Kumar'

>>> s.age=27

>>> s.school='Gugai He Sec School'


>>> s.pri()
hellow  Sathish Kumar and his age  27


>>> class student(object):
	school='Gugai Hr Sec School'
	name=''
	age=0
	def pri(self):
		print(self.school)
		print('hellow ',self.name,'and his age ',self.age)

		


>>> s=student()

>>> s.name='Gopiraj'

>>> s.age=21

>>> s.pri()
Gugai Hr Sec School
hellow  Gopiraj and his age  21



>>> student.school='Muthayammal Collage of Atrs & Science'

>>> s.name='Gopi & Sathish '
>>> s.age=21

>>> s.pri()
Muthayammal Collage of Atrs & Science
hellow  Gopi & Sathish  and his age  21

>>> #--------------------------------

>>> #  constructor

>>> class myclass(object):
	language='Python'
	def __init__(self):
		self.name=''
		self.age=0
		self.education=''

		

>>> s=myclass()

>>> s.name
''

>>> s.age
0

>>> s.education
''

>>> s.name='Gopi'

>>> s.age=21

>>> s.education='B.Sc Mathematics'


>>> s.language
'Python'

>>> s.age
21

>>> s.education
'B.Sc Mathematics'

>>> s.language
'Python'

>>> s.name
'Gopi'


>>> class myclass(object):
	language='Python'
	def __init__(self,name,age,education):
		self.name=name
		self.age=age
		self.education=education

		

>>> s=myclass('gopi',21,'Math')

>>> s.age
21

>>> s.education
'Math'

>>> s.language
'Python'

>>> s.name
'gopi'

>>> myclass.language
'Python'


>>> class myclass(object):
	language='Python'
	def __init__(self,name='gopi',age=21,education='Math'):
		self.name=name
		self.age=age
		self.education=education

		

>>> s=mylass(name='Sathish')
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    s=mylass(name='Sathish')
NameError: name 'mylass' is not defined


>>> s=myclass(name='Satish Kumar')

>>> s.name
'Satish Kumar'

>>> s.age
21

>>> s.education='BE Bio Technology'


>>> s.language
'Python'

>>> s.education
'BE Bio Technology'

>>> s.age
21

>>> s.name
'Satish Kumar'


>>> class myclass(object):
	language='Python'
	def __init__(self,name,age,education):
		self.name=name
		self.age=age
		self.education=education

		

>>> s=myclass('Gopi',21,'Math')

>>> s.education
'Math'

>>> s.education='B.Sc Math'

>>> s.age
21

>>> s.education
'B.Sc Math'

>>> s.language
'Python'

>>> s.name
'Gopi'

>>> s.language='java'

>>> s.language
'java'

>>> myclass.language='Any Language'

>>> s.language
'java'

>>> s=myclass('Gopi',21,'B.Sc Math')


>>> s.language
'Any Language'

>>> s.name
'Gopi'
>>> s.age
21

>>> s.education
'B.Sc Math'

>>> #--------------------------


>>> class Student:
    def __init__(self):
        self.__name=''
    def setname(self, name):
        print('setname() called')
        self.__name=name
    def getname(self):
        print('getname() called')
        return self.__name
    name=property(getname, setname)

    

>>> s=Student()

>>> s.name
getname() called
''

>>> s.name='gopi'
setname() called

>>> s.setname()
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    s.setname()
TypeError: setname() missing 1 required positional argument: 'name'

>>> s.getname()
getname() called
'gopi'

>>> s.setname('sathish')
setname() called

>>> s.getname
<bound method Student.getname of <__main__.Student object at 0x00000211F02EBE20>>

>>> s.getname()
getname() called
'sathish'

>>> s.setname('gopi')
setname() called

>>> s.name
getname() called
'gopi'

>>> s.getname
<bound method Student.getname of <__main__.Student object at 0x00000211F02EBE20>>

>>> s.getname()
getname() called
'gopi'

>>> #------------------------------

>>> class Alphabet:
    def __init__(self, value):
        self._value = value
 
    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value
 
    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value
 
    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value
 
    value = property(getValue, setValue,
                     delValue, )

    


>>> s=Alphabet('Gopiraj')

>>> s.value
Getting value
'Gopiraj'

>>> s.getValue()
Getting value
'Gopiraj'

>>> s.setValue('Satish Kumar')
Setting value to Satish Kumar

>>> s.value
Getting value
'Satish Kumar'

>>> s.getValue()
Getting value
'Satish Kumar'


>>> s.delValue()
Deleting value


>>> s.value
Getting value
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    s.value
  File "<pyshell#246>", line 8, in getValue
    return self._value
AttributeError: 'Alphabet' object has no attribute '_value'

>>> s.value='Parimala'
Setting value to Parimala

>>> s.getValue()
Getting value
'Parimala'

>>> s.setValue('Shanmugam')
Setting value to Shanmugam

>>> s.value
Getting value
'Shanmugam'


>>> class Alphabet:
    def __init__(self, value):
        self._value = value
 
    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value
 
    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value
 
    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value
 

    
>>> s=Alphabet('Gopi')

>>> s.getValue()
Getting value
'Gopi'

>>> s.setValue('Sathish Kumar')
Setting value to Sathish Kumar

>>> s.getValue()
Getting value
'Sathish Kumar'

>>> s.delValue()
Deleting value

>>> s.setValue()
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    s.setValue()
TypeError: setValue() missing 1 required positional argument: 'value'

>>> s.setValue('Indu')
Setting value to Indu

>>> s.getValue()
Getting value
'Indu'
