# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# %%
houses=pd.read_csv('train.csv')
                   

# %%
houses.head()

# %%
houses.info()

# %%
houses['Neighborhood'].unique()


# %%
corrmat=houses.corr()
fig, ax=plt.subplots(figsize=(16,13))
sns.heatmap(corrmat)
plt.show()

# %%
print(corrmat)

# %%
luj=corrmat.nlargest(10, 'SalePrice')
luj.head()

# %%
luj=corrmat.nlargest(15, "SalePrice")['SalePrice'].index
print(luj)

# %%
eh=np.corrcoef(houses[luj].values.T)
print(eh)

# %%
hm=sns.heatmap(data=eh, annot=True, xticklabels=luj, yticklabels=luj)

# %%
plt.show()

# %%
houses=houses.dropna(axis=0, subset=['GarageYrBlt','MasVnrArea'])

# %%
houses['GarageYrBlt'].isna().sum()

# %%
eh=np.corrcoef(houses[luj].values.T)

# %%
fig, ax=plt.subplots(figsize=(16,13))
hm=sns.heatmap(data=eh, annot=True, annot_kws={"size":10}, xticklabels=luj, yticklabels=luj)

plt.show()

# %%
na_values=len(houses)-houses.count()
for i in na_values:
    if na_values[i]!=0:
        print(na_values[i])
        

# %%
