# The data for your website

data = {
    # Example of a collection
    "items": [
        {
            "name": 'iphone 5',
            "price": '50000$',
            'category': 'Phones',
            "manufacturer": 'Apple',
            'operating_system': 'IOS',
            'form_factor': 'Touchscreen',
            'dimensions': '123.80 x 58.60 x 7.60',
            'weight': '112',
            'battery_capacity': '1440',
            'removable_battery': 'No',
            'colors': 'White, Black',
            "image_url": 'https://static.wixstatic.com/media/41d000_421de6df461a44ef2b1ecf6d5b4055f7.png/v1/fill/w_395,h_238,al_c,lg_1/41d000_421de6df461a44ef2b1ecf6d5b4055f7.png'
        },
        {
            "name": 'LG G6',
            "price": '500$',
            "category ": 'Phones',
            "manufacturer": 'LG',
            'operating_system': 'Android',
            'form_factor': 'Touchscreen',
            'dimensions ': '148.9 x 71.9 x 7.9',
            'weight': '163',
            'battery_capacity': '3300',
            'removable_battery': 'No',
            'colors': 'White, Black, Gray',
            'image_url': 'https://static.wixstatic.com/media/41d000_421de6df461a44ef2b1ecf6d5b4055f7.png/v1/fill/w_395,h_238,al_c,lg_1/41d000_421de6df461a44ef2b1ecf6d5b4055f7.png'
        },
        {
            "name": 'Samsung Galaxy S9',
            "price": '50000$',
            "category ": 'Phones',
            "manufacturer": 'Samsung',
            'operating_system': 'Android',
            'form_factor': 'Touchscreen',
            'dimensions ': '158.1 x 73.8 x 8.5',
            'weight': '189',
            'battery_capacity': '3500',
            'removable_battery': 'No',
            'colors': 'Blue, Black, Purple, Gray',
            'image_url': 'https://static.wixstatic.com/media/41d000_421de6df461a44ef2b1ecf6d5b4055f7.png/v1/fill/w_395,h_238,al_c,lg_1/41d000_421de6df461a44ef2b1ecf6d5b4055f7.png'
        },
    ],
    "images": [
      {"url": '/shared/images/corgi.jpg'},
      {"url": '/shared/images/cavalier.jpg'},
      {"url": '/shared/images/aussi.jpg'},
      {"url": '/shared/images/corgi.jpg'},
      {"url": '/shared/images/cavalier.jpg'},
      {"url": '/shared/images/aussi.jpg'},
    ],
    "sizes":[
      {"name": "small", "toString":"Small"},
      {"name": "medium", "toString":"Medium"},
      {"name": "big", "toString":"Big"},
    ],
    "cities":[
      {"id":"telAviv", "toString": "Tel Aviv xoxo"},
      {"id":"2", "toString":"Haifa"}
    ],
    "days": [0, 1, 2],
    "hours": [[1, 2, 3, 4], [2, 3, 4], [3, 4]]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection])

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
