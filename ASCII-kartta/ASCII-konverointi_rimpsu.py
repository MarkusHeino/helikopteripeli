import sys, random, argparse
import numpy as np
import math

# Pitää määrittää 1) mistä kuva importataan - nyt location 2) kuvan nimeäminen - nyt image
# Mutta periaatteessa tällä voi mallailla mitä tahansa kuvia - mustavalkona tai väreissä - ASCII-kartaksi peliin nyt tai jatkossa

from location import Image

# harmaansävyt pitää katsoa erikseen, mutta laitoin nyt skaalan vaan 0-255 (ks. alla rivi ~87)

# tämä merkkijono antaa Pythonille 70 harmaan eri sävyä
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Ja nämä merkit 10
gscale2 = '@%#*+=-:. '


def getAverageL(image):

    # numpy määrittää kuvan tällä
    im = np.array(image)

    # muoto
    w, h = im.shape

    # muoto keskiarvon mukaan
    return np.average(im.reshape(w * h))


def ConvertImageToAscii(fileName, cols, scale, moreLevels):

    # annetaan perusarvot
    global gscale1, gscale2

    # avaa kuva ja muunna harmaasävyksi
    image = Image.open(fileName).convert('L')

    # tallennetaan kuvan mitat annetun perusteella
    W, H = image.size[0], image.size[1]
    print("Anna kuvan koko: %d x %d" % (W, H))

    # merkin leveys
    w = W / cols

    # merkin koko kuvan skaalan mukaan
    h = w / scale

    # montako riviä kuva vie
    rows = int(H / h)

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # varmista että kuvan mittasuhteet ovat sopivan isot/eivät liian pienet
    if cols > W or rows > H:
        print("Liian pieneen tilaan liikaa merkkejä ja värejä!")
        exit(0)

    # ASCII-kuva on valittujen merkkien muodostama jono
    aimg = []
    # kuvan mittasuhteet generoidaan
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)

        # viimeinen merkkitiili jiiriin
        if j == rows - 1:
            y2 = H

        # tyhjän jonon liite/append
        aimg.append("")

        for i in range(cols):

            # mikä kroppi per yhden merkin koko/sen viemä tila
            x1 = int(i * w)
            x2 = int((i + 1) * w)

            # viimeinen merkkijono
            if i == cols - 1:
                x2 = W

            # kropataan kuva oikean kokoiseksi
            img = image.crop((x1, y1, x2, y2))

            # valkoisuuden/gscale-skaala 0-255
            avg = int(getAverageL(img))

            # säädetään ASCII-merkit
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]

            # ASCII-merkit merkkisarjaksi
            aimg[j] += gsval

    # palauttaa txt-tiedoston
    return aimg


# pääohjelma/-funktio
def main():
    # luodaan parsija
    descStr = "Tämä ohjelma muuntaa kuvan ASCII-kartaksi."
    parser = argparse.ArgumentParser(description=descStr)
    # kaikki eri muuttujat ja päättäjät määriteltävä
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')

    # parsitaan argumentit kasaan
    args = parser.parse_args()

    imgFile = args.imgFile

    # mikä output fileen nimeksi?
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile

    # skaalaus pitää katsoa tarkkaan ettei kuva veny
    # fontin skaalaus "Courier"
    scale = 0.43
    if args.scale:
        scale = float(args.scale)

    # värit
    cols = 80
    if args.cols:
        cols = int(args.cols)

    print('generating ASCII art...')
    # muunnetaan kuva ASCII-tekstiksi
    aimg = ConvertImageToAscii(imgFile, cols, scale, args.moreLevels)

    # avataan tiedosto kirjoitusta varten
    f = open(outFile, 'w')

    # kirjoitetaan kartta
    for row in aimg:
        f.write(row + '\n')

    # putsataan turhat pois
    f.close()
    print("ASCII valmis %s" % outFile)


