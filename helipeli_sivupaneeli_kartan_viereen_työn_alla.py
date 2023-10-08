def draw_map(map_info, heliports_in_range, player_coordinates, MAX_RANGE, heliports_visited, goal=False, player_location=None, consumed_co2=None, remaining_fuel=None):
    # piirretään kartta sivupaneelilla
    map = draw_blank_map()

    count = 1

    # sivupaneelin koodi lähimmille kahdeksalle kentälle
    side_panel = []
    for i in range(1, 9):
        if i <= len(heliports_in_range):
            side_panel.append(
                f"{i}: {heliports_in_range[i - 1]['name']} ({heliports_in_range[i - 1]['distance_from_player']:.0f} km)")
        else:
            side_panel.append(f"{i}: -")

    # väliin viisi tyhjää riviä
    for _ in range(5):
        side_panel.append(" ")

    # Pelaajan sjainti, käytetty CO2, jäljellä oleva polttoaine ja vuoron numero helipadien alle
    if player_location is not None:
        side_panel.append(f"Player Location: {player_location}")
    if consumed_co2 is not None:
        side_panel.append(f"Consumed CO2: {consumed_co2}")
    if remaining_fuel is not None:
        side_panel.append(f"Remaining Fuel: {remaining_fuel}")
    if turn_counter is not None:
        side_panel.append(f"Turn: {turn_counter}")

    # printtaa kartan ja sivupaneelin
    for i, row in enumerate(map):
        line = ""
        if i == 0:
        #printtaa "headerit"
        elif 0.0 <= float(count) <= (len(heliports_in_range)):
            if count == (len(heliports_in_range)):
                line += (
                    f" | {count:2d}.{heliports_in_range[count - 1]['name']:22.22s} | {heliports_in_range[count - 1]['distance_from_player']:.0f} km | {'':39.39s}|")
                line += f"{' ' * 3}".join(side_panel)
                print(''.join(row) + line)
                count += 1
            else:
                for c in range(2):
                    line += (
                        f" | {count:2d}.{heliports_in_range[count - 1]['name']:22.22s} | {heliports_in_range[count - 1]['distance_from_player']:.0f} km | ")
                    count += 1
                line += f"{' ' * 3}".join(side_panel)
                print(''.join(row) + line)
                line = ""


# draw_map hakee nyt myös tiedot bensamittariin, hiilijalanjälkeen ja pelaajan sijaintiin - allaolevat muuttujat voi tietty muuttaa tarpeen mukaan
# draw_map(map_info, heliports_in_range, player_coordinates, MAX_RANGE, heliports_visited, player_location="Location", consumed_co2="123", remaining_fuel="456")
