---
navigation:
  title: Affixes & Reforging
  icon: apotheosis:sigil_of_rebirth
  parent: adventure.md
  position: 1
item_ids:
  - apotheosis:simple_reforging_table
  - apotheosis:reforging_table
  - apotheosis:sigil_of_rebirth
  - apotheosis:sigil_of_enhancement
  - apotheosis:sigil_of_withdrawal
  - apotheosis:sigil_of_socketing
  - apotheosis:sigil_of_unnaming
  - apotheosis:common_material
  - apotheosis:uncommon_material
  - apotheosis:rare_material
  - apotheosis:epic_material
  - apotheosis:mythic_material
---
# <Color id="dark_purple">Affixes & Reforging</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_purple">Affixes & Reforging</Color>
  <ItemImage id="sigil_of_rebirth" scale="2" />

  Affix Items are procedurally generated equipment with special modifiers called Affixes, similar to enchantments. Each item has a Rarity that determines how many stats, effects, and sockets it can roll.
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Rarities</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

- <Color id="gray">Common</Color> — 1 stat, possibly a 2nd.
- <Color id="green">Uncommon</Color> — 2 stats, possibly a 3rd, may get 1 socket.
- <Color id="blue">Rare</Color> — 3 stats + 1 effect, possibly a 2nd effect, may get a socket, slight durability bonus.
- <Color id="dark_purple">Epic</Color> — 3 stats + 1 effect, possibly a 4th stat + 2nd effect, up to 2 sockets, stronger durability bonus.
- <Color id="gold">Mythic</Color> — 4 stats + 2 effects, possibly a 3rd effect + 3 sockets, significant durability bonus.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Affix Types</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

- <Color id="aqua">Stat Affixes</Color> — Attribute bonuses such as increased damage, armor, or movement speed.
- <Color id="green">Socket Affixes</Color> — Empty slots that can hold Gems for additional bonuses.

Exclusive <Color id="blue">Rare+</Color> Affixes:

- <Color id="light_purple">Effect Affixes</Color> — Special abilities that trigger during combat or other actions.
- <Color id="yellow">Durability Affix</Color> — A flat durability multiplier that stacks multiplicatively with Unbreaking.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Sigils</Color>
</Column>

<Row>
  <ItemImage id="sigil_of_rebirth" />
  ### <Color id="aqua">Sigil of Rebirth</Color>
</Row>

Used in Reforging Tables to re-roll all Affixes on an item.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="sigil_of_enhancement" />
  ### <Color id="aqua">Sigil of Enhancement</Color>
</Row>

Used in the Augmenting Table to upgrade or reroll existing individual Affixes.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="sigil_of_socketing" />
  ### <Color id="aqua">Sigil of Socketing</Color>
</Row>

Used in a Smithing Table to add an extra Gem Socket to an Affix item (up to the tier cap).

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="sigil_of_withdrawal" />
  ### <Color id="aqua">Sigil of Withdrawal</Color>
</Row>

Used in a Smithing Table to remove the last socketed Gem from an Affix item.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="sigil_of_unnaming" />
  ### <Color id="aqua">Sigil of Unnaming</Color>
</Row>

Used in a Smithing Table to remove an Affix item name.

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Reforging & Augmenting</Color>
</Column>

Reforging re-rolls all Affixes on an item, potentially turning ordinary gear into powerful Affix items. Two types of reforges are available:

<Row>
  <ItemImage id="simple_reforging_table" />
  ### <Color id="aqua">Simple Reforging Table</Color>
</Row>

Can reforge items up to <Color id="blue">Rare</Color> quality. A good early-game option for improving your gear.


<ItemImage id="minecraft:air" scale="0.5" />

<Row>
  <ItemImage id="reforging_table" />
  ### <Color id="aqua">Reforging Table</Color>
</Row>

Can reforge items up to <Color id="gold">Mythic</Color> quality; The full-power version for late-game crafting.

Reforging requires three inputs: the item to reforge, Rarity Materials, and a <ItemLink id="sigil_of_rebirth"/>. You will be offered 3 choices which require more exp but provide better overall options, similar to enchanting. Items can be reforged multiple times.


<ItemImage id="minecraft:air" scale="0.25" />

<Row>
  <ItemImage id="augmenting_table" />
  ### <Color id="aqua">Augmenting Table</Color>
</Row>

The Augmenting Table is an end-game station that lets you upgrade or reroll individual Affixes on an Affixed item using a <Color id="gold"><ItemLink id="sigil_of_enhancement" /></Color>.

- <Color id="green">Upgrade</Color> — Costs <Color id="red">2 Sigils</Color>. Boosts the selected Affix by 25% strength.
- <Color id="aqua">Reroll</Color> — Costs <Color id="red">1 Sigil</Color>. Randomly re-rolls the selected Affix to another within the selected Affix pool.
