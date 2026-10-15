---
navigation:
  title: Variables & Logic
  icon: integrateddynamics:variable
  parent: index.md
  position: 3
item_ids:
  - integrateddynamics:variable
  - integrateddynamics:variablestore
  - integrateddynamics:logic_programmer
  - integrateddynamics:labeller
---
# <Color id="aqua">Variables & Logic</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="aqua">Variables & Logic</Color>
  <ItemImage id="variable" scale="2" />

  Variable Cards are the foundation of Integrated Dynamics logic. They carry references to values that can be read, combined, and/or evaluated across any network.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Variable Cards</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="variable" scale="1" />
  ### <Color id="aqua">Variable Card</Color>
</Row>

A variable contains a readable Value from your minecraft world, which is often associated with a specific Variable Type (see below). Variables can either be **static** or **dynamic**.

Static variables are defined once and never change, like setting an **integer** of 64 to match a minecraft item stack.

Dynamic variables are values that change, like the time of day or the amount of items in a player's inventory.

Each Variable Card has a unique ID for debugging purposes. Use a <ItemLink id="labeller" /> to give your variables readable names so you can keep track of what each one does.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Logic Programmer</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="logic_programmer" scale="1" />
  ### <Color id="aqua">Logic Programmer</Color>
</Row>

The Logic Programmer allows you to create your own variable cards instead of using a Reader by applying an Operator on one or more Variable Cards to produce a new Variable Card.

For example, you can compare the amount of items in a stack to always keep 8 coal stocked as fuel inside a furnace.

The Programmer contains an absurdly large collection of Operators and also allows creating static Variable Cards for all Value Types, though you will most likely use less than 5% of these for day-to-day minecraft automation.

The Logic Programmer exists in both block and item form and you can freely convert between them via the crafting grid.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Variable Store</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="variablestore" scale="1" />
  ### <Color id="aqua">Variable Store</Color>
</Row>

Some dynamic variables are evaluated based on other variables, and access to those referenced variables must be possible within the same network. For example, a dynamic variable representing the addition of two variables must be able to access those other variables when evaluated.

Place your referenced Variable Cards into a Variable Store that is connected to the same network as where the dynamic variable is being evaluated. This ensures all dependencies can be resolved at evaluation time.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Value Types</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

If you're familiar with programming you'll recognize some of the variable types supported by Integrated Dynamics, but some of these are exclusive minecraft:

- **Boolean** — True or False
- **Integer** — Whole numbers, ranging from -2 billion to 2 billion
- **Double** — Decimal numbers for precise measurements
- **Long** — Larger integers that become essentially infinite; for Integer is not enough
- **String** — Text values
- **List** — A collection of values sharing the same type (usually Strings or Integers)
- **Operator** — A reference to an operator (supports currying for partial application)
- **NBT** — Complex data tags for advanced data handling (reads things like mana inside a botania flower or blood inside Blood Magic's Altar)
- **Block, Item, Entity, Fluid** — References to Minecraft objects
- **Ingredients, Recipe** — Crafting-related data

All of these can be created as static values in the Logic Programmer, or read dynamically from the world using Readers.
