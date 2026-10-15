---
navigation:
  title: Getting Started
  icon: bloodmagic:altar
  parent: index.md
  position: 1
item_ids:
  - bloodmagic:altar
  - bloodmagic:sacrificialdagger
  - bloodmagic:blankslate
  - bloodmagic:daggerofsacrifice
  - bloodmagic:sacrificerune
  - bloodmagic:reinforcedslate
  - bloodmagic:infusedslate
  - bloodmagic:demonslate
  - bloodmagic:etherealslate
---
# <Color id="red">Getting Started</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Getting Started</Color>
  <ItemImage id="bloodmagic:altar" scale="2" />
  The core of Blood Magic begins with the Blood Altar. Place it down, grab a Sacrificial Knife, and start generating LP by sacrificing your own health next to it.
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Blood Altar</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

The Blood Altar stores Life Points (LP) that can be used to craft items within the Altar. A fresh Altar holds <Color id="red">10,000 LP</Color>, and about 10% of that is reserved for an invisible internal tank used to move Life Essence in and out.

Right-click the Altar with an item to put it in, right-click with an empty hand to take it back out. Once an item is inside, the Altar drains LP to transform it. Red particles mean it is making progress; grey smoke means the Altar is empty and the craft is <Color id="red">losing</Color> progress.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Gaining LP</Color>
</Column>

<Row>
  <ItemImage id="bloodmagic:sacrificialdagger" />
  <Column>
    ### <Color id="aqua">Sacrificial Knife</Color>
  </Column>
</Row>

The <Color id="green">Sacrificial Knife</Color> is your first tool for generating <Color id="red">LP</Color>. Right-click <Color id="yellow">while aiming at the air</Color> to trade one heart for <Color id="red">200 LP</Color>, which goes into a nearby Blood Altar. Aiming at a block does nothing, so stand back from the Altar when you use it.

<ItemImage id="minecraft:air" scale="0.5"/>

<Row>
  <ItemImage id="bloodmagic:daggerofsacrifice" />
  <Column>
    ### <Color id="aqua"> Dagger of Sacrifice </Color>
  </Column>
</Row>

Upon reaching [Altar Tier 2](altar_tiers.md), you can craft the <Color id="green">Dagger of Sacrifice</Color> from an Iron Sword for <Color id="red">3,000 LP</Color>. Hit any mob, hostile or passive, that is standing <Color id="yellow">within 2 blocks of your Altar</Color> and it dies instantly, giving the Altar a lump of LP. Different mobs are worth different amounts, and <ItemLink id="bloodmagic:sacrificerune" /> increases the payout.

Note that this dagger only works next to the Altar. It is not a weapon.

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Slates</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

You'll be able to craft different slates as you level up your [Altar Tiers](altar_tiers.md).

The <Color id="green"><ItemLink id="bloodmagic:blankslate" /></Color> is the most basic slate in Blood Magic. Place Stone in a Blood Altar with at least <Color id="red">1,000 LP</Color> in it to craft some.

><Color id="red">Important:</Color> The LP cost is multiplied by the size of the stack you insert. If the Altar runs dry partway through, the craft does not fail outright, it just sits there bleeding progress until you feed it more LP.

Each slate needs the one below it and a higher Altar tier:

| Slate | Altar Tier | LP Cost |
|-------|------------|---------|
| <ItemImage id="bloodmagic:blankslate" scale="0.5" /> <ItemLink id="bloodmagic:blankslate" /> | 1 | 1,000 |
| <ItemImage id="bloodmagic:reinforcedslate" scale="0.5" /> <ItemLink id="bloodmagic:reinforcedslate" /> | 2 | 2,000 |
| <ItemImage id="bloodmagic:infusedslate" scale="0.5" /> <ItemLink id="bloodmagic:infusedslate" /> | 3 | 5,000 |
| <ItemImage id="bloodmagic:demonslate" scale="0.5" /> <ItemLink id="bloodmagic:demonslate" /> | 4 | 15,000 |
| <ItemImage id="bloodmagic:etherealslate" scale="0.5" /> <ItemLink id="bloodmagic:etherealslate" /> | 5 | 30,000 |