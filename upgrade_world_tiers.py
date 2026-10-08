import json, pathlib
root=pathlib.Path(__file__).resolve().parent
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_modifiers'
index=root/'src/main/resources/data/neoforge/loot_modifiers/global_loot_modifiers.json'
idx=json.loads(index.read_text())
world=['haven','frontier','ascent','summit','pinnacle']
mult=[0.55,0.8,1.0,1.3,1.65]
for kind in ('affix','gem'):
    old=base/f'apotheosis_{kind}_bonus.json'
    data=json.loads(old.read_text())
    original=f'hardcore_loot_overhaul:apotheosis_{kind}_bonus'
    idx['entries']=[x for x in idx['entries'] if x!=original and not x.startswith(f'hardcore_loot_overhaul:apotheosis_{kind}_world_')]
    for tier,factor in zip(world,mult):
        name=f'apotheosis_{kind}_world_{tier}'
        entries=[dict(e,chance=round(min(0.95,e['chance']*factor),5)) for e in data['entries']]
        payload={'type':data['type'],'conditions':[{'condition':'apotheosis:has_world_tier','tiers':[tier]}],'entries':entries}
        (base/(name+'.json')).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
        idx['entries'].append('hardcore_loot_overhaul:'+name)
    old.unlink()
index.write_text(json.dumps(idx,indent=2)+'\n')
print('World tier gated affix/gem modifiers:',len(world)*2)
