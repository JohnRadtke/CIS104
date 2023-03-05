text = "X-DSPAM-Confidence:    0.8475"
start = text.find('0')
result =float(text[start : ])
print (result)
