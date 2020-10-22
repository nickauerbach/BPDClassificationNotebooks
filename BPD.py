import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# RAW DATA
# https://www.burlingtonvt.gov/Police/Data/OpenData

# Arrests by charge and arrestee demographics since 2012. Includes date of arrest, gender, age and race of arrestee.
# NOTE: Each row represents one charge, not one arrest. A single arrest may include multiple charges.
arraign = pd.read_csv("arraignment_data_2019_5_30.csv")
arraign.info()

# Traffic stops from 2012 through 2019. There are 16 variables plus flags for traffic violation types.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/Data%20Dictionary%202019.pdf
arrests = pd.read_csv("Arrests_2020-10-01.csv")
arrests.info()

# Use-of-Force incidents by subject from 2012 through 2018. Includes demographic data and flags for type of resistance and force used.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/UOF%20Data%20Dictionary.pdf
useOfForce = pd.read_csv("BPD_UseOfForce_2012_2018.csv")
useOfForce.info()

# Case level data set on BPD cases arraigned since September, 2017 through May, 2019.
# The data is described in more detail here: https://www.burlingtonvt.gov/sites/default/files/u585/Reports/ArraignmentDataDictionary.pdf
hateCrime = pd.read_csv("HateCrimeOpenData.csv")
hateCrime.info()

# Hate crime offenses from 2012 through November 2018 including 41 misdemeanor offenses and 3 felony offenses.
incidents = pd.read_csv("Incidents_2020-10-01.csv")
incidents.info()

# Merge all datasets up until latest common incident - 11/2018
bpd_all = arraign.merge(arrests)
bpd_all = arraign.merge(useOfForce)
bpd_all = arraign.merge(hateCrime)
bpd_all = arraign.merge(incidents)


