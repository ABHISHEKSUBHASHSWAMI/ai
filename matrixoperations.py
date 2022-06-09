#Abhishek Subhash Swami 21 AIML
#Program for matrix operation

import tensorflow as tf 

matrix1=[[4,2,1],[6,4,2],[6,8,9]]
matrix2=[[1,3,1],[1,2,9],[9,1,7]]

#matrix addition
sum=tf.add(matrix1,matrix2)
print("\nAddition of matrix1 and matrix2 :\n",sum)

#matrix subtraction
difference=tf.subtract(matrix1,matrix2)
print("\nDifference between matrix1 and matrix2 :\n",difference)

#matrix multiplication
product=tf.matmul(matrix1,matrix2)
print("\nMatrix multiplication :\n",product)

#matrix division
division=tf.divide(matrix1,matrix2)
print("\nMatrix division :\n",division)

#transpose
transpose=tf.transpose(matrix1)
print("\nTranspose of matrix1 :\n",transpose)