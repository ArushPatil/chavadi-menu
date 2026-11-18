# Writes sample/data.js: a few categories from ../menu.json, with hand fixes to the owner's data.
import json
m = json.load(open('menu.json'))
PICK = [  # (tab, category shown, source category, item ids)
    ('Food', 'Starters', 'Starter (Veg)', [29, 32, 31]),
    ('Food', 'Starters', 'Starters (Non Veg)', [54, 46, 57]),
    ('Food', 'Wood-fired pizza', 'Wood-Fried Pizza', [69, 73, 74, 77]),
    ('Food', 'Curries', 'Main Course (Veg)', [94, 99]),
    ('Food', 'Curries', 'Main Course (Non Veg)', [100, 103]),
    ('Food', 'Workday Oota', 'Workday Oota By Chavadi Native Kitchen', [457, 458, 461, 462]),
    ('Food', 'Desserts', 'Desserts', [125, 469, 126]),
    ('Drinks', 'Mocktails', 'Mocktails', [144, 148, 150]),
    ('Drinks', 'Coffee', 'Coffee', [131]),
    ('Bar', 'Cocktails', 'Cocktails', [154, 157, 164]),
    ('Bar', 'Beer', 'Beer', [205, 207]),
]
# Owner's data is wrong on these; fixed for the sample, listed in README.
VEG_FIX = {103: False}
DESC_FIX = {69: 'Spinach, fresh corn, sautéed mushrooms, jalapeños and mozzarella.',
            71: ''}
out, seen = [], set()
for tab, cat, src, ids in PICK:
    for iid in ids:
        rows = [i for i in m if i['id'] == iid and i['category'] == src]
        r = rows[0]
        sizes = sorted({x['price'] for x in rows})
        name = r['name'].split(' - ')[0] if iid in (100,) else r['name']
        out.append(dict(id=iid, tab=tab, cat=cat, name=name.strip(),
            sub=r['name'].split(' - ', 1)[1] if ' - ' in r['name'] and iid in (54, 100) else '',
            desc=DESC_FIX.get(iid, r['description']), veg=VEG_FIX.get(iid, r['veg']),
            spicy=r['spicy'] or (iid in (57, 54, 29)),  # these descriptions say spicy
            prices=sizes, img=f'img/{iid}.jpg' if r['image'] else ''))
open('sample/data.js', 'w').write('window.MENU = ' + json.dumps(out, ensure_ascii=False, indent=0) + ';\n')
print(len(out), 'items')
assert all(o['prices'] for o in out)
