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
            print(f'Error: Number of elements in the {filename} file\n'+
                  f'({num_elements_in_file}) does not match the expected number ({input_num_elements}))')
            return None
        else:
            print('╔' + '═'*49 + '╗\n'+
                 f'║ Data loaded successfully from {filename} ║\n'+
                 f'║ The number of elements in {filename} is: {num_elements_in_file} ║\n'+
                  '╚' + '═'*49 + '╝')
            
#=============================================================================
        #Creating an empty 3D array with the specified dimensions
        array_3d=np.zeros((Nz, Ny, Nx))
        
        
        #Reshape the 1D array into the 3D array according the rules given
        for z in range (Nz):
            for y in range(Ny):
                for x in range(Nx):
                    index_1d=z+y*Nz+x*Ny*Nz
                    array_3d[z,y,x]=array_1d[index_1d]
        data=array_3d
#==============================================================================
        #Alternative (working) 3D array arrangment
#==============================================================================
        #data=array_1d.reshape((Nx, Ny, Nz))
        #data=np.transpose(data, (2, 1, 0))
#==============================================================================
           
     
        return data


def dataStatistics(data, statistic, Yref=None, Zref=None, DeltaX=None):
#===============================================================================    
#Reshaping [Nz x Ny x Nx] array to [Nx x Ny x Nz] for further stats calculations
#==============================================================================
    
    data=data.transpose((2,1,0))#Delete this if we are using transpose up in dataLoad
    result=np.zeros((data.shape[1], data.shape[2]))
    Nx, Ny, Nz = data.shape
    
# =============================================================================
#                   Creating if statements for stats calculations
# =============================================================================
    
    if statistic == "Mean":
        result=np.round(np.mean(data, axis=0),3)       
# =============================================================================
#         Alternative option for mean calculation (gives same result):
# =============================================================================
        # for y in range(data.shape[1]):
        #     for z in range(data.shape[2]):
        #         array_yz[y,z] = np.mean(data[:,y,z])
        # mean_yz=array_yz
        # return mean_yz
        

       
    if statistic == "Variance":
        result=np.round(np.var(data,axis=0),3)       
# =============================================================================
#         Alternative option for variance calculation (gives same result):
# =============================================================================
        # for y in range(data.shape[1]):
        #     for z in range(data.shape[2]):
        #         array_yz[y,z] = np.mean(data[:,y,z])
        # mean_yz=array_yz
        # variance_yz=np.sum((data-mean_yz)**2,axis=0)/data.shape[0]
        # return variance_yz
        
               
        
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
        summation=np.sum(multiply_array,axis=0)      

        result=np.round(summation/(Nx-DeltaX),3)
    assert result.shape==(Ny,Nz),(f'Erorr:{statistic} has invalid shape')
    return result

def dataPlot (data, statistic):
    
# =============================================================================
# [1]-Contour plots
# =============================================================================
    # if statistic == 'Mean':
        
    #     print('Mean plot has been successfully generated. Continue if needed or enter [4]')
        
    #     #Creating x, y coordiantes for the contour plot
    #     x=np.arange(data.shape[1])
    #     y=np.arange(data.shape[0])
    #     X,Y=np.meshgrid(x,y)
        
    #     #Creating the contour plot
    #     fig,ax=plt.subplots()
    #     contour=ax.contourf(X,Y, data)
    #     fig.colorbar(contour)
        
    #     #Setting the title and axis labels
    #     ax.set_title(f'Contour Plot of Mean array with size {data.shape[0]}x{data.shape[1]}')
    #     ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    #     ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
    #     #Show the plot
    #     plt.show(block=False)
        
    #     return (dataPlot)
    
    # if statistic == 'Variance':
        
    #     print('Variance plot has been successfully generated. Continue if needed or enter [4]')
        
    #     #Creating x, y coordiantes for the contour plot
    #     x=np.arange(data.shape[1])
    #     y=np.arange(data.shape[0])
    #     X,Y=np.meshgrid(x,y)
        
    #     #Creating the contour plot
    #     fig,ax=plt.subplots()
    #     contour=ax.contourf(X,Y, data)
    #     fig.colorbar(contour)
        
    #     #Setting the title and axis labels
    #     ax.set_title(f'Contour Plot of Variance array with size {data.shape[0]}x{data.shape[1]}')
    #     ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    #     ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
    #     #Show the plot
    #     plt.show(block=False)
        
    #     return (dataPlot)
    
    # if statistic == 'Cross-Correlation':
        
    #     print('Cross-Correlation plot has been successfully generated. Continue if needed or enter [4]')
        
    #     #Creating x, y coordiantes for the contour plot
    #     x=np.arange(data.shape[1])
    #     y=np.arange(data.shape[0])
    #     X,Y=np.meshgrid(x,y)
        
    #     #Creating the contour plot
    #     fig,ax=plt.subplots()
    #     contour=ax.contourf(X,Y, data)
    #     fig.colorbar(contour)
        
    #     #Setting the title and axis labels
    #     ax.set_title(f'Contour Plot of Cross-correlation array with size {data.shape[0]}x{data.shape[1]}')
    #     ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
    #     ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
    #     #Show the plot
    #     plt.show(block=False)
        
    #     return (dataPlot)

# =============================================================================
# [2] - Surface Plot:
# =============================================================================

    if statistic == 'Mean':
        
        print('Mean plot has been successfully generated. Continue if needed or enter [4]')
        
        #Creating x, y coordiantes for the contour plot
        x=np.arange(data.shape[1])
        y=np.arange(data.shape[0])
        X,Y=np.meshgrid(x,y)
        
        #Creating the surface plot
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        surf=ax.plot_surface(X, Y, data, cmap='coolwarm')
        fig.colorbar(surf)
        
        #Setting the title and axis labels
        ax.set_title(f'Surface Plot of Mean array with size {data.shape[0]}x{data.shape[1]}')
        ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
        ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
        #Show the plot
        plt.show(block=False)
        
        return (dataPlot)
    
    if statistic == 'Variance':
        
        print('Variance plot has been successfully generated. Continue if needed or enter [4]')
        
        #Creating x, y coordiantes for the contour plot
        x=np.arange(data.shape[1])
        y=np.arange(data.shape[0])
        X,Y=np.meshgrid(x,y)
        
        #Creating the surface plot
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        surf=ax.plot_surface(X, Y, data, cmap='coolwarm')
        fig.colorbar(surf)
        
        #Setting the title and axis labels
        ax.set_title(f'Surface Plot of Variance array with size {data.shape[0]}x{data.shape[1]}')
        ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
        ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
        #Show the plot
        plt.show(block=False)
        
        return (dataPlot)
    
    if statistic == 'Cross-Correlation':
        
        print('Cross-Correlation plot has been successfully generated. Continue if needed or enter [4]')
        
        #Creating x, y coordiantes for the contour plot
        x=np.arange(data.shape[1])
        y=np.arange(data.shape[0])
        X,Y=np.meshgrid(x,y)
        
        #Creating the surface plot
        fig=plt.figure()
        ax=fig.add_subplot(111,projection='3d')
        surf=ax.plot_surface(X, Y, data, cmap='coolwarm')
        fig.colorbar(surf)
        
        #Setting the title and axis labels
        ax.set_title(f'Surface Plot of Cross-correlation array with size {data.shape[0]}x{data.shape[1]}')
        ax.set_xlabel('Wind speed in z direction (Vz (m/s)')
        ax.set_ylabel('Wind speed in y direction (Vy (m/s)')
        
        #Show the plot
        plt.show(block=False)
        
        return (dataPlot)     
        

        