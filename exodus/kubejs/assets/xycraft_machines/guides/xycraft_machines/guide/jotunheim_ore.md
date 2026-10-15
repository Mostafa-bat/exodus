---
navigation:
  title: Aluminum and Kivi
  icon: ftbmaterials:aluminum_stone_ore
  parent: index.md
  position: 3
item_ids:
  - ftbmaterials:aluminum_stone_ore
  - ftbmaterials:aluminum_deepslate_ore
  - ftbmaterials:aluminum_ingot
  - xycraft_world:kivi
  - xycraft_machines:machine_base
---
# <Color id="aqua">Aluminum and Kivi</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="aqua">Aluminum and Kivi</Color>
  <ItemImage id="ftbmaterials:aluminum_stone_ore" scale="2" />

  Every Xycraft machine starts with a <ItemLink id="xycraft_machines:machine_base" />, and that needs Aluminum. This page covers where to find it, and where Kivi comes from.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Aluminum Is Unified</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="yellow">Xycraft's own Aluminum does not exist in this pack.</Color> Aluminum is unified across every mod that adds it, so the Xycraft ore blocks, ingot, nugget, raw form and sheet are all stripped of their tags and hidden from JEI.

What actually generates is the shared version:

<ItemGrid>
  <ItemIcon id="ftbmaterials:aluminum_stone_ore" />
  <ItemIcon id="ftbmaterials:aluminum_deepslate_ore" />
</ItemGrid>

- <ItemLink id="ftbmaterials:aluminum_stone_ore" /> in stone
- <ItemLink id="ftbmaterials:aluminum_deepslate_ore" /> in deepslate

Both give <ItemLink id="ftbmaterials:aluminum_ingot" />, which is what the Machine Base recipe wants. If you go looking through JEI for a Xycraft aluminum ore, you will not find one.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Where to Mine It</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

| Realm | Notes |
|---|---|
| <Color id="green">Midgard</Color> and the Overworld | Standard Xycraft distribution, since both count as overworld biomes |
| <Color id="aqua">Jotunheim</Color> | Added by the pack as an extra biome modifier, at the same rate as the Overworld |
| <Color id="aqua">Niflheim</Color> | Added by the pack, <Color id="gold">9 veins per chunk between Y -64 and Y -50</Color> |

Niflheim is the densest source by a wide margin, but it all sits in the deepslate layer, so bring something that mines quickly.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Kivi</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="xycraft_world:kivi" />
  ### <Color id="aqua">Kivi</Color>
</Row>

Kivi is the other Xycraft material you will need, most immediately for the [Light Field](light_field.md).

Alongside its normal Xycraft generation, the pack seeds <Color id="aqua">Kivi geodes in Niflheim</Color>. Since Niflheim is also the best Aluminum layer, one trip down there covers both requirements for your first Machine Base and Light Field.

<ItemImage id="minecraft:air" scale="0.25"/>
