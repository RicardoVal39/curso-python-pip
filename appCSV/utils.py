
def get_population(country):
    population = {}
    population['2022'] = int(country['2022 Population'])
    population['2020'] = int(country['2020 Population'])
    population['2015'] = int(country['2015 Population'])
    population['2010'] = int(country['2010 Population'])
    population['2000'] = int(country['2000 Population'])
    population['1990'] = int(country['1990 Population'])
    population['1980'] = int(country['1980 Population'])
    population['1970'] = int(country['1970 Population'])
    keys = population.keys()
    values = population.values()
    return keys , values  

def population_by_country(data, country):
    data = list(filter(lambda x:x['Country'] == country, data))
    return data