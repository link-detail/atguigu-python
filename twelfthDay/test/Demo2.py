f1 = open("diary.md", mode="r", encoding="utf8")

context = f1.read()
newContent = context.split("pyrjb\n")
print(newContent)
