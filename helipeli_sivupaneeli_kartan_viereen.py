def draw_map(map_info, heliports_in_range, player_coordinates, MAX_RANGE, heliports_visited, goal=False):
    # create a blank map
    map = draw_blank_map()

    # ... (rest of the code remains the same)

    count = 1

    # Create a side panel to display heliports in range from 1 to 8
    side_panel = []
    for i in range(1, 9):
        if i <= len(heliports_in_range):
            side_panel.append(f"{i}: {heliports_in_range[i - 1]['name']} ({heliports_in_range[i - 1]['distance_from_player']:.0f} km)")
        else:
            side_panel.append(f"{i}: -")

    # Print the map and side panel
    for i, row in enumerate(map):
        line = ""
        if i == 0:
            # ... (print headers)
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
        # ... (rest of the code remains the same)

# Example usage:
# You can call draw_map with your data here, e.g.,
# draw_map(map_info, heliports_in_range, player_coordinates, MAX_RANGE, heliports_visited)
