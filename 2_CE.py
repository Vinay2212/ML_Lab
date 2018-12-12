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
s_hypothesis=specific_hypothesis
g_hypothesis=generic_hypothesis
print("Findig maximally specific hypothesis:")
s_hypothesis = a[0][:-1]
for i in range(len(a)):
    if a[i][-1]=="Yes":
        for j in range(num_attributes):
            if a[i][j]!=s_hypothesis[j]:
                s_hypothesis[j]="?"
            else:
                s_hypothesis[j]=a[i][j]
    print("For training example no:",i+1,"the specific hypothesis is",s_hypothesis)
    if a[i][-1]=="No":
        for k in range(num_attributes):
            b=["?"]*num_attributes
            if s_hypothesis[k]!=a[i][k]:
                b[k]=s_hypothesis[k]
            if b not in g_hypothesis:
                g_hypothesis.append(b)
    print("For training example no:",i+1,"the general hypothesis is",g_hypothesis)        
print("The maximally specific hypothesis is:",s_hypothesis)
print("The maximally general hypothesis is:",g_hypothesis)