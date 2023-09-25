# kartan koko esimerkiksi
map_width = 50
map_height = 25

# kartan pitäisi olla täynnä pisteitä, mutta ei ole :D
default_texture = '.'
south_africa_map = [[default_texture for _ in range(map_width)] for _ in range(map_height)]

# määritellään helipadien sijainnit koordinaatteina eli pisteinä kartalla kuten shakkilaudassa
heliport_coordinates = [(10, 10), (20, 15), (35, 5)]

# piirretään kartta
def draw_border(map):
    border_char = '#'
    coastline_char = '='
    for i in range(map_height):
        if i < 5 or i >= map_height - 5:
            map[i] = [border_char] * map_width
        else:
            map[i][0] = border_char
            map[i][map_width - 1] = border_char

    for i in range(map_width):
        map[0][i] = border_char
        map[map_height - 1][i] = border_char
        if i < map_width // 2:
            map[map_height // 2][i] = coastline_char

# tekstuurit ei näy ainakaan PyCharmissa
def fill_with_texture(map, texture_char):
    for y in range(1, map_height - 1):
        for x in range(1, map_width - 1):
            map[y][x] = texture_char

# funktio kartan tulostamiseen
draw_border(south_africa_map)

# tekstuurien funktio, ehkä
texture_char = ' '
fill_with_texture(south_africa_map, texture_char)

# tällä merkitään helipadien sijainnit määrittelyn mukaan
for x, y in heliport_coordinates:
    if 0 <= x < map_width and 0 <= y < map_height:
        south_africa_map[y][x] = 'H'  # H on tässä helipadin sijainnin merkintä

# Tällä yritin lisätä kompassin ilmansuunnat karttaan - ne ei oikein näy, mutta ovat siellä seassa
south_africa_map[0][map_width // 2] = 'N'
south_africa_map[map_height - 1][map_width // 2] = 'S'
south_africa_map[map_height // 2][0] = 'W'
south_africa_map[map_height // 2][map_width - 1] = 'E'

# Ja sitten printataan
for row in south_africa_map:
    print(''.join(row))
