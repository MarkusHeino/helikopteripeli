# kartan koko esimerkiksi
map_width = 50
map_height = 25

# Create an empty map filled with spaces
south_africa_map = [[' ' for _ in range(map_width)] for _ in range(map_height)]

# Define the coordinates of fictional public heliports
heliport_coordinates = [(10, 10), (20, 15), (35, 5)]

# Mark the heliports on the map
for x, y in heliport_coordinates:
    if 0 <= x < map_width and 0 <= y < map_height:
        south_africa_map[y][x] = 'H'  # Use 'H' to represent heliports

# Print the South Africa map
for row in south_africa_map:
    print(''.join(row))