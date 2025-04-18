# generate_csv

This directory is used to generate CSVs from a json equipment dump provided by the Unora dev team. The raw json files themselves will not be uploaded into this repo, but are necessary to generate an up to date list of all current equipment in the game. You will need to collect a dump of the equipment to accurately re-generate these files.

## Explanation

Inside of the `original` directory, an extracted list of folders provided by the Unora dev team should be placed here. It doesn't matter what the folders or files are called as we're just globbing all `.json` files in this directory.

Running `python main.py` will parse through all of the jsons, creating an organized dict that categorizes all of the equipment by type. It sorts them in ascending order by level and writes the output to a csv, which is then placed into the appropriate location in the `docs/` directory, providing static content tables for each of equipment types.

## To do

- Create a lookup file that holds the locations for where equipment can be found. Merge these with the CSVs during generation time
- Continue mucking with the CSS to show a coherent table with many columns

## Example

Here's a (sanitized) example of what a pair of boots looks like in a single json file. The data here is sanitized as the development team does not want certain keys shared in these files:

```json
{
    "buyCost": 100,
    "category": "Boots",
    "color": "Navy",
    "displaySprite": 1,
    "equipmentType": "Boots",
    "gender": "Unisex",
    "isModifiable": true,
    "maxDurability": 3000,
    "maxStacks": 1,
    "modifiers": {
        "dex": 1
    },
    "sellValue": 50,
    "weight": 2,
    "advClass": "None",
    "class": "Peasant",
    "description": "Footwear designed for basic protection and mobility.",
    "level": 1,
    "name": "Boots",
    "panelSprite": 95
}
```
