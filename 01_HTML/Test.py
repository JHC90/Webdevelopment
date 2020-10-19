fobj = open("HelloWorld.md", "r")
for line in fobj:
    print(line.rstrip())

print(fobj)
