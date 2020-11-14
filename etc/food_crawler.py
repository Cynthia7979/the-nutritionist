import requests
import json
from bs4 import BeautifulSoup
from os.path import exists


def get_soup(link):
    raw = requests.get(link).content
    return BeautifulSoup(raw, features='html.parser')


def get_image_name(img_link: str):
    return img_link[img_link.rfind("/")+1:img_link.find("?")]


def download_image(img_link: str):
    print('Downloading', img_link, '...')
    filepath = f'../images/{get_image_name(img_link)}'
    if not exists(filepath):
        resolved = False
        while not resolved:
            try:
                image_content = requests.get(img_link).content
                resolved = True
            except Exception:
                print('Retrying')
        with open(f'../images/{filepath}', 'wb') as f:
            f.write(image_content)
        f.close()
    else: print(filepath, 'Already exists')


def store_image_link(img_link: str):
    with open('img_links.txt', 'a') as f:
        f.write(img_link+'\n')
    return get_image_name(img_link)


def get_nutrition_value(classes_: list):
    total = 0
    for class_ in classes_:
        try:
            strvalue = recipe_soup.find('tr', class_=class_).find_all('td')[1].text.\
                    replace('mg', '').replace('mcg', '').replace('RAE', '').replace('DFE', '')
            if strvalue != 'N/A': total += float(strvalue)
            else: total += 0
        except AttributeError: pass
    return total


LINK = 'https://www.choosemyplate.gov/myplatekitchen/recipes?' \
       'search=&items_per_page=100&sort_bef_combine=search_api_relevance_DESC&f%5B0%5D=course%3A{courseIndex}'
COURSE_INDEX = {116: 'Appetizers', 117: 'Beverages', 118: 'Breads', 119: 'Breakfast', 120: 'Desserts', 121: 'Main Dishes',
                122: 'Salads', 123: 'Sandwiches', 124: 'Sauces, Condiments & Dressings', 125: 'Side Dishes', 126: 'Snacks',
                # 127: 'Soups & Stews'
                }

results = [
    # {
    #     'name': 'Name of course',
    #     'description': 'Short description',
    #     'category': 'Diary',
    #     'courseType': 'Appetizers',
    #     'image': 'MyPlate-Kitchen-image-placeholder.png,
    #     'Energy': 500,
    #     'Sodium': 10,
    #     'Mineral': 50,
    #     'Vitamin': 1000
    # }
]

for courseIndex, name in COURSE_INDEX.items():
    recipe_count = 0
    recipe_page_soup = get_soup(LINK.format(courseIndex=courseIndex))

    recipe_list = recipe_page_soup.find('div', class_='view-content')

    for recipe in recipe_list.find_all('div', class_='views-row'):
        if recipe_count == 10: break
        recipe_object = {}

        image = recipe.find('img')
        # Takes way to long
        # download_image('https://www.choosemyplate.gov'+image['src'])
        recipe_object['image'] = store_image_link('https://www.choosemyplate.gov'+image['src'])

        course_link_element = recipe.find('div', class_='right').find('a')
        recipe_object['name'] = course_link_element.text
        course_link = 'https://www.choosemyplate.gov'+course_link_element['href']
        print(course_link)

        recipe_soup = get_soup(course_link)
        try:
            recipe_object['category'] = recipe_soup.find_all('div', class_='np_label inline')[1].text
        except IndexError:
            continue
        recipe_object['courseType'] = name
        recipe_object['description'] = recipe_soup.find('div', class_='recipe-details card flex').text

        recipe_object['Energy'] = get_nutrition_value(['np_row total_calories font-xl bold_underline odd'])
        recipe_object['Sodium'] = get_nutrition_value(['np_row bold sodium odd'])
        recipe_object['Mineral'] = get_nutrition_value(['np_row calcium odd', 'np_row potassium even',# 'np_row sodium odd',
                                                        'np_row copper even', 'np_row iron odd', 'np_row magnesium even',
                                                        'np_row phosphorus odd', 'np_row selenium even', 'np_row zinc odd'])
        recipe_object['Vitamin'] = get_nutrition_value(['np_row vitamin_a odd', 'np_row vitamin_b6 even', 'np_row vitamin_b12 odd',
                                                        'np_row vitamin_c even', 'np_row vitamin_d odd', 'np_row vitamin_e even',
                                                        'np_row vitamin_k odd'])
        print(recipe_object)
        results.append(recipe_object)
        recipe_count += 1
    print('End of', name)
    print()

with open('../food_data.json', 'w') as f:
    json.dump(results, f)
