#!/usr/bin/env python3
"""Expand HLO's own bonus loot pools across Apotheosis world tiers.
Preserves structure-based loot tiers, scales per-pool chances and enchantment levels.
"""
import json, pathlib, copy, math
root=pathlib.Path(__file__).resolve().parent
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
world=('haven','frontier','ascent','summit','pinnacle')
chance_factor=(0.55,0.8,1.0,1.3,1.65)
level_factor=(0.75,0.9,1.0,1.2,1.4)
processed=0; changed_pools=0; changed_enchants=0

def update_enchants(node, factor):
    global changed_enchants
    if isinstance(node,dict):
        if node.get('function')=='minecraft:set_enchantments':
            for name, level in node.get('enchantments',{}).items():
                if isinstance(level,(int,float)) and not isinstance(level,bool):
                    node['enchantments'][name]=max(1,min(255,round(level*factor)))
                    changed_enchants+=1
        for val in node.values():update_enchants(val,factor)
    elif isinstance(node,list):
        for val in node:update_enchants(val,factor)

for path in sorted(base.glob('bonus_*.json')):
    data=json.loads(path.read_text(encoding='utf-8'))
    original=data.get('pools',[])
    expanded=[]
    for pool in original:
        for tier, chance_mult, level_mult in zip(world,chance_factor,level_factor):
            variant=copy.deepcopy(pool)
            conditions=variant.setdefault('conditions',[])
            conditions.append({'condition':'apotheosis:has_world_tier','tiers':[tier]})
            def scale_chances(node):
                if isinstance(node,dict):
                    if node.get('condition')=='minecraft:random_chance' and isinstance(node.get('chance'),(int,float)):
                        node['chance']=round(min(0.95,max(0.0,node['chance']*chance_mult)),6)
                    for val in node.values():scale_chances(val)
                elif isinstance(node,list):
                    for val in node:scale_chances(val)
            scale_chances(variant)
            update_enchants(variant,level_mult)
            expanded.append(variant)
            changed_pools+=1
    data['pools']=expanded
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    processed+=1
print(f'Full world tier integration: {processed} tables, {changed_pools} gated pools, {changed_enchants} enchantment level adjustments')
