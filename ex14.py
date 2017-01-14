#coding= utf-8
from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s ,I'm the %s script." %(user_name, script )
print "Now I'd like to ask you some questions."
print "Do you like me %s?"%user_name
likes = raw_input(prompt)

print "ok and where do you live %s?"%user_name
lives = raw_input(prompt)

print "ok uh~ what kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright , so %s you said %r about liking me.
You live in %r, though not sure where it is .
And you have a %r couputer. Thanks.abs
"""%(user_name, likes, lives, computer) 