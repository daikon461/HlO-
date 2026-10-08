import csv,json,pathlib,collections
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'mod_rewards.json').read_text())
rows=list(csv.DictReader((root/'verified_targets.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
counts=collections.Counter()
if cfg['enabled']:
 for i,row in enumerate(rows):
  target=row['loot_table_id'].lower()
  tier='high' if any(x in target for x in ('ancient_city','end_city','bastion','treasure','vault','citadel','cataclysm','trial_chambers','temple')) else ('mid' if any(x in target for x in ('dungeon','stronghold','fortress','tower','crypt','shipwreck','pyramid','mineshaft')) else 'low')
  # Each structure gets a distinctive focus, with a small cross-category selection.
  focus='cataclysm' if target.startswith('cataclysm:') else ('create' if 'factory' in target or 'mineshaft' in target else ('irons_spellbooks' if 'magic' in target or 'wizard' in target else 'ars_nouveau'))
  order=[focus]+[k for k in cfg['mod_items'] if k!=focus]
  entries=[]
  for j,mod in enumerate(order):
   items=cfg['mod_items'][mod]
   if not items:continue
   chosen=items[:2] if tier=='low' else (items[:4] if tier=='mid' else items)
   for item in chosen:
    if tier=='low' and any(x in item for x in ('epic','legendary','ignitium','cursium','void_core')):continue
    entries.append({'type':'minecraft:item','name':item,'weight':7 if j==0 else 2})
  if not entries:continue
  path=base/f'bonus_{i:03d}.json'
  data=json.loads(path.read_text())
  data['pools'].append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':cfg['chances'][tier]}],'entries':entries})
  path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
  counts[tier]+=1
print('Mod item reward pools added:',dict(counts))
