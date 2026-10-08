import json,csv,pathlib,collections
root=pathlib.Path(__file__).resolve().parent
rows=list(csv.DictReader((root/'verified_targets.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
config=json.loads((root/'loot_balance.json').read_text(encoding='utf-8'))
counts=collections.Counter()
for i,row in enumerate(rows):
    name=row['loot_table_id'].lower()
    if any(x in name for x in ('ancient_city','end_city','bastion','treasure','vault','citadel','cataclysm','trial_chambers','netherite','temple')): tier='high'
    elif any(x in name for x in ('dungeon','stronghold','fortress','tower','crypt','shipwreck','pyramid','mineshaft')): tier='mid'
    else: tier='low'
    counts[tier]+=1
    p=base/f'bonus_{i:03d}.json'
    if not p.exists(): raise RuntimeError(f'Missing generated resource {p}')
    obj=json.loads(p.read_text())
    # Keep original v0.1 pools intact; add a second independently rolled reward pool.
    pool={
      'rolls':1,
      'entries':[{'type':'minecraft:item','name':item,'weight':weight} for item,weight in config['tiers'][tier]['rewards']],
      'conditions':[{'condition':'minecraft:random_chance','chance':config['tiers'][tier]['chance']}]
    }
    obj['pools'].append(pool)
    if tier=='high':
      obj['pools'].append({'rolls':1,'entries':[{'type':'minecraft:item','name':x,'weight':w} for x,w in config['jackpot']['rewards']], 'conditions':[{'condition':'minecraft:random_chance','chance':config['jackpot']['chance']}]})
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('v0.2 resource enhancement complete:',dict(counts),'targets',len(rows))
