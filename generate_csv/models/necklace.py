class Necklace:
    def __init__(self, data: dict):

        if data.get('requiresMaster'):
            level = 'Master'
        else:
            level = data.get('level', '-')

        self.row = [
            data.get('name'),
            data.get('location', '-'),
            data.get('offenseelement', '-').capitalize(),
            level,
            data.get('weight', '-'),
            data.get('modifiers', {}).get('ac', '-'),
            data.get('modifiers', {}).get('maximumHp', '-'),
            data.get('modifiers', {}).get('maximumMp', '-'),
            data.get('modifiers', {}).get('attackSpeedPct', '-'),
            data.get('modifiers', {}).get('magicResistance', '-'),
            data.get('modifiers', {}).get('str', '-'),
            data.get('modifiers', {}).get('int', '-'),
            data.get('modifiers', {}).get('wis', '-'),
            data.get('modifiers', {}).get('con', '-'),
            data.get('modifiers', {}).get('dex', '-'),
            data.get('modifiers', {}).get('dmg', '-'),
            data.get('modifiers', {}).get('hit', '-'),
            data.get('modifiers', {}).get('flatSkillDamage', '-'),
            data.get('modifiers', {}).get('skillDamagePct', '-'),
            data.get('modifiers', {}).get('flatSpellDamage', '-'),
            data.get('modifiers', {}).get('spellDamagePct', '-'),
            data.get('modifiers', {}).get('healBonus', '-'),
            data.get('modifiers', {}).get('healBonusPct', '-'),
            data.get('modifiers', {}).get('cooldownReductionPct', '-'),
        ]
