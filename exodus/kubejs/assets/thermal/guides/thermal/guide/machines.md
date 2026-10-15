---
navigation:
  title: Machines
  icon: thermal:machine_pulverizer
  parent: index.md
  position: 2
item_ids:
  - thermal:machine_furnace
  - thermal:machine_pulverizer
  - thermal:machine_smelter
  - thermal:machine_sawmill
  - thermal:machine_press
  - thermal:machine_centrifuge
  - thermal:machine_crafter
  - thermal:machine_crucible
  - thermal:machine_chiller
  - thermal:machine_refinery
  - thermal:machine_pyrolyzer
  - thermal:machine_bottler
  - thermal:machine_brewer
  - thermal:machine_crystallizer
  - thermal:machine_insolator
  - thermal:device_rock_gen
  - thermal:device_water_gen
  - thermal:device_tree_extractor
  - ftb:nether_sap_bucket
  - thermal:device_collector
  - thermal:device_nullifier
  - thermal:device_soil_infuser
  - thermal_extra:component_assembly
  - thermal_extra:advanced_refinery
  - thermal_extra:endothermic_dehydrator
  - thermal_extra:fluid_mixer
  - thermal_extra:nitratic_igniter
  - thermal_extra:device_harvester
  - thermal_extra:device_lava_gen
---
# <Color id="red">Machines</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Machines</Color>
  <ItemImage id="thermal:machine_pulverizer" scale="2" />
  Thermal Expansion machines process items using Redstone Flux (FE). Every machine is built from a <ItemLink id="thermal:machine_frame" /> and can be upgraded with [Augments](augments.md) for improved performance.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">Tip:</Color> Every machine has augment slots. Integral Components raise its base stats, and specialised augments change how it behaves. See [Augments](augments.md).

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Item Processing</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_furnace" />
  ### <Color id="aqua">Redstone Furnace</Color>
</Row>

Smelts items using FE instead of fuel. Never needs refuelling, and it uses very little energy on food specifically. Your first step up from a coal furnace.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_pulverizer" />
  ### <Color id="aqua">Pulverizer</Color>
</Row>

Crushes ores into dusts for doubled smelting output, and converts many items into other forms. Accepts a catalyst such as <ItemLink id="thermal:cinnabar" /> to improve the secondary output chance. One of the two machines worth building immediately.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_smelter" />
  ### <Color id="aqua">Induction Smelter</Color>
</Row>

Combines two ingredients at high temperature. This is where every Thermal alloy is made, including <ItemLink id="thermal:invar_ingot" />, <ItemLink id="thermal:electrum_ingot" /> and <ItemLink id="thermal:signalum_ingot" />. Ores smelted with Sand give bonus secondary output, and <ItemLink id="thermal:cinnabar" /> guarantees it.

<Color id="yellow">Note:</Color> it will not cook food. Use the Redstone Furnace for that.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_sawmill" />
  ### <Color id="aqua">Sawmill</Color>
</Row>

Cuts logs into planks with bonus Sawdust, and reprocesses existing wooden objects back into materials. Gets far more out of a tree than hand-crafting.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_press" />
  ### <Color id="aqua">Multiservo Press</Color>
</Row>

Squeezes items into new shapes. It takes a <Color id="aqua">die</Color> in its second slot to decide the output: Gearworking Die for gears, Numismatic Die for coins, and Packing / Unpacking Dies for block compression.

In this pack the Press is also how you make <Color id="green">Printed Silicon</Color> for AE2 processors.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_centrifuge" />
  ### <Color id="aqua">Centrifugal Separator</Color>
</Row>

Separates items into their component parts. Some items yield a fluid component as well as solids, so it usually wants somewhere to pipe that off to.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_crafter" />
  ### <Color id="aqua">Sequential Fabricator</Color>
</Row>

An autocrafter. Lay a recipe into its grid, press confirm, and it repeats that craft from its input inventory. Not every recipe is valid.

<Color id="yellow">Note:</Color> In this pack the Sequential Fabricator unlocks once you reach <Color id="aqua">Midgard</Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fluid Machines</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_crucible" />
  ### <Color id="aqua">Magma Crucible</Color>
</Row>

Melts solid materials into fluids at high heat. Cobblestone into Lava, Ice into Water, Ender Pearls into Resonant Ender, and so on. The backbone of most fluid chains.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_chiller" />
  ### <Color id="aqua">Blast Chiller</Color>
</Row>

The reverse of the Magma Crucible: it rapidly freezes items and fluids back into solids. It accepts a <Color id="aqua">forming cast</Color> (Ingot, Ball or Rod) to decide what shape a fluid sets into.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_refinery" />
  ### <Color id="aqua">Fractionating Still</Color>
</Row>

Refines one fluid into other fluids, sometimes leaving a solid behind. This is the oil processing machine, and the usual feed for a Compression Dynamo.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_pyrolyzer" />
  ### <Color id="aqua">Pyrolyzer</Color>
</Row>

Decomposes solids with heat, producing charcoal, coke and creosote-type outputs. Its main use is purifying fuels into something a Dynamo gets more out of.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_bottler" />
  ### <Color id="aqua">Fluid Encapsulator</Color>
</Row>

Fills containers with fluid. Buckets, bottles, tanks. It is also required to bottle certain drinkable fluids before you can consume them.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_brewer" />
  ### <Color id="aqua">Alchemical Imbuer</Color>
</Row>

Brews potions and imbues fluids. Because each pass applies one step, you generally want a few chained together.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_crystallizer" />
  ### <Color id="aqua">Crystallizer</Color>
</Row>

Grows and reforms crystalline structures. It needs a fluid and at least one item to work.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Agriculture</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:machine_insolator" />
  ### <Color id="aqua">Phytogenic Insolator</Color>
</Row>

Grows crops and saplings inside its own inventory using FE and Water, with no farmland required. Add a fertilizer such as <ItemLink id="thermal:phytogro" /> in the catalyst slot for faster growth and a better bonus-output chance. See [Cultivation](cultivation.md) for the crop list.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Devices</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Devices are the cheap single-purpose blocks that sit alongside the machines. Most use little or no power.

<ItemImage id="minecraft:air" scale="0.25"/>

| Device | What it does |
|---|---|
| <ItemLink id="thermal:device_rock_gen" /> | <Color id="aqua">Igneous Extruder.</Color> Generates stone types. Needs an adjacent lava source and cooling; the block underneath changes the product |
| <ItemLink id="thermal:device_water_gen" /> | <Color id="aqua">Aqueous Accumulator.</Color> Endless water, from adjacent water sources |
| <ItemLink id="thermal:device_tree_extractor" /> | <Color id="aqua">Arboreal Extractor.</Color> Taps adjacent trees for latex; fertilizer boosts output. In this pack it also taps Nether fungi for <Color id="green">Nether Sap</Color> |
| <ItemLink id="thermal:device_collector" /> | <Color id="aqua">Vacuumulator.</Color> Picks up nearby items, with filtering |
| <ItemLink id="thermal:device_nullifier" /> | <Color id="aqua">Nullifier.</Color> Voids items and fluids. Automated input is destroyed instantly |
| <ItemLink id="thermal:device_soil_infuser" /> | <Color id="aqua">Phyto-Soil Infuser.</Color> Feeds FE to nearby Phyto-Soil, one layer above and below |

Also available: the Batch Composter, Aquatic Entangler (autofisher), Hive Hopper, Decoctive Diffuser (area potion effects) and Insightful Condenser (XP collection).

<Color id="yellow">Note:</Color> the Igneous Extruder unlocks once you reach <Color id="aqua">Jotunheim</Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="yellow">Note:</Color> Point the Arboreal Extractor at a Crimson or Warped stem instead of an overworld tree and it produces <Color id="green">Nether Sap</Color> instead of latex. Nether Sap is required later for crafting certain Simply Swords legendary weapons, so this device is not just an early-game latex tap.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Thermal Extra Machines</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

The Thermal Extra addon adds machines that sit on top of the base Thermal infrastructure. They run on FE the same way and accept the same augment families.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:component_assembly" />
  ### <Color id="aqua">Component Assembler</Color>
</Row>

Uses fluids to assemble several items into a more complex one. It is the most important addition for this pack, because it is where the <Color id="green">AE2 processors</Color> are made.

The pack's processor flow runs like this:

1. <ItemLink id="thermal:machine_press" /> turns Silicon into <Color id="green">Printed Silicon</Color>
2. The Component Assembler stamps the printed plates: Gold to Logic, Diamond to Engineering, Certus Quartz to Calculation, Sky Steel to Accumulation, and Dawnstone to Dwarven
3. The Component Assembler then combines a printed plate, Printed Silicon and 50mB of molten Redstone into the finished processor

See the Processors page in the AE2 guide for the wider context. EnderIO's slicing recipes cover the same steps if you would rather go that way.

To craft the Component Assembler: Paraffin Wax, 4x <ItemLink id="thermal:obsidian_glass" />, a <ItemLink id="thermal:machine_frame" />, 2x <Color id="aqua">Twinite Gear</Color> and 2x <ItemLink id="thermal:rf_coil" />.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:advanced_refinery" />
  ### <Color id="aqua">Adv. Refinery</Color>
</Row>

A stronger <ItemLink id="thermal:machine_refinery" />. It supports more item and fluid outputs than the Fractionating Still, so it can split an oil into several distinct products in one pass instead of a chain.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:endothermic_dehydrator" />
  ### <Color id="aqua">Endothermic Dehydrator</Color>
</Row>

Dries items and fluids out to yield new products. It can also concentrate a fluid into a more potent version of itself.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:fluid_mixer" />
  ### <Color id="aqua">Fluid Mixer</Color>
</Row>

Mixes two fluids into a new one, sometimes with a <Color id="aqua">second fluid</Color> as a byproduct. Fills the gap the Magma Crucible cannot.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:nitratic_igniter" />
  ### <Color id="aqua">Nitratic Igniter</Color>
</Row>

Harnesses explosions to break items into small pieces, including ores that resist ordinary grinding. A heavier alternative to the Pulverizer.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:device_harvester" />
  ### <Color id="aqua">Crop Harvester</Color>
</Row>

Breaks crops and plants in its radius once they are ready. Fit a Radial Enhancement augment to widen the area.

<Color id="yellow">Important:</Color> it only <Color id="red">breaks</Color> the crops. It does not pick anything up, so pair it with a Vacuumulator or a hopper floor.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal_extra:device_lava_gen" />
  ### <Color id="aqua">Magmatic Accumulator</Color>
</Row>

Provides a slow but steady supply of lava, and runs faster in the <Color id="red">Nether</Color> and nether-tagged dimensions such as Muspelheim.

<Color id="yellow">Important:</Color> it is not a lava generator from nothing. It <Color id="red">requires adjacent lava sources</Color> to function, in the same way the Aqueous Accumulator needs adjacent water.

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">Note:</Color> The Gelid Dynamo is also a Thermal Extra block, covered on the [Dynamos](dynamos.md) page.

<ItemImage id="minecraft:air" scale="0.25"/>
