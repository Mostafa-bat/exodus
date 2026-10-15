---
navigation:
  title: Light Field
  icon: xycraft_machines:light_field
  parent: index.md
  position: 2
item_ids:
  - xycraft_machines:light_field
  - xycraft_world:kivi
  - xycraft_machines:machine_base
---
# <Color id="yellow">Light Field</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="yellow">Light Field</Color>
  <ItemImage id="xycraft_machines:light_field" scale="2" />

  The Light Field is a single-block <Color id="green">mob spawn suppressor</Color>. Place one and it prevents hostile mob spawns within a cubed volume centred on the block - much simpler than scattering torches everywhere or building a full lighting grid.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">What It Does</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

The <ItemLink id="xycraft_machines:light_field" /> suppresses mob spawns in the chunked area around itself - both surface and dark indoor areas. Useful for:

- <Color id="green">Base perimeters</Color> - one Light Field instead of a torch ring.
- <Color id="green">Underground builds</Color> - keep tunnels mob-free without lighting the walls.
- <Color id="green">Bridges & infrastructure</Color> - stop arrow spawns mid-crossing.

The block does <Color id="yellow">not</Color> suppress mobs that have already spawned, nor mobs spawned by spawners or summoning rituals. It only blocks the natural spawn event.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Recipe</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

A 3×3 shaped craft:

- <Color id="green">4×</Color> Xychorium Light Gems (corners) - tagged `forge:gems/xychorium_light`
- <Color id="green">2×</Color> <ItemLink id="xycraft_world:kivi" /> (middle sides) - tagged `xycraft:building/kivi`
- <Color id="green">1×</Color> <ItemLink id="minecraft:glowstone" /> (centre)
- <Color id="green">1×</Color> Silica Glass (top middle) - tagged `forge:glass/silica`
- <Color id="green">1×</Color> <ItemLink id="xycraft_machines:machine_base" /> (bottom middle)

<RecipeFor id="xycraft_machines:light_field" fallbackText="Check JEI - the Light Field uses Xychorium Light gems and Kivi blocks around a Glowstone core." />

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Where to Get the Materials</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

- <Color id="green">Xychorium Light Gems</Color> - from <Color id="aqua">Light Xychorium Ore</Color>, which generates in overworld-tagged biomes, so Midgard and the Overworld. The pack adds ore processing for it in most machines: a furnace or blast furnace gives 1 gem, while a SAG Mill, Crushing Wheel, Pulverizer, Squeezer or Crusher gives <Color id="gold">2 gems plus a 33% chance of a third</Color>.
- <Color id="green">Kivi</Color> - from Xycraft worldgen, and from the Kivi geodes the pack seeds in <Color id="aqua">Niflheim</Color>.
- <Color id="green">Aluminum</Color> for the Machine Base - see [Aluminum and Kivi](jotunheim_ore.md).
