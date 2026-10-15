---
navigation:
  title: Getting Started
  icon: ars_nouveau:source_gem
  parent: index.md
  position: 1
item_ids:
  - ars_nouveau:novice_spell_book
  - ars_nouveau:apprentice_spell_book
  - ars_nouveau:archmage_spell_book
  - ars_nouveau:source_gem
  - ars_nouveau:imbuement_chamber
  - ars_nouveau:scribes_table
  - ars_nouveau:blue_archwood_log
  - ars_nouveau:magebloom_crop
  - ars_nouveau:magebloom_fiber
  - ars_nouveau:blank_parchment
  - ftb:codex_glyph_1
---
# <Color id="light_purple">Getting Started</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">Getting Started</Color>
  <ItemImage id="source_gem" scale="2" />

  Welcome to Ars Nouveau. This guide covers everything you need to begin your journey into spell crafting, from finding natural resources to building your first magical workstations.

  To get started with this mod, you'll need to clear the <CommandLink command="/ftbquests open_book 00770A59B8189794" title="Go to Maze Quest" close={true}><Color id="red">Helheim Maze</Color></CommandLink>.
</Column>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">World Generation</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Several resources spawn naturally in realms other than <Color id="red">Helheim</Color>. <Color id="green">Archwood Trees</Color> come in decorative variants and are used for crafting Casting Wands. <Color id="green">Source Berries</Color> do NOT spawn in the world, but can be crafted using <CommandLink command="/guideme open @s bloodmagic:guide bloodmagic:crafting.md" title="Open GuideMe Page" close={true}><Color id="red">Blood Magic Alchemy Arrays</Color></CommandLink> and can be used to craft Mana Regen potions.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Obtaining Source Gems</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="imbuement_chamber" />
  ### <Color id="aqua">Imbuement Chamber</Color>
</Row>

Build an <Color id="green">Imbuement Chamber</Color> and drop an ingredient inside. The chamber imbues it with Source over time, and works faster when it can draw from nearby Source Jars.

Two ingredients produce <ItemLink id="source_gem" /> in this pack:

<ItemGrid>
  <ItemIcon id="minecraft:amethyst_shard" />
  <ItemIcon id="malum:arcane_spirit" />
</ItemGrid>

- <ItemLink id="minecraft:amethyst_shard" />, the standard route
- <ItemLink id="malum:arcane_spirit" />, added by this pack

<Color id="yellow">The Lapis recipe has been removed</Color>, so do not plan around it.

The <Color id="green">Imbuement Chamber</Color> itself is buildable in <Color id="red">Helheim</Color>. Its recipe is <ItemLink id="malum:runewood_planks" /> around a pair of gold nuggets, so Malum's runewood is the real prerequisite for starting Ars Nouveau.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Spell Books</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="novice_spell_book" />
  ### <Color id="aqua">Ars Spell Books</Color>
</Row>

Three tiers of spell books unlock progressively more powerful glyphs. The <Color id="green">Novice Spell Book</Color> grants access to Tier 1 spells, the <Color id="green">Apprentice Spell Book</Color> unlocks Tier 2, and the <Color id="green">Archmage Spell Book</Color> unlocks Tier 3.

Higher tier books provide more spell slots, additional mana, and increased mana regeneration. Upgrading your spell book transfers all learned spells. Books can also be dyed to customize their appearance.

<Color id="yellow">Two of the three are gated in this pack:</Color>

| Book | Requirement |
|---|---|
| <Color id="green">Novice</Color> | Clear the <Color id="red">Helheim Maze</Color> |
| <Color id="green">Apprentice</Color> | Crafted in a normal crafting table from your Novice book plus obsidian, 3 diamonds, 2 quartz blocks and 2 gold ingots |
| <Color id="green">Archmage</Color> | Unlocks once you reach <Color id="aqua">Niflheim</Color> |

The Apprentice recipe is shapeless and preserves the NBT of the book you feed it, so every glyph you have already scribed carries across.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Learning New Glyphs</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="scribes_table" />
  ### <Color id="aqua">Scribe's Table</Color>
</Row>

The <Color id="green">Scribe's Table</Color> is used to learn new glyphs. Use a spell book on the table to open the codex. Each glyph requires a specific set of items (check JEI for each Glyph) and experience points.

Select a glyph, throw the required items onto the table, and the table scribes a new glyph into your spell book. The Scribe's Table is also used for inscribing spells onto [Equipment, Wand, and Spell Parchments](equipment.md).

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="ftb:codex_glyph_1" />
  ### <Color id="aqua">Codex Glyphs</Color>
</Row>

This pack adds a second way to learn glyphs. <Color id="gold">Random Codex Glyph</Color> items are handed out as rewards throughout the <Color id="light_purple">General Magic</Color> quest chapter, and using one instantly unlocks a random glyph of the matching tier.

<ItemGrid>
  <ItemIcon id="ftb:codex_glyph_1" />
  <ItemIcon id="ftb:codex_glyph_2" />
  <ItemIcon id="ftb:codex_glyph_3" />
</ItemGrid>

A codex only ever picks a glyph you do not already know, and it draws from the addon glyphs as well as the base mod. If you already know everything in that tier, it pays out experience instead.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Mana</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Spell Mana is consumed when casting spells. Your maximum mana and regeneration rate can be increased in several ways:

- Wearing <Color id="green">Mage Armor</Color> sets
- Applying <Color id="green">Mana Boost</Color> and <Color id="green">Mana Regen</Color> enchantments to your gear
- Unlocking more glyphs in your spell book

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Materials</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="magebloom_crop" />
  ### <Color id="aqua">Magebloom</Color>
</Row>

Using the Enchanting Apparatus, you can craft <Color id="light_purple">Magebloom Seeds</Color>. When harvested, Magebloom can be turned into <ItemLink id="magebloom_fiber" />, the key ingredient for crafting magical armor.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="blank_parchment" />
  ### <Color id="aqua">Blank Parchment</Color>
</Row>

Magebloom Fiber can also be used to craft <Color id="green">Blank Parchment</Color>. To inscribe a spell, use the parchment on a Scribe's Table, select the spell in your Spell Book, then sneak-right click the parchment. Spell Parchment is used for spell turrets, reactive enchantments, item filters, and crafting Warp Scrolls.

<ItemImage id="minecraft:air" scale="0.25"/>