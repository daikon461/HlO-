import json,pathlib,csv,sys
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'miracle_v05.json').read_text(encoding='utf-8'))
if cfg['unique_weapons']['enabled'] or any(cfg['unique_weapons'][m]['enabled'] for m in ('simplyswords','simplymore')):
 raise SystemExit('ERROR: Direct unique weapon insertion is blocked until native initialization and loot integration are verified.')
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
rows=list(csv.DictReader((root/'verified_targets.csv').open(encoding='utf-8-sig')))
assert len(rows)==250
for i in range(len(rows)):
 p=base/f'bonus_{i:03d}.json'
 obj=json.loads(p.read_text(encoding='utf-8'))
 for pool in obj.get('pools',[]):
  for entry in pool.get('entries',[]):
   if entry.get('name','').startswith(('simplyswords:','simplymore:')):
    raise SystemExit(f'ERROR: unverified direct unique weapon entry: {p}')
print('v0.6: 250 loot tables validated; no unsafe Simply Swords/Simply More injection')
