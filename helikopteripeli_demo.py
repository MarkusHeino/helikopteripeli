import random
import MySQL

# tietokantaan yhdistäminen
conn = MySQL.connect('flight_game.db')
cursor = conn.cursor()

# pelaajan lompakko jalokiviä varten ja bensatankki
wallet = 0
fuel = 0

# määritellään arvot lentämiselle ja onnettomuudelle
FUEL_COST_PER_KM = 1
HELICOPTER_RANGE = 500
BREAKDOWN_PENALTY = 1000

# "miten tankataan" yritelmä
def refill_fuel(wallet, fuel):
    refill_amount = int(input("Kuinka paljon bensaa saisi olla (litroina)? "))
    if refill_amount > wallet:
        print("Sinulla ei ole tarpeeksi rahaa.")
    else:
        random_multiplier = random.uniform(1.1, 1.5)
        fuel_to_buy = refill_amount / random_multiplier
        fuel += fuel_to_buy
        wallet -= refill_amount
        print(f"Bensatankkiin tankattu {fuel_to_buy} litraa.")

# funktio lentokentälle lentämistä varten
def fly_to_heliport(current_heliport):
    destination = input("Anna helikopterikentän ICAO-koodi: ")

    # tarkastetaan voiko kohteeseen asti lentää
    distance = get_distance(current_heliport, destination)
    if distance > fuel:
        print("Ei ole tarpeeksi polttoainetta tuonne lentämistä varten.")
        return current_heliport

    # vähennetään polttoainetta kulutksen verran
    fuel_cost = distance * FUEL_COST_PER_KM
    fuel -= fuel_cost

    # tarkastetaan onko perillä onnettomuus-token
    check_destination(destination)

    return destination

# funktio joka laskee kahden helikopterikentän välinen etäisyys
def get_distance(heliport1, heliport2):
    # helikopterikenttien välinen etäisyys
    pass

# funktio joka tarkastaa kohteiden sisältämät jalokivet tai tokenit
def check_destination(heliport):
    # jalokivien ja tokenien tarkistus
    pass

# pääohjelma
current_heliport = input("Anna helikopterikentän ICAO-koodi: ")
while True:
    print(f"Nykyinen helikopterikenttä: {current_heliport}")
    print(f"Lompakon sisältö: ${wallet}")
    print(f"Bensaa: {fuel} litroina")

    # kysytään pelaajalta mitä tehdään
    action = input("Mitä tehdään (tankkaa/lennä/lopeta)?: ").lower()

    if action == "tankkaa":
        refill_fuel(wallet, fuel)
    elif action == "lennä":
        current_heliport = fly_to_heliport(current_heliport)
    elif action == "lopeta":
        break
    else:
        print("Väärä valinta. Valitse 'tankkaa', 'lennä' tai 'lopeta'.")

# suljetaan tietokantayhteys
conn.close()