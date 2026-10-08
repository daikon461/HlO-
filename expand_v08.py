import csv,json,pathlib,copy
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'expansion_v08.json').read_text(encoding='utf8'))
existing={r['loot_table_id'] for r in csv.DictReader((root/'verified_targets.csv').open(encoding='utf-8-sig'))}
rows=list(csv.DictReader((root/'extra_targets_v08.csv').open(encoding='utf-8-sig')))
assert len(rows)==len(set(r['loot_table_id'] for r in rows))
assert not any(r['loot_table_id'] in existing for r in rows)
base=root/'src/main/resources/data/hardcore_loot_overhaul'
index=pathlib.Path(root/'src/main/resources/data/neoforge/loot_modifiers/global_loot_modifiers.json')
idx=json.loads(index.read_text())
for n,row in enumerate(rows):
    target=row['loot_table_id'];tier=row['tier'];name=f'extra_{n:03d}'
    assert tier in cfg['chance_by_tier']
    chance=cfg['chance_by_tier'][tier]
    assert 0<=chance<=1
    pool={'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':chance}],'entries':[{'type':'minecraft:item','name':item,'weight':weight} for item,weight in cfg['items_by_tier'][tier]]}
    miracle=cfg['miracle_chance']
    pools=[pool]
    if miracle:
        pools.append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':miracle}],'entries':[{'type':'minecraft:item','name':'minecraft:enchanted_golden_apple'}]})
    (base/'loot_table/chests'/f'{name}.json').write_text(json.dumps({'type':'minecraft:chest','pools':pools},indent=2)+'\n')
    (base/'loot_modifiers'/f'{name}.json').write_text(json.dumps({'type':'neoforge:add_table','conditions':[{'condition':'neoforge:loot_table_id','loot_table_id':target}],'table':f'hardcore_loot_overhaul:chests/{name}'},indent=2)+'\n')
    idx['entries'].append(f'hardcore_loot_overhaul:{name}')
index.write_text(json.dumps(idx,indent=2)+'\n')
print('v0.8 additional tables:',len(rows),'total modifiers:',len(idx['entries']))
