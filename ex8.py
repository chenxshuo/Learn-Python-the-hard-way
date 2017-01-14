formatter = "%r %r %r %r"

print formatter % (2, 4, 6, 8)
print formatter % ("two", "four", "six", "eight")
print formatter % (True, False, True, False)
#注意布尔开头字母的大小写
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "aaaaaaaaa",
        "bbbbbbbbbbb",
        "ccccccccc",
        "ssssssssss",
)
