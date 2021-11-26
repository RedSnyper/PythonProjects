from bs4 import BeautifulSoup
import requests
import multiprocessing

f = open('veganbell_data_multiProc.txt', 'w')


def scrape(page_number):
    try:
        source = requests.get(
            f'https://www.veganbell.com/vegan-recipes/page/{page_number}').text
        soup = BeautifulSoup(source, 'lxml')
        for title in soup.find_all('h1', class_='elementor-post__title'):
            link = title.a['href']
            recipe_title = title.text
            p = multiprocessing.Process(
                target=individual_page, args=(link, recipe_title))
            p.start()
    except Exception as e:
        print("error in scrape {}".format(e))


def individual_page(link, recipe_title):
    ingredientList = []
    instructionList = []
    nutritionList = []

    try:
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')

        ytLink = soup.find('iframe')['data-lazy-src']
        ytLink = ytLink.split('?')[0]
        ytLink = ytLink.replace('embed/', 'watch?v=')

        for ingredients in soup.find_all('li', class_='wprm-recipe-ingredient'):
            ingredientList.append(ingredients.text)

        for instruction in soup.find_all('li', class_='wprm-recipe-instruction'):
            ins = instruction.text.replace('\U0001f642', '')
            instructionList.append(ins)
        for nutrition in soup.find_all('span', class_='wprm-nutrition-label-text-nutrition-container'):
            nutritionList.append(nutrition.text)
  
        f.write(recipe_title)
        f.write(ingredientList)
        f.write(instructionList)
        f.write(nutritionList)
        f.write(ytLink)

    except Exception as e:
        print(f'error in indivdiual page {e}')


if __name__ == '__main__':
    for i in range(1, 6):
        mp = multiprocessing.Process(target=scrape, args=(i,))
        mp.start()
f.close()
