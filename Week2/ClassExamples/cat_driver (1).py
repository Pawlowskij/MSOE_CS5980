from cat import Cat


kitty = Cat("Sunny", "Orange")
# where is self? -> we don't specify it


print(type(kitty))

print(f"hello {kitty.name}")

cat2 = Cat("Doug", "red")

print(cat2.color)

# what the type?
kitty.hisses_at(cat2)

#"private" variables
#print(kitty._shhh)

# declares an emptylist (think array/arrayList from other coding languages)
my_cats = []

my_cats.append(kitty)
my_cats.append(cat2)
kitty.temper = "very nice"

print("how many things are in the loop?")
print(len(my_cats))
# something similar to java.toString() ?
print(my_cats)
print(kitty)
print(str(kitty))

# another way to print out all info in a list
for c in my_cats:
    print(f"cat: {c.name}", end="|||") # end specifies whether you want a newline or something else