import textract
import re
import json

if __name__ == "__main__":
    path = "./img"
    # NOT recommended!
    for i in range(1, 6):
        exec(f"menu{i} = textract.process(f'{path}/menu{i}.jpg')")
        if i != 3:
            exec(f'menu{i}_str = str(menu{i}).replace("\\x0c","")')
        else:
            menu3_str = menu3.decode("utf-8")
    # Preprocessing steps, specific to this stores menu format
    milk_teas = [i.strip("b'") for i in menu1_str.split("\\n") if len(i) > 1]
    fruit_teas = [
        i.strip("b'").strip(".").capitalize() + " Tea"
        for i in menu2_str.split("\\n")
        if len(i) > 5
    ]
    ice_teas = [
        i.strip("b'").strip(".").capitalize().strip()
        for i in menu3_str.replace("\\n", " ").split("Mix")
        if len(i) > 1
    ]
    ice_teas_helper = [
        i + "lemonade)" if c == 0 else i.strip()
        for c, i in enumerate(ice_teas[0].split("lemonade"))
    ]
    ice_teas_helper.extend(ice_teas[1:])
    ice_teas = [
        i.capitalize().replace("_", "").replace("\n", " ")
        for i in ice_teas_helper
        if len(i) > 1
    ]
    ice_blend = [
        i.strip("b'").strip(".").capitalize().strip().replace("frop", "frap")
        for i in menu4.decode("utf-8").replace("\n", " ").replace("‘", "").split("Mix")
        if len(i) > 1
    ]
    toppings = [
        i.strip("b'")
        .strip(".")
        .capitalize()
        .strip()
        .replace("jl", "jelly")
        .replace("jey", "jelly")
        .replace("je ", "jelly")
        .replace("pobbies", "pobbles")
        for i in menu5.decode("utf-8")
        .replace("\n", " ")
        .replace("‘", "")
        .replace("!", "")
        .replace("jl", "jelly")
        .replace("je", "jelly")
        .split("Mix")
        if len(i) > 1
    ]
    tapioca = [
        i.strip("b'").strip(".").capitalize().strip() + " tapioca"
        for i in toppings[0].split("tapioca")
        if len(i) > 1 and len(i) < 75
    ]
    jelly = [
        i.strip("b'").strip(".").capitalize().strip() + " jelly"
        for i in toppings[0].split("jelly")
        if len(i) > 1 and len(i) < 75
    ]
    pobbles = [
        i.strip("b'").strip(".").capitalize().strip() + " pobbles"
        for i in toppings[0].split("pobbles")
        if len(i) > 1 and len(i) < 75
    ]
    toppings = tapioca + pobbles + jelly
    toppings[2] = [i for i in toppings[2].split("tapioca")][-1].strip()
    toppings = [i.capitalize() for i in toppings if len(i) > 1]
    milk_teas = [i.capitalize() for i in milk_teas if len(i) > 1]
    ice_teas = [i.capitalize() for i in ice_teas if len(i) > 1]
    fruit_teas = [i.capitalize() for i in fruit_teas if len(i) > 1]
    res = {
        "Milk Tea": milk_teas,
        "Fruit Tea": fruit_teas,
        "Ice Tea": ice_teas + ice_blend,
        "Toppings": toppings,
    }
    with open("./data/data.json", "w+") as f:
        json.dump(res, fp=f)
