def input_ascii_image():
    print(",**,,,,.,,,,,*,./../(/.,,..**....,.,,,,,,,,,,,,,,,,,,,,,,,,,,,
   ,,,,,,..***,,*//,,..,,,.,.,*,,.. .../**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
   ,,,,,.*/,,,,,,/....,.,,,,/,..,,...,....,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
     ,,,,,,,,,,*,...,.,.*,,..,,,..,...,.*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
      ,,,,,,,,.,..,...*&**..../.....,,...*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
      *,,,,#*.,... /....,.,,..(../,....,./,/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
       ,,,,,,,.*,,.,,,,,,(,.*....,,,,,*/.*./,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        , ,,,,,,,,,,,,,/(,,,,*,,..**,.,,,,./*//*,,,,,,,,,,,,,,,,,,,,,,,,,
         ,,,,,,,,,.*,,,,,,*.//.*.*,*,,.*.,.../,/(.*,,,,,,,,,,,,,,,,,,,,,,
      ,,,,,,,,,,,.*,,,,,,,,**/ *./,(,,.,,.......,..,,,,,,,,,,,,,,,,,,,,,,
   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,...,...,,.. //..,.*...,*,,,,,,,,,,,,,,,,,,
   ,,,,,,,,,,,,,,,,,,,,,,,,,,**,..,,*,,,**/...,/../*,.,,,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,*#..**,,,,,..,*.*/...../,,..,,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,,,,,,,,,,,,,**...(.//,,,**..,.. **...,,,,,,,,,,,,,,,,,,,
   .,,,,,,,,,,,,/* ..,/*,.,*,..(,,. ..,,.,,..**. .....,*.,,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,,/(..,,..,#,.*.*..***..*./,.//./ ....,...*,,,,,,,,,,,,,,,
    ,,,,,,,,,,,,...,..,,.**//,..,,.,,.....*.***/,(......,,/.../.../,,,,,,
   ,,,,,,,,,,*,,,,,,/./,,,,,../*. *,.,,/. ./* (.*,.././(,,./( . ..., .,,,
   ,,,,,,,,,,,,,,,,//,*.,,....,./,../*(*,,,../..,,*,,*.,/ *..,,.. .*.**,,
   ,,,,,,,,,,,,,,,,,/*,,,.,,,*,.....*,(/../.,*.,*,.  ...,....,..,*. ,.,,,
   ,,,,,,,,,,,,,//..,*,.,,,,/..,.,.. ..,*...#.//......*,*.,.(#....,..*(,,
   ,,,,,,,,,,,....,.,,..,.,...../,.,,...,.(,..*.**...(./.,... .  ,**,,,,,
   ,,,,,,,,,.,,..**, ..,***,,*..,.,./**,/.*.,*.,,/..%*/.*,.../...**,,,,,,
   ,,,,,,,,,..*,,,**.....,*/.(*..*...**.,., ...*(.(/*.,**,(./...,,,,,,,,,
   ,,,,,,,,,,,,,,,,,,*,*/.,*(,,,,.,...*.,..**,.*.,(,**//&../*,,,,,,,,,,,,
   ,,,,,,,,,,,,,,,,,,,,*,*(*((,..../*,,//....,.(./ / *......,, ...,.,,,,,
   ,,,,,,,,,,,,,,/,..,,,/..,*.(/.*,,**./.,, ....,.*...,..,,*...*,(,*,,,,,
   ,,,,,,,,,,,,,,.....,,,..**. . ..,,.../((.,,,*.,, ..........,,(,,,,,,
   ,,,,,,,,,,,,,,,,.,....,*,...,.,..**.(* ..,.,,/,***,(,/.*,,,,,,,,,,,
   ,,,,,,,,,,...,,/*.,,.*,*,,**,,.*.(*.,,/,,.*,,,,,,,,,,,,,,,,,,,,,,,,
   ,,,,,,,*//..,/*./,,..,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
   ,,,*,,*...,,,,,,,*,,,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
   ,,,,,,. ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,......")

    ascii_image = []

    # ASCII-kartan voi periaatteessa tuoda mistä vain tai copypastettaa tuohon ylle, kunnes laitetaan done-komento
    while True:
        line = input()
        if line.strip().lower() == 'done':
            break
        ascii_image.append(line)

    return "\n".join(ascii_image)


def main():
    ascii_image = input_ascii_image()
    print(ascii_image)

