import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# RAW DATA
# https://www.burlingtonvt.gov/Police/Data/OpenData

# Incident level data for all call types from 2012. Variables include type of call, origin of call (Officer, Phone, etc), call time and street.
# It also includes an approximate latitude and longitude for mapping, for all but the most sensitive types of calls.
# New: data now includes Ward, District and Type (severity). Data is updated approximately every month.
incidents = pd.read_csv("Incidents_2020-10-01.csv")
incidents.info()

# Arrests by charge and arrestee demographics since 2012. Includes date of arrest, gender, age and race of arrestee.
# NOTE: Each row represents one charge, not one arrest. A single arrest may include multiple charges.
arrests = pd.read_csv("Arrests_2020-10-01.csv")
arrests.info()
fig, ax = plt.subplots()
ax.plot(arrests["age"])
plt.gcf().canvas.set_window_title("Age of Arrested")
plt.show()

# Traffic stops from 2012 through 2019. There are 16 variables plus flags for traffic violation types.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/Data%20Dictionary%202019.pdf
trafficStops = pd.read_csv("BPDTrafficStops2012_2019.csv")
#trafficStops.info()

# Use-of-Force incidents by subject from 2012 through 2018. Includes demographic data and flags for type of resistance and force used.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/UOF%20Data%20Dictionary.pdf
useOfForce = pd.read_csv("BPD_UseOfForce_2012_2018.csv")
#useOfForce.info()

# Hate crime offenses from 2012 through November 2018 including 41 misdemeanor offenses and 3 felony offenses.
# Note: Data updated on 11/16/2018.
hateCrime = pd.read_csv("HateCrimeOpenData.csv")
#hateCrime.info()

# SEPARATE DATA (2017-19)

# Case level data set on BPD cases arraigned since September, 2017 through May, 2019.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/ArraignmentDataDictionary.pdf
arraign = pd.read_csv("arraignment_data_2019_5_30.csv")
#arraign.info()


arrests=arrests.rename(columns={"gender":'genderA', "age":"ageA", "race":"raceA", "charge":"chargeA"})
trafficStops=trafficStops.rename(columns={'gender':'genderT', "age":"ageT", "race":"raceT"})
useOfForce=useOfForce.rename(columns={'gender':'genderF', "age":"ageF", "race":"raceF", "arrest":"arrestF"})
arraign=arraign.rename(columns={'gender':'genderR', "race":"raceR", "charge":"chargeR"})

incident1=pd.merge(left=incidents, right=arrests, how="left", left_on="incident_number", right_on="incident_number")

incident2=pd.merge(left=incident1, right=trafficStops, how="left", left_on="incident_number", right_on="incident_number")
incident3=pd.merge(left=incident2, right=useOfForce, how="left", left_on="incident_number", right_on="incident_number")
incident4=pd.merge(left=incident3, right=hateCrime, how="left", left_on="incident_number", right_on="incident_number")
incident5=pd.merge(left=incident4, right=arraign, how="left", left_on="incident_number", right_on="incident_number")
incident5.head()

incident5 = incident5.fillna('')
incident5['age'] = ''
incident5['charge'] = ''
incident5['gender'] = ''
incident5['race'] = ''

i=0
age=[]
for rows in incident5["age"]:
    if incident5.loc[i,"ageA"]!='':
        age.append(incident5.loc[i,"ageA"])
    elif incident5.loc[i,"ageT"]!='':
        age.append(incident5.loc[i,"ageT"])
    elif incident5.loc[i,"ageF"]!='':
        age.append(incident5.loc[i,"ageF"])
    else:
        age.append('')
    i=i+1

r=0
race=[]
for rows in incident5["race"]:
    if incident5.loc[r,"raceA"]!='':
        race.append(incident5.loc[r,"raceA"])
    elif incident5.loc[r,"raceR"]!='':
        race.append(incident5.loc[r,"raceR"])
    elif incident5.loc[r,"raceT"]!='':
        race.append(incident5.loc[r,"raceT"])
    elif incident5.loc[r,"raceF"]!='':
        race.append(incident5.loc[r,"raceF"])
    else:
        race.append('')
    r=r+1
#race

g=0
gender=[]
for rows in incident5["gender"]:
    if incident5.loc[g,"genderA"]!='':
        gender.append(incident5.loc[g,"genderA"])
    elif incident5.loc[g,"genderR"]!='':
        gender.append(incident5.loc[g,"genderR"])
    elif incident5.loc[g,"genderT"]!='':
        gender.append(incident5.loc[g,"genderT"])
    elif incident5.loc[g,"genderF"]!='':
        gender.append(incident5.loc[g,"genderF"])
    else:
        gender.append('')
    g=g+1
#gender

c=0
charge=[]
for rows in incident5["charge"]:
    if incident5.loc[c,"chargeA"]!='':
        charge.append(incident5.loc[c,"chargeA"])
    elif incident5.loc[c,"chargeR"]!='':
        charge.append(incident5.loc[c,"chargeR"])
    else:
        charge.append('')
    c=c+1
#charge

incident5['age'] = age
incident5["charge"] = charge
incident5["race"] = race
incident5["gender"] = gender
incident5=incident5.drop(columns=['raceA', 'raceF', 'raceT','raceR','ageA', 'ageT', 'ageF','chargeA', 'chargeR','genderA', 'genderT', 'genderF','genderR'])

#merged with correct columns
incident5