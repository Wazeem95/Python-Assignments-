city = {
    "NEW YORK": {
        "Country": "UNITED STATES OF AMERICA",
        "Approximate_population": "19.49 Million Approx.",
        "Fact": "The New York Public Library has over 50 million books and other items and is the second largest "
                "library system in the nation after the Library of Congress. It is also the 3rd largest library in "
                "the world. "
    },
    "ISTANBUL": {
        "Country": "TURKEY",
        "Approximate_population": "14.6 Million Approx.",
        "Fact": "Istanbul is the only city in the world which is both in Europe and Asia geographically."
    },
    "BERLIN": {
        "Country": "GERMANY",
        "Approximate_population": "3.5 Million Approx.",
        "Fact": "Berlin is considered by many as Germany`s greenest city with over 44% of its area made of waterways, "
                "woods, rivers and green areas. "
    }
}

for i in city.keys():
    print("City Name : ", i)
    print("Country Name  : ", city[i]["Country"])
    print("Approximate population  : ", city[i]["Approximate_population"])
    print("Fact of the City  : ", city[i]["Fact"])
    print(
        "**************************************************************************************************************************************************************************************************************************************")