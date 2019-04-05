class IvCalculator:
    def __init__(self, pokemon_name, powerup_stats, appraisal):
        pkmon = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus', 'Rattata-A', 'Exegutor-A', 'Grimer-A', 'Muk-A', 'Meowth-A', 'Persian-A', 'Vulpix-A', 'Ninetails-A', 'Sandshrew-A', 'Sandslash-A', 'Raticate-A', 'Diglett-A', 'Dugtrio-A', 'Geodude-A', 'Graveler-A', 'Golem-A', 'Raichu-A', 'Marowak-A', 'Castform-Normal', 'Castform-Sunny', 'Castform-Rainy', 'Castform-Snowy']

        if pokemon_name not in pkmon:
            raise NameError("Invalid Pokemon")

        if "-" in pokemon_name:
            sp = pokemon_name.split("-")
            if sp[0] == "Castform":
                self.name = sp[0]
            elif sp[0] == "Nidoran":
                if sp[1] == "M":
                    self.name = "Nidoran♂"
                else:
                    self.name = "Nidoran♀"
            else:
                self.name = "Alolan " + sp[0]
        else:
            self.name = pokemon_name

        self.cp = powerup_stats[0]
        self.hp = powerup_stats[1]
        self.dust = powerup_stats[2]
        self.first = appraisal[0]
        self.second = appraisal[1]
        self.atk = appraisal[2]
        self.defs = appraisal[3]
        self.stam = appraisal[4]


    def calc(self):
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        stat = []
        i = 0
        while "Avg" not in stat:
            if i > 10:
                print("Error")
                break
            try:
                driver = webdriver.Chrome()
                driver.get("https://pokemongo.gamepress.gg/pokemongo-iv-calculator#/")
                driver.set_script_timeout(20)
                try:
                    species = driver.find_elements_by_xpath("//input[@type='text']")[1]
                    species.send_keys(self.name)
                except:
                    species = driver.find_elements_by_xpath("//label/input")[0]
                    species.send_keys(self.name)
                cp = driver.find_elements_by_xpath("//input[@type='number']")[0]
                cp.send_keys(self.cp)
                hp = driver.find_elements_by_xpath("//input[@type='number']")[1]
                hp.send_keys(self.hp)
                stardust = driver.find_elements_by_xpath("//div[@id='calc-view']/div/div[4]/label/select")[0]
                stardust.send_keys(Keys.ARROW_DOWN * self.dust)
                Keys.ENTER
                team = driver.find_elements_by_xpath("//div[2]/img")[0]
                team.click()
                appraisal = driver.find_elements_by_xpath("//div[4]/div/label/select")[0]
                appraisal.click()
                if self.first == 3:
                    t1 = appraisal.send_keys(Keys.ARROW_DOWN)
                    Keys.ENTER
                elif self.first == 2:
                    t2 = appraisal.send_keys(Keys.ARROW_DOWN * 2)
                    Keys.ENTER
                elif self.first == 1:
                    t3 = appraisal.send_keys(Keys.ARROW_DOWN * 3)
                    Keys.ENTER
                elif self.first == 0:
                    t4 = appraisal.send_keys(Keys.ARROW_DOWN * 4)
                    Keys.ENTER

                appraisal2 = driver.find_elements_by_xpath("//div[2]/label/select")[0]
                appraisal2.click()
                if self.second == 3:
                    t1 = appraisal2.send_keys(Keys.ARROW_DOWN)
                    Keys.ENTER
                elif self.second == 2:
                    t2 = appraisal2.send_keys(Keys.ARROW_DOWN * 2)
                    Keys.ENTER
                elif self.second == 1:
                    t3 = appraisal2.send_keys(Keys.ARROW_DOWN * 3)
                    Keys.ENTER
                elif self.second == 0:
                    t4 = appraisal2.send_keys(Keys.ARROW_DOWN * 4)
                    Keys.ENTER

                if self.atk:
                    attack = driver.find_elements_by_xpath("//div[3]/div[2]/label")[0]
                    attack.click()
                if self.defs:
                    defense = driver.find_elements_by_xpath("//div[3]/div[3]/label")[0]
                    defense.click()
                if self.stam:
                    stamina = driver.find_elements_by_xpath("//div[3]/div/label")[0]
                    stamina.click()

                calc = driver.find_elements_by_xpath("//div/button")[0]
                calc.click()
                ivs = driver.find_elements_by_xpath("//div[8]/div/div[2]/label")[0]
                tat = ivs.text
                stat = tat.split()
            except:
                pass

            driver.quit()
            i += 1
        stats = stat[3]
        stats = stats.replace("(", "")
        stats = stats.replace(")", "")
        stats = stats.replace("%", "")
        return stats


    def __repr__(self):

        return self.calc()
