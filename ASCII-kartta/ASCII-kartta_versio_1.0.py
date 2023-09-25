# Define the size of the map (adjust as needed)
map_width = 50
map_height = 25

# Create an empty map filled with a default texture character
default_texture = '.'
south_africa_map = [[default_texture for _ in range(map_width)] for _ in range(map_height)]

# Define the coordinates of fictional public heliports
heliport_coordinates = [(10, 10), (20, 15), (35, 5)]

# Function to draw the border of South Africa on the map
def draw_border(map):
    border_char = '#'
    for i in range(map_height):
        if i < 5 or i >= map_height - 5:
            map[i] = [border_char] * map_width
        else:
            map[i][0] = border_char
            map[i][map_width - 1] = border_char

# Function to fill the map with a simple texture
def fill_with_texture(map, texture_char):
    for y in range(1, map_height - 1):
        for x in range(1, map_width - 1):
            map[y][x] = texture_char

# Draw the South Africa border
draw_border(south_africa_map)

# Fill the map with a texture (you can change the texture_char)
texture_char = ' '
fill_with_texture(south_africa_map, texture_char)

# Mark the heliports on the map
for x, y in heliport_coordinates:
    if 0 <= x < map_width and 0 <= y < map_height:
        south_africa_map[y][x] = 'H'  # Use 'H' to represent heliports

# Print the South Africa map
for row in south_africa_map:
    print(''.join(row))