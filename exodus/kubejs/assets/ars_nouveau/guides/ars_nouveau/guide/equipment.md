---
navigation:
  title: Equipment
  icon: ars_nouveau:enchanters_sword
  parent: index.md
  position: 4
item_ids:
  - ars_nouveau:enchanters_sword
  - ars_nouveau:enchanters_shield
  - ars_nouveau:enchanters_mirror
  - ars_nouveau:enchanters_eye
  - ars_nouveau:spell_bow
  - ars_nouveau:spell_crossbow
  - ars_nouveau:wand
  - ars_nouveau:sorcerer_hood
  - ars_nouveau:sorcerer_robes
  - ars_nouveau:sorcerer_leggings
  - ars_nouveau:sorcerer_boots
  - ars_nouveau:arcanist_hood
  - ars_nouveau:arcanist_robes
  - ars_nouveau:arcanist_leggings
  - ars_nouveau:arcanist_boots
  - ars_nouveau:battlemage_hood
  - ars_nouveau:battlemage_robes
  - ars_nouveau:battlemage_leggings
  - ars_nouveau:battlemage_boots
  - ars_nouveau:alteration_table
  - ars_elemental:fire_hat
  - ars_elemental:aqua_hat
  - ars_elemental:earth_hat
  - ars_elemental:air_hat
  - ars_elemental:fire_focus
  - ars_elemental:water_focus
  - ars_elemental:earth_focus
  - ars_elemental:air_focus
  - ars_elemental:necrotic_focus
---
# <Color id="light_purple">Equipment</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="light_purple">Equipment</Color>
  <ItemImage id="enchanters_sword" scale="2" />

  Ars Nouveau provides a wide range of spell-enhanced weapons, armor sets, and crafting materials to complement your spellcasting.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Armor</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<ItemImage id="minecraft:air" scale="0.25"/>

Ars Nouveau offers three armor sets, each with different strengths:

- **Sorcerer** - Low physical defense, but the strongest Thread Slots for maximum perk customization.
- **Arcanist** - Balanced defense and Thread Slots.
- **Battlemage** - Highest physical defense, but fewer Thread Slots.

All three sets increase <Color id="green">mana regeneration</Color> while worn. Each set can be upgraded through three tiers at the Enchanting Apparatus.

Armor sets can also be upgraded via the <ItemLink id="enchanting_apparatus"/> up to tier 3, unlocking additional and more powerful Thread slots.

<ItemGrid>
  <ItemIcon id="sorcerer_hood" />
  <ItemIcon id="sorcerer_robes" />
  <ItemIcon id="sorcerer_leggings" />
  <ItemIcon id="sorcerer_boots" />
  <ItemIcon id="arcanist_hood" />
  <ItemIcon id="arcanist_robes" />
  <ItemIcon id="arcanist_leggings" />
  <ItemIcon id="arcanist_boots" />
  <ItemIcon id="battlemage_hood" />
  <ItemIcon id="battlemage_robes" />
  <ItemIcon id="battlemage_leggings" />
  <ItemIcon id="battlemage_boots" />
</ItemGrid>

<ItemImage id="minecraft:air" scale="0.5"/>


### <Color id="aqua">Elemental Armors</Color>

<ItemImage id="minecraft:air" scale="0.25"/>

Ars Elemental adds four more sets, each attuned to a school of magic. Every piece amplifies and discounts glyphs of its school and absorbs damage of the matching type. Wear the full set and that absorbed damage is converted into mana, plus a set bonus.

<ItemGrid>
  <ItemIcon id="ars_elemental:fire_hat" />
  <ItemIcon id="ars_elemental:fire_robes" />
  <ItemIcon id="ars_elemental:fire_leggings" />
  <ItemIcon id="ars_elemental:fire_boots" />
  <ItemIcon id="ars_elemental:aqua_hat" />
  <ItemIcon id="ars_elemental:aqua_robes" />
  <ItemIcon id="ars_elemental:aqua_leggings" />
  <ItemIcon id="ars_elemental:aqua_boots" />
  <ItemIcon id="ars_elemental:earth_hat" />
  <ItemIcon id="ars_elemental:earth_robes" />
  <ItemIcon id="ars_elemental:earth_leggings" />
  <ItemIcon id="ars_elemental:earth_boots" />
  <ItemIcon id="ars_elemental:air_hat" />
  <ItemIcon id="ars_elemental:air_robes" />
  <ItemIcon id="ars_elemental:air_leggings" />
  <ItemIcon id="ars_elemental:air_boots" />
</ItemGrid>

| Set | School | Absorbs | Full set bonus |
|---|---|---|---|
| <Color id="red">Pyromancer's</Color> | Fire | Lava, dragon breath, magma | Fire is put out instantly |
| <Color id="aqua">Aquamancer's</Color> | Water | Drowning, freezing, lightning | Refills air when you are about to drown |
| <Color id="green">Geomancer's</Color> | Earth | Starving, berry bushes, cactus, crushing | Feeds you when starving deep underground |
| <Color id="white">Aethermancer's</Color> | Air | Falling, wall impacts, lightning | Fall damage stops being a problem |

Each piece also carries its own mana pool bonus and regeneration bonus on top of the base mage armor effect.

These are not crafted from scratch. Each one is an <Color id="green">upgrade</Color> applied at the Enchanting Apparatus to a matching Sorcerer, Arcanist or Battlemage piece that is already at <Color id="gold">tier 3</Color>, using a Mark of Mastery, a Netherite Ingot and two essences of the matching element. Enchantments and Threads carry over.

<ItemImage id="minecraft:air" scale="0.5"/>


<Row>
  <ItemImage id="alteration_table" />
  ### <Color id="aqua">Alteration Table</Color>
</Row>

Threads (perks) are applied at the <ItemLink id="alteration_table" />. Each piece of mage gear has at least one <Color id="green">Thread Slot</Color>, with the tier shown in the item's tooltip. To use the table, place your armor on the stand. The tablet displays available slots - right click a Thread onto the tablet to apply it. To remove a thread, interact with the display using an empty hand. Armor tiers can be upgraded at the Enchanting Apparatus for additional Thread Slots.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Spell Weapons</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Spells can be inscribed directly onto magical equipment at the Scribe's Table. Equipment casts a specific <Color id="green">Form</Color> by default, so inscribed spells should not include a Form glyph - this frees up that slot for additional effects and augments.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enchanters_sword" />
  ### <Color id="aqua">Enchanter's Sword</Color>
</Row>

Casts a <Color id="light_purple">Touch</Color> spell on the target before dealing damage. The sword also adds one extra <Color id="green">Amplify</Color> augment to the last effect of the spell.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enchanters_shield" />
  ### <Color id="aqua">Enchanter's Shield</Color>
</Row>

Grants <Color id="green">Mana Regen</Color> and <Color id="green">Spell Damage</Color> bonuses for a short duration when you block damage. Self-repairs over time using mana from your pool.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enchanters_mirror" />
  ### <Color id="aqua">Enchanter's Mirror</Color>
</Row>

Casts a <Color id="light_purple">Self</Color>-targeted spell with a mana discount and bonus duration. For example, inscribing just <Color id="green">Heal</Color> creates a mirror that heals you on use.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="spell_bow" />
  ### <Color id="aqua">Spell Bow</Color>
</Row>

When inscribed with a spell, arrows become Spell Arrows that apply the spell on impact. If you have no arrows, a spell arrow with 0 damage is fired instead. If you run out of mana, regular arrows are fired. <Color id="green">Augment Arrows</Color> can further empower the inscribed spell.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="spell_crossbow" />
  ### <Color id="aqua">Spell Crossbow</Color>
</Row>

Functions like the Spell Bow in crossbow form. Also accepts Augment Arrows.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="wand" />
  ### <Color id="aqua">Wand</Color>
</Row>

Holds a single spell that always starts with <Color id="light_purple">Projectile -> Accelerate</Color>. Inscribe with just effect glyphs - for example, inscribing <Color id="green">Break</Color> will cast <Color id="green">Projectile -> Accelerate -> Break</Color> when used. Bypasses the normal 10 glyph cap, allowing longer spell chains.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Elemental Spell Foci</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="ars_elemental:fire_focus" />
  ### <Color id="aqua">Foci of the Schools</Color>
</Row>

Ars Elemental adds casting foci attuned to the four elemental schools. While equipped, a focus amplifies and discounts glyphs of its own school. They come in two grades:

<ItemGrid>
  <ItemIcon id="ars_elemental:lesser_fire_focus" />
  <ItemIcon id="ars_elemental:lesser_water_focus" />
  <ItemIcon id="ars_elemental:lesser_earth_focus" />
  <ItemIcon id="ars_elemental:lesser_air_focus" />
  <ItemIcon id="ars_elemental:fire_focus" />
  <ItemIcon id="ars_elemental:water_focus" />
  <ItemIcon id="ars_elemental:earth_focus" />
  <ItemIcon id="ars_elemental:air_focus" />
</ItemGrid>

- <Color id="green">Lesser foci</Color> buff their own school but weaken the other elemental schools as a drawback.
- <Color id="green">Major foci</Color> double the amplification and drop the penalty.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="ars_elemental:necrotic_focus" />
  ### <Color id="aqua">Focus of Necromancy</Color>
</Row>

Made by corrupting the Focus of Summoning rather than attuning to an element. Anima glyphs gain two free Extend Time, Heal gains two Amplify, and Charm becomes far more likely to land on undead. Summon Steed becomes a Skeletal Steed that walks and breathes underwater, and your Wolves, Undead and Vexes rise once when killed, casting Homing spells alongside you and healing you on their kills.

<ItemImage id="minecraft:air" scale="0.25"/>

***

Looking for curios, trinkets, and utility items? See [Trinkets & Utilities](trinkets.md).
