import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing Data from CSV file

df=pd.read_csv('Monthly_Average_Rainfall_Districtwise_2012.csv')

dis=df['District']
jan=df['Monthly Rainfall - January']
feb=df['Monthly Rainfall - February']
mar=df['Monthly Rainfall - March']
apr=df['Monthly Rainfall - April']
may=df['Monthly Rainfall - May']
jun=df['Monthly Rainfall - June']
jul=df['Monthly Rainfall - July']
aug=df['Monthly Rainfall - August']
sep=df['Monthly Rainfall - September']
ocb=df['Monthly Rainfall - October']
nov=df['Monthly Rainfall - November']
dec=df['Monthly Rainfall - December']
tot=df['Annual 2012 - Total']




#Main Menu (An Overview)

def mainmenu():
    choice=0
    while choice !='d':
        print('I-----------------------------------I')
        print('I    MONTHLY RAINFALL - HARYANA     I')
        print('I-----------------------------------I')
        print('I a) Display Data                   I')
        print('I b) Data Visualization             I')
        print('I c) Data Analysis                  I')
        print('I d) Exit                           I')
        print('I-----------------------------------I')
        choice=input('Your Option')
        if choice=='a':
            print('Displaying Data')
            print(df)
            print(df.District)
        elif choice=='b':
            submenu2()
        elif choice=='c':
            submenu3()
        elif choice=='d':
            print('successfully exited from the menu')
        else:
            print('wrong input')


def submenu2():
        print('I------------------------------------------I')
        print('I       DATA VISUALISATION MENU            I')
        print('I------------------------------------------I')
        print('I 1) Line Graph                            I')
        print('I 2) Bar plot of Total Rainfall            I')
        print('I 3) Horizontal Bar Plot of Total Rainfall I')
        print('I 4) Histogram Plot                        I')
        print('I 5) Horizontal Histogram Plot             I')
        print('I 6) Pie Chart                             I')
        print('I 7) Go Back to the Mainmenu               I')
        print('I------------------------------------------I')
        ch2=int(input('Choose Your Option'))
        if ch2==1:
            #Line Garph
            plt.plot(dis,jan,color='#59114D',marker='o',markerfacecolor='black',label='Rain in January',markersize=3,linewidth=1)
            plt.plot(dis,feb,color='#E98A15',marker='o',markerfacecolor='black',label='Rain in February',markersize=3,linewidth=1)
            plt.plot(dis,mar,color='#020122',marker='o',markerfacecolor='black',label='Rain in March',markersize=3,linewidth=1)
            plt.plot(dis,apr,color='k',marker='o',markerfacecolor='black',label='Rain in April',markersize=3,linewidth=1)
            plt.plot(dis,may,color='#EBCBF4',marker='o',markerfacecolor='black',label='Rain in May',markersize=3,linewidth=1)
            plt.plot(dis,jun,color='#E2AEDD',marker='o',markerfacecolor='black',label='Rain in June',markersize=3,linewidth=1)
            plt.plot(dis,jul,color='#2E0E02',marker='o',markerfacecolor='black',label='Rain in July',markersize=3,linewidth=1)
            plt.plot(dis,aug,color='#832161',marker='o',markerfacecolor='black',label='Rain in August',markersize=3,linewidth=1)
            plt.plot(dis,sep,color='#76E7CD',marker='o',markerfacecolor='black',label='Rain in September',markersize=3,linewidth=1)
            plt.plot(dis,ocb,color='#FF8966',marker='o',markerfacecolor='black',label='Rain in October',markersize=3,linewidth=1)
            plt.plot(dis,nov,color='#E5446D',marker='o',markerfacecolor='black',label='Rain in November',markersize=3,linewidth=1)
            plt.plot(dis,dec,color='#BED558',marker='o',markerfacecolor='black',label='Rain in December',markersize=3,linewidth=1)
            plt.title('Rain in Haryana',fontsize=15)
            plt.xlabel('Month Name',fontsize=15)
            plt.ylabel('Rain in an Year',fontsize=15)
            plt.legend()
            plt.xticks(np.arange(0,21,1),fontsize=9,rotation=30)
            plt.grid(True)
            plt.show()

        elif ch2==2:
            c=['#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF']
            plt.bar(dis,tot,label='Total Rainfall',color=c)
            plt.grid(False)
            plt.legend
            plt.xlabel('Districts',fontsize=15)
            plt.xticks(fontsize=9,rotation=30)
            plt.ylabel('Rainfall in mm',fontsize=15)
            plt.title('Rain in Haryana',fontsize=20)
            plt.show()

        elif ch2==3:
            #Horizontal Bar Chart
            c=['#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF','#320E3B','#7BE0AD','#FFB7C3','#BCF4DE','#313638','#F06543','#F09D51','#7F96FF']
            plt.barh(dis,tot,label='Total Rainfall',color=c)
            plt.grid(False)
            plt.legend
            plt.xlabel('Rainfall in mm',fontsize=15)
            plt.xticks(fontsize=9)
            plt.ylabel('Districts',fontsize=15)
            plt.title('Rain in Haryana',fontsize=20)
            plt.show()

        elif ch2==4:
            #Histogram Plot
            plt.hist(tot,bins=6,label='Rainfall Levels',edgecolor='#EDD382',color='#FC9E4F')
            plt.xlabel('Annual Rainfall in mm',fontsize=15)
            plt.ylabel('Number of Districts',fontsize=15)
            plt.title('Histogram of Annual Rainfall',fontsize=20)
            plt.show()
            plt.legend(loc='upper right')

        elif ch2==5:
            #Horizontal Histogram Plot
            plt.hist(tot,bins=6,label='Rainfall Levels',edgecolor='#EFAAC4',color='#FFC4D1',orientation='horizontal',rwidth=1)
            plt.xlabel('Annual Rainfall in mm',fontsize=15)
            plt.ylabel('Number of Districts',fontsize=15)
            plt.title('Histogram of Annual Rainfall',fontsize=20)
            plt.show()
            plt.legend(loc='upper right')

        elif ch2==6:
            #Pie Chart
            plt.pie(tot,labels=dis,radius=1.2,autopct='%0.0f%%',shadow=False,explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
            plt.show()      
        elif ch2==7:
            mainmenu()
            
        else:
            print('Invalid Option')

def submenu3():
    print('I*********************************************************************************I')
    print('I                             DATA ANAYLSIS MENU                                  I')
    print('I*********************************************************************************I')
    print('I 1.Find the maximum,minimum,mean,sum of - Monthly Rainfall                       I')
    print('I 2.Display the name of those 3 states which have highest rainfall in January     I')
    print('I 3.Display the name of those 3 states which have highest rainfall in February    I')
    print('I 4.Display the name of those 3 states which have highest rainfall in March       I')
    print('I 5.Display the name of those 3 states which have highest rainfall in April       I')
    print('I 6.Display the name of those 3 states which have highest rainfall in May         I')
    print('I 7.Display the name of those 3 states which have highest rainfall in June        I')
    print('I 8.Display the name of those 3 states which have highest rainfall in July        I')
    print('I 9.Display the name of those 3 states which have highest rainfall in August      I')
    print('I 10.Display the name of those 3 states which have highest rainfall in September  I')
    print('I 11.Display the name of those 3 states which have highest rainfall in October    I')
    print('I 12.Display the name of those 3 states which have highest rainfall in November   I')
    print('I 13.Display the name of those 3 states which have highest rainfall in December   I')
    print('I 14.Display the name of those 3 states which have lowest rainfall in January     I')
    print('I 15.Display the name of those 3 states which have lowest rainfall in February    I')
    print('I 16.Display the name of those 3 states which have lowest rainfall in March       I')
    print('I 17.Display the name of those 3 states which have lowest rainfall in April       I')
    print('I 18.Display the name of those 3 states which have lowest rainfall in May         I')
    print('I 19.Display the name of those 3 states which have lowest rainfall in June        I')
    print('I 20.Display the name of those 3 states which have lowest rainfall in July        I')
    print('I 21.Display the name of those 3 states which have lowest rainfall in August      I')
    print('I 22.Display the name of those 3 states which have lowest rainfall in September   I')
    print('I 23.Display the name of those 3 states which have lowest rainfall in October     I')
    print('I 24.Display the name of those 3 states which have lowest rainfall in November    I')
    print('I 25.Display the name of those 3 states which have lowest rainfall in December    I')
    print('I 26.Display the name of those 5 states which have highest annual rainfall        I')
    print('I 27.Display the name of those 5 states which have lowest annual rainfall         I')
    print('I 28.I Quantile,II Quantile and III Quantile of Annual Rainfall                   I')
    print('I 29.Pivot Table - Annual Rainfall Analysis                                       I')
    print('I 30.To export csv file                                                           I')
    print('I 31.Back to main menu                                                            I')
    print('I*********************************************************************************I')
    k=int(input('\nChoose a option for data analysis'))
    if k == 1:
        print('maximum,minimum,mean,sum of - Monthly Rainfall')
        print(df.aggregate({'Monthly Rainfall - January':['max','min','mean','sum'],'Monthly Rainfall - February':['max','min','mean','sum'],'Monthly Rainfall - March':['max','min','mean','sum'],'Monthly Rainfall - April':['max','min','mean','sum'],'Monthly Rainfall - May':['max','min','mean','sum'],'Monthly Rainfall - June':['max','min','mean','sum'],'Monthly Rainfall - July':['max','min','mean','sum'],'Monthly Rainfall - August':['max','min','mean','sum'],'Monthly Rainfall - September':['max','min','mean','sum'],'Monthly Rainfall - October':['max','min','mean','sum'],'Monthly Rainfall - November':['max','min','mean','sum'],'Monthly Rainfall - December':['max','min','mean','sum']}))
    elif k==2:
              print('Name of those 3 states which have highest rainfall in January')
              print(df.sort_values('Monthly Rainfall - January',ascending=False).head(3))
    elif k==3:
              print('Name of those 3 states which have highest rainfall in February')
              print(df.sort_values('Monthly Rainfall - February',ascending=False).head(3))
    elif k==4:
              print('Name of those 3 states which have highest rainfall in March')
              print(df.sort_values('Monthly Rainfall - March',ascending=False).head(3))
    elif k==5:
              print('Name of those 3 states which have highest rainfall in April')
              print(df.sort_values('Monthly Rainfall - April',ascending=False).head(3))
    elif k==6:
              print('Name of those 3 states which have highest rainfall in May')
              print(df.sort_values('Monthly Rainfall - May',ascending=False).head(3))
    elif k==7:
              print('Name of those 3 states which have highest rainfall in June')
              print(df.sort_values('Monthly Rainfall - June',ascending=False).head(3))
    elif k==8:
              print('Name of those 3 states which have highest rainfall in July')
              print(df.sort_values('Monthly Rainfall - July',ascending=False).head(3))
    elif k==9:
              print('Name of those 3 states which have highest rainfall in August')
              print(df.sort_values('Monthly Rainfall - August',ascending=False).head(3))
    elif k==10:
              print('Name of those 3 states which have highest rainfall in September')
              print(df.sort_values('Monthly Rainfall - September',ascending=False).head(3))
    elif k==11:
              print('Name of those 3 states which have highest rainfall in October')
              print(df.sort_values('Monthly Rainfall - October',ascending=False).head(3))
    elif k==12:
              print('Name of those 3 states which have highest rainfall in November')
              print(df.sort_values('Monthly Rainfall - November',ascending=False).head(3))
    elif k==13:
              print('Name of those 3 states which have highest rainfall in December')
              print(df.sort_values('Monthly Rainfall - December',ascending=False).head(3))  
    elif k ==14:
            print('Name of those 3 states which have lowest rainfall in January')
            print(df.sort_values('Monthly Rainfall - February',ascending=True).head(3))
    elif k==15:
              print('Name of those 3 states which have lowests rainfall in February')
              print(df.sort_values('Monthly Rainfall - February',ascending=True).head(3))
    elif k==16:
              print('Name of those 3 states which have lowest rainfall in March')
              print(df.sort_values('Monthly Rainfall - March',ascending=True).head(3))
    elif k==17:
              print('Name of those 3 states which have lowest rainfall in April')
              print(df.sort_values('Monthly Rainfall - April',ascending=True).head(3))
    elif k==18:
              print('Name of those 3 states which have lowest rainfall in May')
              print(df.sort_values('Monthly Rainfall - May',ascending=True).head(3))
    elif k==19:
              print('Name of those 3 states which have lowest rainfall in June')
              print(df.sort_values('Monthly Rainfall - June',ascending=True).head(3))
    elif k==20:
              print('Name of those 3 states which have lowest rainfall in July')
              print(df.sort_values('Monthly Rainfall - July',ascending=True).head(3))
    elif k==21:
              print('Name of those 3 states which have lowest rainfall in August')
              print(df.sort_values('Monthly Rainfall - August',ascending=True).head(3))
    elif k==22:
              print('Name of those 3 states which have lowest rainfall in September')
              print(df.sort_values('Monthly Rainfall - September',ascending=False).tail(3))
    elif k==23:
              print('Name of those 3 states which have lowest rainfall in October')
              print(df.sort_values('Monthly Rainfall - October',ascending=False).tail(3))
    elif k==24:
              print('Name of those 3 states which have lowest rainfall in November')
              print(df.sort_values('Monthly Rainfall - November',ascending=False).tail(3))
    elif k==25:
              print('Name of those 3 states which have lowest rainfall in December')
              print(df.sort_values('Monthly Rainfall - December',ascending=False).tail(3))
    elif k==26:
              print('Name of those 5 states which have highest annual rainfall')
              print(df.sort_values('Annual 2012 - Total',ascending=False).head(5))
    elif k==27:
              print('Name of those 5 states which have lowest annual rainfall')
              print(df.sort_values('Annual 2012 - Total',ascending=False).tail(5))              
    elif k ==28:
             print('I Quantile,II Quantile and III Quantile of Annual Rainfall')
             print(df['Annual 2012 - Total'].quantile([0.25,0.50,0.75]))              
    elif k ==29:
             print('Pivot Table - Annual Rainfall Analysis')
             print(df.pivot_table(index= 'District', values= "Annual 2012 - Total"))
    elif k==30:
             df.to_csv(r'C:Users\user\Desktop\Monthly Rainfall.csv')
    elif k ==31:
               mainmenu()              
    else:
         print('Wrong input try again')                              
           
mainmenu()    
