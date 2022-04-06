from views.employee_requests import EMPLOYEES


CUSTOMERS = [
    {
        "id": 1,
        "first_name": "Bendite",
        "last_name": "Phillip"
    },
    {
        "id": 2,
        "first_name": "Shari",
        "last_name": "Sprules"
    },
    {
        "id": 3,
        "first_name": "Gustaf",
        "last_name": "Chaloner"
    },
    {
        "id": 4,
        "first_name": "Merrilee",
        "last_name": "Gwatkins"
    },
    {
        "id": 5,
        "first_name": "Emile",
        "last_name": "Cattenach"
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer