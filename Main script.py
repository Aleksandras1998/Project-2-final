#File names for testing ↓:
#small 3D array.bin Nx=6 Ny=5 Nz=4
#turbine_32x32x8192.bin Nx=8192 Ny=32 Nz=32

from Data_loader import dataLoader 
from Function_file import dataStatistics, dataPlot
import numpy as np
if __name__=='__main__':

# =============================================================================
#            Creating User interaction Main menu (Everybody)
# =============================================================================
    Nx=0
    Ny=0
    Nz=0
    data_loaded=False
    Yref=None
    Zref=None
    DeltaX=None
    statistics_calculated_mean=False
    statistics_calculated_variance=False
    
    while True:
        
        try:
            user_input=int(input('┏' + '━'*33 + '┓\n'+
                                 '┃'+' '*4+'Your are now in Main menu'+' '*4+'┃\n'+
                                 '┃Please enter a number from 1 to 4┃\n'+
                                 '┗' + '━'*33 + '┛\n'+
                                 '[1] Load data.\n'+
                                 '[2] Display statistics.\n'+
                                 '[3] Generate plots.\n'+
                                 '[4] Quit.\n'+
                                 '>>'))
            if user_input > 4 or user_input<1:

                print('+'+'-'*52+'+')
                print('|' + ' '*22 + 'WARNING!' + ' '*22 + '|')
                raise ValueError('|' + ' '*9 + 'Select a number from the Main menu' + ' '*9 + '|')
        except ValueError as e:
            print(e)
            print('|' + ' '*1 + 'Please try again by inserting a number from 1 to 4' + ' '*1 + '|')
            print('+' + '-'*52 + '+')
            
            continue
# =============================================================================
#             [1]st selection-Uploading 3D array from binary file (Everybody)
# =============================================================================
        if user_input == 1:
            matrix_3d=dataLoader()
            if matrix_3d is not None:
                Nx=matrix_3d.shape[0]
                Ny=matrix_3d.shape[1]
                Nz=matrix_3d.shape[2]
                data_loaded=True

# =============================================================================
#              [2]nd selection - Creating display for statistics (Everybody)
# =============================================================================
        elif user_input == 2:
            
            if not data_loaded:
                print()
                print('+'+'-'*40+'+\n'+
                      '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
                      '|' + ' '*3 + 'Please load data before continuing' + ' '*3 + '|\n'+
                      '+' + '-'*40 + '+')
            else:
                statistic = ['Mean','Variance','Cross-correlation'] #string of statistics
                
                
                while True:
                    try:

                        user_input_statistic=int(input('┏' + '━'*40 + '┓\n'+
                                                    '┃Please select which statistic to display┃\n'+
                                                    '┗' + '━'*40 + '┛\n'+
                                                    "[1] Mean\n" +
                                                    "[2] Variance\n" +
                                                    "[3] Cross-correlation\n"  +
                                                    "[4] Return to the the main menu\n"+
                                                    ">>"))
                        if user_input > 4 or user_input<1:
                            print('+'+'-'*52+'+')
                            print('|' + ' '*22 + 'WARNING!' + ' '*22 + '|')
                            raise ValueError('|' + ' '*9 + 'Select a number from the  menu' + ' '*9 + '|')
                    except ValueError as e:
                        print(e)
                        print('|' + ' '*1 + 'Please try again by inserting a number from 1 to 4' + ' '*1 + '|')
                        print('+' + '-'*52 + '+')
                        
                        continue
# =============================================================================
# [2.1]Mean calculation (Prabhlin, Karen)
# =============================================================================
                    if user_input_statistic ==1:
                           
                        print('┏' + '━'*70 + '┓\n'+
                              '┃Please enter Y, Z coordinates for which you want to calculate the mean┃\n'+
                              '┗' + '━'*70 + '┛\n')
                        while True:
                            message=f'Enter Y coordinate in the range[0,{Ny})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            y=input(('Y:').strip())
                            
                            if y.isdigit():
                                y=int(y)
                                
                                #Checking if Y is not out of bound
                                if y<0 or y>=Ny:
                                    
                                    message = f'Y coordinate should be within the range[0,{Ny})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-8))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                message='Please enter integer values for Y coordinate.'
                                print()
                                print('┏' + '━'*len(message) + '┓\n'+
                                      f'┃{message}┃\n'+
                                      '┗' + '━'*len(message) + '┛\n')
                                continue
                            
                        while True:
                            message=f'Enter Z coordinate value in the range[0,{Nz})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            z=input(('Z:').strip())
                            

                            if z.isdigit():
                                z=int(z)
                                
                                #Checking if Z is not out of bound
                                if z<0 or z>=Nz:
                                    
                                    message = f'Z coordinate should be within the range [0,{Nz})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-2))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-7))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*34 + '┓\n'+
                                      '┃Please enter integer values for Z.┃\n'+
                        +              '┗' + '━'*34 + '┛\n')
                                continue
                            
                        
                           
                        mean=dataStatistics(matrix_3d, statistic[user_input_statistic - 1]) #Calling mean function to return result
                        statistics_calculated_mean = True
                        
                        message_box = f'Where {statistic[user_input_statistic-1]} value of coordinate {y,z} is: {np.round(mean[y,z],3)}'
                        print()
                        print('┏' + '━'*57 + '┓\n'+
                             f'┃The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:┃\n'+
                              '┗' + '━'*57 + '┛\n')
                        print(mean)
                        print('┏' + '━'*len(message_box) + '┓\n'+
                             f'┃{message_box}┃\n'+
                              '┗' + '━'*len(message_box) + '┛\n')
                        
                       
# =============================================================================
# [2.2] Variance calculation (Karen)                    
# =============================================================================
                        
                    elif user_input_statistic == 2:
                           
                        print('┏' + '━'*74 + '┓\n'+
                              '┃Please enter Y, Z coordinates for which you want to calculate the variance┃\n'+
                              '┗' + '━'*74 + '┛\n')
                        while True:
                            
                            message=f'Enter Y coordinate in the range[0,{Ny})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            y=input(('Y:').strip())
                            

                            if y.isdigit():
                                y=int(y)
                                
                                #Checking if Y is not out of bound
                                if y<0 or y>=Ny:
                                    
                                    message = f'Y coordinate should be within the range[0,{Ny})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-8))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                
                                message='Please enter integer values for Y coordinate.'
                                print()
                                print('┏' + '━'*len(message) + '┓\n'+
                                      f'┃{message}┃\n'+
                                      '┗' + '━'*len(message) + '┛\n')
                                continue
                            
                        while True:
                            
                            message=f'Enter Z coordinate value in the range[0,{Nz})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            z=input(('Z:').strip())
                            

                            if z.isdigit():
                                z=int(z)
                                
                                #Checking if Z is not out of bound
                                if z<0 or z>=Nz:
                                    
                                    message = f'Z coordinate should be within the range [0,{Nz})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-2))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-7))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*34 + '┓\n'+
                                      '┃Please enter integer values for Z.┃\n'+
                                      '┗' + '━'*34 + '┛\n')
                                continue
                            
                      
                        
                        variance=dataStatistics(matrix_3d, statistic[user_input_statistic - 1]) #Calling variance function to return result
                        statistics_calculated_variance = True
                        
                        message_box = f'Where {statistic[user_input_statistic-1]} value of coordinate {y,z} is: {np.round(variance[y,z],3)}'
                        print()
                        print('┏' + '━'*61 + '┓\n'+
                             f'┃The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:┃\n'+
                              '┗' + '━'*61 + '┛\n')
                        print(variance)
                        print('┏' + '━'*len(message_box) + '┓\n'+
                             f'┃{message_box}┃\n'+
                              '┗' + '━'*len(message_box) + '┛\n')
                        
# =============================================================================
# [2.3] Cross-correlation calculation (Aleksandras,Karen)
# =============================================================================

                    elif user_input_statistic == 3:
                        print('┏' + '━'*65 + '┓\n'+
                              '┃Please enter Yref, Zref, Δx values to calculate Cross-correlation┃\n'+
                              '┗' + '━'*65 + '┛\n')
                        while True:
                            
                            message=f'Enter Yref value in the range [0,{Ny})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            Yref=input(('Yref:').strip())
                            
                            if Yref.isdigit():
                                Yref=int(Yref)
                                
                                #Checking if Yref is not out of bound
                                if Yref<0 or Yref>=Ny:
                                    
                                    message = f'Yref should be within the range[0,{Ny})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-8))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*37 + '┓\n'+
                                      '┃Please enter integer values for Yref.┃\n'+
                                      '┗' + '━'*37 + '┛\n')
                                continue
                            
                        while True:
                            
                            message=f'Enter Zref value in the range[0,{Nz})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            Zref=input(('Zref:').strip())
                                                       
                            if Zref.isdigit():
                                Zref=int(Zref)
                                
                                #Checking if Zref is not out of bound
                                if Zref<0 or Zref>=Nz:
                                    
                                    message = f'Zref should be within the range[0,{Nz})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-8))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*37 + '┓\n'+
                                      '┃Please enter integer values for Zref.┃\n'+
                                      '┗' + '━'*37 + '┛\n')
                                continue
                            
                        while True:
                            
                            message=f'Enter Δx value in the range[0,{Nx})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            DeltaX=input(('Δx:').strip())
                            

                            
                            if DeltaX.isdigit():
                                DeltaX=int(DeltaX)
                                
                                #Checking if DeltaX is not out of bound
                                if DeltaX<0 or DeltaX>=Nx:
                                    
                                    message = f'Δx should be within the range[0,{Nx})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-8))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*35 + '┓\n'+
                                      '┃Please enter integer values for Δx.┃\n'+
                                      '┗' + '━'*35 + '┛\n')
                            
                        print('┏' + '━'*83 + '┓\n'+
                              '┃Please enter Y, Z coordinates for which you want to calculate the cross correlation┃\n'+
                              '┗' + '━'*83 + '┛\n')
                        while True:
                            
                            message=f'Enter Y coordinate in the range[0,{Ny})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            y=input(('Y:').strip())
                            

                            if y.isdigit():
                                y=int(y)
                                
                                #Checking if Y is not out of bound
                                if y<0 or y>=Ny:
                                    
                                    message = f'Y coordinate should be within the range[0,{Ny})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-3))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-8))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*45 + '┓\n'+
                                      '┃Please enter integer values for Y coordinate.┃\n'+
                                      '┗' + '━'*45 + '┛\n')
                                continue
                            
                        while True:
                            
                            message=f'Enter Z coordinate value in the range[0,{Nz})'
                            
                            print('┏' + '━'*len(message) + '┓\n'+
                                 f'┃{message}┃\n'+
                                  '┗' + '━'*len(message) + '┛\n')
                            
                            z=input(('Z:').strip())
                            

                            if z.isdigit():
                                z=int(z)
                                
                                #Checking if Z is not out of bound
                                if z<0 or z>=Nz:
                                    
                                    message = f'Z coordinate should be within the range [0,{Nz})'
                                    padding = (len(message) // 2)
                                    print('+' + '-' * len(message) + '+\n' +
                                          f'|{(" " * (padding-3))}ERROR!{(" " * (padding-2))}|\n' +
                                          f'|{message}|\n' +
                                          f'|{(" " * (padding-7))}Please try again{(" " * (padding-8))}|\n'
                                          '+' + '-' * len(message) + '+')                  
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*34 + '┓\n'+
                                      '┃Please enter integer values for Z.┃\n'+
                                      '┗' + '━'*34 + '┛\n')
                                continue
                            
                        cross_cor=dataStatistics(matrix_3d, statistic[user_input_statistic - 1], Yref, Zref, DeltaX)

                        
                        message_box = f'Where {statistic[user_input_statistic-1]} value of coordinate {y,z} is: {np.round(cross_cor[y,z],3)}'
                        print()
                        print('┏' + '━'*70 + '┓\n'+
                             f'┃The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:┃\n'+
                              '┗' + '━'*70 + '┛\n')
                        print(cross_cor)
                        print('┏' + '━'*len(message_box) + '┓\n'+
                             f'┃{message_box}┃\n'+
                              '┗' + '━'*len(message_box) + '┛\n') 
                        
# =============================================================================
# [2.4] Return to the main menu (Everybody)                            
# =============================================================================

                    elif user_input_statistic == 4:
                        break
    
                    else:
                        
                        
                        message = 'Please select an existing statistical function'
                        padding = (len(message) // 2)
                        print('+' + '-' * len(message) + '+\n' +
                              f'|{(" " * (padding-4))}WARNING!{(" " * (padding-4))}|\n' +
                              f'|{message}|\n' +
                              '+' + '-' * len(message) + '+')
                               
# =============================================================================
#                           [3]rd selection - Generating plot
# =============================================================================

# =============================================================================
#                               Creating Menu for Plots 
# =============================================================================
        elif user_input == 3:
            if not data_loaded:
                print()
                print('+'+'-'*40+'+\n'+
                      '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
                      '|' + ' '*3 + 'Please load data before continuing' + ' '*3 + '|\n'+
                      '+' + '-'*40 + '+')
           
            else:
                plots=['Mean','Variance','Cross-Correlation']
                
                while True:
                    try:

                        user_input_plot=int(input('┏' + '━'*40 + '┓\n'+
                                                '┃' + ' '*2 + 'Please select which plot to generate' + ' '*2 + '┃\n'+
                                                '┗' + '━'*40 + '┛\n'+
                                                "[1] Mean\n" +
                                                "[2] Variance\n" +
                                                "[3] Cross-Correlation\n"  +
                                                "[4] Return to the the main menu\n"+
                                                ">>"))
                        if user_input > 4 or user_input<1:
                                print('+'+'-'*52+'+')
                                print('|' + ' '*22 + 'WARNING!' + ' '*22 + '|')
                                raise ValueError('|' + ' '*9 + 'Select a number from the  menu' + ' '*9 + '|')
                    except ValueError as e:
                            print(e)
                            print('|' + ' '*1 + 'Please try again by inserting a number from 1 to 4' + ' '*1 + '|')
                            print('+' + '-'*52 + '+')
                        
                            continue
# =============================================================================
# [3.1] Mean Plot (Prabhlin)
# =============================================================================
                    if user_input_plot ==1:
                        if not statistics_calculated_mean:
                            print()
                            print('+'+'-'*54+'+\n'+
                                  '|' + ' '*23 + 'WARNING!' + ' '*23 + '|\n'+
                                  '|' + ' '*1 + 'Please do mean statistic calculation before plotting' + ' '*1 + '|\n'+
                                  '+' + '-'*54 + '+')
                        else:
                            plot_data=dataPlot(mean,plots[user_input_plot-1])

# =============================================================================
# [3.2] Variance Plot (Karen)
# =============================================================================
                        
                    elif user_input_plot == 2:
                        if not statistics_calculated_variance:
                            print()
                            print('+'+'-'*58+'+\n'+
                                  '|' + ' '*25 + 'WARNING!' + ' '*25 + '|\n'+
                                  '|' + ' '*1 + 'Please do variance statistic calculation before plotting' + ' '*1 + '|\n'+
                                  '+' + '-'*58 + '+')
                        else:
                            plot_data=dataPlot(variance, plots[user_input_plot-1])
                            
# =============================================================================
# [3.3] Cross-correlation plot (Aleksandras)
# =============================================================================
                     
                    elif user_input_plot == 3:
                        if Yref is None or Zref is None or DeltaX is None:
                            print()
                            print('+'+'-'*55+'+\n'+
                                  '|' + ' '*23 + 'WARNING!' + ' '*24 + '|\n'+
                                  '|' + ' '*1 + 'Please do cross-correlation statistic before plotting' + ' '*1 + '|\n'+
                                  '+' + '-'*55 + '+')
                        else:
                            plot_data=dataPlot(cross_cor, plots[user_input_plot - 1])
                            
# =============================================================================
# [3.4] Return back to the Main menu (Everybody)
# =============================================================================

                    elif user_input_plot ==4:
                        break
                    
                    else:
                        print('+'+'-'*39+'+\n'+
                              '|' + ' '*16 + 'WARNING!' + ' '*15 + '|\n'+
                              '|Please select an existing plot function|\n'+
                              '+' + '-'*39 + '+')
                       
# =============================================================================
# [4] Quiting the program (Everybody)
# =============================================================================

        if user_input == 4:
            print()
            print('The program has been terminated')
            break
                
            
                