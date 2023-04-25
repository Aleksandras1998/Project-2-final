import numpy as np

# Define the original 1D array
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])

# Define the dimensions of the 3D array
Nx = 2
Ny = 3
Nz = 4

# Create an empty 3D array with the specified dimensions
arr = np.zeros((Nz, Ny, Nx))

# Reshape the 1D array into the 3D array according to the rules given
for i in range(Nz):
    for j in range(Ny):
        for k in range(Nx):
            print(i,j,k)
            index_1d = i + j*Nz + k*Ny*Nz
            arr[i, j, k] = data[index_1d]

# Print the resulting 3D array
print(arr)


# =============================================================================
# As you can see, this 3D array has the shape [Nz, Ny, Nx] and the values are 
# arranged according to the rules given in the description. The first index (i) 
# corresponds to the z-axis, the second index (j) corresponds to the y-axis, and 
# the third index (k) corresponds to the x-axis.
# =============================================================================

# =============================================================================
# If you wanted to reshape this 3D array to have shape [Nx, Ny, Nz], 
# you could use the transpose method of the NumPy array to swap 
# the order of the axes:
# =============================================================================

# Reshape the 3D array to have shape [Nx, Ny, Nz]!!!!!! -it's used for doing stats calculations in futher steps
arr_reshaped = arr.transpose((2, 1, 0))
print(arr_reshaped)

# Print the resulting reshaped array
#print(arr_reshaped)


# =============================================================================
# As you can see, the resulting array now has shape [Nx, Ny, Nz], but the values 
# are arranged differently than in the original 3D array.
# =============================================================================


# =============================================================================
#                               Statistics part
# =============================================================================

# =============================================================================
# To calculate the mean value for each point in the y-z plane over the x-dimension, 
# you need to take the mean along the x-dimension for each y-z point. 
# Here's how you can do it:
# =============================================================================

mean_yz=np.mean(arr_reshaped,axis=0)
print(mean_yz)


mean=np.zeros((Ny,Nz))
print(mean)

for y in range(Ny):
    for z in range(Nz):
        mean[y,z] = np.mean(arr_reshaped[:,y,z])
print(mean)


# =============================================================================
# In the code above, mean() function is used to calculate the mean of each y-z 
# point along the x-dimension (axis=2). The resulting array will have the shape of
# (Nz, Ny), where Nz is the number of stacks, and Ny is the number of rows in the 3D array.
# =============================================================================

# variance_yz=np.var(arr,axis=2)
# print(variance_yz)

# mean=np.zeros((Ny,Nz))
# print(mean.shape)
# print(mean)
# print(arr.shape)

# for z in range(Nz):
#     for y in range(Ny):
#         for x in range(Nx):
            
#             index_1d = i + j*Nz + k*Ny*Nz
#             arr[i, j, k] = data[index_1d]