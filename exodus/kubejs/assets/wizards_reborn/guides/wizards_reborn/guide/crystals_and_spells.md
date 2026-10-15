---
navigation:
  title: Crystals and Spells
  icon: wizards_reborn:earth_crystal_seed
  parent: index.md
  position: 4
item_ids:
  - wizards_reborn:earth_crystal_seed
  - wizards_reborn:water_crystal_seed
  - wizards_reborn:air_crystal_seed
  - wizards_reborn:fire_crystal_seed
  - wizards_reborn:void_crystal_seed
  - wizards_reborn:arcane_wand
  - wizards_reborn:crystal_bag
---

# <Color id="dark_purple">Crystals and Spells</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_purple">Crystals and Spells</Color>

  <ItemImage id="earth_crystal_seed" scale="2" />

  Elemental Crystals are the key to spellcasting. Grow them from seeds, harvest them, and slot one into an Arcane Wand as a lens to refract Wissen into real magic.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Crystal Seeds</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Use the <ItemLink id="wissen_crystallizer" /> to crystallise Arcanum together with elemental ingredients. There are <Color id="aqua">five</Color> types:

<ItemGrid>
  <ItemIcon id="earth_crystal_seed" />
  <ItemIcon id="water_crystal_seed" />
  <ItemIcon id="air_crystal_seed" />
  <ItemIcon id="fire_crystal_seed" />
  <ItemIcon id="void_crystal_seed" />
</ItemGrid>

The first four are made from Arcanum, Arcanum Dust and simple elemental items, so you can reach all of them as soon as the Crystallizer is running.

<Color id="light_purple">Void</Color> is the exception. A Void Crystal Seed combines one seed of each of the other four elements plus Arcacite, so it stays out of reach until the alchemy chain is finished.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Growing Crystals</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

1. Place a Crystal Seed in the world
2. Right-click it with <ItemLink id="arcanum_dust" /> to start it growing
3. Wait for it to mature
4. Break the grown crystal to harvest it

Harvesting sometimes chips off <Color id="aqua">Fractured Crystals</Color> instead of a whole one. They are not wasted: the <ItemLink id="wissen_crystallizer" /> reassembles fractured pieces back into a full crystal.

If waiting is tedious, the <Color id="light_purple">Crystal Growth Acceleration</Color> ritual points a light ray at a growing crystal and speeds it up dramatically. See the Rituals page.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Crystal Stats</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

This is the part that matters most and the part that is easiest to miss. As a seed grows its crystal lattice shifts, and the finished crystal ends up with four independent stats. <Color id="yellow">Two crystals of the same element are not interchangeable.</Color>

| Stat | What it affects |
|------|-----------------|
| <Color id="aqua">Focus</Color> | The power of the spell |
| <Color id="aqua">Balance</Color> | How much Wissen each cast consumes |
| <Color id="aqua">Absorption</Color> | The spell's cooldown |
| <Color id="aqua">Resonance</Color> | The power of a ritual the crystal is used in |

So grow plenty, check what you get, and keep the good ones. A <ItemLink id="crystal_bag" /> is worth crafting early just to keep them sorted.

Polishing a crystal at the <ItemLink id="jeweler_table" /> turns it into a <Color id="aqua">Faceted Crystal</Color>, improving its refraction so it can cast the stronger spells a rough crystal cannot.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Spellcasting</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="arcane_wand" />
  ### <Color id="aqua">Arcane Wand</Color>
</Row>

The Arcane Wand is your casting tool. The crystal you load into it acts as a <Color id="aqua">lens</Color>: its element decides which spells you can pick, and its stats decide how well they perform.

The wand draws Wissen from your accessories and charged items rather than from a block, so keep something like a Wissen Ring or Wissen Keychain on you.

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Controls</Color>

* Press <Color id="aqua">Selection Menu</Color> while holding the wand to choose crystals and spells, and to build spell sets
* <Color id="aqua">Next Spell</Color> and <Color id="aqua">Previous Spell</Color> cycle through the spells in the current set
* Hold <Color id="aqua">Spell Sets Toggle</Color> to switch between sets

All of these are rebindable under <Color id="gold">Wizard's Reborn</Color> in the controls menu.

<ItemImage id="minecraft:air" scale="0.25"/>

Spells come in families that repeat across the elements, such as Projectile, Ray, Charge and Aura, alongside element-specific ones like Blink, Fire Shield and Water Breathing. The <ItemLink id="arcanemicon" /> has a full Spells category listing every one of them.
