import pandas as pd

counties = ['Apache',
            'Cochise',
            'Coconino',
            'Gila',
            'Graham',
            'LaPaz',
            'Maricopa',
            'Mohave',
            'Navajo',
            'Pima',
            'Pinal',
            'SantaCruz',
            'Yavapai',
            'Yuma']
#print(counties)

for county in counties:
    print(county)
    '''file = city+"_HourlyTemps.csv"
    try:
        data = pd.read_csv(file, low_memory=False)
        print(f"Read in data ({len(data)})")
    except FileNotFoundError:
        print(f"Could not open '{file}'")
    grouped_by_day = data.groupby(['Date'])
    max_by_day = pd.DataFrame(grouped_by_day['Temp'].max())
    max_by_day.to_csv(county+"_MaxTemps.csv")'''
