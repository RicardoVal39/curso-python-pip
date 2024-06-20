def get_population(country):
    population = {}
    population['2022'] = country['2022 Population']
    population['2020'] = country['2020 Population']
    population['2015'] = country['2015 Population']
    population['2010'] = country['2010 Population']
    population['2000'] = country['2000 Population']
    population['1990'] = country['1990 Population']
    population['1980'] = country['1980 Population']
    population['1970'] = country['1970 Population']
    return population 

def population_by_country(data, country):
    data = list(filter(lambda x:x['Country'] == country, data))
    return data