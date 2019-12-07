import csv
your_list = list(csv.reader(open('P1_data.csv','r')))

h =['0', '0', '0', '0', '0', '0']
for i in your_list:
  print(i)
  if i[-1]=='TRUE':
    j=0
    for x in i:
      if x!='TRUE' and x!=h[j]:
          if h[j]=='0':
            h[j]=x
          elif h[j]!='0':
            h[j]='?'

      j+=1
print('\nThe maximally specific hypothesis for a given training example is: ')
print(h)

'''
Output:
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'TRUE']
['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'TRUE']
['Rainy', 'Cool', 'High', 'Strong', 'Warm', 'Change', 'FALSE']
['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'TRUE']

The maximally specific hypothesis for a given training example is: 
['Sunny', 'Warm', '?', 'Strong', '?', '?']

'''
