import random


# color generator for common rarity
def common():
    PF = [0,0,0]
    EW = [255,255,255]
    EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for uncommon rarity
def uncommon():
    PF = [0,0,0]
    EW = [0,0,0]
    EC = [random.randint(0, 250),random.randint(0, 250),random.randint(0, 250)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [random.randint(100, 250),random.randint(100, 250),random.randint(100, 250)]
    BG = [250,249,213]
    BK = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for rare rarity
def rare(): # later on this will get complementary colors...
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0]
    EW = [0,0,0]
    EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [255-BC[0],255-BC[1],255-BC[2]]
    BG = [250,249,213]
    BK = [255-EC[0],255-EC[1],255-EC[2]]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for legendary rarity
def legendary_r():
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0]
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [random.randint(50, 255),0,0]
    BC = [random.randint(50, 255),0,0]
    OT = [random.randint(100, 250),0,0]
    BG = [random.randint(1, 255),0,0]
    BK = [random.randint(50, 255),0,0]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for legendary rarity
def legendary_g():
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0]
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [0,random.randint(50, 255),0]
    BC = [0,random.randint(50, 255),0]
    OT = [0,random.randint(100, 255),0]
    BG = [0,random.randint(1, 255),0]
    BK = [0,random.randint(50, 255),0]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for legendary rarity
def legendary_b():
    eyeWhiteColors = [255,0]
    eyeWhite = random.choice(eyeWhiteColors)
    PF = [0,0,0]
    EW = [eyeWhite,eyeWhite,eyeWhite]
    EC = [0,0,random.randint(50, 255)]
    BC = [0,0,random.randint(50, 255)]
    OT = [0,0,random.randint(100, 250)]
    BG = [0,0,random.randint(1, 255)]
    BK = [0,0,random.randint(50, 255)]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for classified rarity
def classified_blk():
    PF = [0,0,0]
    EW = [255,255,255]
    ECr = random.randint(0, 150)
    EC = [ECr,ECr,ECr]
    BCr = random.randint(0, 150)
    BC = [BCr,BCr,BCr]
    OT = [0,0,0]
    BG = [250,249,213]
    BKr = random.randint(0,150)
    BK = [BKr,BKr,BKr]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for classified rarity
def classified_wht():
    PF = [0,0,0]
    EW = [80,80,80]
    ECr = random.randint(120, 200)
    EC = [ECr,ECr,ECr]
    BCr = random.randint(120, 210)
    BC = [BCr,BCr,BCr]
    OT = [255,255,255]
    BG = [28,28,28]
    BKr = random.randint(160,210)
    BK = [BKr,BKr,BKr]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH

# color generator for holiday christmas
def holiday_christmas():
    PF = [0,0,0]
    EW = [255,255,255]
    EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [255-EC[0],255-EC[1],255-EC[2]]
    BG = [28,28,28]
    BK = [255-BC[0],255-BC[1],255-BC[2]]
    CH = [255, 0, 0]

    return PF, EW, EC, BC, OT, BG, BK, CH


# color generator for upside down image
def upsidedown():
    PF = [0,0,0]
    EW = [0,0,0]
    EC = [random.randint(100, 255),random.randint(0, 255),random.randint(0, 255)]
    BC = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]
    OT = [255-EC[0],255-EC[1],255-EC[2]]
    BG = [250,249,213]
    BK = [255-BC[0],255-BC[1],255-BC[2]]
    CH = None

    return PF, EW, EC, BC, OT, BG, BK, CH
