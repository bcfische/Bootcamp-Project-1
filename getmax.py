import pandas as pd

city_to_county = {'SaintJohns':'Apache',
                  'Bisbee':'Cochise',
                  'Flagstaff':'Coconino',
                  'Payson':'Gila',
                  'Safford':'Graham',
                  'Havasu':'LaPaz',
                  'Phoenix':'Maricopa',
                  'Kingman':'Mohave',
                  'Winslow':'Navajo',
                  'Tucson':'Pima',
                  'CasaGrande':'Pinal',
                  'Nogales':'SantaCruz',
                  'Prescott':'Yavapai',
                  'Yuma':'Yuma'}
print(city_to_county)

for city, county in city_to_county.items():
    file = city+"_HourlyTemps.csv"
    try:
        data = pd.read_csv(file, low_memory=False)
        print(f"Read in data ({len(data)})")
    except FileNotFoundError:
        print(f"Could not open '{file}'")
    grouped_by_day = data.groupby(['Date'])
    max_by_day = pd.DataFrame(grouped_by_day['Temp'].max())
    max_by_day.to_csv(county+"_MaxTemps.csv")