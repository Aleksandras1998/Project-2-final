import numpy as np
import matplotlib.pyplot as plt

def dataLoad(filename, Nx, Ny, Nz):
    
    input_num_elements=Nx*Ny*Nz
    
    with open(filename, mode='rb') as file:
        
        #Read data from the binary file
        array_1d=np.fromfile(file,dtype=np.float32)
        
        #Checking if the number of elements in the file 
        #matches the number of elements from input
        
        num_elements_in_file=array_1d.size

        if num_elements_in_file != input_num_elements:
            print()
            print('+' + '-' * 64 + '+\n' +
                  '|' + ' ' * 29 + 'ERROR!' + ' ' * 29 + '|\n' +
                  f'| Number of elements in the {filename} is: ({num_elements_in_file}) |\n' +
                  f'| {" " * 11}does not match the expected number ({input_num_elements}){" " * 12}|\n' +
                  '|' + ' ' * 12 + 'Please check the input size of 3D array' + ' ' * 13 + '|\n' +
                  '+' + '-' * 64 + '+')

            return None
        else:
            print('╔' + '═'*62 + '╗\n'+
                 f'║{" " * 4} Data loaded successfully from {filename}{" " * 4} ║\n'+
                 f'║ The number of elements in {filename} is: {num_elements_in_file} ║\n'+
                  '╚' + '═'*62 + '╝')
            
#=============================================================================
        #Creating an empty 3D array with the specified dimensions
        array_3d=np.zeros((Nz, Ny, Nx))
        
        
        #Reshape the 1D array into the 3D array according the rules given
        data=array_1d.reshape((Nz, Ny, Nx), order='F')
        data=np.transpose(data, (2, 1, 0))

        return data


def dataStatistics(data, statistic, Yref=None, Zref=None, DeltaX=None):
#===============================================================================    
#Reshaping [Nz x Ny x Nx] array to [Nx x Ny x Nz] for further stats calculations
#==============================================================================
    
    
    result=np.zeros((data.shape[1], data.shape[2]))
    Nx, Ny, Nz = data.shape
    
# =============================================================================
#                   Creating if statements for stats calculations
# =============================================================================
    
    if statistic == "Mean":
        result=np.round(np.mean(data,axis=0).astype(np.float32),3)    

        

       
    if statistic == "Variance":
        result=np.round(np.var(data,axis=0).astype(np.float32),3)  

               
        
    if statistic == "Cross-correlation":
        if Yref is None or Zref is None or DeltaX is None:
            raise ValueError('Yref, Zref, and DeltaX must be provided for cross-correlation calculation')
        
        #Assigning variables for cross-correlation calculations      
        lower_bound=0
        upper_bound=Nx-DeltaX

        #Creating an empty 3D array to store multiplied elements
        multiply_array=np.zeros((Nx-DeltaX,Ny,Nz))
        
        for x in range (lower_bound,upper_bound):
            for y in range (Ny):
                for z in range (Nz):
                    multiply_array[x,y,z]=data[x,y,z]*data[x+DeltaX,Yref,Zref]

        summation=np.sum(multiply_array,axis=0).astype(np.float32)      

        result=np.round(summation/(Nx-DeltaX),3)
    assert result.shape==(Ny,Nz),(f'Erorr:{statistic} has invalid shape')
    return result

def dataPlot(data, statistic):
        
    x = np.linspace(0, 32, 32)
    y = np.linspace(0, 32, 32)

    X, Y = np.meshgrid(x, y)

    plt.title(f'{statistic} Surface Plot with size {data.shape[1]}x{data.shape[0]}')
    plt.xlabel('y-coordinate')
    plt.ylabel('z-coordinate')

    plt.contourf(X, Y, data, 20, cmap='coolwarm')
    plt.colorbar()
            
    
#     #Show the plot
    plt.show(block=False)
    
    return (dataPlot)
    
        