import csv,json,pathlib
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'relic_rewards.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
for i,row in enumerate(rows):
 tier=row['tier']; settings=cfg['tiers'][tier]; chance=settings['chance']; level=settings['level']
 assert 0<=chance<=1 and 1<=level<=255
 if not cfg['enabled'] or chance==0:continue
 path=base/f'bonus_{i:03d}.json'; data=json.loads(path.read_text(encoding='utf-8'))
 material='iron' if tier in ('starter','early_mid') else ('diamond' if tier in ('mid','mid_late') else 'netherite')
 # Treasure items get two complementary enchantments; books provide a third outcome.
 gear=[(f'minecraft:{material}_sword',{'minecraft:sharpness':level,'minecraft:unbreaking':min(level,6)},5),
       (f'minecraft:{material}_chestplate',{'minecraft:protection':max(1,level-1),'minecraft:unbreaking':min(level,6)},4),
       (f'minecraft:{material}_pickaxe',{'minecraft:efficiency':level,'minecraft:unbreaking':min(level,6)},4)]
 entries=[{'type':'minecraft:item','name':name,'weight':weight,'functions':[{'function':'minecraft:set_enchantments','enchantments':ench}]} for name,ench,weight in gear]
 entries.append({'type':'minecraft:item','name':'minecraft:enchanted_book','weight':3,'functions':[{'function':'minecraft:set_enchantments','enchantments':{'minecraft:unbreaking':min(level,6),'minecraft:mending':1}}]})
 data['pools'].append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':chance}],'entries':entries})
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('RC4 relic pools:',len(rows))
