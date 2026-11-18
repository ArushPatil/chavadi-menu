# Chavadi Native Kitchen: concept menu

A new concept menu for the owner of Chavadi Native Kitchen. It starts from their current digital menu:
https://chavadi-native-kitchen.godirekt.in/spark/app/#/mainpage (run by Devourin).

**Who does what:** Arush builds the structure. The co-founder designs it.

## What is here

| Path | What it is |
|---|---|
| `menu.md` | The whole current menu to read, by section and category. 📷 marks items with a photo. |
| `menu.json`, `menu.csv` | The same 274 items as data. Build the menu from these. |
| `images/items/` | Dish and drink photos, named by item id (`13.png` is item 13). |
| `images/brand/` | The logo and the 2 homepage banners. |
| `raw/` | Untouched API responses from the current site. |
| `pull.py` | Rebuilds `menu.*` from `raw/` and downloads any missing photos. |

Fields of each item in `menu.json`: `id`, `section`, `category`, `name`, `price` (INR, before tax), `description`, `veg`, `spicy`, `chef_special`, `hours` (when it can be ordered), `image` (local path, empty if none), `image_url`.

Sections: Food (122 items), Liquor (61), Happy Hours (40), Beverages (30), Art Menu (13), Workday Oota (8).

## Gaps to know about

- Only 98 of 274 items have a description. Most copy still needs writing.
- 244 items have a photo. Beverages is the thinnest: 12 of 30.
- `veg` is guessed from the icon file name on each item. It is spot-checked, not fully checked.
- These are the delivery-menu prices, pulled on 2026-11-18. Dine-in prices may differ.
- Some photos are 4 to 5 MB. Compress them before they go on a page.

## Refresh the data

The current site reads from these public endpoints (base `https://chavadi-native-kitchen.godirekt.in/nebula-services-1.6/chavadinativekitchen/`):

- `getmenubytypeandbranch?type=Rest_Delivery&id=1&src=SPARK`, saved as `raw/menu.json`
- `itemimagesbybrsrc?br=1&src=SPARK`, saved as `raw/images.json`
- `currentslidersbybranch?id=1`, saved as `raw/sliders.json`

Save fresh copies over the files in `raw/`, then run:

```bash
python3 -I pull.py
```

## Online ordering (not decided)

The current Devourin site already takes dine-in, delivery and takeaway orders, with Razorpay for payment. The suggested route is that the new menu is the front end and its order buttons link into the existing Devourin ordering, so the kitchen's setup does not change. A fully custom checkout would need Devourin to accept orders from outside systems, which nobody has checked yet.

## Next

1. Arush: decide the structure (pages, sections, how a dish is shown) and add it here.
2. Co-founder: design it from `menu.json` and `images/`.
3. Decide how ordering works (see above).
