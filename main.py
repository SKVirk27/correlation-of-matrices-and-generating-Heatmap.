#!/usr/bin/python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read a csv file into dataframes
matrix1_dataframe= pd.read_csv("matrix1.txt",delimiter='\t')# delimiter separating values('\t)
matrix1_dataframe.to_csv("matrix1_csv.csv", index=[0])
# Removing "Unnamed" column
matrix1_dataframe.drop(matrix1_dataframe.filter(regex="Unnamed"),axis=1, inplace=True)
# Calculating correlation of matrix1 using person method.
matrix1_csv = matrix1_dataframe.corr(method='pearson')
#Saving co-related matrix1
matrix1_csv.to_csv('matrix1_corr.csv')
# heatmap details of matrix 1 figure.
matrix1_Heatmap_Fig=plt.figure(figsize=(16,6),dpi=80)
matrix1_Heatmap = sns.heatmap(matrix1_csv.corr(), cmap="cubehelix",vmin=-1,vmax=1, annot=True)
matrix1_Heatmap.set_title('MATRIX1 Heatmap', fontdict={'fontsize':10}, pad=9)
matrix1_Heatmap.set_xticklabels(matrix1_Heatmap.get_xmajorticklabels(), fontsize =10)
matrix1_Heatmap.set_yticklabels(matrix1_Heatmap.get_ymajorticklabels(), fontsize =10)
matrix1_Heatmap_Fig.savefig("matrix1_Heatmap_figure1.png")
#Reading matrix2 file as csv.
matrix2_dataframe = pd.read_csv("matrix2.txt",delimiter='\t')
matrix2_dataframe.to_csv("matrix2_csv.csv", index=[0])
matrix2_dataframe.drop(matrix2_dataframe.filter(regex="Unnamed"),axis=1,inplace=True)
#Matrix 2 is cor-related with method pearson.
matrix2_csv = matrix2_dataframe.corr(method='pearson')
#Saving cor-related matrix.
matrix2_csv.to_csv('matrix2_corr.csv')
#Figure detail of heatmap 2 of matrix2.
matrix2_Heatmap_Fig=plt.figure(figsize=(16,6),dpi=80)
matrix2_Heatmap= sns.heatmap(matrix2_csv.corr(), cmap="BrBG", annot=True)
matrix2_Heatmap.set_xticklabels(matrix2_Heatmap.get_xmajorticklabels(), fontsize =10)
matrix2_Heatmap.set_yticklabels(matrix2_Heatmap.get_ymajorticklabels(), fontsize =10)
#res.set_yticklabels(res.get_ymajorticklabels(), fontsize = 18)
matrix2_Heatmap.set_title('Correlation matrix2_Heatmap', fontdict={'fontsize':9}, pad=9)
matrix2_Heatmap_Fig.savefig("matrix2_Heatmap.png")
#Cor-relating matrix1 with matrix2.
matrix1_dataframe_with_suffix=matrix1_dataframe.add_suffix('_1') #adding suffix in columns headers to differentiate between matrices
matrix2_dataframe_with_suffix=matrix2_dataframe.add_suffix('_2')
Corr_matrix1_2 =pd.concat([matrix1_dataframe_with_suffix, matrix2_dataframe_with_suffix], axis=1, keys=['df1', 'df2']).corr().loc['df2', 'df1']
Corr_matrix1_2.to_csv('Corr_matrix1&2.csv',index=[0])









