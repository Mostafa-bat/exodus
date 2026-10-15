---
navigation:
  title: Alchemy
  icon: embers:alchemy_tablet
  parent: index.md
  position: 6
item_ids:
  - embers:alchemy_tablet
  - embers:alchemy_pedestal
  - embers:beam_cannon
  - embers:mnemonic_inscriber
  - embers:entropic_enumerator
  - embers:explosion_charm
  - embers:iron_crystal_seed
  - embers:copper_crystal_seed
  - embers:gold_crystal_seed
  - embers:lead_crystal_seed
  - embers:silver_crystal_seed
  - embers:tin_crystal_seed
  - embers:nickel_crystal_seed
  - embers:zinc_crystal_seed
  - embers:aluminum_crystal_seed
---
# <Color id="gold">Alchemy</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="gold">Alchemy</Color>
  <ItemImage id="alchemy_tablet" scale="2" />

  Ember alchemy is the art of transmuting materials through the focused application of Ember energy, aspecti, and catalytic ingredients. Master the Exchange Tablet and its supporting devices to unlock powerful transmutations.
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Transmutation</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<ItemGrid>
  <ItemIcon id="alchemy_tablet" />
  <ItemIcon id="alchemy_pedestal" />
  <ItemIcon id="beam_cannon" />
</ItemGrid>

Ember alchemy is truly a marvelous discovery. The first key is the Exchange Tablet: right-click on it to insert an item. The next is the Alchemy Pedestal: these bear aspecti on the bottom and ingredients on the top. For an alchemy recipe, place a pedestal for each needed ingredient about the Tablet, add one of the required aspecti on every pedestal, and strike the Tablet with the Beam Cannon.

The transmutation output will appear in a <ItemLink id="bin" /> placed underneath the Exchange Tablet.

<Color id="aqua">Setup steps:</Color>
1. Place the <ItemLink id="alchemy_tablet" /> and right-click to insert the target item.
2. Place <ItemLink id="alchemy_pedestal" /> blocks around the Tablet - one per required ingredient.
3. Place the required <Color id="green">aspectus</Color> on the bottom of each pedestal and the ingredient on top.
4. Fire the <ItemLink id="beam_cannon" /> at the Exchange Tablet to trigger the transmutation.


<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Aspecti</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Wrapping molten metal about an Ember Shard, you have devised the Aspectus. These items can focus the alchemical energies produced by burning ingredients into a particular elemental alignment, when placed on the bottom of Alchemy Pedestals during a Transmutation. Not every aspectus theorized for a recipe is always required.

Different metals produce different aspecti, each aligned to a different elemental force. Experiment with combinations to discover which aspecti are needed for each recipe.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Alchemy Accessories</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mnemonic_inscriber" />
  ### <Color id="aqua">Mnemonic Inscriber</Color>
</Row>

When attached to an exchange tablet and provided with a piece of paper, it will inscribe any successful alchemy recipe onto the paper. This is invaluable for recording recipes you have discovered, so you do not need to remember the exact combination of aspecti and ingredients.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="entropic_enumerator" />
  ### <Color id="aqua">Entropic Enumerator</Color>
</Row>

Loosens the restrictions a bit but also introduces a chance for the recipe to fail randomly. Each one allows two correct aspecti on the wrong ingredient, each additional one allows one more. Useful when you know the correct aspecti but are unsure of the exact placement.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="explosion_charm" />
  ### <Color id="aqua">Explosion Charm</Color>
</Row>

While wearing this charm, explosions that go off near you will be dissipated, their destructive force absorbed into the charm. It can also be placed on an Alchemy Pedestal for passive explosion protection around your workshop.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Notable Recipes</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Some particularly useful transmutations to discover:

* <Color id="green">Adhesive</Color> - A slime replacement, useful when slimeballs are scarce.
* <Color id="green">Archaic Bricks</Color> - Ancient building material. You need one to begin with, and Ancient Golems drop them.
* <Color id="green">Assorted Syntheses</Color> - Produces Netherrack and Soul Sand without a trip to the Nether.
* <Color id="green">Metallurgic Dust</Color> - Thrown into the world, transmutes nearby ore into a different type. It can also fail and leave you worthless rock, so test it before betting a vein on it.
* <Color id="green">Ancient Motive Core</Color> - The part that makes tools and armor augmentable. See [Tools & Equipment](tools.md).
* <Color id="green">Inflictor Gems</Color> - Damage-absorbing crystals for your Ashen armor.

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Crystal Seeds</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="iron_crystal_seed" />
  ### <Color id="aqua">Renewable Metal</Color>
</Row>

Crystal Seeds turn a metal into a slow renewable trickle. Transmute three ingots of a metal into a seed of that metal, place it, and feed it Ember.

<ItemGrid>
  <ItemIcon id="iron_crystal_seed" />
  <ItemIcon id="copper_crystal_seed" />
  <ItemIcon id="gold_crystal_seed" />
  <ItemIcon id="lead_crystal_seed" />
  <ItemIcon id="silver_crystal_seed" />
  <ItemIcon id="tin_crystal_seed" />
  <ItemIcon id="nickel_crystal_seed" />
  <ItemIcon id="zinc_crystal_seed" />
  <ItemIcon id="aluminum_crystal_seed" />
</ItemGrid>

Injecting Ember does two things. The seed grows and produces metal, and it slowly becomes more <Color id="green">pure</Color>. The purer a fully grown crystal is, the more metal each harvest yields. Check purity with a Tinker's Lens.

<Color id="yellow">Purity is lost the moment you break the seed</Color>, so pick the spot before you start feeding it, not after.

Treat seeds as a convenience next to your Embers setup rather than a production plan. If you want metal in bulk, <Color id="light_purple">ProjectE</Color> EMC and <Color id="green">Mystical Agriculture</Color> both do it faster and with far less fuss.
