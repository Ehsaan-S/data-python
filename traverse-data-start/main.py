file=open("age-data.txt","r")
ageData=[]
for line in file:
    line=line.strip()
    ageData.append(line)

file=open("number-data.txt","r")
numberData=[]
for line in file:
    line=line.strip()
    numberData.append(line)


file=open("survey-results.txt","r")
surveyResults=[]
for line in file:
    line=line.strip()
    surveyResults.append(line)

def Age(ageData):
    under18=sum(1 for age in ageData if int(age)<18)
    between18to35=sum(1 for age in ageData if 18<=(age)>=35)
    between35to65=sum(1 for age in ageData if 35<=(age)>=65)
    over65=sum(1 for age in ageData if int(age)>65)
    return{"Under 18": under18,"18to35": between18to35,"35to65":between35to65,"over65":over65}





