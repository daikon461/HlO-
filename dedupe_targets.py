import json,pathlib
base=pathlib.Path('src/main/resources/data')
p=base/'neoforge/loot_modifiers/global_loot_modifiers.json'
d=json.loads(p.read_text());seen=set();keep=[];removed=[]
for e in d['entries']:
 ns,name=e.split(':',1)
 obj=json.loads((base/ns/'loot_modifiers'/f'{name}.json').read_text())
 ids=tuple(c['loot_table_id'] for c in obj.get('conditions',[]) if c.get('condition')=='neoforge:loot_table_id')
 if ids and ids in seen:removed.append(e);continue
 seen.add(ids);keep.append(e)
d['entries']=keep;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('Removed duplicate-target modifiers:',removed)
