---
navigation:
  title: Alchemy
  icon: wizards_reborn:alchemy_machine
  parent: index.md
  position: 5
item_ids:
  - wizards_reborn:wissen_wand
  - wizards_reborn:alchemy_furnace
  - wizards_reborn:alchemy_machine
  - wizards_reborn:alchemy_glass
  - wizards_reborn:alchemy_boiler
  - wizards_reborn:fluid_extractor
  - wizards_reborn:steam_extractor
  - wizards_reborn:steam_pipe
  - wizards_reborn:fluid_pipe
  - wizards_reborn:orbital_fluid_retainer
  - wizards_reborn:steam_thermal_storage
---

# <Color id="dark_purple">Alchemy</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_purple">Alchemy</Color>

  <ItemImage id="alchemy_machine" scale="2" />

  Alchemy lets you transform items and fluids into new materials. The setup needs steam, fluids and Wissen working together. There is a working example at the bottom of this page.

  The short version: the <Color id="aqua">Furnace</Color> makes steam, pipes carry it to the <Color id="aqua">Machine</Color>, and the <Color id="aqua">Boiler</Color> sits on top of the Machine to hold it all.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Alchemy Machines</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

The alchemy system uses three core blocks:

<Row>
  <ItemImage id="alchemy_furnace" />
  ### <Color id="aqua">Alchemy Furnace</Color>
</Row>

The steam source. It burns fuel to boil water into steam and holds its heat for a long time afterwards, so it does not need constant feeding. It doubles as an ordinary furnace if you want to smelt something in it.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="alchemy_machine" />
  ### <Color id="aqua">Alchemy Machine</Color>
</Row>

The main processing block. It transforms both items and fluids using steam, and most recipes want some Wissen as well. Nearly everything on the Advanced Materials page is made here, along with <ItemLink id="alchemy_glass" />, long-lasting potions and the mod's teas.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="alchemy_boiler" />
  ### <Color id="aqua">Alchemy Boiler</Color>
</Row>

<Color id="yellow">The Boiler does not make steam.</Color> It is the Alchemy Machine's top half and must be <Color id="aqua">placed directly above it</Color> for the machine to run at all. The Boiler is what actually holds the steam, the Wissen and any fluid the recipe produces.

Your steam still has to come from the Alchemy Furnace and be piped in.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Steam & Fluid Handling</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Moving steam and fluids between machines requires pipes and extractors:

<Row>
  <ItemImage id="steam_extractor" />
  ### <Color id="aqua">Steam Extractor</Color>
</Row>

Pulls steam out of a storage block and pushes it down the pipes. <Color id="yellow">It only runs while it has a redstone signal</Color>, which catches most people out. Right-click it to flip it into inversion mode.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="steam_pipe" />
  ### <Color id="aqua">Steam Pipe</Color>
</Row>

Moves steam from pipe to pipe. Connections are set with the <ItemLink id="wissen_wand" />, and Reload Mode clears a pipe that has clogged.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="fluid_extractor" />
  ### <Color id="aqua">Fluid Extractor</Color>
</Row>

The same idea for fluids. Also redstone-activated, and also right-clickable to invert.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="fluid_pipe" />
  ### <Color id="aqua">Fluid Pipe</Color>
</Row>

Moves fluids from pipe to pipe, configured and unclogged the same way as Steam Pipes.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fluid & Steam Storage</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="orbital_fluid_retainer" />
  ### <Color id="aqua">Orbital Fluid Retainer</Color>
</Row>

Stores fluids for your alchemy network.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="steam_thermal_storage" />
  ### <Color id="aqua">Steam Thermal Storage</Color>
</Row>

Buffers steam so your boiler output can be stored and used on demand.

***

<Column alignItems="center" fullWidth={true}>
  ### <Color id="gold">Working Example</Color>
</Column>

<GameScene zoom="5" interactive={true}>
  <ImportStructure src="assets/alchemy_example.nbt" />
</GameScene>