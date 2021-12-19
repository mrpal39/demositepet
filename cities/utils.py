import unicodedata
import csv
import itertools
import os

from django.conf import settings

from cities import models


# def get_states_filename(country):
#     return os.path.join(settings.CITIES_DATA_LOCATION, country.lower(), "citie.csv")


def get_cities_filename(country):
    return os.path.join(settings.CITIES_DATA_LOCATION, country.lower(), "citie.csv")


# def get_postcode_cities_filename(country):
#     return os.path.join(settings.CITIES_DATA_LOCATION, country.lower(), "citie.csv")


def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# def load_states_from_file(filename):
#     states = load_file(filename)

#     for state in states:
#         models.State.objects.get_or_create(
#             name=state.get("statename"), abbr=state.get("statename")
#         )
#         print(state.get("statename"))


def load_cities_from_file(filename):
    cities = load_file(filename)
    cities = sorted(cities, key=lambda c: c["Districtname"])
    grouped_cities = itertools.groupby(cities, key=lambda c: c["statename"])
    # print (states)

    for state_abbr, cities in grouped_cities:
        states = models.State.objects.get(abbr=state_abbr)
        print(states)
        for city in cities:
            models.District.objects.get_or_create(
                state=states, name=city.get("Districtname"),code=city.get("pincode"),
            )


        #     print(city.get("name"))


# def load_post_cities_from_file(filename):
#     cities = load_file(filename)
#     cities = sorted(cities, key=lambda c: c["statename"])
#     grouped_cities = itertools.groupby(cities, key=lambda c: c["statename"])
 
#     # for state_abbr, cities in grouped_cities:
#     #     print(state_abbr)
#     #     states = models.State.objects.get(name=state_abbr)
#     #     for l, m in grouped_dist:
#     #         cit = models.City.objects.get(name=l)
#     # #         print(cit)
#     #         print(l)
#     #         for city in m:
#     #             models.PostcodeCites.objects.get_or_create(
#     #                 state=states, city=cit, name=city.get("officename"), pincode=city.get("pincode"))

#         # cit=models.City.objects.get(state=states)
#         # for c in cit:

#         #     print (c)

# #         for city in cities:
# #             models.PostcodeCites.objects.get_or_create(
# #                 state=states, name=city.get("officename"),pincode=city.get("pincode"))
# # # officename,pincode,officeType,Deliverystatus,divisionname,regionname,circlename,Taluk,Districtname,statename,Telephone,Related Suboffice,Related Headoffice,longitude,latitude

            # print(city.get("name"))


def clear_text(txt):
    normalized_text = unicodedata.normalize("NFD", txt)
    non_comb = "".join(
        c for c in normalized_text if not unicodedata.combining(c) and c not in ["~", "´", "`", "¨", "^"]
    )
    return unicodedata.normalize("NFC", non_comb)
