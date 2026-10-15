---
navigation:
  title: Altar Tiers
  icon: bloodmagic:blankrune
  parent: index.md
  position: 3
item_ids:
  - bloodmagic:blankrune
  - bloodmagic:speedrune
  - bloodmagic:dislocationrune
  - bloodmagic:accelerationrune
  - bloodmagic:chargingrune
  - bloodmagic:altarcapacityrune
  - bloodmagic:bettercapacityrune
  - bloodmagic:orbcapacityrune
  - bloodmagic:sacrificerune
  - bloodmagic:selfsacrificerune
  - bloodmagic:largebloodstonebrick
  - bloodmagic:dungeon_metal
  - bloodmagic:dungeon_ore
  - bloodmagic:daggerofsacrifice
  - animus:crystallized_demon_will_block
---
# <Color id="red">Altar Tiers</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Altar Tiers</Color>
  <ItemImage id="bloodmagic:blankrune" scale="2" />
  The Blood Altar runs from <Color id="gold">Tier 1 to Tier 6</Color>. You raise its tier by ringing it with Blood Runes and building up the pillars around it. Higher tiers unlock better recipes and hold far more LP.
</Column>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Rune Types</Color>
</Column>

Runes do two jobs at once. They count towards the Altar's tier, and most of them also upgrade it. A <ItemLink id="bloodmagic:blankrune" /> only counts for the tier and gives no bonus, so swap in useful runes as you can afford them.

<ItemGrid>
  <ItemIcon id="bloodmagic:blankrune" />
  <ItemIcon id="bloodmagic:speedrune" />
  <ItemIcon id="bloodmagic:altarcapacityrune" />
  <ItemIcon id="bloodmagic:bettercapacityrune" />
  <ItemIcon id="bloodmagic:orbcapacityrune" />
  <ItemIcon id="bloodmagic:sacrificerune" />
  <ItemIcon id="bloodmagic:selfsacrificerune" />
  <ItemIcon id="bloodmagic:dislocationrune" />
  <ItemIcon id="bloodmagic:accelerationrune" />
  <ItemIcon id="bloodmagic:chargingrune" />
</ItemGrid>

<ItemImage id="minecraft:air" scale="0.25"/>

| Rune | Effect per rune |
|------|-----------------|
| <ItemLink id="bloodmagic:blankrune" /> | Nothing. Counts towards the tier only. |
| <ItemLink id="bloodmagic:speedrune" /> | +20% crafting speed, additive |
| <ItemLink id="bloodmagic:altarcapacityrune" /> | +20% Altar LP capacity, additive |
| <ItemLink id="bloodmagic:bettercapacityrune" /> | +7.5% Altar LP capacity, multiplicative, applied after Runes of Capacity |
| <ItemLink id="bloodmagic:orbcapacityrune" /> | +2% capacity of the Blood Orb sitting in the Altar, while it is in there |
| <ItemLink id="bloodmagic:sacrificerune" /> | +10% LP from killing mobs at the Altar |
| <ItemLink id="bloodmagic:selfsacrificerune" /> | +10% LP from your own health |
| <ItemLink id="bloodmagic:dislocationrune" /> | +20% flow rate when pumping Life Essence to or from an external tank |
| <ItemLink id="bloodmagic:accelerationrune" /> | Speeds up Charging and Displacement Runes by one tick each, down to a floor of one operation per tick |
| <ItemLink id="bloodmagic:chargingrune" /> | Banks LP while the Altar is idle and dumps it into the next craft. Holds 1,000 LP per rune. |


Every rune has a <Color id="aqua">Reinforced</Color> version that doubles its effect. Those need Netherite Scrap and Intricate Hellforged Parts looted from the Demon Realm, and can be reverted in the Alchemical Reaction Chamber if you change your mind.

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tier 2</Color>
</Column>

Ring the Altar with <Color id="aqua">8 Blood Runes</Color>. This unlocks the <ItemLink id="bloodmagic:daggerofsacrifice" />, so you can start feeding the Altar with something other than your own health.

<GameScene zoom="3" background="#222222" interactive={true}>
  <ImportStructure src="assets/tier_2.nbt" />
</GameScene>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tier 3</Color>
</Column>

Add <Color id="aqua">20 more runes</Color>, 5 per side, one block down and two blocks out from the first ring. Then raise a two-block pillar in each corner and cap it with <Color id="gold">Glowstone</Color>. Any solid block works for the pillar itself, the Stone Bricks shown here are just tidy.

Tier 3 is the gate for <Color id="light_purple">Rituals</Color>.

<GameScene zoom="2" background="#222222" interactive={true}>
  <ImportStructure src="assets/tier_3.nbt" />
</GameScene>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tier 4</Color>
</Column>

Add <Color id="aqua">28 more runes</Color>, 7 per side, again one down and two out. Raise four-block corner pillars and cap them with <ItemLink id="bloodmagic:largebloodstonebrick" />.

<Color id="yellow">Note:</Color> Bloodstone Bricks are made from <Color id="green">Tau Fruit</Color>, which only grows in the dungeons opened by the <Color id="light_purple">Edge of the Hidden Realm</Color> ritual. Tier 4 is where Blood Magic stops being self-contained.

<GameScene zoom="2" background="#222222" interactive={true}>
  <ImportStructure src="assets/tier_4.nbt" />
</GameScene>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tier 5</Color>
</Column>

Add <Color id="aqua">52 more runes</Color>, 13 per side, one down and three out, leaving a one-block gap at either end. Put a <ItemLink id="bloodmagic:dungeon_metal" /> at each corner.

<Color id="yellow">Note:</Color> Hellforged Blocks are smelted from <ItemLink id="bloodmagic:dungeon_ore" />, which is only found in <Color id="green">The Mines</Color> inside a Blood Magic dungeon. You need a Foreman's Key to unlock the Spatial Distortion that leads there.

<GameScene zoom="1.5" background="#222222" interactive={true}>
  <ImportStructure src="assets/tier_5.nbt" />
</GameScene>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Tier 6</Color>
</Column>

Tier 6 is added by <Color id="dark_red">Animus</Color>, not by Blood Magic itself. The final ring is capped with <ItemLink id="animus:crystallized_demon_will_block" />, so you will need a working Demon Will setup before you can finish it.

<GameScene zoom="1" background="#222222" interactive={true}>
  <ImportStructure src="assets/tier_6.nbt" />
</GameScene>
