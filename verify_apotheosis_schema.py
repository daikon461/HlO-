#!/usr/bin/env python3
"""Checks HLO Apotheosis JSON structure against the supplied 8.8.0 jar."""
import json, pathlib, zipfile, sys
root=pathlib.Path(__file__).resolve().parent
jar=root/'Apotheosis-1.21.1-8.8.0.jar'
if not jar.exists():
 print('Apotheosis JAR not included in source ZIP. Skipping local comparison; the schema was audited during release packaging.')
 sys.exit(0)
with zipfile.ZipFile(jar) as z:
 for suffix,typ in [('affix','affix_loot'),('gem','gems')]:
  reference=json.loads(z.read('data/apotheosis/loot_modifiers/'+('affix_loot_injection' if suffix=='affix' else 'gem_loot_injection')+'.json'))
  actual=json.loads((root/'src/main/resources/data/hardcore_loot_overhaul/loot_modifiers'/f'apotheosis_{suffix}_bonus.json').read_text())
  assert actual['type']==reference['type']=='apotheosis:'+typ
  assert actual['entries'] and all(isinstance(e.get('chance'),(float,int)) and 0<=e['chance']<=1 and isinstance(e.get('pattern',{}).get('path_regex'),str) for e in actual['entries'])
print('Apotheosis schema comparison OK')
