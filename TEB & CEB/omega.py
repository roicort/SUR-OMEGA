
import pandas as pd

df = pd.read_excel(io='Market.xls', sheet_name='Vehicle')

key = "Vehicle Type No" 
#key = "Model"

print("\nOrder by: " + key+"\n")

df = df.sort_values(by=key)

#df.drop(columns=["Manufacturer","Vehicle Index No","Platform Index No","Fleet Type","Classic Fleet Type","Vehicle Safety Class","CVCM Class","EPA Class","Baseline Price - Cycle1","Baseline Sales","Annual Sales - Cycle 1","Annual Sales - Cycle 2","Annual Sales - Cycle 3","Annual Sales - Cycle 4","Annual Sales - Cycle 5","Annual Sales - Cycle 6","Annual Sales - Cycle 7","Annual Sales - Cycle 8","Combined FE (mpg)","Tailpipe Co2 (g/mi)","Footprint (ft2)","Curb Weight (lb)","No. of Cylinders","Displacement (L)","Horsepower","Max Seating","Transmission Type","Drive","Structure","Towing Capacity","Primary Fuel Type","Combined EC (kWh/mi)","Refrigerant Type","Refrigrent Lifetime Leakage (g)"], inplace=True)

keys = list(set(df[key]))

print("Classes: " + str(keys)+"\n")

TEBDF = pd.DataFrame()
CEBDF = pd.DataFrame()

for k in keys:
    
    df_k = df[df[key] == k]
    #print(key+": "+str(k))
    #print("\n")
    TEBMeans = []
    CEBMeans = []

    for t in range(1,21):

        Q = "TEB Tech. Pkg. "+str(t)
        T = df_k[Q]
        Tm = T.mean()
        #print(Q +" - Mean: "+ str(Tm))
        TEBMeans.append(Tm)

        Q = "CEB Tech. Pkg. "+str(t)
        T = df_k[Q]
        Tm = T.mean()
        #print(Q +" - Mean: "+ str(Tm))
        CEBMeans.append(Tm)

    T_row = pd.Series(TEBMeans)
    row_df = pd.DataFrame([pd.concat([T_row])], index = [str(k)])
    TEBDF = pd.concat([row_df, TEBDF])


    C_row = pd.Series(CEBMeans)
    row_df = pd.DataFrame([pd.concat([C_row])], index = [str(k)])
    CEBDF = pd.concat([row_df, CEBDF])


TEBDF = TEBDF.iloc[::-1]
CEBDF = CEBDF.iloc[::-1]

TEBDF.columns = ["TEB Tech. Pkg. {}".format(t) for t in range(1,21)]
CEBDF.columns = ["CEB Tech. Pkg. {}".format(t) for t in range(1,21)]

TEBDF = TEBDF.to_dict()
CEBDF = CEBDF.to_dict()

print(TEBDF)
print(CEBDF)

#TEBDF.to_excel(excel_writer='TEB.xlsx', sheet_name='TEB')
#CEBDF.to_excel(excel_writer='CEB.xlsx', sheet_name='CEB')





