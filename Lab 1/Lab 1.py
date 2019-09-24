import csv
with open('CSVFile.csv', 'r') as f:
  reader = csv.reader(f)
  # header = next(reader)
  your_list = list(reader)

h =[['0', '0', '0', '0', '0', '0']]
for i in your_list:
  print(i)
  if i[-1]=='Yes':
    j=0
    for x in i:
      if x!='Yes' and x!=h[0][j]:
          if h[0][j]=='0':
            h[0][j]=x
          elif h[0][j]!='0':
            h[0][j]='?'

      j+=1
print('\nThe maximally specific hypothesis for a given training example is: ')
print(h)

'''
Output:
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes']
['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes']
['Rainy', 'Cool', 'High', 'Strong', 'Warm', 'Change', 'No']
['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']

The maximally specific hypothesis for a given training example is: 
[['Sunny', 'Warm', '?', 'Strong', '?', '?']]

'''
