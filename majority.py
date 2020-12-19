Input = [2, 2, 1, 1, 1, 2, 2]
import emoji

for i in Input:
    if Input.count(i) > len(Input) / 2:
        print(i)
        break
print(emoji.emojize("pyhon is :thumbs_up: "))
