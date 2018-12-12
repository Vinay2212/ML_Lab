import csv
a=[]
with open('C:\\Users\\Rohit Nayar\\Downloads\\findsss.csv') as csvFile:
    reader=csv.reader(csvFile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes=len(a[0])-1
generic_hypothesis=["?"]*num_attributes
specific_hypothesis=["0"]*num_attributes
print("The most generic hypothesis is:",generic_hypothesis)
print("The most specific hypothesis is:",specific_hypothesis)
hypothesis=specific_hypothesis
print("Findig maximally specific hypothesis:")
hypothesis = a[0][:-1]
for i in range(len(a)):
    if a[i][-1]=="Yes":
        for j in range(num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]="?"
    print("For training example no:",i+1,"the hypothesis is",hypothesis)
print("The maximally specific hypothesis is:",hypothesis)