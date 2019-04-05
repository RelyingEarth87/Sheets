def main():
    import Sheets
    from IvCalc import IvCalculator as calculator
    species, level, iv, cp, hp, tier, best, good = Sheets.main()
    dust = []
    first = []
    second = []
    iv_calc = []

    for i in level:
        i = float(i)
        if i <= 2.5:
            dust.append(1)
        elif i <= 4.5:
            dust.append(2)
        elif i <= 6.5:
            dust.append(3)
        elif i <= 8.5:
            dust.append(4)
        elif i <= 10.5:
            dust.append(5)
        elif i <= 12.5:
            dust.append(6)
        elif i <= 14.5:
            dust.append(7)
        elif i <= 16.5:
            dust.append(8)
        elif i <= 18.5:
            dust.append(9)
        elif i <= 20.5:
            dust.append(10)
        elif i <= 22.5:
            dust.append(11)
        elif i <= 24.5:
            dust.append(12)
        elif i <= 26.5:
            dust.append(13)
        elif i <= 28.5:
            dust.append(14)
        elif i <= 30.5:
            dust.append(15)
        elif i <= 32.5:
            dust.append(16)
        elif i <= 34.5:
            dust.append(17)
        elif i <= 36.5:
            dust.append(18)
        elif i <= 38.5:
            dust.append(19)
        elif i <= 39.5:
            dust.append(20)
        else:
            dust.append(0)

    for i in tier:
        if i == "Not likely/May not be great/Room for improvement":
            first.append(0)
        elif i == "Above average/Decent/Pretty decent":
            first.append(1)
        elif i == "Certainly caught/Strong/Really strong":
            first.append(2)
        else:
            first.append(3)

    for i in good:
        if i == "Not out of the norm/Don't point to greatness/Kinda basic":
            second.append(0)
        elif i == "Noticeably trending/Get the job done/Good stats":
            second.append(1)
        elif i == "Certainly impressed/Excellent stats/Really strong":
            second.append(2)
        elif i == "Exceed calculations/Blown away/Best I've ever seen":
            second.append(3)

    i = 0

    while i <= len(species):
        try:
            if best[i] == "HP":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, False, False, True))
                calc = cal.calc()
                iv_calc.append(calc)
            elif best[i] == "Attack":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, True, False, False))
                calc = cal.calc()
                iv_calc.append(calc)
            elif best[i] == "Defense":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, False, True, False))
                calc = cal.calc()
                iv_calc.append(calc)
            elif best[i] == "HP, Attack":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, True, False, True))
                calc = cal.calc()
                iv_calc.append(calc)
        except:
            if best[i] == "HP":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, False, False, True))
                calc = cal.calc()
                iv_calc.append(calc)
            elif best[i] == "Attack":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, True, False, False))
                calc = cal.calc()
                iv_calc.append(calc)
            elif best[i] == "Defense":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, False, True, False))
                calc = cal.calc()
                iv_calc.append(calc)
            elif best[i] == "HP, Attack":
                cal = calculator(species[i], [cp[i], hp[i], dust[i], False], (first, second, True, False, True))
                calc = cal.calc()
                iv_calc.append(calc)
        print(iv_calc[i])
        i += 1


    


if __name__ == "__main__":
    main()
