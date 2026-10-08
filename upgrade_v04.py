import csv,json,pathlib,collections,hashlib
root=pathlib.Path(__file__).resolve().parent
cfg=json.loads((root/'loot_v04.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((root/'verified_targets.csv').open(encoding='utf-8-sig')))
base=root/'src/main/resources/data/hardcore_loot_overhaul/loot_table/chests'

def tier_for(s):
 s=s.lower()
 if any(k in s for k in ('cataclysm:chests/','ancient_city','end_city_treasure','bastion_treasure','acropolis','leviathan','citadel')):return 'apex'
 if any(k in s for k in ('bastion','end_city','trial_chambers','vault','fortress','stronghold','treasure','temple')):return 'late'
 if any(k in s for k in ('dungeon','crypt','tower','pyramid','shipwreck','ruins')):return 'mid_late'
 if any(k in s for k in ('mineshaft','jungle','desert','outpost','igloo')):return 'mid'
 if any(k in s for k in ('village','supply','spawn','starter')):return 'starter'
 return 'early_mid'

def focus_for(s):
 s=s.lower()
 if s.startswith('cataclysm:'):return 'cataclysm'
 if any(k in s for k in ('mineshaft','factory','engineer','industrial')):return 'create'
 if any(k in s for k in ('wizard','magic','arcane','spell','tower')):return 'irons_spellbooks'
 return 'ars_nouveau'

def chance(v,m):return round(min(1,max(0,v*m)),6)
def pool(items,p):return {'rolls':1,'conditions':[{'condition':'minecraft:random_chance','chance':p}],'entries':[{'type':'minecraft:item','name':i,'weight':w} for i,w in items]}
counts=collections.Counter();report=[]
for idx,row in enumerate(rows):
 target=row['loot_table_id'];tier=tier_for(target);focus=focus_for(target)
 path=base/f'bonus_{idx:03d}.json'
 if not path.exists():raise FileNotFoundError(path)
 obj=json.loads(path.read_text(encoding='utf-8'))
 # Replace original prototype bonus pool: v0.1 contained top-tier rewards in common chests.
 obj['pools']=[]
 if cfg['settings']['enabled']:
  t=cfg['tiers'][tier]
  p=chance(t['vanilla_chance'],cfg['settings']['vanilla_multiplier'])
  if p:obj['pools'].append(pool(t['vanilla'],p))
  # The prototype's four MOD namespaces are retained; mod presence must be checked by players.
  groups=[focus]+[x for x in cfg['mod_items'] if x!=focus]
  choices=[]
  for j,mod in enumerate(groups):
   for item in cfg['mod_items'][mod]:
    if tier in ('starter','early_mid') and any(x in item for x in ('epic','legendary','ignitium','cursium','void_core','rare_ink','precision_mechanism')):continue
    if tier in ('mid','mid_late') and any(x in item for x in ('legendary','ignitium','cursium','void_core')):continue
    choices.append((item,7 if j==0 else 2))
  mp=chance(t['mod_chance'],cfg['settings']['mod_multiplier'])
  if mp and choices:obj['pools'].append(pool(choices,mp))
  if tier in cfg['jackpot']['tiers']:
   jp=chance(cfg['jackpot']['chances'][tier],cfg['settings']['jackpot_multiplier'])
   if jp:obj['pools'].append(pool(cfg['jackpot']['rewards'],jp))
 path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 counts[tier]+=1;report.append((target,tier,focus,len(obj['pools'])))
with (root/'tier_report.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['loot_table_id','tier','focus','bonus_pools']);w.writerows(report)
print('v0.4 generated:',len(report),'targets, tiers:',dict(counts))
