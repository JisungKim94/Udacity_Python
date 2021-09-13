# The split method has two additional arguments (sep and maxsplit). The sep argument stands for "separator". It can be used to identify how the string should be split up (e.g., whitespace characters like space, tab, return, newline; specific punctuation (e.g., comma, dashes)). If the sep argument is not provided, the default separator is whitespace.

# split 사용법
new_str = "The cow jumped over the moon."
print(new_str.split())
new_str = "The cow jumped over the moon."
print(new_str.split(" ", 3), "\n")

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"

length = len(verse)
print(length, "\n")  # 362
first_idx = verse.find("and")
print(first_idx, "\n")  # 65
last_idx = verse.rfind("you")
print(last_idx, "\n")  # 186
count = verse.count("you")
print(count, "\n")  # 8

# format 사용법
print("Verse has a length of {} characters.".format(len(verse)))

# format 사용법 2
print(
    "The first occurence of the word 'and' occurs at the {}th index.".format(
        verse.find("and")
    )
)

# format 사용법 3
message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

print(message.format(length, first_idx, last_idx, count))
