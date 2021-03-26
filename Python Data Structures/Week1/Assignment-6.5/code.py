
text = "X-DSPAM-Confidence:    0.8475"
startPos = text.find('0.8475')
piece = text[startPos:]
end = float(piece)
print(end)
