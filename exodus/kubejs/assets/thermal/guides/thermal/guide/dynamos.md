---
navigation:
  title: Dynamos
  icon: thermal:dynamo_stirling
  parent: index.md
  position: 3
item_ids:
  - thermal:dynamo_stirling
  - thermal:dynamo_compression
  - thermal:dynamo_magmatic
  - thermal:dynamo_numismatic
  - thermal:dynamo_lapidary
  - thermal:dynamo_disenchantment
  - thermal:dynamo_gourmand
  - thermal:energy_cell
  - thermal_extra:dynamo_frost
---
# <Color id="red">Dynamos</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Dynamos</Color>
  <ItemImage id="thermal:dynamo_stirling" scale="2" />
  Dynamos are the power generators of the Thermal Series. Each type consumes a different fuel to produce Redstone Flux (FE). Upgrade them with [Augments](augments.md) to boost output and fuel efficiency.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">Tip:</Color> Dynamos output power from their coil face (the orange side). Point this at your machines, a Fluxduct, or a <ItemLink id="thermal:energy_cell" />.

<Color id="gold">Tip:</Color> Fit an <Color id="aqua">Excitation Field Limiter</Color> augment early. Without one a Dynamo keeps consuming fuel after its buffer fills and the energy is simply lost. See [Augments](augments.md).

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fuel-Based Dynamos</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_stirling" />
  ### <Color id="aqua">Stirling Dynamo</Color>
</Row>

Burns furnace fuels - Coal, Charcoal, Wood, Blaze Rods, and other combustibles. The simplest and cheapest Dynamo. Build this first for early power.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_compression" />
  ### <Color id="aqua">Compression Dynamo</Color>
</Row>

Burns liquid fuels such as oils and refined fuels. Pair with a Fractionating Still or external oil processing for a strong mid-game power source. Higher energy output per fuel unit than the Stirling Dynamo.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_magmatic" />
  ### <Color id="aqua">Magmatic Dynamo</Color>
</Row>

Generates power from extremely hot fluids, Lava being the obvious one. A reliable early-to-mid game option since Lava is easy to source. Pair it with a <ItemLink id="thermal:machine_crucible" /> melting Cobblestone for an endless supply.

<Color id="yellow">Note:</Color> the fluid is consumed outright, not returned.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Specialty Dynamos</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_numismatic" />
  ### <Color id="aqua">Numismatic Dynamo</Color>
</Row>

Generates power from coins and other currency items. Niche but useful if you have a coin source from mob drops or trading systems.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_lapidary" />
  ### <Color id="aqua">Lapidary Dynamo</Color>
</Row>

Burns gems - Diamonds, Emeralds, <ItemLink id="thermal:ruby" />, <ItemLink id="thermal:sapphire" />, Lapis, and Quartz. High energy per gem makes this efficient if you have surplus gemstones.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_disenchantment" />
  ### <Color id="aqua">Disenchantment Dynamo</Color>
</Row>

Extracts power from enchanted items. Feed it enchanted gear from mob farms to turn unwanted enchantments into energy. Higher-level enchantments produce more FE.

<Color id="yellow">Note:</Color> the item is destroyed along with the enchantment, so do not feed it anything you want to keep.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:dynamo_gourmand" />
  ### <Color id="aqua">Gourmand Dynamo</Color>
</Row>

Generates power from food items. Higher-saturation foods produce more energy. A good option if you have a large automated farm.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Thermal Extra Dynamos</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:dynamo_frost" />
  ### <Color id="aqua">Gelid Dynamo</Color>
</Row>

Added by Thermal Extra. Generates Redstone Flux from extreme cold rather than heat, burning Blizz Cubes, Snowballs, Ice, Packed Ice and Blue Ice. The cold counterpart to the Magmatic Dynamo.


<ItemImage id="minecraft:air" scale="0.25"/>
