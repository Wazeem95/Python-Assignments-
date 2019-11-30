person_details = {"First_Name": "WASEEM",
                  "Last_Name": "AHMED",
                  "Age": "23",
                  "City": "KARACHI",
                  }

for i in person_details.values():
    print(i)

person_details.update({"qualification": "Under Graduate"})

print(person_details["qualification"])

person_details["qualification"] = "Graduate"
print("After Update Qualification : ", person_details["qualification"])

del person_details["qualification"]

print(person_details)
