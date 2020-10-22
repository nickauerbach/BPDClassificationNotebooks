import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# RAW DATA
# https://www.burlingtonvt.gov/Police/Data/OpenData

# Incident level data for all call types from 2012. Variables include type of call, origin of call (Officer, Phone, etc), call time and street.
# It also includes an approximate latitude and longitude for mapping, for all but the most sensitive types of calls.
# New: data now includes Ward, District and Type (severity). Data is updated approximately every month.
incidents = pd.read_csv("Incidents_2020-10-01.csv",encoding='cp1252')
incidents.info()

# Arrests by charge and arrestee demographics since 2012. Includes date of arrest, gender, age and race of arrestee.
# NOTE: Each row represents one charge, not one arrest. A single arrest may include multiple charges.
arrests = pd.read_csv("Arrests_2020-10-01.csv",encoding='cp1252')
arrests.info()

# Traffic stops from 2012 through 2019. There are 16 variables plus flags for traffic violation types.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/Data%20Dictionary%202019.pdf
trafficStops = pd.read_csv("BPDTrafficStops2012_2019.csv",encoding='cp1252')
trafficStops.info()

# Use-of-Force incidents by subject from 2012 through 2018. Includes demographic data and flags for type of resistance and force used.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/UOF%20Data%20Dictionary.pdf
useOfForce = pd.read_csv("BPD_UseOfForce_2012_2018.csv",encoding='cp1252')
useOfForce.info()

# Hate crime offenses from 2012 through November 2018 including 41 misdemeanor offenses and 3 felony offenses.
# Note: Data updated on 11/16/2018.
hateCrime = pd.read_csv("HateCrimeOpenData.csv",encoding='cp1252')
hateCrime.info()

# Merge all 2012-2018 datasets up until latest common incident - 11/2018 based on incidents dataframe
bpd_all = incidents.merge(arrests)
bpd_all = incidents.merge(hateCrime)
bpd_all = incidents.merge(useOfForce)
bpd_all = incidents.merge(trafficStops)


# SEPARATE DATA (2017-19)

# Case level data set on BPD cases arraigned since September, 2017 through May, 2019.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/ArraignmentDataDictionary.pdf
arraign = pd.read_csv("arraignment_data_2019_5_30.csv")
arraign.info()