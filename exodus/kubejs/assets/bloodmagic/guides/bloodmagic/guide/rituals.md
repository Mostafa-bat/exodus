---
navigation:
  title: Rituals
  icon: bloodmagic:ritualdiviner
  parent: index.md
  position: 7
item_ids:
  - bloodmagic:masterritualstone
  - bloodmagic:ritualstone
  - bloodmagic:activationcrystalweak
  - bloodmagic:ritualdiviner
  - bloodmagic:airscribetool
  - bloodmagic:firescribetool
  - bloodmagic:waterscribetool
  - bloodmagic:earthscribetool
  - bloodmagic:duskscribetool
  - bloodmagic:airritualstone
  - bloodmagic:fireritualstone
  - bloodmagic:waterritualstone
  - bloodmagic:earthritualstone
  - bloodmagic:duskritualstone
  - bloodmagic:lightritualstone
  - bloodmagic:ritualtinkerer
---
# <Color id="red">Rituals</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Rituals</Color>
  <ItemImage id="bloodmagic:ritualstone" scale="2" />
  Rituals use LP from your Soul Network to perform various powerful tasks such as generating ores, growing crops, damaging mobs for LP, and many more.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Setting Up a Ritual</Color>
</Column>

Rituals are centered around the <Color id="light_purple">Master Ritual Stone</Color>, with a number of <Color id="dark_green">Ritual Stones</Color> placed in specific patterns nearby. You need a <Color id="aqua">Tier 3 Altar</Color> before you can make the parts.

Range is not fixed. Every ritual has its own area, and many of them reach several blocks above and below the Master Ritual Stone, so check before you build one into a ceiling.

A <ItemLink id="bloodmagic:ritualtinkerer" /> reconfigures a running ritual. Sneak + right-click cycles its three modes: read the ritual's function, set which types of <Color id="gray">Demon Will</Color> it draws from the Aura by holding the matching crystals in your hotbar, or redefine its working area. Enlarging the area raises the LP cost.

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Step 1: Build the Structure</Color>

Place a <Color id="light_purple">Master Ritual Stone</Color> and surround it with <Color id="dark_green">Ritual Stones</Color> in the correct pattern for your chosen ritual.

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Step 2: Color the Stones</Color>

Use <Color id="green">Inscription Tools</Color> to color the Ritual Stones. Each ritual requires specific colors in specific positions. The tools no longer have durability, so you can also use them purely for decoration.

<ItemGrid>
  <ItemIcon id="bloodmagic:airscribetool" />
  <ItemIcon id="bloodmagic:firescribetool" />
  <ItemIcon id="bloodmagic:waterscribetool" />
  <ItemIcon id="bloodmagic:earthscribetool" />
  <ItemIcon id="bloodmagic:duskscribetool" />
</ItemGrid>

<ItemGrid>
  <ItemIcon id="bloodmagic:airritualstone" />
  <ItemIcon id="bloodmagic:fireritualstone" />
  <ItemIcon id="bloodmagic:waterritualstone" />
  <ItemIcon id="bloodmagic:earthritualstone" />
  <ItemIcon id="bloodmagic:duskritualstone" />
  <ItemIcon id="bloodmagic:lightritualstone" />
</ItemGrid>

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Step 3: Activate</Color>

Right-click the <Color id="light_purple">Master Ritual Stone</Color> with an <Color id="green">Activation Crystal</Color> to start the ritual.

<Row>
  <ItemImage id="bloodmagic:activationcrystalweak" />
  <Column>
    The <ItemLink id="bloodmagic:activationcrystalweak" /> is the basic crystal needed to activate most rituals.
  </Column>
</Row>

<ItemImage id="minecraft:air" scale="0.25"/>

Bind the crystal to yourself by right-clicking it first, or nothing will happen. The crystal does <Color id="yellow">not</Color> have to be bound to you, though. Whoever the crystal belongs to is the one paying the LP.

If it fails, the message tells you what went wrong:

* <Color id="green">"A rush of energy flows through the ritual!"</Color> means it worked.
* <Color id="yellow">"You feel a push, but are too weak..."</Color> means your Soul Network is short of LP.
* <Color id="red">"These runes are not configured correctly..."</Color> means the pattern is wrong or something is blocking it.

><Color id="aqua">Tip:</Color> Every ritual responds to redstone. A lever on the side of the Master Ritual Stone is the simplest way to shut one down before it drains your network dry.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Automatically Setting up Rituals</Color>
</Column>

<Row>
  <ItemImage id="bloodmagic:ritualdiviner" />
  <Column>
    ### <Color id="aqua">Ritual Diviner</Color>
  </Column>
</Row>

The <Color id="green">Ritual Diviner</Color> makes building rituals much easier. Sneak + right-click, or sneak + left-click, to cycle through rituals in either direction, then hold right-click on the <Color id="light_purple">Master Ritual Stone</Color> and it places and colours every stone from whatever Ritual Stones you are carrying.

Plain right-click rotates the ritual, which matters for the few that are not symmetrical, such as the Ritual of Speed. Hold sneak while hovering it in your inventory to see how many stones the selected ritual needs.

It clears grass and snow but not solid blocks, so level the site first.

It is <Color id="red">highly recommended</Color> to craft one before attempting any rituals.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:ritualdiviner" />
  <Column>
    ### <Color id="aqua">Ritual Diviner (Dusk)</Color>
  </Column>
</Row>

The base Diviner can only build the simpler rituals. The Dusk version handles everything that needs <Color id="aqua"><ItemLink id="bloodmagic:duskritualstone"/></Color> or <Color id="aqua"><ItemLink id="bloodmagic:lightritualstone"/></Color>, and requires a Tier 4 Altar to make its two Dusk Inscription Tools.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Blood Magic Ritual List</Color>
  Check the <Color id="green"><ItemLink id="patchouli:guide_book" tag='{"patchouli:book":"bloodmagic:guide"}' /></Color> for more details on these rituals.
</Column>

<ItemImage id="minecraft:air" scale="0.55"/>

<Row>
  <Column>
    - Ritual of the Shepherd
    - Ritual of Living Evolution
    - Reverence of the Condor
    - Rhythm of the Beating Anvil
    - Ritual of the Crusher
    - Gathering of the Forsaken Souls
    - Crack of the Fractured Crystal
    - Resonance of the Faceted Crystal
    - Focus of the Ellipsoid
    - Ritual of the Feathered Knife
    - Crash of the Timberman
  </Column>

  <Column>
    - Ritual of the Satiated Stomach
    - Ritual of the Geode's Bounty
    - Ritual of the Green Grove
    - The Sinner's Burden
    - Reap of the Harvest Moon
    - Ritual of the High Jump
    - Serenade of the Nether
    - Penance of the Leadened Soul
    - Ritual of Magnetism
    - Mark of the Falling Tower
    - Domain of the Filler
  </Column>

  <Column>
    - Ritual of Regeneration
    - Edge of the Hidden Realm
    - Ritual of Speed
    - Dawn of the New Moon
    - Pathway to the Endless Realm
    - Sound of the Cleansing Soul
    - Ritual of the Full Spring
    - Well of Suffering
    - Yawning of the Void
    - Call of the Zephyr
    </Column>
</Row>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Animus Ritual List</Color>
  Check the <Color id="dark_green"><ItemLink id="patchouli:guide_book" tag='{"patchouli:book":"animus:codex_animus"}' /></Color> for more details on these rituals.
</Column>

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <Column>
    - Ritual of Culling
    - Ritual of Endless Greed
    - Ritual of Entropy
    - Ritual of Luna
    - Ritual of Sol
    - Ritual of Nature's Leach
  </Column>

  <Column>
    - Ritual of Nolite Ignem
    - Ritual of Peaceful Beckoning
    - Ritual of Persistence
    - Ritual of Relentless Tides
    - Ritual of Siphon
    - Ritual of Reparare
  </Column>

  <Column>
    - Ritual of Serenity
    - Ritual of the Steadfast Heart
    - Ritual of Unmaking
    - Ritual of Source Vitaeum
    - Ritual of Floral Supremacy
    - Ritual of Arcane Mastery
  </Column>
</Row>

<ItemImage id="minecraft:air" scale="0.25"/>

><Color id="yellow">Note:</Color> The last three need Ars Nouveau, Botania and Iron's Spellbooks respectively. All three are in this pack.
