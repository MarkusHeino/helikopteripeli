import tkinter as tk
# import tkinter.ttk as ttk
from geopy import distance

map_width = 58
map_height = 18

# funktio, joka luo listan kahdeksasta lähimmästä lentokentästä - lisätään tuohon vieläoikeat parit map_infolle ja player_coordinatesille
def get_eight_nearest_heliports(heliport_info, player_coordinates):
    distances = []
    for info in heliport_info:
        distance_between = get_distance_to_heliport(info, player_coordinates)
        distances.append((info, distance_between))

    # sortataan lähimmästä kauimpaan 1-8
    distances.sort(key=lambda x: x[1])
    eight_nearest = distances[:8]

    return eight_nearest


# GUI:n mukaantulo - NO NIIN! :D - eli luodaan graafiseen käyttöliittymään (tkinter) kartta, wallet ja lista lähimmistä kentistä
def update_heliports_list():
    # haetaan kahdeksan lähintä kenttää
    eight_nearest = get_eight_nearest_heliports(map_info, player_coordinates)

    # poistetaan edellisen vuoron lista
    heliports_list.delete(0, tk.END)

    # lisätään uusi kahdeksan kentä lista
    for i, (info, distance) in enumerate(eight_nearest, start=1):
        heliports_list.insert(tk.END, f"{i}. {info['name']} - {int(distance)} km")


# luodaan GUI pääliittymä
root = tk.Tk()
root.title("Helipeli 2.0")

# tässä kohtaa voidaan laittaa koko alarimpsu piiloon häshtägein jos tuota GUI:ta ei käytetäkään

# kartan pohja on valkoinen ja pikselit siinä 1:1
map_canvas = tk.Canvas(root, width=400, height=400, bg="white")
map_canvas.pack(side=tk.LEFT, padx=10, pady=10)

# Wallet eli kerättyjen varojen counter, joka päivitettävissä
wallet_label = tk.Label(root, text="Wallet:")
wallet_label.pack(side=tk.LEFT, anchor=tk.W, padx=10, pady=(10, 0))

# Walletin counter
wallet_counter = tk.Label(root, text="0")
wallet_counter.pack(side=tk.LEFT, anchor=tk.W, padx=10, pady=(0, 10))

# Nearest Heliports -teksti
side_panel_label = tk.Label(root, text="Nearest Heliports:")
side_panel_label.pack(side=tk.LEFT, anchor=tk.W, padx=10)

# Päivittyvä lista lähimmille heliporteille
heliports_list = tk.Listbox(root)
heliports_list.pack(side=tk.LEFT, anchor=tk.W, padx=10)

# Nappi, joka päivittää lähimmät kentät - tämän voi automatisoida kaiketi, mutta jotain tekemistä pelaajalle numeronappien painamisen lisäksi?
update_button = tk.Button(root, text="Update Heliports", command=update_heliports_list)
update_button.pack(side=tk.RIGHT, anchor=tk.W, padx=10, pady=(0, 10))

# GUI:n main loop
root.mainloop()

# Koodi 1.0 alkaa

def get_distance_to_heliport(heliport_info, player_coordinates):
    distance_between = distance.distance((heliport_info['longitude_deg'], heliport_info['latitude_deg']),
                                         (player_coordinates))
    return distance_between


def check_if_visited(info, heliports_visited):
    visited = False
    for he_vi in heliports_visited:
        if info['ident'] == he_vi['location']:
            visited = True
    return visited


# luo tyhjän kartan reunamerkkeineen
def draw_blank_map():
    # luo kartan perustan
    default_texture = ' '
    map = [[default_texture for _ in range(map_width)] for _ in range(map_height)]

    border_char = '#'
    for i in range(map_height):
        map[i][0] = border_char
        map[i][map_width - 1] = border_char

    for i in range(map_width):
        map[0][i] = border_char
        map[map_height - 1][i] = border_char

    # Tällä yritin lisätä kompassin ilmansuunnat karttaan - ne ei oikein näy, mutta ovat siellä seassa
    map[0][map_width // 2] = 'N'
    map[map_height - 1][map_width // 2] = 'S'
    map[map_height // 2][0] = 'W'
    map[map_height // 2][map_width - 1] = 'E'

    return map


def draw_map(map_info, heliports_in_range, player_coordinates, MAX_RANGE, heliports_visited):
    # luodaan tyhjä kartta, johon asetetaan kenttien merkkejä
    map = draw_blank_map()

    # tällä merkitään helipadien sijainnit määrittelyn mukaan
    # ensin piirretään P kentän paikalle jossa pelaaja on, ulottumattomissa olevien kenttien paikalle H
    # counter = 0
    for info in map_info:
        distance_between = get_distance_to_heliport(info, player_coordinates)
        if 0 <= info['x'] < map_width and 0 <= info['y'] < map_height:
            """
            voidaan käyttää sijaintien numerointiin kartalla, debuggin
            counter+=1
            print(counter)
            if map[info['y']][info['x']] == ' ':
                map[info['y']][info['x']] = f"|{counter}|"
            else:
                map[info['y']][info['x']] += f"{counter}|"
            """
            # Jos pelaaja on kentällä, aseta siihen P
            if distance_between == 0:
                map[info['y']][info['x']] = '\33[0;31mP\33[0m'
            # jos kenttä ei ole pelaajan etäisyydellä, aseta H
            elif distance_between > MAX_RANGE:  # and map[info['y']][info['x']] != 'H':
                visited = check_if_visited(info, heliports_visited)
                if visited:
                    map[info['y']][info['x']] = '\33[1;33mH\33[0m'
                else:
                    map[info['y']][info['x']] = '\33[1;32mH\33[0m'  # H on tässä helipadin sijainnin merkintä

    # seuraavaksi asetetaan pelaajan etäisyydellä olevat kentät numeroituna lähimmästä kauimpaan
    for heli in heliports_in_range:
        if 0 <= heli['x'] < map_width and 0 <= heli['y'] < map_height:
            # asettaa kentälle numeron, jos paikalla ei ole jo numeroa
            visited = check_if_visited(heli, heliports_visited)
            if map[heli['y']][heli['x']] == " " and visited:
                map[heli['y']][heli['x']] = f"\33[1;33m{heli['range_index']}\33[0m"
            elif map[heli['y']][heli['x']] == " ":
                map[heli['y']][heli['x']] = f"\33[0;36m{heli['range_index']}\33[0m"
            # jos paikalla on jo numero tai pelaaja P, lisää sen perään pilkku sekä numero,
            # koska kentän koordinaatistoruudulla saattaa olla samassa kohdassa useampi kenttä.
            # Väritetään kentän merkki eri värillä jos kentällä on jo käyty
            elif map[heli['y']][heli['x'] + 1] == " " and visited:
                map[heli['y']][heli['x'] + 1] = f"\33[1;33m{heli['range_index']}\33[0m"
            elif map[heli['y']][heli['x'] + 1] == " ":
                map[heli['y']][heli['x'] + 1] = f"\33[0;35m{heli['range_index']}\33[0m"
            elif map[heli['y'] + 1][heli['x']] == " " and visited:
                map[heli['y'] + 1][heli['x']] = f"\33[1;33m{heli['range_index']}\33[0m"
            elif map[heli['y'] + 1][heli['x']] == " ":
                map[heli['y'] + 1][heli['x']] = f"\33[1;35m{heli['range_index']}\33[0m"
            else:
                map[heli['y']][heli['x']] += f",\33[0;35m{heli['range_index']}\33[0m"

    # kartan sivulle ensimmäselle riville
    line = ""
    for c in range(2):
        line += f"{'':8.8s} {'Heliport name':22.22s} {'distance':8.8s} "
    count = 1

    # Ja asetetaan kartan sivuun tietoja, i on rivin numero, row on rivin merkkijono, jonka perään lisätään
    # haluttuja tietoja
    print(len(heliports_in_range), len(heliports_in_range) / 2)
    for i, row in enumerate(map):
        if i == 0:
            print(''.join(row) + line)
            line = ""
        elif 0.0 <= float(count) <= (len(heliports_in_range)):
            if count == (len(heliports_in_range)):
                line += (
                    f" | {count:2d}.{heliports_in_range[count - 1]['name']:22.22s} | {heliports_in_range[count - 1]['distance_from_player']:4.0f} km | ")
                print(''.join(row) + line)
                count += 1
            else:
                for c in range(2):
                    line += (
                        f" | {count:2d}.{heliports_in_range[count - 1]['name']:22.22s} | {heliports_in_range[count - 1]['distance_from_player']:4.0f} km | ")
                    count += 1
                print(''.join(row) + line)
                line = ""
        else:
            print(''.join(row), i)