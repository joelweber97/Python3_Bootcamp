kms = input('Enter the length of your run (in km): ')
print('Ok, you said ' + kms + ' kilometers')
#kms is currently in string format so we need to convert it to a float
miles = float(kms) / 1.60934
miles = round(miles,2)
print(f"Your run was {miles} miles long")


#this also works
kms = input('Enter the length of your run (in km): ')
print('Ok, you said ' + kms + ' kilometers')
miles = round(float(kms) / 1.60934,2)
print(f"Your run was {miles} miles long")


#this also works
kms = input('Enter the length of your run (in km): ')
print('Ok, you said ' + kms + ' kilometers')
miles = float(kms) / 1.60934
print(f"Your run was {round(miles,2)} miles long")