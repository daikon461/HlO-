import csv,json,pathlib
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'enchant_progression.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
items=[('minecraft:iron_sword','minecraft:sharpness',4),('minecraft:iron_chestplate','minecraft:protection',3),('minecraft:iron_pickaxe','minecraft:efficiency',3)]
advanced=[('minecraft:diamond_sword','minecraft:sharpness',4),('minecraft:diamond_chestplate','minecraft:protection',3),('minecraft:diamond_pickaxe','minecraft:efficiency',3)]
ultimate=[('minecraft:netherite_sword','minecraft:sharpness',4),('minecraft:netherite_chestplate','minecraft:protection',3),('minecraft:netherite_pickaxe','minecraft:efficiency',3)]
for i,r in enumerate(rows):
 tier=r['tier'];settings=cfg['tiers'][tier]
 path=base/f'bonus_{i:03d}.json';obj=json.loads(path.read_text(encoding='utf-8'))
 if cfg['enabled'] and settings['chance']>0:
  equipment=items if tier in ('starter','early_mid') else (advanced if tier in ('mid','mid_late') else ultimate)
  entries=[]
  for name,enchant,weight in equipment:
   entries.append({'type':'minecraft:item','name':name,'weight':weight,'functions':[{'function':'minecraft:set_enchantments','enchantments':{enchant:settings['levels'][enchant]}}]})
  obj['pools'].append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':settings['chance']}],'entries':entries})
 path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Enchant progression pools:',len(rows))
