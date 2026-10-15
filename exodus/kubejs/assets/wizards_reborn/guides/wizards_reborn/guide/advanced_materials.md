---
navigation:
  title: Advanced Materials
  icon: wizards_reborn:arcacite
  parent: index.md
  position: 6
item_ids:
  - wizards_reborn:alchemy_oil_bucket
  - wizards_reborn:alchemy_calx
  - wizards_reborn:enchanted_calx
  - wizards_reborn:scorched_calx
  - wizards_reborn:natural_calx
  - wizards_reborn:distant_calx
  - wizards_reborn:arcacite
  - wizards_reborn:arcane_iterator
  - wizards_reborn:wissen_crystallizer
  - wizards_reborn:arcane_linen
  - wizards_reborn:arcane_linen_seeds
---

# <Color id="dark_purple">Advanced Materials</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_purple">Advanced Materials</Color>

  <ItemImage id="arcacite" scale="2" />

  Once your alchemy setup is running, you can produce advanced materials needed for the Arcane Iterator and ritual components.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Arcane Linen</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="arcane_linen" />
  ### <Color id="aqua">Arcane Linen</Color>
</Row>

Arcane Linen is the catalyst that the whole alchemy chain runs on. Craft <ItemLink id="arcane_linen_seeds" /> at the <ItemLink id="wissen_crystallizer" />, then farm them like any other crop.

Plant more than you think you need. Alchemy Oil eats four Linen per bucket and almost every recipe below wants Oil.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Alchemy Oil</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="alchemy_oil_bucket" />
  ### <Color id="aqua">Alchemy Oil</Color>
</Row>

Alchemy Oil is the base fluid of the whole system, and the recipe is simpler than it looks: <Color id="aqua">4 Arcane Linen and 1 Petals</Color> in the Alchemy Machine yields a full bucket. It needs steam but no Wissen at all.

Every Calx, Arcacite and most alchemy potions consume Oil, so this is the first thing to automate.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Calx Types</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Calx are reaction enhancers. <ItemLink id="alchemy_calx" /> is the base one, ground from quartz, calcite, bone meal and Arcane Linen. The other four are all made by taking <Color id="aqua">2 Alchemy Calx</Color>, adding themed ingredients and a themed brew, and reacting them with Alchemy Oil.

<ItemGrid>
  <ItemIcon id="alchemy_calx" />
  <ItemIcon id="natural_calx" />
  <ItemIcon id="scorched_calx" />
  <ItemIcon id="distant_calx" />
  <ItemIcon id="enchanted_calx" />
</ItemGrid>

<ItemImage id="minecraft:air" scale="0.25"/>

| Calx | Themed around | What it is for |
|------|---------------|----------------|
| <ItemLink id="alchemy_calx" /> | Quartz and calcite | The base for the other four, and for Arcanum Lenses |
| <ItemLink id="natural_calx" /> | Moss, slime, seeds and petals | Nature-aligned recipes such as Petals of Innocence |
| <ItemLink id="scorched_calx" /> | Netherrack, soul sand, nether fungi | The one you need for <ItemLink id="arcacite" /> |
| <ItemLink id="distant_calx" /> | End stone, ender pearls, chorus fruit | End-aligned recipes |
| <ItemLink id="enchanted_calx" /> | An enchanted book, lapis and diamond | Crafting the <ItemLink id="arcane_iterator" /> itself |

<Color id="yellow">Note:</Color> Enchanted Calx is the expensive one, at 250 Wissen per batch against 50 for the others.

Each Calx also works in an Arcane Censer, where burning it grants a potion effect matching its theme.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Arcacite</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="arcacite" />
  ### <Color id="aqua">Arcacite</Color>
</Row>

Arcacite is Arcanum restructured by alchemy: stronger than the original, but with its refractive properties burned away. That trade-off is the point. It is no good as a spell lens, but it is the structural material for everything late in the mod.

Made in the Alchemy Machine from <Color id="aqua">2 Arcanum, 2 Quartz, 1 Scorched Calx and 250mB of Alchemy Oil</Color>, at a cost of 200 Wissen and 200 steam.

You will need it for the <ItemLink id="arcane_iterator" />, Wisestone Plates, Void Crystal Seeds, the Jeweler Table and Arcacite trinkets.
