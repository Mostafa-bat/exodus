---
navigation:
  title: Tools & Ducts
  icon: thermal:wrench
  parent: index.md
  position: 7
item_ids:
  - thermal:wrench
  - thermal:lock
  - thermal:earth_charge
  - thermal:lightning_charge
  - thermal:ice_charge
  - thermal:niter
  - thermal:xp_crystal
  - thermal:device_xp_condenser
  - thermal:energy_duct
  - thermal:fluid_duct
  - thermal:item_buffer
  - thermal:flux_drill
  - thermal:flux_saw
  - thermal:flux_magnet
  - thermal:flux_capacitor
  - thermal:fluid_reservoir
  - thermal:potion_infuser
  - thermal:potion_quiver
  - thermal:charge_bench
  - thermal:tinker_bench
---
# <Color id="red">Tools & Ducts</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Tools & Ducts</Color>
  <ItemImage id="thermal:wrench" scale="2" />
  The Thermal Series includes utility tools, RF-powered portable gear, and a duct system for moving energy and fluids.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Utility Tools</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:wrench" />
  ### <Color id="aqua">Crescent Hammer</Color>
</Row>

The Thermal wrench. Right-click machines and Dynamos to rotate them, sneak-right-click to dismantle them with contents and augments intact. Works on a lot of non-Thermal blocks too.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:lock" />
  ### <Color id="aqua">Signalum Security Lock</Color>
</Row>

Enables security on compatible blocks and items, binding them to you so other players cannot open them. Worth having on a shared server.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:xp_crystal" />
  ### <Color id="aqua">Insightful Crystal</Color>
</Row>

Portable experience storage. Bank levels before something dangerous and pull them back out afterwards.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:device_xp_condenser" />
  ### <Color id="aqua">Insightful Condenser</Color>
</Row>

Collects experience from nearby blocks that produce it, and lets you draw the stored experience off as a fluid. Point it at a mob farm or an XP-producing machine.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Charging and Augmenting</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

| Block | Purpose |
|---|---|
| <ItemLink id="thermal:charge_bench" /> | <Color id="aqua">Energetic Infuser.</Color> Charges several items at once |
| <ItemLink id="thermal:tinker_bench" /> | <Color id="aqua">Tinker Bench.</Color> Installs augments into items, and charges and refills them |

You need the Tinker Bench to put augments into the portable gear below. Machines are augmented in their own GUI instead.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Elemental Charges</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Throwable items crafted from Thermal minerals. There are three:

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:earth_charge" />
  ### <Color id="aqua">Earth Charge</Color>
</Row>

Converts blocks on impact, working stone down towards gravel and sand. Handy for terrain work.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:lightning_charge" />
  ### <Color id="aqua">Lightning Charge</Color>
</Row>

Calls down a strike on impact.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:ice_charge" />
  ### <Color id="aqua">Ice Charge</Color>
</Row>

Freezes water and puts out fires. Made with <ItemLink id="thermal:niter" /> and Blizz Powder.

<ItemImage id="minecraft:air" scale="0.25"/>

Each also has a Grenade and a TNT variant if you want the same effect over a wider area.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Thermal Dynamics - Ducts</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Thermal Dynamics on 1.20 is deliberately small. There are <Color id="aqua">two duct types</Color>, and neither is tiered.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:energy_duct" />
  ### <Color id="aqua">Fluxduct</Color>
</Row>

Carries Redstone Flux between Dynamos, machines and Cells. One tier only, so there is nothing to upgrade to later.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermal:fluid_duct" />
  ### <Color id="aqua">Fluiduct</Color>
</Row>

Carries fluids. A windowed version exists so you can see what is flowing through.

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="yellow">There are no Itemducts.</Color> Thermal does not ship item transport on this version, so use another mod's pipes, or the Logistical Item Buffer below, for moving items around.

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Attachments</Color>

Attachments clip onto the end of a duct where it meets a block:

| Attachment | Purpose |
|---|---|
| <Color id="aqua">Servo</Color> | Extracts from the attached block. Redstone control enables extraction |
| <Color id="aqua">Turbo-Servo</Color> | A much faster Servo, with more limited filtering |
| <Color id="aqua">Filter</Color> | Restricts what passes. Can filter inbound, outbound or both directions |
| <Color id="aqua">Redstone Flux Limiter</Color> | Caps how much energy flows through, configurable per direction |

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Support Blocks</Color>

| Block | Purpose |
|---|---|
| <ItemLink id="thermal:item_buffer" /> | <Color id="aqua">Logistical Item Buffer.</Color> Holds set items and quantities and can auto-extract. Latch mode waits until every listed item is present before releasing anything, which is ideal for keeping ratios |

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Thermal Innovation - Portable Gear</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Thermal Innovation gear runs on stored Redstone Flux instead of durability. Charge it at an <ItemLink id="thermal:charge_bench" /> or from a <ItemLink id="thermal:flux_capacitor" /> carried in your inventory.

<ItemImage id="minecraft:air" scale="0.25"/>

| Item | What it does |
|---|---|
| <ItemLink id="thermal:flux_capacitor" /> | Stores RF and recharges your other items as you carry it |
| <ItemLink id="thermal:flux_drill" /> | <Color id="aqua">Fluxbore.</Color> Mines blocks with RF. Takes Radial and Axial augments to widen the dig area |
| <ItemLink id="thermal:flux_saw" /> | <Color id="aqua">Fluxsaw.</Color> Cuts wood with RF, also area-upgradeable |
| <ItemLink id="thermal:flux_magnet" /> | <Color id="aqua">FluxoMagnet.</Color> Pulls in nearby dropped items |
| <ItemLink id="thermal:fluid_reservoir" /> | <Color id="aqua">Reservoir.</Color> Stores fluid and refills equipped items; also places and collects fluids |
| <ItemLink id="thermal:potion_infuser" /> | <Color id="aqua">Potion Infuser.</Color> Stores potions and applies them to you |
| <ItemLink id="thermal:potion_quiver" /> | <Color id="aqua">Alchemical Quiver.</Color> Imbues your arrows with a stored potion |

<Color id="gold">Tip:</Color> The Potion Infuser and Alchemical Quiver both take the Alchemical Amplifier and Alchemical Extender augments to raise potion strength or duration.

<ItemImage id="minecraft:air" scale="0.25"/>
