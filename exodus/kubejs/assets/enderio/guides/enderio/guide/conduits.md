---
navigation:
  title: Conduits
  icon: enderio:item_conduit
  parent: index.md
  position: 5
item_ids:
  - enderio:item_conduit
  - enderio:fluid_conduit
  - enderio:pressurized_fluid_conduit
  - enderio:ender_fluid_conduit
  - enderio:energy_conduit
  - enderio:redstone_conduit
  - enderio:conduit_binder
  - enderio:conduit_binder_composite
  - enderio:basic_item_filter
  - enderio:advanced_item_filter
  - enderio:basic_fluid_filter
  - enderio:conduit_probe
---
# <Color id="dark_aqua">Conduits</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_aqua">Conduits</Color>
  <ItemImage id="enderio:item_conduit" scale="2" />
  Conduits are Ender IO's signature transport system. Multiple conduit types can share a single block space - run items, fluids, energy, and redstone all through one line. No more tangled pipe spaghetti.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Conduit Basics</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:conduit_binder" />
  ### <Color id="aqua">Conduit Binder</Color>
</Row>

Every conduit is six <ItemLink id="enderio:conduit_binder" /> around three of a metal, so this is the material you will burn through fastest. It takes two steps, and the two items are easy to mix up:

1. Craft <ItemLink id="enderio:conduit_binder_composite" /> in a crafting table from <Color id="gray">gravel, sand and clay balls</Color>. One craft makes <Color id="green">8</Color>.
2. Smelt or blast the Composite to get <ItemLink id="enderio:conduit_binder" />, <Color id="green">2 per Composite</Color>.

The Composite is the raw form and the Binder is the finished one. Recipes call for the Binder.

<Color id="yellow">The Composite is gated behind reaching <Color id="aqua">Jotunheim</Color>.</Color>


<ItemImage id="minecraft:air" scale="0.25"/>

Place conduits by right-clicking on a block or existing conduit. Multiple conduit types placed in the same block automatically merge into a single bundle. Use the <ItemLink id="enderio:yeta_wrench" /> to disconnect conduits from specific sides or to break individual conduit types from a bundle.

<ItemImage id="minecraft:air" scale="0.25"/>

Right-click a conduit connection point (where it meets a machine or inventory) to open the conduit GUI. Here you can configure extraction, insertion, filtering, and channel colors.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Item Conduits</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:item_conduit" />
  ### <Color id="aqua">Item Conduit</Color>
</Row>

Transports items between inventories. Configure each connection as Insert, Extract, or both. Use channel colors to create separate item networks within the same conduit bundle - items only travel between matching colors.


<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">Filtering:</Color> Insert an <ItemLink id="enderio:basic_item_filter" /> or <ItemLink id="enderio:advanced_item_filter" /> into a connection's filter slot to control which items pass through. The Advanced Item Filter supports NBT matching and ore dictionary filtering.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fluid Conduits</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:fluid_conduit" />
  ### <Color id="aqua">Fluid Conduit</Color>
</Row>

Basic fluid transport. Moves fluids at a standard rate between tanks and machines. One fluid type per conduit network.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:pressurized_fluid_conduit" />
  ### <Color id="aqua">Pressurized Fluid Conduit</Color>
</Row>

Higher transfer rate than the basic variant. Use when you need to move large volumes of fluid quickly - such as feeding multiple machines from a single source.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:ender_fluid_conduit" />
  ### <Color id="aqua">Ender Fluid Conduit</Color>
</Row>

The top-tier fluid conduit. Supports multiple fluid types in a single network using channel colors, just like Item Conduits. Enables complex multi-fluid setups without dedicated lines for each fluid.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Energy Conduits</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:energy_conduit" />
  ### <Color id="aqua">Energy Conduit</Color>
</Row>

Distributes energy between generators, storage, and machines. Energy Conduits have no loss and balance power across all connected consumers. Simple to set up - just connect and go.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Redstone Conduits</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:redstone_conduit" />
  ### <Color id="aqua">Redstone Conduit</Color>
</Row>

Transmits redstone signals without visible dust trails. Supports channel colors for multiple independent redstone signals in one bundle. Each connection can be set to input (read signal) or output (emit signal).


<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="gold">Redstone Filters:</Color> Insert redstone filters into conduit connections for logic operations. Available filters include AND, OR, NOT, NAND, NOR, XOR, XNOR, Toggle, Timer, Counter, and Sensor - enabling compact redstone logic without bulky circuits.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tools & Diagnostics</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enderio:conduit_probe" />
  ### <Color id="aqua">Conduit Probe</Color>
</Row>

Right-click a conduit to see diagnostic information about the network - what is connected, what channels are in use, and current transfer rates. Invaluable for debugging complex conduit setups.


<ItemImage id="minecraft:air" scale="0.25"/>
