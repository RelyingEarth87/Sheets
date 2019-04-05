# Sheets

An extension of https://github.com/RelyingEarth87/PokemonGoDataCollection where I am using Selenium and Google Drive API to recover data that would have been lost otherwise and using Gamepress' IV calculator to recover it.

Get_Data.py is the main file that would be called, and it imports data from the other two files, parses, splits, and organizes it, then feeds it through the loop to get the output. Sheets.py imports all the data from each pokemon from a spreadsheet using the Google Drive API, and IvCalc.py takes the data and pushes it through <a href="https://pokemongo.gamepress.gg/pokemongo-iv-calculator#/">Gamepress' IV Calculator</a> using Selenium and grabs the average IV percentage. 
