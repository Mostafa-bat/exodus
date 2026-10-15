---
navigation:
  title: Main Machines
  icon: enderio:alloy_smelter
  parent: index.md
  position: 2
item_ids:
  - enderio:alloy_smelter
  - enderio:sag_mill
  - enderio:slice_and_splice
  - enderio:soul_binder
  - enderio:powered_spawner
  - enderio:ensouled_chassis
  - enderio:dark_steel_grinding_ball
  - enderio:energetic_alloy_grinding_ball
  - enderio:vibrant_alloy_grinding_ball
  - enderio:conductive_alloy_grinding_ball
  - enderio:pulsating_alloy_grinding_ball
  - enderio:redstone_alloy_grinding_ball
  - enderio:copper_alloy_grinding_ball
  - enderio:end_steel_grinding_ball
  - enderio:soularium_grinding_ball
---
# <Color id="dark_aqua">Main Machines</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_aqua">Main Machines</Color>
  <ItemImage id="enderio:alloy_smelter" scale="2" />
  Ender IO machines form the backbone of your tech infrastructure. Most require <ItemLink id="enderio:dark_steel_ingot" /> and power from a generator to function.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">All machines accept Capacitor upgrades</Color> to increase speed, energy storage, and efficiency. See [Power](power.md) for capacitor details.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Processing Machines</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:alloy_smelter" />
  ### <Color id="aqua">Alloy Smelter</Color>
</Row>

The heart of Ender IO. Combines up to three ingredients into alloys like <ItemLink id="enderio:dark_steel_ingot" />, <ItemLink id="enderio:energetic_alloy_ingot" />, and <ItemLink id="enderio:vibrant_alloy_ingot" />. Also functions as a standard furnace for single-item smelting. Insert a <ItemLink id="enderio:basic_capacitor" /> or better to boost speed and energy capacity.

The Alloy Smelter's interface allows side input/output configuration, redstone configuration, and swapping between three modes:

- <Color id="yellow">Alloy only mode</Color>: Only allows the Alloy Smelter to create alloys.
- <Color id="yellow">Furnace only mode</Color>: Treats the Alloy Smelter as a furnace.
- <Color id="yellow">Alloying and Smelting</Color>: Does both, which can be problematic when automating as some items will be smelted before turning into alloys.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="enderio:sag_mill" />
  ### <Color id="aqua">SAG Mill</Color>
</Row>

Grinds ores into dusts for double output, and breaks down items into component materials. Insert a Grinding Ball to improve its results. Flint works as a cheap starter ball.

Each ball has three separate multipliers, and they pull in different directions. <Color id="green">Output</Color> raises the main product, <Color id="green">Chance</Color> raises the bonus roll, and <Color id="green">Power</Color> is energy cost, so lower is better. Durability is how many operations it lasts.

<ItemImage id="minecraft:air" scale="0.25"/>

| Grinding Ball | Output | Chance | Power | Durability |
|---|---|---|---|---|
| <ItemImage id="enderio:vibrant_alloy_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:vibrant_alloy_grinding_ball" /></Color> | <Color id="gold">1.75</Color> | 1.35 | 1.13 | 80,000 |
| <ItemImage id="enderio:energetic_alloy_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:energetic_alloy_grinding_ball" /></Color> | 1.6 | 1.1 | 1.1 | 80,000 |
| <ItemImage id="enderio:end_steel_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:end_steel_grinding_ball" /></Color> | 1.4 | <Color id="gold">2.4</Color> | 0.7 | 75,000 |
| <ItemImage id="enderio:dark_steel_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:dark_steel_grinding_ball" /></Color> | 1.35 | 2.0 | 0.7 | <Color id="gold">125,000</Color> |
| <ItemImage id="enderio:conductive_alloy_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:conductive_alloy_grinding_ball" /></Color> | 1.35 | 1.0 | 1.0 | 40,000 |
| <ItemImage id="enderio:soularium_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:soularium_grinding_ball" /></Color> | 1.2 | 2.15 | 0.9 | 80,000 |
| <ItemImage id="enderio:copper_alloy_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:copper_alloy_grinding_ball" /></Color> | 1.2 | 1.65 | 0.8 | 40,000 |
| <ItemImage id="minecraft:flint" scale="0.5" /> <Color id="aqua">Flint</Color> | 1.2 | 1.25 | 0.85 | 24,000 |
| <ItemImage id="enderio:pulsating_alloy_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:pulsating_alloy_grinding_ball" /></Color> | 1.0 | 1.85 | 1.0 | 100,000 |
| <ItemImage id="enderio:redstone_alloy_grinding_ball" scale="0.5" /> <Color id="aqua"><ItemLink id="enderio:redstone_alloy_grinding_ball" /></Color> | 1.0 | 1.0 | <Color id="gold">0.35</Color> | 30,000 |

Reading that table:

- <Color id="green">Most product</Color> comes from Vibrant Alloy, at the cost of using more power than it saves.
- <Color id="green">Most bonus rolls</Color> come from End Steel, which also cuts power use by 30%. This is the all-round best ball.
- <Color id="green">Cheapest to run</Color> is Redstone Alloy at 0.35 power, though it adds nothing else at all.
- <Color id="green">Longest lasting</Color> is Dark Steel at 125,000, and it is strong everywhere else too, which makes it the one to settle on before End Steel is realistic.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Soul Machines</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Soul machines work with mob souls captured in <ItemLink id="enderio:empty_soul_vial" />. This is the late-game line of Ender IO, requiring <ItemLink id="enderio:soularium_ingot" /> to craft.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:slice_and_splice" />
  ### <Color id="aqua">Slice'N'Splice</Color>
</Row>

A grim machine that combines mob heads and other materials to create advanced components. Used to craft the <ItemLink id="enderio:ensouled_chassis" /> needed for the Powered Spawner and other soul machinery.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:soul_binder" />
  ### <Color id="aqua">Soul Binder</Color>
</Row>

Binds captured mob souls from <ItemLink id="enderio:filled_soul_vial" /> into items, creating soul-infused components for advanced crafting. Essential for setting up Powered Spawners.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:powered_spawner" />
  ### <Color id="aqua">Powered Spawner</Color>
</Row>

The crown jewel of soul machinery. It spawns <Color id="green">4 mobs</Color> at a time using power. The mob type comes from the Broken Spawner used to craft it, and every vanilla Spawner you break drops one, so there is no luck involved. Change the type by combining a Broken Spawner with a <ItemLink id="enderio:filled_soul_vial" /> of the mob you want in the <ItemLink id="enderio:soul_binder" />. Check JEI for the crafting recipe (press U on a Broken Spawner).

Two limits catch people out. A spawner <Color id="yellow">shuts off</Color> once 2 or more of its mob are already nearby, so you must clear the output. And past <Color id="yellow">10 spawners</Color> in an area they all start losing efficiency.

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="red">This pack blacklists bosses and elite mobs.</Color> Roughly 65 entity types cannot be placed in a Powered Spawner, and a similar list cannot be captured in a Soul Vial at all. Cataclysm bosses, the Wither, the Ender Dragon and the pack's own boss entities are all excluded, so do not plan a farm around one.

<ItemImage id="minecraft:air" scale="0.25"/>