import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                     dataLoad function (Aleksandras, Karen, Prabhlin)
# =============================================================================

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
            message = f'Number of elements in the {filename} is: ({num_elements_in_file})'
            padding = (len(message) // 2)
            print('+' + '-' * len(message) + '+\n' +
                  f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                  f'|{message}|\n' +
                  f'|{(" " * (padding-22))}does not match the expected number ({input_num_elements}){(" " * (padding-22))}|\n' +
                  f'|{(" " * (padding-19))}Please check the input size of 3D array{(" " * (padding-20))}|\n'
                  '+' + '-' * len(message) + '+')       
            return None
        else:
            
            message = f'The number of elements in {filename} is: {num_elements_in_file}'
            padding = (len(message) // 2)
            print('╔' + '═'*len(message) + '╗\n'+
                 f'║{(" " * (padding-24))}Data loaded successfully from {filename}{(" " * (padding-24))}║\n' +
                 f'║{message}║\n' +
                  '╚' + '═'*len(message) + '╝')
         
        #Reshape the 1D array into the 3D array according the rules given
        data=array_1d.reshape((Nz, Ny, Nx), order='F')
        data=np.transpose(data, (2, 1, 0))

        return data

# =============================================================================
#                      dataStatistics function (Aleksandras, Karen)
# =============================================================================

def dataStatistics(data, statistic, Yref=None, Zref=None, DeltaX=None):
  
    #Creating zero matrix to store result from statistic calculation
    result=np.zeros((data.shape[1], data.shape[2]))
    Nx, Ny, Nz = data.shape
    

    #Creating if statements for stats calculations

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

# =============================================================================
#                      dataPlot function (Aleksandras, Karen)
# =============================================================================

def dataPlot(data, statistic):
    
    print()
    print(f'{statistic} plot has been successfully generated. Continue if needed or enter [4]')    
    
    #Creating x, y coordinates for the contour plot
    
    #print(data.shape)
    z=np.arange(data.shape[1]) # Correspond to Nz
    #print(z)
    y=np.arange(data.shape[0])
    #print(y)

    Z, Y = np.meshgrid(z, y)
    
    #Creating the contour plot
    fig,ax=plt.subplots()
    contour=ax.contourf(Z,Y,data, 20, cmap='coolwarm')
    fig.colorbar(contour)
    
    
    #Setting the title and axis labels
    ax.set_title(f'Contour Plot of {statistic} array with size {data.shape[0]}x{data.shape[1]}')
    ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
       
    
    #Show the plot
    plt.show(block=False)
    
    return (dataPlot)
    
        