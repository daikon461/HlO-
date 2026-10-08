#!/usr/bin/env python3
"""Set a dedicated world-tier chance for HLO's enchant-progression equipment pool.
Run AFTER upgrade_full_world_tiers.py. Idempotent on generated loot JSON.
"""
import json,csv,pathlib
root=pathlib.Path(__file__).resolve().parent
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
chances={'haven':.12,'frontier':.22,'ascent':.38,'summit':.58,'pinnacle':.80}
# Structure difficulty scales these chances, but preserves monotonic tier growth.
structure={'starter':.75,'early_mid':.85,'mid':1.,'mid_late':1.08,'late':1.15,'apex':1.20}
changed=0
for i,row in enumerate(rows):
    path=base/f'bonus_{i:03d}.json'
    if not path.exists():continue
    data=json.loads(path.read_text(encoding='utf-8'))
    for pool in data.get('pools',[]):
        # Only the three-item enchant-progression equipment pool; avoid changing
        # enchanted relics, Apotheosis loot, or unrelated bonus rolls.
        entries=pool.get('entries',[])
        if len(entries)!=3 or not all(any(f.get('function')=='minecraft:set_enchantments' for f in e.get('functions',[])) for e in entries):
            continue
        if not all(e.get('name','').startswith('minecraft:') for e in entries):continue
        tier=next((t for c in pool.get('conditions',[]) if c.get('condition')=='apotheosis:has_world_tier' for t in c.get('tiers',[]) if t in chances),None)
        if tier is None:continue
        probability=round(min(.95,chances[tier]*structure.get(row['tier'],1)),6)
        condition=next((c for c in pool.get('conditions',[]) if c.get('condition')=='minecraft:random_chance'),None)
        if condition is None:pool.setdefault('conditions',[]).append({'condition':'minecraft:random_chance','chance':probability})
        else:condition['chance']=probability
        changed+=1
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert changed==len(rows)*5,(changed,len(rows))
print(f'Enchanted equipment probability overrides: {changed} (targets {len(rows)}, world tiers 5)')
