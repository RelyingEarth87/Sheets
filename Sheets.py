def main():
    import time
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('pokemon data-9990ee34e5e1.json', scope)

    gc = gspread.authorize(credentials)

    wks = gc.open("Copy of Old Catch IV Responses").sheet1

    labels = ["What Pokémon did you catch?", "What was the level of the caught Pokémon?", "How closely do you know the IVs of your Pokémon?", "CP?", "HP?", "Overall IV tier?", "Best IV?", "How good is the best IV?", "CP at next level?"]

    sp = species(wks)
    time.sleep(100)
    
    lvl = level(wks)
    time.sleep(100)
    
    vi = iv(wks)
    time.sleep(100)
    
    pc = cp(wks)
    time.sleep(100)
    
    ph = hp(wks)
    time.sleep(100)
    
    t = tier(wks)
    time.sleep(100)
    
    b = best(wks)
    time.sleep(100)
    
    g = good(wks)

    return sp, lvl, vi, pc, ph, t, b, g
        

    

def species(wks):
    species = []

    for i in range(18, 77):
        i = str(i)
        x = ("H" + i)
        sp = wks.acell(x).value
        sp.replace("-A", "")
        species.append(sp)

    return species

def level(wks):
    level = []

    for i in range(18, 77):
        i = str(i)
        y = ("I" + i)
        lv = wks.acell(y).value
        lv = eval(lv)
        level.append(lv)

    return level

def iv(wks):
    iv = []

    for i in range(18, 77):
        i = str(i)
        z = ("J" + i)
        ivs = wks.acell(z).value
        iv.append(ivs)

    return iv

def cp(wks):
    cp = []

    for i in range(18, 77):
        i = str(i)
        a = ("P" + i)
        p = wks.acell(a).value
        p = eval(p)
        cp.append(p)

    return cp

def hp(wks):
    hp = []

    for i in range(18, 77):
        i = str(i)
        b = ("Q" + i)
        h = wks.acell(b).value
        h = eval(h)
        hp.append(h)

    return hp

def tier(wks):
    tier = []

    for i in range(18, 77):
        i = str(i)
        c = ("R" + i)
        t = wks.acell(c).value
        tier.append(t)

    return tier

def best(wks):
    best = []

    for i in range(18, 77):
        i = str(i)
        d = ("S" + i)
        est = wks.acell(d).value
        best.append(est)

    return best

def good(wks):
    good = []

    for i in range(18, 77):
        i = str(i)
        e = ("T" + i)
        goo = wks.acell(e).value
        good.append(goo)

    return good

def next_cp(wks):
    next_cp = []

    for i in range(18, 77):
        i = str(i)
        f = ("U" + i)
        nex = wks.acell(f).value
        nex = eval(nex)
        next_cp.append(nex)

    return next_cp
        
if __name__ == "__main__":
    main()
