from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.CSS_SELECTOR, 'div [aria-label="vuelo"] h2')
    signin_button = (By.CSS_SELECTOR, 'div[class="J-sA"] div[role="button"]')
    search_button = (By.CSS_SELECTOR, 'button[aria-label="Buscar"]')
    origin_input = (By.CSS_SELECTOR, 'input[aria-label="Ubicación de origen"]')
    destination_input = (By.CSS_SELECTOR, 'input[placeholder="Destino"]')
    menu_item_flights_a = (By.CSS_SELECTOR, 'a[aria-label="Buscar vuelos"]')
    menu_item_stays_a = (By.CSS_SELECTOR, 'a[aria-label="Buscar alojamientos"]')
    menu_item_cars_a = (By.CSS_SELECTOR, 'a[aria-label="Buscar autos"]')
    lateral_menu_button = (By.CSS_SELECTOR, 'div[aria-label="Abrir navegación principal"]')
    lateral_menu_flights_a = (By.CSS_SELECTOR, 'li > a[aria-label="Buscar vuelos "]')
    lateral_menu_stays_a = (By.CSS_SELECTOR, 'li > a[aria-label="Buscar alojamientos "]')
    lateral_menu_cars_a = (By.CSS_SELECTOR, 'li > a[aria-label="Buscar autos "]')
    lateral_menu_ai_mode_a = (By.CSS_SELECTOR, 'li > a[aria-label="Ir al Modo IA "]')
    lateral_menu_explore_a = (By.CSS_SELECTOR, 'li > a[aria-label="Ir a Explore "]')
    lateral_menu_blogs_a = (By.CSS_SELECTOR, 'li > a[aria-label="Visita nuestro blog "]')
    lateral_menu_direct_flights_a = (By.CSS_SELECTOR, 'li > a[aria-label="Buscar vuelos directos "]')
    lateral_menu_discover_a = (By.CSS_SELECTOR, 'li > a[aria-label="Descubre el mejor momento para viajar "]')
    lateral_menu_business_a = (By.CSS_SELECTOR, 'li > a[aria-label="KAYAK for Business NUEVO"]')
    lateral_menu_trips_div = (By.CSS_SELECTOR, 'div > a[aria-label="Trips "]')


