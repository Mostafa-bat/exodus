---
navigation:
  title: Automation
  icon: ars_nouveau:starbuncle_charm
  parent: index.md
  position: 6
item_ids:
  - ars_nouveau:starbuncle_charm
  - ars_nouveau:wixie_charm
  - ars_nouveau:drygmy_charm
  - ars_nouveau:whirlisprig_charm
  - ars_nouveau:amethyst_golem_charm
  - ars_nouveau:basic_spell_turret
  - ars_nouveau:spell_prism
  - ars_nouveau:spell_sensor
  - ars_nouveau:void_prism
  - ars_nouveau:redstone_relay
  - ars_nouveau:allow_scroll
  - ars_nouveau:deny_scroll
  - ars_nouveau:mimic_scroll
  - starbunclemania:star_bucket
  - starbunclemania:star_battery
  - starbunclemania:star_bin
  - starbunclemania:direction_scroll
  - starbunclemania:wyrm_degree
  - starbunclemania:fluid_jar
  - starbunclemania:source_condenser
  - starbunclemania:smelting_wixie_cauldron
---
# <Color id="light_purple">Automation</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">Automation</Color>
  <ItemImage id="starbuncle_charm" scale="2" />

  Ars Nouveau provides magical creatures and spell-casting devices that can automate item transport, crafting, farming, and more.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Magical Creatures</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="starbuncle_charm" />
  ### <Color id="aqua">Starbuncle</Color>
</Row>

Handles item transport. Wild Starbuncles appear in wooded areas hunting for gold nuggets. Give one a <ItemLink id="minecraft:gold_nugget" /> and it vanishes, leaving a <Color id="gold">Starbuncle Token</Color> behind. Craft that token into a <ItemLink id="starbuncle_charm" /> at the Enchanting Apparatus with four gold ingots, then use the charm on the ground to summon your own.

Setting one up with the <Color id="green">Dominion Wand</Color> follows the usual source then destination order:

- <Color id="aqua">To deposit into a chest:</Color> wand the <Color id="green">Starbuncle first</Color>, then the chest.
- <Color id="aqua">To pull from a chest:</Color> wand the <Color id="green">chest first</Color>, then the Starbuncle.

One Starbuncle can service as many inventories as you like, and looking at it tells you how many it is taking from and delivering to. Sneak-use the wand on it to reset everything. Control what they carry with <ItemLink id="allow_scroll" /> and <ItemLink id="deny_scroll" />, or by hanging an item frame on the inventory itself. Can be dyed any color.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="wixie_charm" />
  ### <Color id="aqua">Wixie</Color>
</Row>

Auto-crafting assistant. Cast <Color id="green">Dispel</Color> on a Witch at half health or less to get a <Color id="gold">Wixie Token</Color>, then craft it into a <ItemLink id="wixie_charm" /> at the Enchanting Apparatus. Place the charm on a Cauldron to summon the Wixie.

To set a crafting recipe, use the desired output item on the Wixie's Cauldron. Place chests nearby with the required ingredients, and keep a Source Jar next to the Cauldron - each craft requires a small amount of Source. Use a <Color id="green">Dominion Wand</Color> to set the output storage. Wixies can also auto-craft potions when Potion Jars are nearby.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="drygmy_charm" />
  ### <Color id="aqua">Drygmy</Color>
</Row>

Produces mob drops without killing. Wild Drygmys are found following animals, though rarely. Give one a <Color id="green">Wilden Horn</Color> for a <Color id="gold">Drygmy Token</Color>, then craft it into a <ItemLink id="drygmy_charm" /> at the Enchanting Apparatus.

Use the <Color id="light_purple">Drygmy Charm</Color> on a Mossy Cobblestone block to set its home, which converts into a <Color id="green">Drygmy Henge</Color>. The Drygmy harvests drops from any mob within 10 blocks of the Henge, depositing items and experience gems into adjacent chests. Each harvest requires Source from a nearby jar.

Use more charms on the henge to add Drygmys and increase output, but the bigger lever is happiness, which rises with the number and diversity of nearby creatures. Drygmys can also harvest from mobs stored in <Color id="green">Containment Jars</Color>, allowing you to safely use hostile mobs.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="whirlisprig_charm" />
  ### <Color id="aqua">Whirlisprig</Color>
</Row>

Produces natural materials such as wood, crops, seeds, and flowers from surrounding vegetation. Grow a tree near a wild Whirlisprig for a <Color id="gold">Whirlisprig Token</Color>, then craft it into a <ItemLink id="whirlisprig_charm" /> at the Enchanting Apparatus.

Use the charm on any flower to summon the Whirlisprig and set its home, which reaches 10 blocks in every direction. They need Source nearby and a chest placed next to the flower, or they produce nothing. A more diverse habitat increases their happiness and output, and what you plant decides what you get: more trees means more logs, more crops means more seeds and harvests. Mood takes several minutes to update after you place blocks.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="amethyst_golem_charm" />
  ### <Color id="aqua">Amethyst Golem</Color>
</Row>

Harvests, grows, and collects Amethyst clusters. Obtained via the <Color id="green">Ritual of Awakening</Color> performed near Budding Amethyst blocks.

Use the charm on a block to summon the Golem, then set its home with a <Color id="green">Dominion Wand</Color> by selecting the Golem first and then a block. The Golem will harvest any crystals within 10 blocks of its home, and does nothing at all until a home is set.

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Other Golems</Color>

<ItemGrid>
  <ItemIcon id="georenouveau:coal_geore_golem_charm" />
  <ItemIcon id="georenouveau:copper_geore_golem_charm" />
  <ItemIcon id="georenouveau:diamond_geore_golem_charm" />
  <ItemIcon id="georenouveau:emerald_geore_golem_charm" />
  <ItemIcon id="georenouveau:gold_geore_golem_charm" />
  <ItemIcon id="georenouveau:iron_geore_golem_charm" />
  <ItemIcon id="georenouveau:lapis_geore_golem_charm" />
  <ItemIcon id="georenouveau:quartz_geore_golem_charm" />
  <ItemIcon id="georenouveau:redstone_geore_golem_charm" />
  <ItemIcon id="georenouveau:zinc_geore_golem_charm" />
  <ItemIcon id="ars_nouveau:amethyst_golem_charm" />
</ItemGrid>

With <Color id="gold">GeOres</Color>, golems can harvest much more than just Amethyst. Perform the <Color id="green">Ritual of Awakening</Color> near a golem's respective block to summon and command it.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Spell Automation</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="basic_spell_turret" />
  ### <Color id="aqua">Spell Turret</Color>
</Row>

Casts spells on a redstone signal, functioning like a magical dispenser. Accepts Touch and Projectile form spells. Draws Source from nearby jars. Can use Place Block and Item Pickup glyphs with an adjacent inventory.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="spell_prism" />
  ### <Color id="aqua">Spell Prism</Color>
</Row>

Redirects spell projectiles in the direction the block faces. Sends a signal to adjacent Observers when a spell passes through.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="spell_sensor" />
  ### <Color id="aqua">Spell Sensor</Color>
</Row>

Outputs a redstone signal when a spell is cast nearby. Signal strength scales based on the length of the spell cast.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="void_prism" />
  ### <Color id="aqua">Void Prism</Color>
</Row>

Destroys any spell projectiles that pass through it. Useful for stopping stray spells in automated setups.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Filter Scrolls</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="allow_scroll" />
  ### <Color id="aqua">Allow Scroll</Color>
</Row>

Magical creatures will only interact with items listed on this scroll. Use it to restrict a Starbuncle to specific materials.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="deny_scroll" />
  ### <Color id="aqua">Deny Scroll</Color>
</Row>

Magical creatures will interact with everything except items listed on this scroll. The inverse of the Allow Scroll.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mimic_scroll" />
  ### <Color id="aqua">Mimic Scroll</Color>
</Row>

Magical creatures will only insert items that match the contents of the attached inventory. Useful for sorting systems.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Starbuncle Mania</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

This addon turns Starbuncles into a general purpose logistics system and gives Wixies extra trades.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="starbunclemania:star_bucket" />
  ### <Color id="aqua">Starbuncle Accessories</Color>
</Row>

Give a Starbuncle an accessory and it hauls something other than items. Link them with the Dominion Wand exactly like item routing.

<ItemGrid>
  <ItemIcon id="starbunclemania:star_bucket" />
  <ItemIcon id="starbunclemania:star_battery" />
  <ItemIcon id="starbunclemania:star_bin" />
</ItemGrid>

- <ItemLink id="starbunclemania:star_bucket" /> moves fluids between tanks
- <ItemLink id="starbunclemania:star_battery" /> moves Forge Energy between blocks
- <ItemLink id="starbunclemania:star_bin" /> voids any item dropped nearby

Sneak-clicking a Starbuncle with an accessory makes it cosmetic only, so you can dress your familiar without giving it a job.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="starbunclemania:direction_scroll" />
  ### <Color id="aqua">Direction Scroll and Wyrm Degree</Color>
</Row>

Vanilla Starbuncle routing does not care which face of a block it touches, which breaks machines that separate inputs from outputs. A <ItemLink id="starbunclemania:direction_scroll" /> used on a Starbuncle, or placed in an item frame on the block, pins the interaction to one face. The <ItemLink id="starbunclemania:wyrm_degree" /> lets a Starbuncle insert and extract from specific sides.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="starbunclemania:smelting_wixie_cauldron" />
  ### <Color id="aqua">Wixie Jobs</Color>
</Row>

A Wixie no longer needs a Cauldron. Place one on a different workstation and it automates that station's recipes instead:

| Placed on | Becomes |
|---|---|
| Furnace | <Color id="green">Wixie's Furnace</Color>, smelting and smoking |
| Stonecutter | <Color id="green">Wixie's Stonecutter</Color> |
| Cutting Board | <Color id="green">Wixie's Cutting Board</Color> |
| Cooking Pot | <Color id="green">Wixie's Cooking Pot</Color> |

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="starbunclemania:fluid_jar" />
  ### <Color id="aqua">Fluid Handling</Color>
</Row>

The <ItemLink id="starbunclemania:fluid_jar" /> is a 16 bucket tank built from Cascading Archwood. Store a potion fluid in one with a Potion Jar above it and the contents transfer up for flask filling and melding.

The <ItemLink id="starbunclemania:source_condenser" /> runs the Source network in reverse, condensing Source from jars into <Color id="aqua">Liquefied Source</Color> and pushing it into tanks below. Paired with the <ItemLink id="starbunclemania:fluid_sourcelink" />, which burns fluids for Source, this lets you move Source through normal fluid pipes.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Ars Creo</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="ars_creo:starbuncle_wheel" />
  ### <Color id="aqua">Starbuncle Wheel</Color>
</Row>

Bridges Ars Nouveau into <Color id="gold">Create</Color>. The <ItemLink id="ars_creo:starbuncle_wheel" /> generates rotational force, and placing a gold block in front of it raises the RPM.

Ars Creo also makes several Ars blocks work on moving contraptions. Source Jars keep their contents, and Spell Turrets fire while mounted: a <Color id="green">Basic</Color> turret fires when interacted with, a <Color id="green">Timer</Color> turret fires on its interval, and an <Color id="green">Enchanted</Color> turret fires on every new block the contraption reaches.
