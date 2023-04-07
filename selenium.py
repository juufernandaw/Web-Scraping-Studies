from selenium import webdriver


navegador = webdriver.Chrome()
navegador.maximize_window()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element("xpath", '//*[@id="mainContent"]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a[2]').click()
# pensar em como já salvar de forma automática o embed pdf
