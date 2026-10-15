---
navigation:
  title: Devices
  icon: botania:hourglass
  parent: index.md
  position: 5
item_ids:
  - botania:hourglass
  - botania:enchanter
  - mythicbotany:mana_infuser
  - mythicbotany:mana_collector
  - botania:turntable
  - botania:alchemy_catalyst
  - botania:conjuration_catalyst
  - botania:brewery
  - botania:terra_plate
  - botania:runic_altar
  - botania:open_crate
  - botania:crafty_crate
  - botania:drum_wild
  - botania:abstruse_platform
  - botania:spectral_platform
  - botania:red_string_container
  - botania:red_string_dispenser
  - botania:red_string_relay
  - botania:animated_torch
  - botania:fel_pumpkin
  - botania:cocoon
  - botania:incense_plate
  - botania:avatar
---
# <Color id="green">Devices</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="green">Devices</Color>
  <ItemImage id="hourglass" scale="2" />
  Botania offers a wide range of utility devices powered by Mana. From crafting stations to automation tools, these blocks form the backbone of any Botania setup.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Crafting & Infusion</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="runic_altar" />
  ### <Color id="aqua">Runic Altar</Color>
</Row>

Crafts Runes. Toss or right-click the recipe ingredients onto the altar, then point a Mana Spreader at it and let the Mana flow. Once the altar has taken enough Mana, drop a Livingrock on top and use a Wand of the Forest to collect the Rune. Any Runes used as ingredients act as catalysts and are returned to you.

Mythic Botany adds the nine realm Runes to this altar, so Runes of Asgard, Alfheim, Helheim and the rest are all made here rather than at the Mana Infuser.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="brewery" />
  ### <Color id="aqua">Botanical Brewery</Color>
</Row>

Brews Botania potions using Mana. Add a Managlass Vial or Alfglass Flask by right-clicking or tossing it in, add the reagents the same way, then point a Mana Spreader at the Brewery. The finished Brew drops out on its own. Each container holds several doses, and partly used ones can be topped up with another of the same Brew.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="terra_plate" />
  ### <Color id="aqua">Terrestrial Agglomeration Plate</Color>
</Row>

Converts resources into Terrasteel using enormous amounts of Mana. The plate sits on a 3x3 checkerboard of Lapis Lazuli Blocks and Livingrock (Shimmerrock also works). Feed it Mana, with a Spark being by far the fastest way, then toss one Manasteel Ingot, one Mana Diamond and one Mana Pearl onto the plate to begin.

A single Terrasteel costs roughly half a Mana Pool. Picking any of the three items back up cancels the infusion and every point of Mana already transferred is lost.

<GameScene zoom="3" background="#222222" interactive={true}>
  <ImportStructure src="assets/terra_plate.nbt" />
</GameScene>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="enchanter" />
  ### <Color id="aqua">Mana Enchanter</Color>
</Row>

Enchants items using Mana instead of XP, and does not consume the books. It is a large multiblock, roughly 11x7, built from 17 Obsidian, 10 Mystical Flowers of any colour (Glimmering and Floating variants count), 6 Mana Pylons and a single Lapis Lazuli Block at the core.

Right-click the core with a Wand of the Forest to activate it. Place the item to be enchanted into the enchanter and drop Enchanted Books inside the obsidian circle, then right-click with the wand again to start. Feed Mana with bursts or, much faster, a Spark hovering over the core. Only the first enchantment on each book is read, and pre-enchanted items cannot be used.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mythicbotany:mana_infuser" />
  ### <Color id="aqua">Mana Infuser</Color>
</Row>

Mythic Botany's upgraded Terrestrial Agglomeration Plate. Like the plate it needs a platform underneath, but a different one: a 3x3 of Shimmerrock at the four corners and the centre, with Gold Blocks on the four edges. The Infuser itself sits on top of the centre.

Toss the ingredients onto the Infuser and feed it Mana the same way you would a Terra Plate. It makes everything the plate does plus Gaiasteel, Overgrowth Seed and Alfsteel.

<GameScene zoom="3" background="#222222" interactive={true}>
  <ImportStructure src="assets/alfheim_plate.nbt" />
</GameScene>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="mythicbotany:mana_collector" />
  ### <Color id="aqua">Mana Collector</Color>
</Row>

A compact 10,000 Mana buffer for when your generating flowers produce faster than a Spreader can carry it away. Flowers can feed it directly and a Spark can attach to it, which puts their output straight onto a Spark network without needing a Mana Pool. You will normally want a Recessive Spark Augment on it to move the Mana onward. Point a Wand of the Forest at it to read how full it is.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Catalysts</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="alchemy_catalyst" />
  ### <Color id="aqua">Alchemy Catalyst</Color>
</Row>

Attach it to the underside of a Mana Pool to enable Alchemy recipes. Toss the input item into the pool above it to transform it into something else.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="conjuration_catalyst" />
  ### <Color id="aqua">Conjuration Catalyst</Color>
</Row>

Attach it to the underside of a Mana Pool to enable Conjuration recipes, which duplicate simple resources such as Redstone, Glowstone, Quartz and Coal at the cost of Mana.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Automation & Utility</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="hourglass" />
  ### <Color id="aqua">Hovering Hourglass</Color>
</Row>

A precise redstone timer. Right-click to add up to a stack of Sand, Red Sand or Soul Sand. When the sand finishes draining it emits a redstone pulse and flips over. One block of Sand takes a second, Red Sand ten seconds and Soul Sand a full minute, so the sand type and stack size set the interval.

Filling it with Mana Powder instead turns it from a timer into a counter: it drops one unit of powder per Mana Burst that hits it, and pulses when the powder runs out.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="open_crate" />
  ### <Color id="aqua">Open Crate</Color>
</Row>

Takes items from a Hopper or other inserter and drops them straight down through its open bottom. Give it a redstone signal and the items it drops will resist pickup by Hopperhocks, Rannuncarpuses and Pollidisiacs for about ten extra seconds.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="crafty_crate" />
  ### <Color id="aqua">Crafty Crate</Color>
</Row>

A 3x3 crafting grid in block form. Its nine slots fill left to right, top to bottom, and a Crafting Placeholder stands in for a gap so recipes like pickaxes and chests still work. Filling all nine slots crafts and ejects the result automatically, or you can right-click with a Wand of the Forest to force an attempt. Patterns can be applied to lock specific slots.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="animated_torch" />
  ### <Color id="aqua">Animated Torch</Color>
</Row>

A redstone torch that points in one horizontal direction and only powers that side. It turns whenever it is actuated by a Mana Burst or an adjacent Hovering Hourglass. By default it flips 180 degrees, acting as a T flip-flop; a Wand of the Forest switches it to Rotate or Random mode.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Platforms & Red String</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="abstruse_platform" />
  ### <Color id="aqua">Abstruse Platform</Color>
</Row>

Solid only to entities standing on top of it that are not sneaking. Sneak, or approach from below, and you pass straight through. Mana Bursts travel through it freely. Right-click it with any simple block to disguise it, or apply Phantom Ink to make it fully invisible.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="spectral_platform" />
  ### <Color id="aqua">Spectral Platform</Color>
</Row>

An Abstruse Platform with no physical body at all. Everything passes through it from every direction, regardless of sneaking.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="red_string_container" />
  ### <Color id="aqua">Red String Blocks</Color>
</Row>

Each Red Stringed block binds to a compatible block up to eight blocks away in the direction it faces. The Container proxies inventories and preserves sidedness, the Dispenser fires a bound Dispenser or Dropper on a redstone signal, the Nutrifier passes Bone Meal along, the Comparator repeats a bound block's comparator reading, the Spoofer makes a bound flower behave as the one placed on top of it, and the Interceptor emits a pulse whenever its bound block is right-clicked. Red Stringed blocks cannot be chained.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Summoning & Misc</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="fel_pumpkin" />
  ### <Color id="aqua">Fel Pumpkin</Color>
</Row>

Place it on top of two Iron Bars, the same way you would build a Snow Golem, to spawn a Blaze. Blazes made this way are fragile and drop Blaze Powder instead of a Blaze Rod.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="cocoon" />
  ### <Color id="aqua">Cocoon of Caprice</Color>
</Row>

Slowly hatches into a baby animal, usually a farm animal but occasionally something rarer such as a Wolf or Horse. A cocoon near water produces aquatic animals instead, and feeding it an Emerald, a Chorus Fruit or a Gaia Spirit steers the result somewhere stranger.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="incense_plate" />
  ### <Color id="aqua">Incense Plate</Color>
</Row>

Right-click the plate with an Incense Stick to load it, then light it with Flint and Steel. While it burns it grants the Brew infused into the stick to every player within 30 blocks, and a stick lasts sixty times as long as the same Brew drunk from a Vial. A lit stick cannot be taken back. Single-effect Brews only.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="avatar" />
  ### <Color id="aqua">Livingwood Avatar</Color>
</Row>

Give it a Botania Rod and it will use that rod for you, drawing Mana from a Spreader pointed at it. Not every rod is supported. A redstone signal stops it casting.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="turntable" />
  ### <Color id="aqua">Spreader Turntable</Color>
</Row>

Continuously rotates a Mana Spreader placed on top of it, which is how you sweep a burst across multiple targets. A redstone signal pauses the spin. Right-click with a Wand of the Forest to change speed, sneak-right-click to reverse direction.
