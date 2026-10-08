import json,pathlib,csv
root=pathlib.Path(__file__).resolve().parent
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'
# Extra independent chance for an additional premium reward; does not overwrite native loot.
bonus={
 'starter':(.11,[('minecraft:emerald',6),('minecraft:gold_ingot',4),('minecraft:iron_ingot',7)]),
 'early_mid':(.16,[('minecraft:diamond',3),('minecraft:emerald',6),('minecraft:golden_apple',1)]),
 'mid':(.23,[('minecraft:diamond',5),('minecraft:golden_apple',2),('minecraft:experience_bottle',5)]),
 'mid_late':(.30,[('minecraft:diamond',6),('minecraft:golden_apple',3),('minecraft:echo_shard',2)]),
 'late':(.39,[('minecraft:diamond',8),('minecraft:netherite_scrap',2),('minecraft:golden_apple',3)]),
 'apex':(.49,[('minecraft:diamond',9),('minecraft:netherite_scrap',3),('minecraft:enchanted_golden_apple',1)])}
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
for i,r in enumerate(rows):
 path=base/f'bonus_{i:03d}.json'; obj=json.loads(path.read_text()); chance,items=bonus[r['tier']]
 obj['pools'].append({'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':chance}], 'entries':[{'type':'minecraft:item','name':name,'weight':weight} for name,weight in items]})
 path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print('Luxury extra bonus pools:',len(rows))
