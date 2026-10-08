#!/usr/bin/env python3
"""Add a distinct rare enchanted gear pool without interfering with mod affix generation."""
import csv,json,pathlib
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'legendary_v05.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
count=0
for i,row in enumerate(rows):
    tier=row['tier']; setting=cfg['tiers'][tier]; chance=setting['chance']; level=setting['level']
    assert 0<=chance<=1 and 1<=level<=255
    if not cfg['enabled'] or chance==0:continue
    path=base/f'bonus_{i:03d}.json'; data=json.loads(path.read_text(encoding='utf-8'))
    material='iron' if tier in ('starter','early_mid') else ('diamond' if tier in ('mid','mid_late') else 'netherite')
    def item(name, enchants, weight):
        return {'type':'minecraft:item','name':name,'weight':weight,'functions':[{'function':'minecraft:set_enchantments','enchantments':enchants}]}
    entries=[
        item(f'minecraft:{material}_sword',{'minecraft:sharpness':level,'minecraft:unbreaking':min(5,level),'minecraft:looting':min(5,max(1,level-1))},5),
        item(f'minecraft:{material}_axe',{'minecraft:efficiency':level,'minecraft:unbreaking':min(5,level),'minecraft:fortune':min(4,max(1,level-2))},4),
        item(f'minecraft:{material}_boots',{'minecraft:protection':max(1,level-1),'minecraft:feather_falling':min(6,level),'minecraft:unbreaking':min(5,level)},4),
        item('minecraft:bow',{'minecraft:power':level,'minecraft:unbreaking':min(5,level),'minecraft:flame':1},3),
        item('minecraft:enchanted_book',{'minecraft:efficiency':level,'minecraft:unbreaking':min(5,level)},3)
    ]
    data['pools'].append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':chance}],'entries':entries})
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');count+=1
print('RC5 premium pools:',count)
