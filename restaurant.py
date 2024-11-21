# List of restaurants
restaurants = [
    {
        "ID": 1,
        "Name": "Vikings Luxury Buffet",
        "Location": "Pasay City",
        "Cuisine Type": "Buffet",
        "Established Year": 2011,
        "Website or Contact": "www.vikings.ph"
    },
    {
        "ID": 2,
        "Name": "Antonio's Restaurant",
        "Location": "Tagaytay",
        "Cuisine Type": "Fine Dining",
        "Established Year": 2002,
        "Website or Contact": "www.antoniosrestaurant.ph"
    },
    {
        "ID": 3,
        "Name": "Mesa Filipino Moderne",
        "Location": "Makati City",
        "Cuisine Type": "Filipino",
        "Established Year": 2009,
        "Website or Contact": "www.mesa.ph"
    },
    {
        "ID": 4,
        "Name": "Manam Comfort Filipino",
        "Location": "Quezon City",
        "Cuisine Type": "Filipino",
        "Established Year": 2013,
        "Website or Contact": "www.manam.ph"
    },
    {
        "ID": 5,
        "Name": "Ramen Nagi",
        "Location": "Various Locations",
        "Cuisine Type": "Japanese",
        "Established Year": 2013,
        "Website or Contact": "www.ramennagi.com.ph"
    }
]

# Loop through the list of restaurants and print their details
for restaurant in restaurants:
    print(f"ID: {restaurant.get('ID')}, Name: {restaurant.get('Name')}, Location: {restaurant.get('Location')}, Cuisine Type: {restaurant.get('Cuisine Type')}, Established Year: {restaurant.get('Established Year')}, Website or Contact: {restaurant.get('Website or Contact')}")