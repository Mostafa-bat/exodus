---
navigation:
  title: Crafting Stations
  icon: bloodmagic:alchemytable
  parent: index.md
  position: 4
item_ids:
  - bloodmagic:alchemytable
  - bloodmagic:arcaneashes
  - bloodmagic:reagentbinding
  - bloodmagic:soulforge
  - bloodmagic:alchemicalreactionchamber
  - bloodmagic:incensealtar
  - bloodmagic:divinationsigil
  - bloodmagic:seersigil
---
# <Color id="red">Crafting Stations</Color>

<Column alignItems="center" fullWidth={true}>

# <Color id="red">Crafting Stations</Color>
<ItemImage id="bloodmagic:alchemytable" scale="2" />

Blood Magic has a few crafting stations beyond the Blood Altar itself.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="bloodmagic:alchemytable" />
  <Column>
    ### <Color id="aqua">Alchemy Table</Color>
  </Column>
</Row>

The Alchemy Table uses <Color id="red">LP</Color> from your Soul Network to craft items. Put a bound [Blood Orb](blood_orbs.md) in the slot on the right along with the ingredients. The orb decides two things: whose network pays, and which recipes are available, since each recipe has a minimum orb tier.

This is where Arcane Ashes, sigil reagents, Anointments and 2x ore processing come from. Hover the LP arrow in JEI to see a recipe's time, drain and required tier.

The six buttons down the side toggle which faces hoppers and pipes may use for the selected slot. Click a slot, then click faces to allow or block them, then click the slot again to deselect.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:soulforge" />
  <Column>
    ### <Color id="aqua">Hellfire Forge</Color>
  </Column>
</Row>

The Hellfire Forge burns [Demon Will](demon_will.md) instead of LP. Drop a charged Tartaric Gem in the gem slot, put your ingredients in the four input slots, and it works through them.

It makes Sentient Tools, Tartaric Gems, sigil reagents, Arcane Ash and a good deal else. Every side can reach every slot, but each cardinal face prefers its own input slot, the top prefers the gem slot, and the bottom will only pull from the output.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:alchemicalreactionchamber" />
  <Column>
    ### <Color id="aqua">Alchemical Reaction Chamber</Color>
  </Column>
</Row>

The ARC doubles as a furnace, triples ore, and is the only source of Weak Blood Shards. It can also revert Blood Orbs, Netherite and Reinforced Runes back into what went into them, using a Sanguine Reverter.

It is sided like a furnace: tools go in the top, inputs from the sides, outputs come out the bottom. Most tools it uses take damage over time, so Unbreaking or Mending pays for itself.

><Color id="yellow">Note:</Color> In this pack the ARC unlocks once you reach <Color id="aqua">Niflheim</Color>.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:incensealtar" />
  <Column>
    ### <Color id="aqua">Incense Altar</Color>
  </Column>
</Row>

Not a crafting station so much as a multiplier on your own blood. Place it down and stay within 5 blocks, and it starts transforming your Sacrificial Knife. Once the knife glows, hold and release right-click near a Blood Altar to sacrifice <Color id="red">90% of your health</Color> in one go, with a bonus on top based on the area's <Color id="green">Tranquility</Color>.

Point a <ItemLink id="bloodmagic:divinationsigil" /> or <ItemLink id="bloodmagic:seersigil" /> at the Incense Altar to read its current Tranquility and bonus. Extending the setup outwards with the right blocks raises both.

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Alchemy Arrays</Color>
</Column>

<Row>
  <ItemImage id="bloodmagic:arcaneashes" />
  <Column>
    ### <Color id="aqua">Arcane Ashes</Color>
  </Column>
</Row>

Arcane Ashes draw <Color id="green">Alchemy Arrays</Color> on the ground. Right-click a block face with the ashes in hand to spend one of their 20 uses and draw a blank array.

An array takes exactly two items, clicked in one at a time. The <Color id="gold">base</Color> goes in first and changes the array's pattern if it is a valid combination, then the <Color id="gold">catalyst</Color> goes in second and sets it off. Arrays either craft an item, like most of the sigils, or perform a standing effect on the world around them.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:reagentbinding" />
  <Column>
    ### <Color id="aqua">Binding Reagent</Color>
  </Column>
</Row>

Binding Reagent is the array catalyst that makes [Living Armor](living_armor.md). It is crafted in the Alchemy Table and needs enough Demon Will that you will want a Common Tartaric Gem first.

Draw an array, apply the Binding Reagent, then drop an iron armour piece on it. The same reagent also repairs finished Living Armor in an anvil.
