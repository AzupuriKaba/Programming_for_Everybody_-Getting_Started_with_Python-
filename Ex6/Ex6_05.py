text = "X-DSPAM-Confidence:    0.8475"
first_number = text.find('0')
last_number = text.find('5')

number_in_text = text[first_number : last_number + 1]
print(float(number_in_text))
