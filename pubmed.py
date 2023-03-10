from selenium.webdriver.common.by import By

url = 'https://pubmed.ncbi.nlm.nih.gov'


def get_doi_from_pmid(driver, pmid):
    driver.get(f'{url}/{pmid}')
    try:
        doi_text = driver.find_element(By.CLASS_NAME, 'identifier.doi').text.split(' ')[1]
        return f'https://doi.org/{doi_text}'
    except:
        return 'Not Found'
    
    
def get_doi_from_reference(driver, reference):
    driver.get(url)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/form/div/div[1]/div/span/input').send_keys(reference)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/form/div/div[1]/div/button').click()
    try:
        doi_text = driver.find_element(By.CLASS_NAME, 'identifier.doi').text.split(' ')[1]
        return f'https://doi.org/{doi_text}'
    except:
        return 'Not Found'
