import json, sys
p=json.load(open(sys.argv[1], encoding='utf-8'))
required={'workspace','environment','capacity_percent','tables'}
missing=required-set(p)
if missing: raise SystemExit(f'Missing: {', '.join(sorted(missing))}')
if p['capacity_percent'] >= 75: print('WARNING: capacity >= 75%')
failed=[x['name'] for x in p['tables'] if not x.get('synchronized')]
if failed: raise SystemExit('Unsynchronized: '+', '.join(failed))
print('PASS: Fabric release validation')
