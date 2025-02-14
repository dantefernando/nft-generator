from PIL import Image
dimensions = 400,400


cigarette = Image.open('accessories/cigarette.png')
cigarette = cigarette.resize(dimensions, resample=0)

christmas = Image.open("accessories/christmas.png")
christmas = christmas.resize(dimensions, resample=0)

gold_chain = Image.open("accessories/gold_chain.png")
gold_chain = gold_chain.resize(dimensions, resample=0)

back_cap = Image.open("accessories/back_cap.png")
back_cap = back_cap.resize(dimensions, resample=0)

bow_tie = Image.open("accessories/bow_tie.png")
bow_tie = bow_tie.resize(dimensions, resample=0)

joint = Image.open("accessories/joint.png")
joint = joint.resize(dimensions, resample=0)