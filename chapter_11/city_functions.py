## ex 11.1 and 11.2 city, country, population



## passing test case
# def city_country(city, country):
    # ans = city.title() + ', ' + country.title()
    # return ans


## failing test case
# def city_country(city, country, population):
    # ans = city.title() + ', ' + country.title() + ' - Population: ' + str(population)
    # return ans

## resolved function
def city_country(city, country, population = ''):
    if population:
        ans = city.title() + ', ' + country.title() + ' - Population: ' + str(population)
    else:
        ans = city.title() + ', ' + country.title()
    
    return ans


### *** WOW, THE FUNCTION PARAM CAN BE STR AND YOU CAN STILL PUT INT()!!! *** ####
city_country('san', 'chil', 50000)
