---
navigation:
  title: Generating Flora
  icon: botania:endoflame
  parent: index.md
  position: 3
item_ids:
  - botania:endoflame
  - botania:hydroangeas
  - botania:thermalily
  - botania:rosa_arcana
  - botania:munchdew
  - botania:narslimmus
  - botania:gourmaryllis
  - botania:shulk_me_not
  - botania:dandelifeon
  - botania:rafflowsia
  - botania:spectrolus
  - botania:kekimurus
  - botania:entropinnyum
  - botania:heisei_dream
  - botania:apothecary_default
  - botania:cell_block
  - botania:vivid_grass
  - botania:enchanted_soil
  - mythicbotany:raindeletia
  - mythicbotany:wither_aconite
  - mythicbotany:mana_collector
---
# <Color id="green">Generating Flora</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="green">Generating Flora</Color>
  <ItemImage id="endoflame" scale="2" />
  Botania's Flowers from the <Color id="green">Generating Flora</Color> subtype can produce <Color id="aqua">Mana</Color> through a variety of methods. Said flowers can be linked to the nearest Mana Spreader either Automatically or by using a <ItemLink id="twig_wand"/>, and they will fill that spreader's <Color id="aqua">Mana Buffer</Color> over time.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Basic Generating Flora</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="endoflame" />
  ### <Color id="dark_green">Endoflame</Color>
</Row>

Burns any <Color id="gold">furnace fuel</Color> dropped in its vicinity, one item at a time.

It will not touch fuels that leave a byproduct behind, so you can't feed it with <Color id="red">Lava Buckets</Color>.

Because it can only burn one item at a time, make sure to automate it with some kind of timer to avoid wasting fuel when feeding it high-density solid fuels (e.g. <Color id="dark_gray">Coal Blocks</Color>).

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="hydroangeas" />
  ### <Color id="dark_green">Hydroangeas</Color>
</Row>

Consumes <Color id="blue">water blocks</Color> within the eight blocks surrounding it, provided they're at its own altitude.

Passively generates small amounts of <Color id="aqua">Mana</Color> as long as the <Color id="blue">water source</Color> is infinite.

It works a little faster in the <Color id="blue">rain</Color>, but <Color id="gray">decays</Color> after some time, so treat it as a stopgap rather than long-term infrastructure.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Advanced Generating Flora</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="thermalily" />
  ### <Color id="dark_green">Thermalily</Color>
</Row>

Similar to a <Color id="dark_green"><ItemLink id="hydroangeas"/></Color>, it consumes <Color id="red">Lava Blocks</Color> around it to produce <Color id="aqua">Mana</Color>, but unlike its <Color id="blue">water-consuming</Color> counterpart, it generates far more <Color id="aqua">Mana</Color>.

It generates <Color id="aqua">Mana</Color> continuously for about 30 seconds, after which it enters a <Color id="yellow">cooldown</Color> period lasting between 20 seconds and 5 minutes.

<Color id="dark_red">Comparators</Color> can be used to determine how much its <Color id="yellow">cooldown</Color> will last for, reading 20 seconds per level of <Color id="dark_red">signal strength</Color>.

One important thing to note, however, is that although this flower is capable of generating huge amounts of <Color id="aqua">Mana</Color>, any <Color id="red">Lava</Color> near it during its <Color id="yellow">cooldown</Color> will be consumed and wasted.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="gourmaryllis" />
  ### <Color id="dark_green">Gourmaryllis</Color>
</Row>

Similar to an <Color id="dark_green"><ItemLink id="endoflame"/></Color>, but it's hungry for delightful foods instead.

Any excess <Color id="gold">food</Color> dropped in its vicinity goes to waste, so make sure to use a timer to avoid wasting any.

<Color id="gold">Foods</Color> with a bigger nutritional value take longer to digest but provide much more <Color id="aqua">Mana</Color> in return.

And just like a true gourmand, this flower also requires a diverse menu so do not feed it only <Color id="gold">bread</Color>!

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="munchdew" />
  ### <Color id="dark_green">Munchdew</Color>
</Row>

Will ferociously consume any <Color id="green">leaves</Color> inside its range in exchange for <Color id="aqua">Mana</Color>, and once it's all eaten, it enters a <Color id="yellow">cooldown</Color> state for 1 minute.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="entropinnyum" />
  ### <Color id="dark_green">Entropinnyum</Color>
</Row>

Absorbs the blast of <Color id="red">TNT</Color> detonated on dry land in its vicinity, converting all of the entropy into <Color id="aqua">huge amounts of mana</Color>.

There's a catch, though: it can only do that once its internal <Color id="aqua">Mana buffer</Color> is completely empty. If you don't have a <Color id="yellow">timer</Color> set up correctly to manage that, <Color id="dark_red">explosions won't be nullified</Color> and will simply occur as usual.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="spectrolus" />
  ### <Color id="dark_green">Spectrolus</Color>
</Row>

Consumes a specific <Color id="red">c</Color><Color id="gold">o</Color><Color id="green">l</Color><Color id="aqua">o</Color><Color id="light_purple">r</Color> of Wool, in a set order, dropped in its vicinity, to generate a good amount of <Color id="aqua">Mana</Color>.

It won't generate any <Color id="aqua">Mana</Color> if the incorrect <Color id="red">c</Color><Color id="gold">o</Color><Color id="green">l</Color><Color id="aqua">o</Color><Color id="light_purple">r</Color> of Wool is provided and you can check this by holding a <Color id="dark_green"><ItemLink id="twig_wand" /></Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="kekimurus" />
  ### <Color id="dark_green">Kekimurus</Color>
</Row>

Eats <Color id="gold">Cake</Color> blocks placed in range, a slice at a time, and turns them into <Color id="aqua">Mana</Color>.

<Color id="dark_gray">*Long-time players might recall a certain starlit trick for turning pumpkins into cake.*</Color>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Mob-Based Generating Flora</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="rosa_arcana" />
  ### <Color id="dark_green">Rosa Arcana</Color>
</Row>

Drains <Color id="green">experience</Color> straight out of nearby players, and also absorbs loose <Color id="green">experience orbs</Color> lying in the small area around it.

It also strips the enchantments stored within <Color id="light_purple">enchanted items</Color> lying nearby, leaving the items themselves untouched.

Everything it absorbs is converted into <Color id="aqua">Mana</Color>.

Keep it away from anywhere you want to hold onto your levels or, alternatively, consider placing it near a <Color id="dark_red">Mob Grinder</Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="narslimmus" />
  ### <Color id="dark_green">Narslimmus</Color>
</Row>

Absorbs <Color id="green">Slimes</Color> that spawn naturally in a <Color id="green">Slime Chunk</Color>, paying out more for larger ones. It only counts naturally spawned <Color id="green">Slimes</Color>, so a spawner will not feed it.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="shulk_me_not" />
  ### <Color id="dark_green">Shulk Me Not</Color>
</Row>

Feeds on the power of <Color id="light_purple">Shulker Levitation</Color> rather than on kills directly. When a nearby monster is struck by a <Color id="light_purple">Shulker</Color>'s projectile while the flower's buffer is empty, both the monster and the <Color id="light_purple">Shulker</Color> die, producing an absurd amount of <Color id="aqua">Mana</Color>.

Both entities must be within this flower's range, and any <Color id="green">experience</Color> or <Color id="gold">loot</Color> that would be generated by them will be voided.

A <Color id="dark_green"><ItemLink id="heisei_dream"/></Color> can be used to manipulate a mob's <Color id="red">anger</Color>, making it especially useful for automating this Shulker <Color id="aqua">Mana</Color>-generating process.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Complex Generating Flora</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="rafflowsia" />
  ### <Color id="dark_green">Rafflowsia</Color>
</Row>

Similar to a <Color id="dark_green"><ItemLink id="kekimurus"/></Color>, this flower also eats blocks placed in its vicinity; however, it does not eat <Color id="gold">Cake</Color>, it will instead eat any flower that can be crafted at a <Color id="dark_green"><ItemLink id="apothecary_default"/></Color>.

Similarly to a <Color id="dark_green"><ItemLink id="gourmaryllis"/></Color>, it requires a varied menu of flowers to avoid diminishing returns. This flower is capable of generating ludicrous amounts of <Color id="aqua">Mana</Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="dandelifeon" />
  ### <Color id="dark_green">Dandelifeon</Color>
</Row>

The <Color id="dark_green"><ItemLink id="dandelifeon"/></Color> is not recommended for the faint of heart. While it's likely the most efficient generating flower in the botanist's toolbox, it's also one of the least straightforward to use.

This flower's function is based on a cellular "minigame" known as Conway's Game of Life. The area for this game is a 25x25 square, centred on the flower itself, and it steps the "minigame" twice a second for as long as it has a <Color id="dark_red">redstone signal</Color> applied directly to it.

Each location within that area counts as a Cell, alive if its block is a <Color id="dark_green"><ItemLink id="cell_block"/></Color>, or dead if it's anything else. The Neighbors of a cell are the eight blocks surrounding it.

Every step, the following happens to each cell simultaneously: any live cell with exactly 2 or 3 live neighbours survives; any live cell that fails that condition dies; and any dead cell with exactly three live neighbours becomes alive.

All cells have an age, starting at zero. A surviving cell's age increases by one each step, while a newly born cell's age becomes that of its oldest neighbour plus one, capped at 100.

The 3x3 zone at the center absorbs any cell that would otherwise be born there, converting it into a frankly ludicrous amount of <Color id="aqua">Mana</Color>. The older the cell, the more Mana it yields, age-zero cells pay nothing.

Whenever a live cell is absorbed by that central zone, every other cell on the board dies. Cells within range of two or more Dandelifeons also die, though well-spaced Dandelifeons can pass cells between themselves, at the cost of some Mana lost at the boundary.

<Color id="dark_green"><ItemLink id="cell_block"/></Color>s are extremely fragile: they yield nothing when broken and can't be moved by Pistons. A Dandelifeon won't generate one on a cell that isn't air, and outside a Dandelifeon's range they hold no special properties.

The most efficient generator in the mod, and by far the hardest setup to build.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Mythic Botany Generators</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Mythic Botany adds two generating flowers, both with floating variants.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mythicbotany:wither_aconite" />
  ### <Color id="dark_green">Wither Aconite</Color>
</Row>

Consumes <Color id="dark_purple">Nether Stars</Color> dropped in its vicinity for a colossal amount of <Color id="aqua">Mana</Color>. If it cannot get through a star within <Color id="yellow">five minutes</Color>, the star despawns like any other item, so do not bury it in a pile of them.

Once it starts consuming a <Color id="dark_purple">Nether Star</Color>, the item itself turns into a faded Nether Star with a specific <Color id="yellow">durability bar</Color>; that bar is what gets slowly consumed as this flower generates <Color id="aqua">Mana</Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mythicbotany:raindeletia" />
  ### <Color id="dark_green">Raindeletia</Color>
</Row>

Produces <Color id="aqua">Mana</Color> when it's raining, and even more <Color id="aqua">Mana</Color> when it's thundering.

Planting it on <Color id="green"><ItemLink id="vivid_grass"/></Color> or <Color id="gold"><ItemLink id="enchanted_soil"/></Color> makes it generate much more. On regular soil, it's too weak to generate any <Color id="aqua">Mana</Color> during normal rain.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mythicbotany:mana_collector" />
  ### <Color id="dark_green">Mana Collector</Color>
</Row>

At some point in your progression as a botanist, your flowers will create <Color id="aqua">Mana</Color> so fast that Spreaders aren't enough to handle it.

With a <Color id="dark_green"><ItemLink id="mythicbotany:mana_collector"/></Color>, you can feed that <Color id="aqua">Mana</Color> directly into a Spark network instead. It acts as a small buffer that receives from flowers and talks to Sparks, so you'll most likely need a <Color id="dark_green"><ItemLink id="spark_upgrade_recessive"/></Color> on it to push the Mana onward.

<ItemImage id="minecraft:air" scale="0.25"/>
