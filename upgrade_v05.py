import csv,json,pathlib,random
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'miracle_v05.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
assert len(rows)==250, f'Expected 250 target tables, got {len(rows)}'
for i,row in enumerate(rows):
    path=base/f'bonus_{i:03d}.json'
    obj=json.loads(path.read_text(encoding='utf-8'))
    tier=row['tier']
    if cfg['enabled']:
        p=cfg['miracle_chance_by_tier'][tier]
        if not 0<=p<=1:raise ValueError('Invalid miracle chance')
        if p:
            obj['pools'].append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':p}], 'entries':[{'type':'minecraft:item','name':name,'weight':weight} for name,weight in cfg['miracle_items']]})
    if cfg['unique_weapons']['enabled']:
        raise RuntimeError('Unique weapons are intentionally blocked pending verification of registered IDs and native unique generation behavior; do not bypass this guard.')
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('v0.5 miracle pools generated for',len(rows),'targets')
