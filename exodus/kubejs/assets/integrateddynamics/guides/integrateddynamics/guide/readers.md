---
navigation:
  title: Readers
  icon: integrateddynamics:part_redstone_reader
  parent: index.md
  position: 4
item_ids:
  - integrateddynamics:part_audio_reader
  - integrateddynamics:part_block_reader
  - integrateddynamics:part_entity_reader
  - integrateddynamics:part_extradimensional_reader
  - integrateddynamics:part_fluid_reader
  - integrateddynamics:part_inventory_reader
  - integrateddynamics:part_machine_reader
  - integrateddynamics:part_network_reader
  - integrateddynamics:part_redstone_reader
  - integrateddynamics:part_world_reader
---
# <Color id="aqua">Readers</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="aqua">Readers</Color>
  <ItemImage id="part_redstone_reader" scale="2" />

  The simplest method for creating a dynamic variable is done using Readers. Different types of readers exist for reading information from blocks or machines in the world and storing it inside Variable Cards. Each Reader contains one or more Aspect for reading different Values and Types. Readers are placed on Logic Cables facing a target block.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Reader Types</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_audio_reader" />
  ### <Color id="aqua">Audio Reader</Color>
</Row>

Reads information about music and audio playing in the environment. Useful for detecting note block output or other sound-related signals.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_block_reader" />
  ### <Color id="aqua">Block Reader</Color>
</Row>

Reads information about the block the part is facing. Can detect block type, properties, hardness, and other block-level data.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_entity_reader" />
  ### <Color id="aqua">Entity Reader</Color>
</Row>

Reads information about entities in the space the part is facing. Can detect entity type, health, position, and other entity attributes.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_extradimensional_reader" />
  ### <Color id="aqua">Extra-Dimensional Reader</Color>
</Row>

Reads server-wide information such as the list of online players. Unlike other readers, this one does not need to face a specific block since it reads global data.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_fluid_reader" />
  ### <Color id="aqua">Fluid Reader</Color>
</Row>

Reads values from the fluid tank being faced. Can detect fluid type, amount, capacity, and other tank-related data.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_inventory_reader" />
  ### <Color id="aqua">Inventory Reader</Color>
</Row>

Reads information from the facing inventory, such as slot count, contained items, and fullness. This reader only reads data and does not transfer items.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_machine_reader" />
  ### <Color id="aqua">Machine Reader</Color>
</Row>

Reads from the facing machine, such as its current recipes and work status. Useful for monitoring furnaces, crafting machines, and other processing blocks.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_network_reader" />
  ### <Color id="aqua">Network Reader</Color>
</Row>

Reads information about an Integrated Dynamics network being faced. This can be a different network from the one the reader is attached to, allowing you to monitor external networks.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_redstone_reader" />
  ### <Color id="aqua">Redstone Reader</Color>
</Row>

Reads redstone information from the facing block. Can detect signal strength, whether a block is powered, and comparator output levels.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="part_world_reader" />
  ### <Color id="aqua">World Reader</Color>
</Row>

Reads information about the world such as current weather, time of day, light level, and other environmental data.
