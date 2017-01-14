#coding= utf-8
print "I need your information now"
print "What's your name?",
name = raw_input()
print "How old are you?",
age = raw_input()
print "and how tall are you? ",
height = raw_input()
print "then how much do you weigh?",
weight = raw_input()

print "So,%s, you are %r old %r tall and %r heavy ,thank you!"%(
    name, age, height, weight)
#print后加, 会换行

print "好的 欢迎您参加次调查！"
print "首先 请输入您的名字：",
name = raw_input()
print "好的 请问您今年多大了呢？请输入您的年龄：",
age = raw_input()
print "很好 请问您多高（单位：cm）：",
height  = raw_input()
print "最后一个问题 请问您体重多少（单位：kg）：",
weight = raw_input()

print "非常感谢您的参与 , 您今年%r岁了，身高%rcm,体重%rkg， 不得不说 身材保持的很好 继续努力：）"%(
    name, age, height, weight
)
print "十分感谢您的参与 我们保证不会泄露您的个人信息：）"



