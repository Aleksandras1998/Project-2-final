#small 3D array.bin Nx=6 Ny=5 Nz=4
#turbine_32x32x8192.bin Nx=8192 Ny=32 Nz=32

from Data_loader import dataLoader 
from Function_file import dataStatistics, dataPlot

if __name__=='__main__':

# =============================================================================
#               Here we are creating User interaction Main menu
# =============================================================================
    Nx=0
    Ny=0
    Nz=0
    data_loaded=False
    Yref=None
    Zref=None
    DeltaX=None
    
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
            if user_input >4 or user_input<1:

                print('+'+'-'*40+'+')
                print('|' + ' '*16 + 'WARNING!' + ' '*16 + '|')
                raise ValueError('|' + ' '*3 + 'Select a number from the Main menu' + ' '*3 + '|')
        except ValueError as e:
            print(e)
            print('|' + ' '*12 + 'Please try again by inserting a number from 1 to 4' + ' '*12 + '|')
            print('+' + '-'*40 + '+')
            
            continue
# =============================================================================
# [1]st selection-Uploading 3D array from binary file
# =============================================================================
        if user_input == 1:
            matrix_3d=dataLoader()
            if matrix_3d is not None:
                print(f'{matrix_3d.shape[2]}')
                print(f'{matrix_3d.shape[1]}')
                print(f'{matrix_3d.shape[0]}')
                Nx=matrix_3d.shape[2]
                Ny=matrix_3d.shape[1]
                Nz=matrix_3d.shape[0]
                data_loaded=True

# =============================================================================
# [2]nd selection - Creating display for statistics
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
                    user_input_statistic=int(input('┏' + '━'*40 + '┓\n'+
                                                   '┃Please select which statistic to display┃\n'+
                                                   '┗' + '━'*40 + '┛\n'+
                                                   "[1] Mean\n" +
                                                   "[2] Variance\n" +
                                                   "[3] Cross-correlation\n"  +
                                                   "[4] Return to the the main menu\n"+
                                                   ">>"))
                    if user_input_statistic ==1:
                        mean=dataStatistics(matrix_3d, statistic[user_input_statistic - 1])
                        print()
                        print(f'The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:\n')
                        print(mean)
                        #statistics_calculated=True
                    elif user_input_statistic == 2:
                        variance=dataStatistics(matrix_3d, statistic[user_input_statistic - 1])
                        print()
                        print(f'The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:\n')
                        print(variance)
                        #statistics_calculated=True
                        
                    elif user_input_statistic == 3:
                        print('┏' + '━'*38 + '┓\n'+
                              '┃Please enter Yref, Zref, DeltaX values┃\n'+
                              '┗' + '━'*38 + '┛\n')
                        while True:
                            Yref=input(f'Please enter Yref value in the range[0,{Ny}).\n'+
                                       'Yref:').strip()
                            if Yref.isdigit():
                                Yref=int(Yref)
                                
                                #Checking if Yref is not out of bound
                                if Yref<0 or Yref>=Ny:
                                    print(f'Error: Zref should be within the range[0,{Ny}). Please try again')
                                    continue 
                                else:
                                    break
                            else:
                                print('┏' + '━'*40 + '┓\n'+
                                      '┃Please enter integer values for Yref.┃\n'+
                                      '┗' + '━'*40 + '┛\n')
                                continue
                            
                        while True:
                            Zref=input(f'Please enter Zref value in the range[0,{Nz}).\n'+
                                       'Zref:').strip()
                            if Zref.isdigit():
                                Zref=int(Zref)
                                
                                #Checking if Zref is not out of bound
                                if Zref<0 or Zref>=Nz:
                                    print(f'Error: Zref should be within the range[0,{Nz}). Please try again')
                                    continue 
                                else:
                                    break
                            else:
                                print('┏' + '━'*40 + '┓\n'+
                                      '┃Please enter integer values for Zref.┃\n'+
                                      '┗' + '━'*40 + '┛\n')
                                continue
                            
                        while True:
                            DeltaX=input(f'Please enter DeltaX value in the range[0,{Nx}).\n'+
                                       'DeltaX:').strip()
                            if DeltaX.isdigit():
                                DeltaX=int(DeltaX)
                                
                                #Checking if DeltaX is not out of bound
                                if DeltaX<0 or DeltaX>=Nx:
                                    print(f'Error: DeltaX should be within the range[0,{Nx}). Please try again')
                                    continue 
                                else:
                                    break
                        else:
                            print('┏' + '━'*40 + '┓\n'+
                                  '┃Please enter integer values for DeltaX.┃\n'+
                                  '┗' + '━'*40 + '┛\n')
                            continue
                            
                        cross_cor=dataStatistics(matrix_3d, statistic[user_input_statistic - 1], Yref, Zref, DeltaX)
                        print()
                        print(f'The {statistic[user_input_statistic-1]} are:\n')
                        print(cross_cor)
                        #statistics_calculated=True
                            
                            
                            
                            
                            # Zref=input('Zref: ').strip()
                            # DeltaX=input('DeltaX: ').strip()
                            # if Yref.isdigit() and Zref.isdigit() and DeltaX.isdigit():
                            #     Yref=int(Yref)
                            #     Zref=int(Zref)
                            #     DeltaX=int(DeltaX)
                            #     cross_cor=dataStatistics(matrix_3d, statistic[user_input_statistic - 1], Yref, Zref, DeltaX)
                            #     print()
                            #     print(f'The {statistic[user_input_statistic-1]} are:\n')
                            #     print(cross_cor)
                            #     #statistics_calculated=True
                            #     break
                            # else:
                            #     print('┏' + '━'*40 + '┓\n'+
                            #           '┃Please enter integer values for Yref, Zref, and DeltaX.┃\n'+
                            #           '┗' + '━'*40 + '┛\n')
                            #     continue

                    elif user_input_statistic == 4:
                        break
    
                    else:
                        print('+'+'-'*46+'+\n'+
                              '|' + ' '*19 + 'WARNING!' + ' '*19 + '|\n'+
                              '|Please select an existing statistical function|\n'+
                              '+' + '-'*46 + '+')
                              
# =============================================================================
# #[3]rd selection - Generating plot
# =============================================================================
        elif user_input == 3:
            if not data_loaded:
                print()
                print('+'+'-'*40+'+\n'+
                      '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
                      '|' + ' '*3 + 'Please load data before continuing' + ' '*3 + '|\n'+
                      '+' + '-'*40 + '+') #if not, print
            # elif not statistics_calculated:
            #     print()
            #     print('+'+'-'*40+'+\n'+
            #           '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
            #           '|' + ' '*3 + 'Please do statistic calculations before plotting' + ' '*3 + '|\n'+
            #           '+' + '-'*40 + '+') # change description of an error to 'Please do cross-correlation statistics before generating plot'
            else:
                plots=['Mean','Variance','Cross-Correlation']
                
                while True:
                    user_input_plot=int(input('┏' + '━'*40 + '┓\n'+
                                              '┃' + ' '*2 + 'Please select which plot to generate' + ' '*2 + '┃\n'+
                                              '┗' + '━'*40 + '┛\n'+
                                              "[1] Mean\n" +
                                              "[2] Variance\n" +
                                              "[3] Cross-Correlation\n"  +
                                              "[4] Return to the the main menu\n"+
                                              ">>"))
                    if user_input_plot ==1:
                        #plot_data=dataPlot(mean,plots[user_input_plot-1]) # is used in case if we want to prevent plot generation before statistics calculations (uncomment 'statistics_calcualted=True' ↑)
                        mean_values=dataStatistics(matrix_3d, plots[user_input_plot - 1])
                        plot_data = dataPlot(mean_values,plots[user_input_plot-1])
                        
                    elif user_input_plot == 2:
                        #plot_data=dataPlot(variance, plots[user_input_plot-1])
                        variance_values=dataStatistics(matrix_3d, plots[user_input_plot - 1])
                        plot_data = dataPlot(variance_values,plots[user_input_plot-1])
                      
                    elif user_input_plot == 3:
                        if Yref is None or Zref is None or DeltaX is None:
                            print()
                            print('+'+'-'*40+'+\n'+
                                  '|' + ' '*16 + 'WARNING!' + ' '*16 + '|\n'+
                                  '|' + ' '*3 + 'Please do cross-correlation statistic before plotting' + ' '*3 + '|\n'+
                                  '+' + '-'*40 + '+')
                        else:
                            plot_data=dataPlot(cross_cor, plots[user_input_plot - 1])
                    elif user_input_plot ==4:
                        break
                    else:
                        print('+'+'-'*39+'+\n'+
                              '|' + ' '*16 + 'WARNING!' + ' '*15 + '|\n'+
                              '|Please select an existing plot function|\n'+
                              '+' + '-'*39 + '+')
                       

        if user_input == 4:
            print()
            print('The program has been terminated')
            break
                
            
                