---
navigation:
  title: Storage
  icon: thermal:energy_cell
  parent: index.md
  position: 4
item_ids:
  - thermal:energy_cell
  - thermal:energy_cell_frame
  - thermal:fluid_cell
  - thermal:fluid_tank_augment
---
# <Color id="red">Storage</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Storage</Color>
  <ItemImage id="thermal:energy_cell" scale="2" />
  Thermal Expansion provides dedicated storage blocks for energy and fluids. Both can be upgraded with augments to increase capacity.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Energy Storage</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:energy_cell" />
  ### <Color id="aqua">Redstone Flux Cell</Color>
</Row>

Stores <Color id="gold">1,000,000 FE</Color> at base capacity, moving <Color id="gold">1,000 FE/t</Color> in and out. Each face can be set to input, output or neither in the GUI.

Raise the numbers with Integral Components for overall capacity, a <Color id="aqua">Stabilized RF Coil</Color> for storage, or a <Color id="aqua">High-Flux RF Coil</Color> for throughput. See [Augments](augments.md).


<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">Tip:</Color> RF Cells retain their stored energy when broken with a <ItemLink id="thermal:wrench" /> or Crescent Hammer. This makes them portable energy buffers for moving power between setups.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fluid Storage</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:fluid_cell" />
  ### <Color id="aqua">Fluid Cell</Color>
</Row>

Stores <Color id="gold">32 buckets</Color> (32,000 mB) of a single fluid at base capacity. Like the RF Cell, each face is configured individually. Upgrade with <ItemLink id="thermal:fluid_tank_augment" /> to increase capacity.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:fluid_tank_augment" />
  ### <Color id="aqua">Expanded Tank Constructor</Color>
</Row>

An augment that increases the maximum fluid capacity of Fluid Cells and of any machine with an internal tank. Thermal Extra reissues it in five stronger tiers: Soul Infused, Twinite, Shellite, Dragonsteel and Abyssal.


<ItemImage id="minecraft:air" scale="0.25"/>
