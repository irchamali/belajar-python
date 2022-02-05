# String
# String dalam python dikelilingi oleh tanda kutip tunggal, atau tanda kutip ganda
# 'cinta' or "kasih"

a = "Hello"
print(a)

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(c)

# Get the character at position 1 (remember that the first character has the position 0):
d = "Hello, World!"
print(d[1])

# looping
# Since strings are arrays, we can loop through the characters in a string, with a for loop
for x in "banana":
  print(x)

# String Length
# To get the length of a string, use the len() function.
e = "Hello, World!"
print(len(e))


# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in

txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
