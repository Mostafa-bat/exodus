---
navigation:
  title: Machines
  icon: ars_nouveau:enchanting_apparatus
  parent: index.md
  position: 7
item_ids:
  - ars_nouveau:enchanting_apparatus
  - ars_nouveau:arcane_core
  - ars_nouveau:arcane_pedestal
  - ars_nouveau:storage_lectern
  - ars_nouveau:bookwyrm_charm
  - ars_nouveau:repository
  - ars_nouveau:potion_jar
  - ars_nouveau:potion_melder
  - ars_nouveau:potion_diffuser
  - ars_nouveau:mob_jar
  - ars_nouveau:runic_chalk
  - ars_nouveau:scryers_crystal
  - ars_nouveau:scryers_oculus
  - occultism:spirit_attuned_gem
---
# <Color id="light_purple">Machines</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">Machines</Color>
  <ItemImage id="enchanting_apparatus" scale="2" />

  Ars Nouveau provides a range of magical machines for crafting, storage, potion handling, and remote viewing.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Enchanting Apparatus</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enchanting_apparatus" />
  ### <Color id="aqua">Enchanting Apparatus</Color>
</Row>

The core crafting station of Ars Nouveau. Requires an <ItemLink id="arcane_core" /> placed underneath and <ItemLink id="arcane_pedestal" /> blocks arranged within 3 blocks of the Apparatus. The number of pedestals needed varies by recipe, up to a maximum of 8.

Place recipe ingredients on the pedestals, then use the target item on the Apparatus to begin crafting. Some recipes also require Source from nearby jars. Used for crafting machines, curios, equipment, enchanting items, and upgrading armor.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Storage System</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="storage_lectern" />
  ### <Color id="aqua">Storage Lectern</Color>
</Row>

View, manage, and craft from multiple connected inventories in one interface. Link inventories within <Color id="green">30 blocks</Color> using a <Color id="green">Dominion Wand</Color>, pointing from the inventory to the lectern. How many you can connect is set by how many <Color id="green">Bookwyrms</Color> are bound to the lectern, so add more Bookwyrms as your system grows.

Naming a chest (via anvil or the <Color id="green">Name</Color> spell) creates a separate storage tab in the Lectern interface, making organization easier.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bookwyrm_charm" />
  ### <Color id="aqua">Bookwyrm Charm</Color>
</Row>

Use on a Storage Lectern to add a Bookwyrm to the system. Bookwyrms are obtained via the <Color id="green">Ritual of Awakening</Color> augmented with Book and Quills.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="repository" />
  ### <Color id="aqua">Repository</Color>
</Row>

Stores a double chest worth of items. Can be named for display purposes. Works well with the Storage Lectern network.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Potion System</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="potion_jar" />
  ### <Color id="aqua">Potion Jar</Color>
</Row>

Stores up to 100 doses of a potion. Fill or empty with bottles, flasks, or arrows. Wixies use Potion Jars for auto-crafting potions. Can be locked with a <Color id="green">Dominion Wand</Color> to prevent accidental changes. Outputs a comparator signal based on fill level.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="potion_melder" />
  ### <Color id="aqua">Potion Melder</Color>
</Row>

Combines potions from two input jars into a combined potion stored in an output jar. Requires Source to operate. Useful for creating multi-effect potions.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="potion_diffuser" />
  ### <Color id="aqua">Potion Diffuser</Color>
</Row>

Consumes a potion from a linked jar and applies its effect to nearby entities approximately every 10 minutes. Great for passive buff areas.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Other Machines</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mob_jar" />
  ### <Color id="aqua">Containment Jar</Color>
</Row>

Captures and stores mobs using the <Color id="green">Ritual of Containment</Color>. The mob and the jar both need to be within 3 blocks of the brazier. Placing a Note Block above a jar will play the captured mob's ambient sound.

<Color id="yellow">Unlocks once you reach <Color id="aqua">Niflheim</Color>.</Color>

Jarred mobs keep simulating, which is what makes them useful rather than decorative. Chickens lay eggs, cows can be milked, sheep can be sheared, villagers and piglins can be traded with, and an Ender Dragon can be bottled for Dragon's Breath. Drygmys will also harvest from jarred mobs, which is the safe way to farm hostile drops.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="occultism:spirit_attuned_gem" />
  ### <Color id="aqua">Spirit Jars</Color>
</Row>

Ars Ocultas lets <Color id="dark_purple">Occultism</Color> spirits work from inside a Containment Jar. They keep their normal behaviour and <Color id="gold">stop decaying</Color>, which makes them permanent automation rather than a maintenance chore.

A jarred spirit automatically picks up matching items in a 7x7 around it, so a Crusher Spirit will pull and process ore on its own. You can also hopper or pipe items in, use Starbuncles, or right click items onto the jar directly. Janitor Spirits go further and push their results into an adjacent inventory.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="runic_chalk" />
  ### <Color id="aqua">Runic Chalk</Color>
</Row>

Places permanent runes on the ground that cast inscribed spells on entities walking over them. Runes recharge automatically from nearby Source Jars.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="scryers_crystal" />
  ### <Color id="aqua">Scryer's Crystal & Oculus</Color>
</Row>

Remote viewing tools. The <ItemLink id="scryers_crystal" /> lets you look through it to see a distant location. The <ItemLink id="scryers_oculus" /> combined with Scryer's Scrolls provides remote access to multiple crystals from one location.
