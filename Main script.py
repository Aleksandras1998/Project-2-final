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
    #statistics_calculated=False
    
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

                print('+'+'-'*52+'+')
                print('|' + ' '*22 + 'WARNING!' + ' '*22 + '|')
                raise ValueError('|' + ' '*9 + 'Select a number from the Main menu' + ' '*9 + '|')
        except ValueError as e:
            print(e)
            print('|' + ' '*1 + 'Please try again by inserting a number from 1 to 4' + ' '*1 + '|')
            print('+' + '-'*52 + '+')
            
            continue
# =============================================================================
# [1]st selection-Uploading 3D array from binary file
# =============================================================================
        if user_input == 1:
            matrix_3d=dataLoader()
            if matrix_3d is not None:
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
                        mean=dataStatistics(matrix_3d, statistic[user_input_statistic - 1]) #Calling mean function to return result
                        print()
                        print('┏' + '━'*57 + '┓\n'+
                             f'┃The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:┃\n'+
                              '┗' + '━'*57 + '┛\n')
                        print(mean) #Printing result
                        #statistics_calculated=True
                        
                    elif user_input_statistic == 2:
                        variance=dataStatistics(matrix_3d, statistic[user_input_statistic - 1])
                        print()
                        print('┏' + '━'*61 + '┓\n'+
                             f'┃The {statistic[user_input_statistic-1]} values for each point in the Ny x Nz matrix are:┃\n'+
                              '┗' + '━'*61 + '┛\n')
                        print(variance)
                        #statistics_calculated=True
                        
                    elif user_input_statistic == 3:
                        print('┏' + '━'*65 + '┓\n'+
                              '┃Please enter Yref, Zref, Δx values to calculate Cross-correlation┃\n'+
                              '┗' + '━'*65 + '┛\n')
                        while True:
                            Yref=input('┏' + '━'*36 + '┓\n'+
                                      f'┃Enter Yref value in the range [0,{Ny})┃\n'+
                                       '┗' + '━'*36+ '┛\n'+
                                       'Yref:').strip()
                            if Yref.isdigit():
                                Yref=int(Yref)
                                
                                #Checking if Yref is not out of bound
                                if Yref<0 or Yref>=Ny:
                                    print('+' + '-' * 37 + '+\n' +
                                          '|' + ' ' * 15 + 'ERROR!' + ' ' * 16 + '|\n' +
                                         f'|Yref should be within the range[0,{Ny})|\n'+
                                          '|' + ' '*10 + ' Please try again' + ' '*10 + '|\n'+
                                          '+' + '-' * 37 + '+')
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
                            Zref=input('┏' + '━'*37 + '┓\n'+
                                      f'┃Enter Zref value in the range[0,{Nz})┃\n'+
                                       '┗' + '━'*37+ '┛\n'+
                                       'Zref:').strip()
                            if Zref.isdigit():
                                Zref=int(Zref)
                                
                                #Checking if Zref is not out of bound
                                if Zref<0 or Zref>=Nz:
                                    print('+' + '-' * 39 + '+\n' +
                                          '|' + ' ' * 16 + 'ERROR!' + ' ' * 17 + '|\n' +
                                         f'|Zref should be within the range[0,{Nz})|\n'+
                                          '|' + ' '*11 + ' Please try again' + ' '*11 + '|\n'+
                                          '+' + '-' * 39 + '+')
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
                            DeltaX=input('┏' + '━'*33 + '┓\n'+
                                        f'┃Enter Δx value in the range[0,{Nx})┃\n'+
                                         '┗' + '━'*33+ '┛\n'+
                                         'Δx:').strip()
                            if DeltaX.isdigit():
                                DeltaX=int(DeltaX)
                                
                                #Checking if DeltaX is not out of bound
                                if DeltaX<0 or DeltaX>=Nx:
                                    print('+' + '-' * 35 + '+\n' +
                                          '|' + ' ' * 14 + 'ERROR!' + ' ' * 15 + '|\n' +
                                         f'|Δx should be within the range[0,{Nx})|\n'+
                                          '|' + ' '*9 + ' Please try again' + ' '*9 + '|\n'+
                                          '+' + '-' * 35 + '+')
                                    continue 
                                else:
                                    break
                            else:
                                print()
                                print('┏' + '━'*35 + '┓\n'+
                                      '┃Please enter integer values for Δx.┃\n'+
                                      '┗' + '━'*35 + '┛\n')
                            continue
                            
                        cross_cor=dataStatistics(matrix_3d, statistic[user_input_statistic - 1], Yref, Zref, DeltaX)
                        print()
                        print('┏' + '━'*33 + '┓\n'+
                             f'┃The {statistic[user_input_statistic-1]} values are:┃\n'+
                              '┗' + '━'*33 + '┛\n')
                        print(cross_cor)
                        #statistics_calculated=True
                            

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
                      '+' + '-'*40 + '+') 
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
                
            
                