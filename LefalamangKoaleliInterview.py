#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[9]:


# Read Excel file into a DataFrame

df = pd.read_excel(r"C:\Users\user\Downloads\Palindrome\pone.0212445.s004.xlsx", header=1)

# Display the DataFrame
print(df)


# In[10]:


df


# In[11]:


# Task 1: Total number of people living with HIV (NoPLHIV) in the listed districts according to the Survey estimate
total_noplhiv_survey = df[df['Estimate'] == 'Survey']['NoPLHIV'].sum()
print(f"Total NoPLHIV in districts according to the Survey estimate: {total_noplhiv_survey}")


# In[12]:


# Task 2: Average NoPLHIV of the two estimates used for “Xhariep”
xhariep_data = df[df['District'] == 'Xhariep']
average_noplhiv_xhariep = xhariep_data['NoPLHIV'].mean()
print(f"Average NoPLHIV for Xhariep: {average_noplhiv_xhariep}")


# In[13]:


# Task 3: Add a column and populate it with the number of people not living with HIV for each row
df['NoHIV'] = df['NoPLHIV_UCL'] - df['NoPLHIV']
print(df[['District', 'NoPLHIV', 'NoHIV']])


# In[15]:


df[['District', 'NoPLHIV', 'NoHIV']]


# In[16]:


# Task 4: Total NoPLHIV in all the cities (districts with “city” or “metro” in the name)
total_noplhiv_cities = df[df['District'].str.contains('city|metro', case=False)]['NoPLHIV'].sum()
print(f"Total NoPLHIV in all cities: {total_noplhiv_cities}")


# In[17]:


# Task 5: Remove all the special/non-alphabetic characters from the dataframe column names
df.columns = df.columns.str.replace('[^a-zA-Z0-9]', '')
print("DataFrame column names after removing special characters:")
print(df.columns)


# In[21]:


# Task 6: Plot Prevalence confidence interval for Districts that end in “i” according to Fay-Herriott estimates
fay_herriott_i_districts = df[df['District'].str.lower().str.endswith('i') & (df['Estimate'] == 'Fay-Heriott')]
plt.figure(figsize=(10, 6))
plt.errorbar(fay_herriott_i_districts['District'], fay_herriott_i_districts['Prevalence'],
             yerr=[fay_herriott_i_districts['Prevalence'] - fay_herriott_i_districts['PrevalenceLCL'],
                   fay_herriott_i_districts['PrevalenceUCL'] - fay_herriott_i_districts['Prevalence']],
             fmt='o', label='Prevalence')
plt.title('Prevalence Confidence Interval for Districts ending in "i" (Fay-Herriott Estimates)')
plt.xlabel('District')
plt.ylabel('Prevalence %')
plt.legend()
plt.show()


# In[ ]:




