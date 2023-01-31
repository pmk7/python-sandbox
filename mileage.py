print('How many kilometers did you cycle today?')
kms = input()
miles = float(kms)/1.609354

round(miles, 2)
print(f"OK, you cycled {round(miles, 2)} miles")
