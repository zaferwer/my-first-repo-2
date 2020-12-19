s = "WWe promptly judged antique ivory buckles for the next prize"
s_lower = s.lower()
sets = set(s_lower)
ascii_letters = set("abcdefghijklmnopqrstuvwxyz")
seta = set(ascii_letters)
if seta - sets == set():
    print("pangram")
else:
    print("not pangram")
