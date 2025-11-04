

class TestJoin:




  """"
  Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> Studs=(('name', 'surname', 'dept'), {("Lisa", "Simpson", "Physics"),("Dennis", "Ritchie", "Computing")})
>>> Dpts=(('dept', 'HoD'), {("Mathematics","Georg Cantor"), ("Computing", "Alan Turing"), ("Physics", "John S. Bell")})
>>> Studs[0]
('name', 'surname', 'dept')
>>> Dpts[0]
('dept', 'HoD')
>>> set(Studs[0]).intersection(set(Dpts[0]))
{'dept'}
>>> 
>>> set(Studs[0]).intersection(set(Dpts[0]))
{'dept'}
>>> set(Studs[0]).intersection(set(Dpts[0])).pop()
'dept'
>>> Studs
(('name', 'surname', 'dept'), {('Lisa', 'Simpson', 'Physics'), ('Dennis', 'Ritchie', 'Computing')})
>>> ts=Studs[0]
>>> common=set(Studs[0]).intersection(set(Dpts[0])).pop()
>>> 
>>> ts.
ts.count(  ts.index(  
>>> ts.index(common=
... 
... ;
  File "<stdin>", line 3
    ;
    ^
SyntaxError: invalid syntax
>>> 
>>> ts.index(common)
2
>>> Studs[0].index(common)
2
>>> Studs
(('name', 'surname', 'dept'), {('Lisa', 'Simpson', 'Physics'), ('Dennis', 'Ritchie', 'Computing')})
>>> Dpts
(('dept', 'HoD'), {('Mathematics', 'Georg Cantor'), ('Computing', 'Alan Turing'), ('Physics', 'John S. Bell')})
>>> 
  
  """