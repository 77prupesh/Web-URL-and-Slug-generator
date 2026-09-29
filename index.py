#web url and slug generator
text = input("Enter a sentence :")
#.strip() strips the edges and lower(converts text into lower case)
clean_text = text.strip().lower()
ignore = "!@#.,/\?"
slug = ""
for char in clean_text:
    if char in ignore:
        continue
    elif char == " ":
        slug += "-"
    else:
        slug += char
print("Original sentence:",text)
print("Generated slug:",slug)
