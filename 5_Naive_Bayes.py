import csv
import math
import random

def loadcsv():
    lines=csv.reader(open(r"E:\DATA SET\pima-indians-diabetes.csv"))
    dataset=list(lines)
    for i in range (len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]]
    return dataset

def splitdataset(dataset,splitratio):
    trainsize=int(len(dataset)*splitratio)
    trainset=[]
    copy=list(dataset)
    while len(trainset) < trainsize:
        index=random.randrange(len(copy))
        trainset.append(copy.pop(index))
    return[trainset,copy]

def separatebyclass(dataset):
    separated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if(vector[-1] not in separated):
            separated[vector[-1]]=[]
        separated[vector[-1]].append(vector)
    return separated

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg=mean(numbers)
    varience=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(varience)

def summarize(dataset):
    summaries=[(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarizebyclass(dataset):
    separated=separatebyclass(dataset)
    summaries={}
    for cv,instances in separated.items():
        summaries[cv]=summarize(instances)
    return summaries

def calculateprobability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return(1/(math.sqrt(2*math.pi)*stdev))*exponent

def clacclassprob(summaries,inpvect):
    probabilities={}
    for cv,cs in summaries.items():
        probabilities[cv]=1
        for i in range(len(cs)): 
            mean,stdev=cs[i]
            x=inpvect[i]
            probabilities[cv]*=calculateprobability(x,mean,stdev)
    return probabilities

def predict(summaries,inpvect):
    probabilities=clacclassprob(summaries,inpvect)
    bl,bp=None,-1
    for cv,probability in probabilities.items():
        if bl is None or probability > bp:
            bp=probability
            bl=cv
    return bl
    
def getpredictions(summaries,testset):
    predictions=[]
    for i in range(len(testset)):
        result=predict(summaries,testset[i])
        predictions.append(result)
    return predictions

def getaccuracy(testset,predictions):
    correct=0
    for i in range(len(testset)):
        if testset[i][-1]==predictions[i]:
            correct+=1
    return(correct/float(len(testset)))*100.0

def main():
    splitratio=0.7
    dataset=loadcsv()
  
    print("\n The length of dataset:",len(dataset))
    print("\n THe dataset spliting into training amd testing\n")
    
    trainingset,testset = splitdataset(dataset,splitratio)

    print("\nNumber of rows in trainig set:{0} rows".format(len(trainingset)))
    print("\nNumber of rows in test set:{0} rows".format(len(testset)))
    print("\n First 5 rows of trainig set:\n")

    for i in range(0,5):
        print(trainingset[i],"\n")
    print("\n First 5 rows of test set:\n")
    for i in range(0,5):
        print(testset[i],"\n")

    summaries=summarizebyclass(trainingset)
    print("\nModel summaries:\n",summaries)
    predictions=getpredictions(summaries,testset)
    print("\nPredictions:\n",predictions)
    accuracy=getaccuracy(testset,predictions)
    print("\nAccuracy:{0}%".format(accuracy))

main()
