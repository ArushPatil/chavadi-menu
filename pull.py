# Builds menu.json / menu.csv / menu.md from the raw API dumps in raw/, downloads item + brand images.
import json, csv, os, subprocess, collections
m = json.load(open('raw/menu.json')); im = json.load(open('raw/images.json'))
img = {}
for i in sorted(im, key=lambda i: i['index']):
    if i['imgPath'] and i['active'] and i['itemId'] not in img: img[i['itemId']] = i['imgPath']
def get(url, path):
    if not os.path.exists(path):  # write to .part first so a stopped run never leaves a half image
        subprocess.run(['curl', '-sfL', '--retry', '5', '--retry-all-errors', '-o', path + '.part', url], check=True)
        os.replace(path + '.part', path)
    return path
items = []
for i in sorted(m, key=lambda i: (i['section'], i['catIndex'], i['categoryName'], i['index'], i['name'])):
    url = img.get(i['itemId']); local = ''
    if url: local = get(url, f"images/items/{i['itemId']}{os.path.splitext(url)[1]}")
    items.append(dict(id=i['itemId'], section=i['section'], category=i['categoryName'], name=i['name'].strip(),
        price=i['price'], description=' '.join((i['description'] or '').split()), veg=('veg_icon' in (i['iconPath'] or '') and 'non' not in (i['iconPath'] or '').lower()),
        spicy=i['spicy'], chef_special=i['chefSpecial'], hours=i['availableBetween'], image=local, image_url=url or ''))
json.dump(items, open('menu.json', 'w'), indent=1, ensure_ascii=False)
with open('menu.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, items[0].keys()); w.writeheader(); w.writerows(items)
md = ['# Chavadi Native Kitchen: current menu', '', 'Source: chavadi-native-kitchen.godirekt.in (Devourin), pulled 2026-11-18. Prices in INR before tax.', '']
g = collections.defaultdict(lambda: collections.defaultdict(list))
for i in items: g[i['section']][i['category']].append(i)
for s, cats in g.items():
    md.append(f'## {s}')
    for c, its in cats.items():
        md.append(f'\n### {c}')
        for i in its:
            md.append(f"- **{i['name']}** {i['price']:g}" + (f" · {i['description']}" if i['description'] else '') + (' · 📷' if i['image'] else ''))
    md.append('')
open('menu.md', 'w').write('\n'.join(md))
# brand: logo, sliders, section tiles
b = ['https://chavadi-native-kitchen.godirekt.in/fileserver/chavadinativekitchen/logo/chavadi_nav.png']
b += [s['imagePath'] for s in json.load(open('raw/sliders.json'))]
for u in b: get(u, 'images/brand/' + u.split('/')[-2] + '-' + u.split('/')[-1])
print(len(items), 'items,', sum(1 for i in items if i['image']), 'with photo')
assert all(os.path.getsize(i['image']) > 1000 for i in items if i['image'])
