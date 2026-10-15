---
navigation:
  title: Wissen System
  icon: wizards_reborn:wissen_altar
  parent: index.md
  position: 2
item_ids:
  - wizards_reborn:wissen_altar
  - wizards_reborn:wissen_wand
  - wizards_reborn:wissen_translator
  - wizards_reborn:wissen_cell
  - wizards_reborn:arcanum
  - wizards_reborn:arcanum_dust
---

# <Color id="dark_purple">Wissen System</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_purple">Wissen System</Color>

  <ItemImage id="wissen_altar" scale="2" />

  Wissen is the energy that powers all Wizard's Reborn machines and processes. Generate it from Arcanum and transport it to where it is needed.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Wissen Generation</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="wissen_altar" />
  ### <Color id="aqua">Wissen Altar</Color>
</Row>

The Wissen Altar releases Wissen from Arcanum. Drop the material in and it is consumed over time:

| Input | Wissen released |
|-------|-----------------|
| <ItemLink id="arcanum" /> | 1,000 |
| <ItemLink id="arcanum_dust" /> | 200 |

The altar will also charge Wissen directly into items placed on it, which is the simplest way to fill a wand or an accessory before you have a network running.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Wissen Tools</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="wissen_wand" />
  ### <Color id="aqua">Wissen Wand</Color>
</Row>

The Wissen Wand is the configuration tool for every mechanism in the mod. <Color id="aqua">Sneak + Right Click</Color> in the air to cycle through its five modes, which always come round in this order:

| Mode | What it does |
|------|--------------|
| <Color id="aqua">Functional</Color> | Activates the targeted mechanism. This is how you start a ritual or trigger a machine by hand. |
| <Color id="aqua">Receive Connect</Color> | Links a Wissen Translator so it <Color id="green">pulls</Color> Wissen from a mechanism. |
| <Color id="aqua">Send Connect</Color> | Links a Wissen Translator so it <Color id="green">pushes</Color> Wissen to a mechanism. |
| <Color id="aqua">Reload</Color> | Resets a mechanism's settings. It also unclogs Fluid and Steam Pipes, and stops a running ritual. |
| <Color id="aqua">Off</Color> | Does nothing at all. It is a parking mode so you cannot misclick a live one. |

<Color id="yellow">Connecting things:</Color> in both connect modes you always click the <Color id="aqua">mechanism first</Color> and the <Color id="aqua">Translator second</Color>. The mode you are in decides which way the Wissen flows, not the order you click in.

Holding the wand and pressing the <Color id="aqua">Selection Menu</Color> key opens an extra menu for mechanisms that have one.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Wissen Transport & Storage</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="wissen_translator" />
  ### <Color id="aqua">Wissen Translator</Color>
</Row>

Wissen Translators are what turn a pile of machines into a network. Each one carries Wissen from a source to a destination and holds exactly <Color id="red">one input and one output</Color> connection, so longer runs mean chaining several translators together. Use the <ItemLink id="wissen_wand" /> to set them up.

Giving a Translator a redstone signal stops it working, which is a convenient way to gate part of your network.


<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="wissen_cell" />
  ### <Color id="aqua">Wissen Cell</Color>
</Row>

The Wissen Cell buffers Wissen between your altar and your machines, and charges items placed on it.

Unlike every other mechanism in the mod, a Wissen Cell <Color id="green">keeps its stored Wissen when you break it</Color>, which makes it the only practical way to carry Wissen from one place to another.
