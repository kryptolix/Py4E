text = "X-DSPAM-Confidence:    0.8475"
position = text.find(':')

piece = text[position+1:]
value = float(piece)
print(value)
