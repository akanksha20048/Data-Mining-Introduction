import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pd.read_json('https://api.covid19india.org/states_daily.json') 

states = pd.read_json( (data['states_daily']).to_json(), orient='index')
states.drop(['un'],axis=1,inplace=True)


dict1={"mh":"Maharashtra",
 "mn":"Manipur","ml":"Meghalaya","mz":"Mizoram","nl":"Nagaland","or":"Odisha","py":"Puducherry","pb":"Punjab",	"rj":"Rajasthan","sk":"Sikkim","tn":"Tamil Nadu",	"tg":"Telangana","tr":"Tripura","up":"Uttar Pradesh",	"ut":"Uttarakhand",	"wb":"West Bengal","tt":"Total",	"la":"Ladakh","an":	"Andaman and Nicobar Islands","ap":	"Andhra Pradesh","ar":	"Arunachal Pradesh","as":	"Assam","br":	"Bihar","ch":	"Chandigarh","ct":	"Chhattisgarh","dn":	"Dadra and Nagar Haveli","dd":	"Daman and Diu","dl":	"Delhi","ga":	"Goa","gj":	"Gujarat","hr":"Haryana","hp":"Himachal Pradesh","jk":"Jammu and Kashmir","jh":"Jharkhand","ka":"Karnataka","kl":"Kerala","ld":"Lakshadweep","mp":"Madhya Pradesh",
}

states.rename(columns=dict1, inplace=True)
type(states.columns)




def Q1_1(json_file_path, start_date, end_date):
    
    finalDataFrame = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    result= finalDataFrame.groupby(['status'])['Total'].sum()
    confirmed_count = result[0]
    recovered_count = result[1]
    deceased_count = result[2]
    print('confirmed_count: ',confirmed_count, 'recovered_count: ',recovered_count, 'deceased_count: ',deceased_count)
    return confirmed_count, recovered_count, deceased_count

def Q1_2(json_file_path, start_date, end_date):

    finalDataFrame = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    q2 = finalDataFrame.groupby(['status'])['Delhi'].sum()
    confirmed_count = q2[0]
    recovered_count = q2[1]
    deceased_count = q2[2]
    print('confirmed_count: ',confirmed_count, 'recovered_count: ',recovered_count, 'deceased_count: ',deceased_count)
    return confirmed_count, recovered_count, deceased_count

def Q1_3(json_file_path, start_date, end_date):

    finalDataFrame = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    q3 = finalDataFrame.groupby(['status'])[['Delhi','Maharashtra']].sum()
    sum=q3['Delhi']+q3['Maharashtra']
    q3['Total']=sum
    q3=q3.drop(['Delhi','Maharashtra'],axis=1)
    q3= q3[:].values
    confirmed_count = q3[0]
    recovered_count = q3[1]
    deceased_count = q3[2]
    print('confirmed_count: ',confirmed_count, 'recovered_count: ',recovered_count, 'deceased_count: ',deceased_count)
    return confirmed_count, recovered_count, deceased_count

def Q1_4(json_file_path, start_date, end_date):

    finalDataFrame = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    q4 = finalDataFrame.groupby(['status']).sum()
    q4=q4.drop(['Daman and Diu','Lakshadweep', 'Andaman and Nicobar Islands','Chandigarh','Delhi', 'Dadra and Nagar Haveli','Jammu and Kashmir','Ladakh', 'Lakshadweep','Puducherry'],axis=1)
    q4=q4.drop(['Total'],axis=1)
    maximumRow=q4.max(axis=1)
    maxValueIndexObj = q4.idxmax(axis=1)

    print('Confirmed \n')
    print('Highest affected State is: ',maxValueIndexObj[0])
    print('Highest affected State count is: ',maximumRow[0])
    print('Recovered \n')
    print('Highest affected State is: ',maxValueIndexObj[2])
    print('Highest affected State count is: ',maximumRow[2])
    print('Deceased \n')
    print('Highest affected State is: ',maxValueIndexObj[1])
    print('Highest affected State count is: ',maximumRow[1])

def Q1_5(json_file_path, start_date, end_date):

    finalDataFrame = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    q4 = finalDataFrame.groupby(['status']).sum()
    q4=q4.drop(['Daman and Diu','Lakshadweep', 'Andaman and Nicobar Islands','Chandigarh','Delhi', 'Dadra and Nagar Haveli','Jammu and Kashmir','Ladakh', 'Lakshadweep','Puducherry'],axis=1)
    q4=q4.drop(['Total'],axis=1)
    minimumRow=q4.min(axis=1)
    minValueIndexObj = q4.idxmin(axis=1)

    print('Confirmed \n')
    print('Lowest affected State is: ',minValueIndexObj[0])
    print('Lowest affected State count is: ',minimumRow[0])
    print('Recovered \n')
    print('Lowest affected State is: ',minimumRow[2])
    print('Lowest affected State count is: ', minValueIndexObj[2])
    print('Deceased \n')
    print('Lowest affected State is: ',minimumRow[1])
    print('Lowest affected State count is: ', minValueIndexObj[1])


def Q1_6(json_file_path, start_date, end_date):

    pd.options.mode.chained_assignment = None
    ques6 = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    ques6.sort_values(["Delhi"], axis=0, ascending=False, inplace=True) 
    q6 = ques6.groupby(['status'])[['Delhi','date','status']]
    q6=q6.head(1)
    q6 = q6[:].values
    print('Confirmed \n')
    Highest_spike_day = q6[1][1]
    Highest_spike_count = q6[1][0]
    print('Day: ',Highest_spike_day)
    print('Count: ',Highest_spike_count)
    print('Recovered \n')
    Highest_spike_day = q6[0][1]
    Highest_spike_count = q6[0][0]
    print('Day: ',Highest_spike_day)
    print('Count: ',Highest_spike_count)
    print('Deceased \n')
    Highest_spike_day = q6[2][1]
    Highest_spike_count = q6[2][0]
    print('Day: ',Highest_spike_day)
    print('Count: ',Highest_spike_count)


def Q1_7(json_file_path, start_date, end_date):

    df = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    df=df.drop(['Total','Daman and Diu','Lakshadweep', 'Andaman and Nicobar Islands','Chandigarh','Delhi', 'Dadra and Nagar Haveli','Jammu and Kashmir','Ladakh', 'Lakshadweep','Puducherry'],axis=1)
    q7=df.groupby(['status']).sum()
    q7=q7.transpose()
    q7['Active']=q7['Confirmed']-(q7['Recovered']+q7['Deceased'])

    print(q7)


def Q2_1(json_file_path, start_date, end_date):

   df = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
   df=df.drop('Total',axis=1)
   df=df.groupby(['status','date']).sum().groupby(level=[0]).cumsum()
   df=df.sum(axis=1)

   df['Confirmed'].plot.area()
   df['Recovered'].plot.area()
   df['Deceased'].plot.area()

   plt.xlabel('Dates')
   plt.ylabel('Number of people')
   plt.legend(['Confirmed','Recovered','Deceased'])
   
   plt.show()
   #plt.save()

def Q2_2(json_file_path, start_date, end_date):

    df = states.loc[(states['date']>=start_date) & (states['date']<=end_date)]
    df=df.drop('Total',axis=1)
    df=df.groupby(['status','date'])['Delhi'].sum().groupby(level=[0]).cumsum()
    
    df['Confirmed'].plot.area()
    df['Recovered'].plot.area()
    df['Deceased'].plot.area()
    plt.xlabel('Dates')
    plt.ylabel('Number of people')
    plt.legend(['Confirmed','Recovered','Deceased'])
    
    plt.show()
    #plt.save()


def Q2_3(json_file_path, start_date, end_date):

   df = states.loc[(states['date']>=start_date) & (states['date']<=end_date)] 
   df=df.groupby(['status','date']).sum().groupby(level=[0]).cumsum() 
   df=df.drop('Total',axis=1)
   df=df.sum(axis=1)

   active= df['Confirmed']-(df['Recovered']+df['Deceased']) 

   active.plot.area()
   plt.xlabel('Dates')
   plt.ylabel('Number of people')
   plt.legend(['Active cases'])
    
   plt.show()
   #plt.save()

def Q3(json_file_path, start_date, end_date):

# Implementation of linear regression:


#  for linear regression we require x and y for all the cases

    df = states.loc[(states['date']>=start_date) & (states['date']<=end_date)] 

    confirm=df['status']=='Confirmed'
    recovered=df['status']=='Recovered'
    Deceased=df['status']=='Deceased'
    
    confirm=df[confirm]
    recovered=df[recovered]
    Deceased=df[Deceased]
    


    df2=confirm[['date','Delhi']]
    df3=recovered[['date','Delhi']]
    df4=Deceased[['date','Delhi']]
    
    pd.options.mode.chained_assignment = None
    c = 1
    list = []
    for i in df2['date']:
        list.append(c)
        c = c+1
    df2['Days'] = list
    df3['Days'] = list
    df4['Days'] = list
    df2 = df2.drop('date',axis=1)
    df3 = df3.drop('date',axis=1)
    df4 = df4.drop('date',axis=1)
    df2 = df2[:].values
    df3 = df3[:].values
    df4 = df4[:].values



    def add(val):
        temp=0
        for i in val:
            temp=temp+i
        return temp

    def mean(val):
        return add(val) / float(len(val))

    def cov(x, mean_x, y, mean_y):
        covar = 0.0
        for i  in range(len(x)):
            covar = covar + ((x[i] - mean_x) * (y[i] - mean_y))
        return covar


    def var(values,mean):
        return add([(x-mean) **2 for x in values])


    def coeff(data):
        x = [row[1] for row in data]
        y = [row[0] for row in data]
        x_mean = float(mean(x))
        y_mean = float(mean(y))
        coeff2 = cov(x,x_mean,y,y_mean) / var(x, x_mean) 
        coeff1 = y_mean - coeff2 * x_mean
        return[coeff1, coeff2]

 
    coeff1, coeff2 = coeff(df2)
    confirmed_intercept=coeff1
    confirmed_slope=coeff2
    coeff1, coeff2 = coeff(df3)
    recovered_intercept=coeff1
    recovered_slope=coeff2
    coeff1, coeff2 = coeff(df4)
    deceased_intercept = coeff1
    deceased_slope = coeff2
    print("confirmed_intercept = ",confirmed_intercept )
    print("confirmed_slope = ",confirmed_slope)
    print("recovered_intercept = ",recovered_intercept)
    print("recovered_slope = ",recovered_slope)
    print("deceased_intercept = ",deceased_intercept)
    print("deceased_slope = ",deceased_slope)
    return confirmed_intercept, confirmed_slope, recovered_intercept, recovered_slope, deceased_intercept, deceased_slope

if __name__ == "__main__":
    # execute only if run as a script
    print('MT20048') # Please put this first

    start_date = "2020-03-14"
    end_date = "2020-09-05"
    
    Q1_1('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q1_2('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q1_3('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q1_4('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q1_5('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q1_6('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q1_7('file_path.json', start_date, end_date)
    print(" ")
    print(" ")
    Q2_1('file_path.json', start_date, end_date)
    Q2_2('file_path.json', start_date, end_date)
    Q2_3('file_path.json', start_date, end_date)
    Q3('file_path.json', start_date, end_date)
    #... Rest of the functions