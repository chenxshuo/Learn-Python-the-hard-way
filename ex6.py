#coding= utf-8
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I say that %r." % x
print "I also said that %r." % y
#%r 代表引用一段字符串 输出后会直接加上引号 而%s则不会

hilarious = False
joke_evaluation = "Isn't that a joke?! %r"

print joke_evaluation % hilarious
#另一种方法

w = "this is the left side of ..."
e = "a string with a right side"

print w + e
# 使用+号直接拼合两个字符串



