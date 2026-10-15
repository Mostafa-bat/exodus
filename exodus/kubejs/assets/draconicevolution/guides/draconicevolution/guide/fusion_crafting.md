---
navigation:
  title: Fusion Crafting
  icon: draconicevolution:crafting_core
  parent: index.md
  position: 2
item_ids:
  - draconicevolution:crafting_core
  - draconicevolution:basic_crafting_injector
  - draconicevolution:wyvern_crafting_injector
  - draconicevolution:awakened_crafting_injector
  - draconicevolution:chaotic_crafting_injector
---
# <Color id="red">Fusion Crafting</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Fusion Crafting</Color>
  <ItemImage id="crafting_core" scale="2" />

  Fusion Crafting is Draconic Evolution's advanced crafting system. It uses a central Crafting Core surrounded by Crafting Injectors to fuse ingredients together into powerful items, consuming large amounts of energy in the process.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fusion Crafting Core</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="crafting_core" />
  ### <Color id="aqua">Crafting Core</Color>
</Row>

The Fusion Crafting Core is the central block of the Fusion Crafting system. Place it down and surround it with Fusion Crafting Injectors. The core holds the primary input item, and injectors hold the supporting ingredients. The system requires large amounts of energy to operate.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Fusion Crafting Injectors</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Injectors come in four tiers matching the mod's tier system:

- <ItemLink id="basic_crafting_injector" /> - Draconium (Basic) tier, used for Wyvern tier recipes
- <ItemLink id="wyvern_crafting_injector" /> - Wyvern tier, used for Draconic tier recipes
- <ItemLink id="awakened_crafting_injector" /> - Draconic (Awakened) tier, used for Chaotic tier recipes
- <ItemLink id="chaotic_crafting_injector" /> - Chaotic tier, used for the highest tier recipes

Each injector holds one ingredient. Injectors must sit in a straight line out from the Core on one of the six faces, facing inward, and cannot be directly against it. A recipe's tier sets the <Color id="aqua">minimum</Color> injector tier, so a higher tier injector always works in place of a lower one.

<Color id="light_purple">Pack change:</Color> you cannot swap an item straight into a loaded injector. Right-clicking an occupied injector while holding an item does nothing. <Color id="aqua">Sneak right-click</Color> to pull the contents back out first, then insert the new ingredient. The base mod allowed the swap and duplicated items when you did it mid-craft.


<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Crafting Process</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

1. Place the primary item in the Fusion Crafting Core
2. Place supporting ingredients in the surrounding Injectors
3. Supply energy to the Core (it will show "Ready to craft" when valid)
4. Click Craft - the system will charge, then perform the fusion
5. The output item appears in the Core

The energy cost varies per recipe and is shown in the GUI. JEI shows all Fusion Crafting recipes.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Pack Recipes in the Core</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Architect's Exodus routes a number of recipes from other mods through the Fusion Crafting Core, so the Core is worth building even if you never touch a piece of Draconic gear.

| Result | Injectors | Energy | Notes |
|---|---|---|---|
| <ItemLink id="ftb:aesirium" /> | <Color id="light_purple">Draconic</Color> | 1,000,000,000 FE | The only recipe there is |
| <ItemLink id="mysticalagriculture:awakened_supremium_block" /> | <Color id="aqua">Wyvern</Color> | 50,000,000 FE | Replaces the Awakening Altar recipe, which is removed |
| <ItemLink id="ftb:primordial_dragons_blood" /> | <Color id="aqua">Wyvern</Color> | 2,000,000 FE | Second route alongside the Runic Altar recipe |
| Botania and MythicBotany runes | <Color id="aqua">Wyvern</Color> | 1,000,000 FE each | Elemental, Seasonal, Sin and Realm runes, catalyst is Livingrock |

<ItemImage id="minecraft:air" scale="0.25"/>

<Color id="red">Aesirium is the one that matters.</Color> It is the altar item for the <Color id="gold">Nidhoggr</Color> summoning ritual, and Fusion Crafting is the only way to make it. Finishing the main storyline therefore means a Fusion setup with <Color id="light_purple">Draconic Injectors</Color> and a power supply that can put a billion FE through it. Plan your Energy Core around that.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Building the Structure</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Injectors go on any of the six faces of the Core, three blocks out, all facing inward. You do not need one on every face, only enough to hold the recipe's ingredients.

The scenes below show the Core on its own and then a valid six-injector setup.

<ItemImage id="minecraft:air" scale="0.25"/>

<GameScene zoom="2" background="#333333" interactive={true}>
  <ImportStructure src="assets/crafting_core.nbt"/>
</GameScene>

<GameScene zoom="2" interactive={true}>
  <ImportStructure src="assets/crafting_core_valid_setup.nbt"/>
</GameScene>
