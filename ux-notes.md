# UX notes for the concept menu

What the sample (`sample/index.html`) does, and why. Run it with:

```bash
python3 -m http.server 8811 -d sample
```

Then open http://localhost:8811 on a phone-width window.

## What research says (checked 2026-11-18)

- In Toast's survey of 850 US adults, 81% preferred physical menus, and about two-thirds preferred menus with photos. Toast recommends clear categories, good images and intuitive navigation. Vendor blog, so treat it as marketing-influenced. https://pos.toasttab.com/blog/on-the-line/qr-code-menu-insights
- Iskender et al. (2023), a qualitative study: guests see QR menus as quick but effortful, and often complain of poor design and no interaction. https://emerald.com/insight/content/doi/10.1108/CBTH-11-2022-0194/full/html
- A UiTM study on QR menu use in Malaysian restaurants covers the same ground. https://ir.uitm.edu.my/97893/1/97893.pdf
- Petpooja says QR ordering suits casual dining, and fine dining suits a waiter with a captain app. Vendor guidance. https://blog.petpooja.com/industry-business-guides/choose-qr-ordering-system-restaurant/

## What the current Devourin menu gets wrong

- Photos are small and many items have none.
- Section and category are two levels of navigation, so finding a dish takes several taps.
- No search, and no veg-only filter, though veg is the first thing many Indian diners filter on.
- Title Case descriptions and inconsistent copy.

## What the sample does

| Choice | Why |
|---|---|
| Three tabs: Food, Drinks, Bar | One level of choice before the list, not two. |
| Category chips that follow the scroll | You always see where you are, and can jump. |
| Search, Veg only, Spicy | The three filters a guest reaches for first. |
| Indian veg / non-veg mark on every item | The symbol diners already read without thinking. |
| Text left, square photo right, Add on the photo | Scannable list; photo sells the dish; one tap to add. |
| Tap a dish for a bottom sheet | Big photo, full description, size picker, quantity. |
| "Your list" bar at the bottom | Guests build an order and show it to the server. No checkout yet. |
| 44px tap targets, focus rings, reduced motion respected | Usable one-handed, with a keyboard, and for motion-sensitive guests. |

## The Chavadi feel (from their photos, not their website)

The look comes from the photos of their rooftop on chavadi.co, not from the site's black and gold styling. All colour picks are judgement calls.

| Choice | Taken from |
|---|---|
| Limewash off-white ground | Their white walls and white brick jaali screens |
| Cobalt blue for tabs, active chips and the list bar | The blue tables and railings |
| Leaf green for category headings and origin tags | The vines and creepers over the pergolas |
| Mustard story card | The mustard-yellow wall |
| Terracotta for Add and the main button | The clay pots and floor tiles |
| Thin lattice band under the photo | The jaali brick screens |
| Header photo changes by tab: vines by day (Food), jaali (Drinks), string lights at night (Bar) | Their rooftop by day and by night |
| "Pull up a chair" card | Paraphrased from their printed menu's page on what "chavadi" means |
| Small origin tags (Mangalore, Kerala, Andhra…) | Region names already in dish names and descriptions |

The logo colour differs by source: navy on Devourin, gold on chavadi.co, green on the printed menu. Ask the owner which is current before using it.

Claims from third-party reviews (LBB), not used yet, to confirm with the owner: wood-fire kitchen, stone grinding, clay pots, ingredients from each dish's region, a take-one-leave-one bookshelf, saplings at tables.

## Not done in the sample

- No real ordering. The list is saved on the guest's phone only.
- Pizza size names "Regular" and "Large" are placeholders. The data has two prices but no names.
- Descriptions are the restaurant's own, unedited.
- Only 30 of 274 items.

## Data errors to send the owner

- Margherita (71): its description is the fish fry's text.
- Malpe Fish Curry (103), Gowda Mutton Saaru (319) and Karnataka yele Ootta non veg (464) are marked veg.
- "Chavadis Long Island Ice Tea" is missing its apostrophe.
