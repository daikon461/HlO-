#!/usr/bin/env python3
"""Release validation: resource references, JSON parseability, target uniqueness."""
import json,pathlib,sys,collections
base=pathlib.Path('src/main/resources/data')
manifest=base/'neoforge/loot_modifiers/global_loot_modifiers.json'
errors=[]
def read(p):
 try:return json.loads(p.read_text(encoding='utf-8'))
 except Exception as e:errors.append(f'{p}: {e}');return {}
if not manifest.exists():errors.append('missing GLM manifest')
entries=read(manifest).get('entries',[]) if manifest.exists() else []
if len(entries)!=len(set(entries)):errors.append('duplicate modifier entries')
mods=[];targets=[]
for entry in entries:
 try: namespace,name=entry.split(':',1)
 except ValueError:errors.append('invalid modifier id '+entry);continue
 p=base/namespace/'loot_modifiers'/f'{name}.json'
 if not p.exists():errors.append('missing modifier '+str(p));continue
 d=read(p);mods.append(d)
 if d.get('type') in ('apotheosis:affix_loot','apotheosis:gems'):
  if not d.get('entries'):errors.append('missing Apotheosis entries '+entry)
  continue
 if d.get('type')!='neoforge:add_table':errors.append('unexpected modifier type '+entry)
 table=d.get('table','')
 try:ns,path=table.split(':',1)
 except ValueError:errors.append('invalid table '+table);continue
 loot=base/ns/'loot_table'/f'{path}.json'
 if not loot.exists():errors.append('missing referenced table '+str(loot))
 else:read(loot)
 conditions=d.get('conditions',[])
 ids=[x.get('loot_table_id') for x in conditions if x.get('condition')=='neoforge:loot_table_id']
 if not ids:errors.append('modifier lacks loot table ID condition '+entry)
 targets+=ids
for p in base.rglob('*.json'):read(p)
if len(targets)!=len(set(targets)):errors.append('duplicate target loot tables')
print(f'Modifiers: {len(entries)}, unique targets: {len(set(targets))}, JSON files: {len(list(base.rglob("*.json")))}')
if errors:
 print('VALIDATION FAILED:');print('\n'.join(errors[:40]));sys.exit(1)
print('VALIDATION PASSED')
