# 1. Add to the employee dictionary the keys of name and service_years
julie = {}
julie["name"] = "Julie"
julie["service_years"] = 9
# print(julie)


# 2. Add the new employee into our list of employees
employees = [
    {
        "name": "Mike",
        "service_years": 5
    },
    {
        "name": "Sarah",
        "service_years": 8
    },
    {
        "name": "John",
        "service_years": 2
    }
]
employees.append(julie)

# print(employees)

# 3. There is a mistake, Mike has been working for 6 years. Update Mike's service_years to 6
# mike's service_years = 6
employees[0]["service_years"] = 6
# print(employees)

# 4. A new key is required of age. Add the age key with the string value of UNKNOWN to each employee
employees[0]["age"] = "Unknown"
employees[1]["age"] = "Unknown"
employees[2]["age"] = "Unknown"
employees[3]["age"] = "Unknown"

print(employees)