import csv
import glob
import json
from pathlib import Path

from models.belt import Belt
from models.equip import Equip
from models.necklace import Necklace


def read_file(file: str) -> dict:
    with open(file, 'r') as f:
        data = json.loads(f.read())

    return data


def sanitize_file(file: str) -> dict:
    data = read_file(file)

    data.pop('scriptKeys')
    data.pop('templateKey')

    # keys defined as both defenseelement and defenseElement for some reason
    if data['scriptVars'].get('defenseelement'):
        data['defenseelement'] = data['scriptVars']['defenseelement']['element']

    if data['scriptVars'].get('defenseElement'):
        data['defenseelement'] = data['scriptVars']['defenseElement']['element']

    # keys defined as both offenseelement and offenseElement for some reason
    if data['scriptVars'].get('offenseelement'):
        data['offenseelement'] = data['scriptVars']['offenseelement']['element']

    if data['scriptVars'].get('offenseElement'):
        data['offenseelement'] = data['scriptVars']['offenseElement']['element']

    data.pop('scriptVars')

    return data


def create_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def sort_by_level(data: dict) -> dict:
    return sorted(data, key=lambda x: x.get('level', 0))


equipment = {
    'Accessory': [],
    'Armor': {
        'Monk': {
            'Female': [],
            'Male': [],
        },
        'Peasant': {
            'Female': [],
            'Male': [],
        },
        'Priest': {
            'Female': [],
            'Male': [],
        },
        'Rogue': {
            'Female': [],
            'Male': [],
        },
        'Warrior': {
            'Female': [],
            'Male': [],
        },
        'Wizard': {
            'Female': [],
            'Male': [],
        },
    },
    'Belt': [],
    'Boots': [],
    'Earrings': [],
    'Gauntlet': [],
    'Greaves': [],
    'Helmet': {
        'Monk': {
            'Female': [],
            'Male': [],
            'Unisex': [],
        },
        'Peasant': {
            'Female': [],
            'Male': [],
            'Unisex': [],
        },
        'Priest': {
            'Female': [],
            'Male': [],
            'Unisex': [],
        },
        'Rogue': {
            'Female': [],
            'Male': [],
            'Unisex': [],
        },
        'Warrior': {
            'Female': [],
            'Male': [],
            'Unisex': [],
        },
        'Wizard': {
            'Female': [],
            'Male': [],
            'Unisex': [],
        },
    },
    'Necklace': [],
    'OverArmor': {
        'Female': [],
        'Male': [],
        'Unisex': [],
    },
    'Ring': [],
    'Shield': [],
    'Weapon': {
        'Peasant': [],
        'Monk': [],
        'Priest': [],
        'Rogue': [],
        'Warrior': [],
        'Wizard': [],
    },
}


files = glob.glob('original/**/*.json', recursive=True)

# sanitize data from jsons and sort equipment
for file in files:
    data = sanitize_file(file)

    # organize data within files
    _class = data.get('class', '')
    equip_type = data.get('equipmentType', '')
    gender = data.get('gender', '')

    if equip_type in ['Armor', 'Helmet']:
        equipment[equip_type][_class][gender].append(data)
    elif equip_type in ['OverArmor']:
        equipment[equip_type][gender].append(data)
    elif equip_type in ['Weapon']:
        equipment[equip_type][_class].append(data)
    else:
        equipment[equip_type].append(data)

header = ['Name', 'LOC', 'LVL', 'WGT', 'AC', 'HP', 'MP', 'AS%', 'MR', 'STR', 'INT', 'WIS', 'CON', 'DEX', 'DMG', 'HIT', 'SKD', 'SKD%', 'SPD', 'SPD%', 'FHB', 'HB%', 'CDR%']

# this feels so dirty to do, but am not sure of a cleaner way otherwise.
# we're accessing inconsistent dict keys here and dumping them to a csv file.
# each csv needs to move to a specific folder in the docs/ path.

create_dir('csv')

# accessories
with open('csv/accessories.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Accessory'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: monk :: female
with open('csv/armor_monk_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Monk']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: monk :: male
with open('csv/armor_monk_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Monk']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: peasant :: female
with open('csv/armor_peasant_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Peasant']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: peasant :: male
with open('csv/armor_peasant_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Peasant']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: priest :: female
with open('csv/armor_priest_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Priest']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: priest :: male
with open('csv/armor_priest_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Priest']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: rogue :: female
with open('csv/armor_rogue_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Rogue']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: rogue :: male
with open('csv/armor_rogue_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Rogue']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: warrior :: female
with open('csv/armor_warrior_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Warrior']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: warrior :: male
with open('csv/armor_warrior_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Warrior']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: wizard :: female
with open('csv/armor_wizard_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Wizard']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# armor :: wizard :: male
with open('csv/armor_wizard_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Armor']['Wizard']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# belts
with open('csv/belts.csv', 'w+', newline='') as f:
    # add element type for belts specifically
    belt_header = header[:2] + ['ELE'] + header[2:]

    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(belt_header)

    sorted_data = sort_by_level(equipment['Belt'])

    for i in sorted_data:
        equip = Belt(i)
        csvwriter.writerow(equip.row)


# boots
with open('csv/boots.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Boots'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# earrings
with open('csv/earrings.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Earrings'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# gauntlet
with open('csv/gauntlets.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Gauntlet'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# greaves
with open('csv/greaves.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Greaves'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: monk :: female
with open('csv/helmet_monk_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Monk']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: monk :: male
with open('csv/helmet_monk_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Monk']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: peasant :: female
with open('csv/helmet_peasant_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Peasant']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: peasant :: male
with open('csv/helmet_peasant_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Peasant']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: priest :: female
with open('csv/helmet_priest_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Priest']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: priest :: male
with open('csv/helmet_priest_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Priest']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: rogue :: female
with open('csv/helmet_rogue_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Rogue']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: rogue :: male
with open('csv/helmet_rogue_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Rogue']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: warrior :: female
with open('csv/helmet_warrior_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Warrior']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: warrior :: male
with open('csv/helmet_warrior_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Warrior']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: wizard :: female
with open('csv/helmet_wizard_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Wizard']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# helmet :: wizard :: male
with open('csv/helmet_wizard_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Helmet']['Wizard']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# necklaces
with open('csv/necklaces.csv', 'w+', newline='') as f:
    # add element type for necklaces specifically
    neck_header = header[:2] + ['ELE'] + header[2:]

    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(neck_header)

    sorted_data = sort_by_level(equipment['Necklace'])

    for i in sorted_data:
        equip = Necklace(i)
        csvwriter.writerow(equip.row)


# overarmor :: female
with open('csv/overarmor_f.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['OverArmor']['Female'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# overarmor :: male
with open('csv/overarmor_m.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['OverArmor']['Male'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# overarmor :: unisex
with open('csv/overarmor_u.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['OverArmor']['Unisex'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# rings
with open('csv/rings.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Ring'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# shield
with open('csv/shields.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Shield'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# weapon :: monk
with open('csv/weapon_monk.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Weapon']['Monk'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# weapon :: peasant
with open('csv/weapon_peasant.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Weapon']['Peasant'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# weapon :: priest
with open('csv/weapon_priest.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Weapon']['Priest'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# weapon :: rogue
with open('csv/weapon_rogue.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Weapon']['Rogue'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# weapon :: warrior
with open('csv/weapon_warrior.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Weapon']['Warrior'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# weapon :: wizard
with open('csv/weapon_wizard.csv', 'w+', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(header)

    sorted_data = sort_by_level(equipment['Weapon']['Wizard'])

    for i in sorted_data:
        equip = Equip(i)
        csvwriter.writerow(equip.row)


# finally, we'll move the generated csv files to the place we want them.
# this is done in a secondary step in case you want to debug the content
# of the csvs before overwriting the existing ones.

Path('csv/accessories.csv').replace('../docs/equipment/csv/accessories.csv')
Path('csv/armor_monk_f.csv').replace('../docs/equipment/csv/armour/monk/female/armour.csv')
Path('csv/armor_monk_m.csv').replace('../docs/equipment/csv/armour/monk/male/armour.csv')
Path('csv/armor_peasant_f.csv').replace('../docs/equipment/csv/armour/peasant/female/armour.csv')
Path('csv/armor_peasant_m.csv').replace('../docs/equipment/csv/armour/peasant/male/armour.csv')
Path('csv/armor_priest_f.csv').replace('../docs/equipment/csv/armour/priest/female/armour.csv')
Path('csv/armor_priest_m.csv').replace('../docs/equipment/csv/armour/priest/male/armour.csv')
Path('csv/armor_rogue_f.csv').replace('../docs/equipment/csv/armour/rogue/female/armour.csv')
Path('csv/armor_rogue_m.csv').replace('../docs/equipment/csv/armour/rogue/male/armour.csv')
Path('csv/armor_warrior_f.csv').replace('../docs/equipment/csv/armour/warrior/female/armour.csv')
Path('csv/armor_warrior_m.csv').replace('../docs/equipment/csv/armour/warrior/male/armour.csv')
Path('csv/armor_wizard_f.csv').replace('../docs/equipment/csv/armour/wizard/female/armour.csv')
Path('csv/armor_wizard_m.csv').replace('../docs/equipment/csv/armour/wizard/male/armour.csv')
Path('csv/belts.csv').replace('../docs/equipment/csv/belts.csv')
Path('csv/boots.csv').replace('../docs/equipment/csv/boots.csv')
Path('csv/earrings.csv').replace('../docs/equipment/csv/earrings.csv')
Path('csv/gauntlets.csv').replace('../docs/equipment/csv/gauntlets.csv')
Path('csv/greaves.csv').replace('../docs/equipment/csv/greaves.csv')
Path('csv/helmet_monk_f.csv').replace('../docs/equipment/csv/helmets/monk/female/helmets.csv')
Path('csv/helmet_monk_m.csv').replace('../docs/equipment/csv/helmets/monk/male/helmets.csv')
Path('csv/helmet_peasant_f.csv').replace('../docs/equipment/csv/helmets/peasant/female/helmets.csv')
Path('csv/helmet_peasant_m.csv').replace('../docs/equipment/csv/helmets/peasant/male/helmets.csv')
Path('csv/helmet_priest_f.csv').replace('../docs/equipment/csv/helmets/priest/female/helmets.csv')
Path('csv/helmet_priest_m.csv').replace('../docs/equipment/csv/helmets/priest/male/helmets.csv')
Path('csv/helmet_rogue_f.csv').replace('../docs/equipment/csv/helmets/rogue/female/helmets.csv')
Path('csv/helmet_rogue_m.csv').replace('../docs/equipment/csv/helmets/rogue/male/helmets.csv')
Path('csv/helmet_warrior_f.csv').replace('../docs/equipment/csv/helmets/warrior/female/helmets.csv')
Path('csv/helmet_warrior_m.csv').replace('../docs/equipment/csv/helmets/warrior/male/helmets.csv')
Path('csv/helmet_wizard_f.csv').replace('../docs/equipment/csv/helmets/wizard/female/helmets.csv')
Path('csv/helmet_wizard_m.csv').replace('../docs/equipment/csv/helmets/wizard/male/helmets.csv')
Path('csv/necklaces.csv').replace('../docs/equipment/csv/necklaces.csv')
Path('csv/overarmor_f.csv').replace('../docs/equipment/csv/overarmor/female/overarmor.csv')
Path('csv/overarmor_m.csv').replace('../docs/equipment/csv/overarmor/male/overarmor.csv')
Path('csv/overarmor_u.csv').replace('../docs/equipment/csv/overarmor/unisex/overarmor.csv')
Path('csv/rings.csv').replace('../docs/equipment/csv/rings.csv')
Path('csv/shields.csv').replace('../docs/equipment/csv/shields.csv')
Path('csv/weapon_monk.csv').replace('../docs/equipment/csv/weapons/monk/weapons.csv')
Path('csv/weapon_peasant.csv').replace('../docs/equipment/csv/weapons/peasant/weapons.csv')
Path('csv/weapon_priest.csv').replace('../docs/equipment/csv/weapons/priest/weapons.csv')
Path('csv/weapon_rogue.csv').replace('../docs/equipment/csv/weapons/rogue/weapons.csv')
Path('csv/weapon_warrior.csv').replace('../docs/equipment/csv/weapons/warrior/weapons.csv')
Path('csv/weapon_wizard.csv').replace('../docs/equipment/csv/weapons/wizard/weapons.csv')
