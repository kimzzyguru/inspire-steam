# Name: Valentine Kimani
# Date: 11/02/2026
# string formatting

# Get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The length of the sentence is: {string_length}")

# Splitting a string
sentence2 = "Mathematics physics"
split = sentence2.split(" ")

print(f"The first subject is: ", split[1])


# Make everything CAPS
mpesa_code = "ub12ddsfhg"

capitalized = mpesa_code.upper()

print("New mpesa code is: ", capitalized)

# Make everything small
mpesa_code2 = "UB12DDSFHG"

small = mpesa_code2.lower()
print("New mpesa code is: ", small)

# replacing characters in a string

balance = "100kes"
amount_added = "50kes"

cleaned_balance = balance.replace("kes", "")

print("Cleaned balance is: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("kes", "")
print("Cleaned amount added is: ", cleaned_amount_added)

added_balance = int(cleaned_balance) + int(cleaned_amount_added)
print("Added balance is: ", added_balance)

message = "CONFIRMED you have received 40kes from Phillip"
print(message)
split = message.split(" ")
print(f"The amount received is: ", split[4])
cleaned_amount_received = split[4].replace("kes", "")
print(f"Cleaned amount received is: ", cleaned_amount_received)
balance= "100kes"
cleaned_balance = balance.replace("kes", "")
new_balance = int(cleaned_balance) + int(cleaned_amount_received)
print(f"New balance is: ", new_balance)
