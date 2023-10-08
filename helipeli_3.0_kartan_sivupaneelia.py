from geopy import distance

map_width = 58
map_height = 18


def get_distance_to_heliport(heliport_info, player_coordinates):
    distance_between = distance.distance((heliport_info['longitude_deg'],heliport_info['latitude_deg']), (player_coordinates))
    return distance_between

def check_if_visited(info, heliports_visited):
    visited = False
    for he_vi in heliports_visited:
        if info['ident'] == he_vi['location']:
            visited = True
    return visited


#luo tyhjän kartan reunamerkkeineen
def draw_blank_map(heliports_in_range):
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

    # luodaan sivupaneeli, joka näyttää lähimmät helikentät 1-8
    side_panel = []
    for i in range(1, 9):
        if i <= len(heliports_in_range):
            side_panel.append(f"{i}: {heliports_in_range[i - 1]['name']} ({heliports_in_range[i - 1]['distance_from_player']:.0f} km)")
        else:
            side_panel.append(f"{i}: -")

    # printataan sivupaneeli
    for i, row in enumerate(map):
        line = ""
        if i == 0:
    #headerit
        elif 0.0 <= float(count) <= (len(heliports_in_range)):
            if count == (len(heliports_in_range)):
                line += (f" | {count:2d}.{heliports_in_range[count-1]['name']:22.22s} | {heliports_in_range[count-1]['distance_from_player']:4.0f} km | {'':39.39s}|")
                line += f"{' ' * 3}".join(side_panel)
                print(''.join(row) + line)
                count += 1
            else:
                for c in range(2):
                    line += (
                        f" | {count:2d}.{heliports_in_range[count-1]['name']:22.22s} | {heliports_in_range[count-1]['distance_from_player']:4.0f} km | ")
                    count += 1
                line += f"{' ' * 3}".join(side_panel)
                print(''.join(row) + line)
                line = ""


def draw_map(map_info, heliports_in_range, player_coordinates, MAX_RANGE, heliports_visited, goal=False):
    #luodaan tyhjä kartta, johon asetetaan kenttien merkkejä
    map = draw_blank_map()

    # tällä merkitään helipadien sijainnit määrittelyn mukaan
    #ensin piirretään P kentän paikalle jossa pelaaja on, ulottumattomissa olevien kenttien paikalle H
    #counter = 0
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
            #Jos pelaaja on kentällä, aseta siihen P, ja ota tieto ylös jotta se voidaan esittää kartan sivussa
            if distance_between == 0:
                map[info['y']][info['x']] = '\33[0;31mP\33[0m'
                player_heliport = info
            #jos kenttä ei ole pelaajan etäisyydellä, aseta H
            elif distance_between > MAX_RANGE:# and map[info['y']][info['x']] != 'H':
                visited = check_if_visited(info,heliports_visited)
                if visited:
                    map[info['y']][info['x']] = '\33[1;33mH\33[0m'
                else:
                    map[info['y']][info['x']] = '\33[1;32mH\33[0m'  # H on tässä helipadin sijainnin merkintä

    #seuraavaksi asetetaan pelaajan etäisyydellä olevat kentät numeroituna lähimmästä kauimpaan
    for heli in heliports_in_range:
        if 0 <= heli['x'] < map_width and 0 <= heli['y'] < map_height:
            #katsotaan onko pelaaja käynyt jo kentällä, väritetään kentän merkki eri värillä myöhemmin jos on
            visited = check_if_visited(heli, heliports_visited)
            # asettaa kentälle numeron, jos paikalla ei ole jo numeroa
            if map[heli['y']][heli['x']] == " " and visited:
                map[heli['y']][heli['x']] = f"\33[1;33m{heli['range_index']}\33[0m"
            elif map[heli['y']][heli['x']] == " ":
                map[heli['y']][heli['x']] = f"\33[0;36m{heli['range_index']}\33[0m"
            #jos paikalla on jo numero tai pelaaja P, lisää sen perään pilkku sekä numero,
            #koska kentän koordinaatistoruudulla saattaa olla samassa kohdassa useampi kenttä.
            #Väritetään kentän merkki eri värillä jos kentällä on jo käyty
            elif map[heli['y']][heli['x']+1] == " " and visited:
                map[heli['y']][heli['x']+1] = f"\33[1;33m{heli['range_index']}\33[0m"
            elif  map[heli['y']][heli['x']+1] == " ":
                map[heli['y']][heli['x']+1] = f"\33[0;35m{heli['range_index']}\33[0m"
            elif map[heli['y']+1][heli['x']] == " " and visited:
                map[heli['y']+1][heli['x']] = f"\33[1;33m{heli['range_index']}\33[0m"
            elif map[heli['y']+1][heli['x']] == " ":
                map[heli['y']+1][heli['x']] = f"\33[1;35m{heli['range_index']}\33[0m"
            else:
                map[heli['y']][heli['x']] += f",\33[0;35m{heli['range_index']}\33[0m"

    count = 1

    # Ja asetetaan kartan sivuun tietoja, i on rivin numero, row on rivin merkkijono, jonka perään lisätään
    #haluttuja tietoja, line:n sisään voi laittaa halutut tiedot.
    for i, row in enumerate(map):
        line = ""
        if i == 0:
            for c in range(2):
                line += f"{'':8.8s} {'Heliport name':22.22s} {'distance':8.8s} "
            print(''.join(row) , line)
        elif 0.0 <= float(count) <= (len(heliports_in_range)):
            if count == (len(heliports_in_range)):
                line += (f" | {count:2d}.{heliports_in_range[count-1]['name']:22.22s} | {heliports_in_range[count-1]['distance_from_player']:4.0f} km | {'':39.39s}|")
                print(''.join(row) + line)
                count += 1
            else:
                for c in range(2):
                    line += (
                        f" | {count:2d}.{heliports_in_range[count-1]['name']:22.22s} | {heliports_in_range[count-1]['distance_from_player']:4.0f} km | ")
                    count += 1
                print(''.join(row) + line)
                line = ""
        elif i == 5 or i == 7:
            line += " |"
            for _ in range(78):
                line += f"="
            line += "|"
            print(''.join(row) + line)
        elif i == 6:
            line += f" | Player at location: {player_heliport['name']:56.56s} |"
            print(''.join(row) + line)
        elif i == 8 :
            line += "|"
            if goal != False and goal['name'] != 'Breakdown':
                line += f"  You have found {goal['name']}, gained {goal['target_value']} |"
            elif goal != False and goal['name'] == 'Breakdown':
                line += f"  You have had a {goal['name']}, you lose {goal['target_value']} |"
            print(''.join(row), line)
        else:
            print(''.join(row), i)