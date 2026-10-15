---
navigation:
  title: Getting Started
  icon: draconicevolution:draconium_ingot
  parent: index.md
  position: 1
item_ids:
  - draconicevolution:nether_draconium_ore
  - draconicevolution:draconium_ingot
  - draconicevolution:draconium_dust
  - draconicevolution:draconium_core
  - draconicevolution:wyvern_core
  - draconicevolution:awakened_core
  - draconicevolution:chaotic_core
  - draconicevolution:dragon_heart
  - draconicevolution:chaos_shard
  - draconicevolution:large_chaos_frag
  - draconicevolution:medium_chaos_frag
  - draconicevolution:small_chaos_frag
  - draconicevolution:awakened_draconium_ingot
  - draconicevolution:info_tablet
---
# <Color id="red">Getting Started</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Getting Started</Color>
  <ItemImage id="draconium_ingot" scale="2" />

  Draconic Evolution is a powerful endgame mod centered around Draconium, the Ender Dragon, and the Chaos Guardian. This page covers the essential materials and progression tiers you need to know.
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

<Color id="gold">Tip:</Color> Craft an <ItemLink id="info_tablet" /> early. It is the mod's built-in reference for its own blocks.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Draconium</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="nether_draconium_ore" />
  ### <Color id="aqua">Draconium Ore</Color>
</Row>

<Color id="yellow">In Architect's Exodus, Draconium Ore generates in <Color id="green">Muspelheim</Color> and nowhere else.</Color> Overworld, Nether and End generation are all switched off in the pack's datapack, so there is no point hunting for it in the End.

Look for <ItemLink id="nether_draconium_ore" /> between <Color id="aqua">Y 20 and Y 80</Color>, at roughly four veins per chunk, thickest around Y 50. That makes Muspelheim access the real gate on this entire mod.

<Color id="yellow">End Comets are switched off too</Color>, so the other vanilla source of Draconium is gone as well.

Smelt the ore for one <ItemLink id="draconium_ingot" />, or crush it for two. Create's Crushing Wheels and the EnderIO SAG Mill both give <Color id="aqua">2 <ItemLink id="draconium_dust" /></Color> per ore, and each dust smelts into an ingot.

<ItemImage id="minecraft:air" scale="0.25"/>

### <Color id="aqua">Draconium Outside This Mod</Color>

Several pack recipes that have nothing to do with Draconic Evolution still want Draconium, so mine more than the mod alone suggests:

* <Color id="green">Ancient Dust</Color> (Thermal Extra) from Draconium Dust in the Crystallizer
* <Color id="green">Purple Chalk</Color> (Occultism) from Draconium Dust
* <Color id="green">Epic gem dust</Color> (Apotheosis) from Draconium Ingots
* The <Color id="green">Infernal Dragon</Color> elite summoning ritual, which uses a Draconium Block as its altar item

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tier System</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Draconic Evolution runs on <Color id="aqua">four</Color> tiers, each with its own core item. Almost every recipe in the mod keys off one of these, and the tier names carry through to tools, armour, modules, injectors and energy controllers.

| Tier | Core | Made from |
|---|---|---|
| 1 | <ItemImage id="draconium_core" scale="0.5" /> <Color id="aqua">Draconium Core</Color> | <ItemLink id="draconium_ingot" /> |
| 2 | <ItemImage id="wyvern_core" scale="0.5" /> <Color id="aqua">Wyvern Core</Color> | Draconium Cores, fusion crafted |
| 3 | <ItemImage id="awakened_core" scale="0.5" /> <Color id="light_purple">Draconic Core</Color> | <ItemLink id="awakened_draconium_ingot" /> |
| 4 | <ItemImage id="chaotic_core" scale="0.5" /> <Color id="red">Chaotic Core</Color> | <ItemLink id="chaos_shard" /> fragments |

<Color id="yellow">Note:</Color> the base tier is <Color id="aqua">Draconium</Color>, not Wyvern. Wyvern is the second step and has its own core item, so do not expect a Draconium Core to satisfy a Wyvern recipe.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Dragon Heart</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="dragon_heart" />
  ### <Color id="aqua">Dragon Heart</Color>
</Row>

Dropped by the Ender Dragon. Fusion crafting a Dragon Heart with Draconium turns it into <ItemLink id="awakened_draconium_ingot" />, which unlocks the whole Draconic tier.

Since the Ender Dragon can be resummoned, this is a renewable bottleneck rather than a hard one.

<Color id="light_purple">Keep a spare.</Color> A Dragon Heart is also one of the ingredients in the <Color id="gold">Nidhoggr</Color> summoning ritual, so the main storyline needs one on top of whatever you spend on Awakened Draconium.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Chaos Shards</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="chaos_shard" />
  ### <Color id="aqua">Chaos Shard</Color>
</Row>

Chaos Shards gate the Chaotic tier, and they come from Chaos Islands in the outer End.

<Color id="yellow">The Chaos Guardian does not drop them.</Color> The guardian protects a <Color id="dark_purple">Chaos Crystal</Color>, and that crystal is what you break once the fight is over. It yields <Color id="gold">5 Chaos Shards</Color> per island.

<ItemImage id="minecraft:air" scale="0.25"/>

Shards break down into progressively smaller fragments, nine to one at each step:

| Item | Worth |
|---|---|
| <ItemLink id="chaos_shard" /> | 1 shard |
| <ItemLink id="large_chaos_frag" /> | 1/9 shard |
| <ItemLink id="medium_chaos_frag" /> | 1/81 shard |
| <ItemLink id="small_chaos_frag" /> | 1/729 shard |

<Color id="yellow">Careful with the names.</Color> The item IDs are offset by one step from what they display as: `medium_chaos_frag` shows in game as <Color id="aqua">Small Chaos Fragment</Color>, and `small_chaos_frag` shows as <Color id="aqua">Tiny Chaos Fragment</Color>. Recipes that ask for a "Tiny" fragment are asking for the smallest one.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">The Chaos Guardian in This Pack</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

The Chaos Guardian is Draconic Evolution's own boss, and in Architect's Exodus it is an <Color id="green">optional</Color> challenge sitting past the end of the main story. The quest book covers it under <Color id="gold">One Final Challenge</Color>.

<Color id="light_purple">The pack changes how it fights.</Color> Its Ground Effect and Aerial Bombard attacks no longer cut your flight or trap you in the arena, and everything else about the fight is untouched.

The [Chaos Guardian](chaos_guardian.md) page walks through the crystals, the shield and what the pack changed.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Pack Progression Gate</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="red">All three Draconic Evolution chestpieces are stage-locked.</Color> The Wyvern, Draconic and Chaotic Chestpieces need the <Color id="aqua">draconic stage</Color>, which is granted by the <Color id="gold">Restored Asgard</Color> quest, that is, by slaying Nidhoggr and finishing the main storyline.

Tools, modules, the reactor, energy cores and everything else are available as soon as you can build them. It is only the chest armour that waits until the end.

<ItemImage id="minecraft:air" scale="0.25" />
