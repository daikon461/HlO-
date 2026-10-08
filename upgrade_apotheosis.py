import pathlib,json,csv,re,collections
root=pathlib.Path(__file__).resolve().parent
settings=json.loads((root/'apotheosis_integration.json').read_text())
rows=list(csv.DictReader((root/'tier_report.csv').open(encoding='utf-8-sig')))
rows=list({r['loot_table_id']:r for r in rows+list(csv.DictReader((root/'extra_targets_v08.csv').open(encoding='utf-8-sig')))}.values())
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_modifiers'
index=root/'src/main/resources/data/neoforge/loot_modifiers/global_loot_modifiers.json'
idx=json.loads(index.read_text())
# A single modifier per category. Patterns are exact full-path matches, grouped by namespace and tier.
for kind,modtype in [('affix','apotheosis:affix_loot'),('gem','apotheosis:gems')]:
    entries=[]
    grouped=collections.defaultdict(list)
    for row in rows:
        domain,path=row['loot_table_id'].split(':',1)
        grouped[(row['tier'],domain)].append(path)
    for (tier,domain),paths in sorted(grouped.items()):
        for i in range(0,len(paths),20):
            chunk=paths[i:i+20]
            regex='^(?:'+'|'.join(re.escape(p) for p in chunk)+')$'
            entries.append({'chance':settings[kind+'_chance'][tier], 'pattern':{'domain':domain,'path_regex':regex}})
    name='apotheosis_'+kind+'_bonus'
    (base/(name+'.json')).write_text(json.dumps({'type':modtype,'conditions':[],'entries':entries},indent=2)+'\n')
    identifier='hardcore_loot_overhaul:'+name
    if identifier not in idx['entries']:idx['entries'].append(identifier)
index.write_text(json.dumps(idx,indent=2)+'\n')
print('Apotheosis bonuses generated:',len(rows),'targets',len(idx['entries']),'total modifiers')
