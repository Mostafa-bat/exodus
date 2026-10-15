---
navigation:
  title: Demon Will
  icon: bloodmagic:basemonstersoul
  parent: index.md
  position: 5
item_ids:
  - bloodmagic:soulsnare
  - bloodmagic:basemonstersoul
  - bloodmagic:soulgempetty
  - bloodmagic:soulgemlesser
  - bloodmagic:soulgemcommon
  - bloodmagic:soulgemgreater
  - bloodmagic:soulforge
  - bloodmagic:soulsword
  - bloodmagic:demoncrucible
  - bloodmagic:demoncrystallizer
  - bloodmagic:defaultcrystal
  - bloodmagic:corrosivecrystal
  - bloodmagic:destructivecrystal
  - bloodmagic:steadfastcrystal
  - bloodmagic:vengefulcrystal
---
# <Color id="red">Demon Will</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Demon Will</Color>
  <ItemImage id="bloodmagic:basemonstersoul" scale="2" />
  Demon Will is a second resource, entirely separate from LP. It fuels the <ItemLink id="bloodmagic:soulforge"/> and powers Sentient tools, and later it becomes an atmospheric resource that rituals feed on.
</Column>

***
<ItemImage id="minecraft:air" scale="0.25"/>

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Getting Your First Will</Color>
</Column>

<Row>
  <ItemImage id="bloodmagic:soulsnare" />
  <Column>
    ### <Color id="gold">Soul Snares</Color>
  </Column>
</Row>

Craft a stack of Soul Snares in the Altar and throw them at <Color id="yellow">hostile</Color> mobs. White particles mean the snare stuck. Kill the mob while it is marked and it drops Demon Will. <Color id="green">Looting</Color> increases the amount.

Snares do nothing to passive mobs, so do not waste them on cows.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:soulsword" />
  <Column>
    ### <Color id="gold">Sentient Sword</Color>
  </Column>
</Row>

Once you have enough will for a Sentient Sword, that becomes your main source. Any hostile mob it kills drops Will, no snare needed. The sword also grows stronger the more Will you are carrying.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:basemonstersoul" />
  <Column>
    ### <Color id="gold">Demon Will</Color>
  </Column>
</Row>

Will drops as an item you walk over to collect. All of it is plain <Color id="gray">Raw Will</Color>. The four coloured aspects are not random drops, they are made later by splitting crystals.

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tartaric Gems</Color>
</Column>

Tartaric Gems absorb and store Demon Will as it is picked up, acting as a portable will battery. Drop loose Will on the floor and a gem in your inventory will hoover it up. Right-click while holding a gem to pour its contents into the first other valid gem you are carrying.

| Gem | Capacity |
|-----|----------|
| <ItemImage id="bloodmagic:soulgempetty" scale="0.5" /> <Color id="green"><ItemLink id="bloodmagic:soulgempetty" /></Color> | 64 |
| <ItemImage id="bloodmagic:soulgemlesser" scale="0.5" /> <Color id="aqua"><ItemLink id="bloodmagic:soulgemlesser" /></Color> | 256 |
| <ItemImage id="bloodmagic:soulgemcommon" scale="0.5" /> <Color id="red"><ItemLink id="bloodmagic:soulgemcommon" /></Color> | 1,024 |
| <ItemImage id="bloodmagic:soulgemgreater" scale="0.5" /> <Color id="light_purple"><ItemLink id="bloodmagic:soulgemgreater" /></Color> | 4,096 |

><Color id="yellow">Note:</Color> Each upgrade is crafted from the gem below it, and the Hellfire Forge will spend the Will out of the gem being upgraded before touching the one in the gem slot. There is no Grand Tartaric Gem in this version.

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">The Will Aura</Color>
</Column>

Storing Will in gems is only the first half of the system. The second half is putting it into the world.

<Row>
  <ItemImage id="bloodmagic:demoncrucible" />
  <Column>
    ### <Color id="aqua">Demon Crucible</Color>
  </Column>
</Row>

Drop a charged Tartaric Gem, loose Will, or a Will crystal into the Crucible and it burns it off into the <Color id="green">Aura</Color>. The Aura is tracked <Color id="yellow">per chunk</Color>, so it stays where you built it. Several rituals get stronger when there is Will in the chunk.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:demoncrystallizer" />
  <Column>
    ### <Color id="aqua">Demon Crystallizer</Color>
  </Column>
</Row>

The Crystallizer pulls Will back out of the Aura and grows it into crystal clusters. The first spire costs 100 Will, each further spire costs 45 and burns for 50, so a mature cluster is a small net gain. Clusters cap at 7 spires.

Right-click a cluster bare-handed to harvest everything but the central spire, which needs 512 Will across your gems to do. A pickaxe takes the lot, central spire included.

<ItemImage id="minecraft:air" scale="0.5"/>

### <Color id="aqua">Aspected Will</Color>

Run a crystal cluster through the <Color id="light_purple">Resonance of the Faceted Crystal</Color> ritual and it splits into four aspects, one per elemental rune:

<ItemGrid>
  <ItemIcon id="bloodmagic:corrosivecrystal" />
  <ItemIcon id="bloodmagic:destructivecrystal" />
  <ItemIcon id="bloodmagic:steadfastcrystal" />
  <ItemIcon id="bloodmagic:vengefulcrystal" />
</ItemGrid>

Aspects can be burned in the Crucible like Raw Will, and they change how Sentient tools behave:

* <Color id="gray">Raw:</Color> straight damage increase
* <Color id="dark_green">Corrosive:</Color> chance to poison or wither on hit, otherwise as Raw
* <Color id="red">Vengeful:</Color> less damage than Raw, but faster attacks and a movement speed buff that scales with your stored Will
* <Color id="blue">Steadfast:</Color> less damage than Raw, but grants Absorption after a kill
* <Color id="gold">Destructive:</Color> the highest damage of any aspect, at the cost of attack speed
