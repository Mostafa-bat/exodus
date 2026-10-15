---
navigation:
  title: Arcane Iterator and Rituals
  icon: wizards_reborn:arcane_iterator
  parent: index.md
  position: 7
item_ids:
  - wizards_reborn:arcane_iterator
  - wizards_reborn:arcanum_lens
  - wizards_reborn:wisestone_plate
  - wizards_reborn:runic_pedestal
  - wizards_reborn:arcane_pedestal
  - wizards_reborn:runic_wisestone_plate
  - wizards_reborn:light_emitter
  - wizards_reborn:light_transfer_lens
  - wizards_reborn:arcacite
  - wizards_reborn:enchanted_calx
  - wizards_reborn:wissen_wand
---

# <Color id="dark_purple">Arcane Iterator and Rituals</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="dark_purple">Arcane Iterator and Rituals</Color>

  <ItemImage id="arcane_iterator" scale="2" />

  The Arcane Iterator is the gateway to ritual magic. Build it, produce its specialized components, and set up light-based ritual systems.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Arcane Iterator</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="arcane_iterator" />
  ### <Color id="aqua">Arcane Iterator</Color>
</Row>

The Arcane Iterator is the mod's top-tier crafting station. It makes ritual components, applies Arcane Enchantments, works as an alternative to the enchanting table, and produces Innocent Wood tools. Crafting it needs an Arcacite Block plus <ItemLink id="enchanted_calx" />, so the alchemy chain has to be finished first.

<Color id="yellow">Placement matters and is easy to get wrong.</Color> The Iterator is not a standalone block:

* It must sit <Color id="aqua">two blocks directly above an <ItemLink id="arcane_pedestal" /></Color>, with a one-block gap between them. That pedestal is the <Color id="aqua">main</Color> one and holds the item being worked on, or receives the result.
* Ingredient pedestals go anywhere within <Color id="aqua">5 blocks horizontally and 3 blocks vertically</Color> of the Iterator.

Iteration spends Wissen, your experience, and in some cases your health, so top up before starting an expensive one.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Iterator Products</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

The Arcane Iterator produces several key components:

<Row>
  <ItemImage id="arcanum_lens" />
  ### <Color id="aqua">Arcanum Lens</Color>
</Row>

Wissen sealed in a glass shell. It is the shared component in every light block you are about to build, appearing in the <ItemLink id="light_emitter" />, the <ItemLink id="light_transfer_lens" /> and the <ItemLink id="runic_pedestal" />, so make several.

It is also a portable battery in its own right. Break one and the Wissen inside is released into the items you are carrying.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="wisestone_plate" />
  ### <Color id="aqua">Wisestone Plate</Color>
</Row>

Flat plates of Wisestone used as ritual foundations.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="runic_wisestone_plate" />
  ### <Color id="aqua">Runic Wisestone Plate</Color>
</Row>

Created by inscribing a Crystal Ritual onto a <ItemLink id="wisestone_plate" /> at the Arcane Iterator. Each plate holds exactly one ritual, so you need a separate plate for each. There are five:

| Ritual | Effect |
|--------|--------|
| <Color id="aqua">Focusing</Color> | Fills the light ray with the crystal's power |
| <Color id="aqua">Artificial Fertility</Color> | Grows nearby plants and grass |
| <Color id="aqua">Ritual Breeding</Color> | Feeds nearby animals |
| <Color id="aqua">Crystal Growth Acceleration</Color> | Greatly speeds up a growing crystal |
| <Color id="aqua">Crystal Infusion</Color> | Combines the items on surrounding pedestals into one |

Crystal Infusion is the one that unlocks new content, including Petals of Innocence, Innocent Wood Saplings and the Arcanum Seed.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Light System</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

Rituals in Wizard's Reborn are powered by light. You need these components to direct light to the ritual's Crystal:

<Row>
  <ItemImage id="light_emitter" />
  ### <Color id="aqua">Light Emitter</Color>
</Row>

Concentrates a light ray, consuming Wissen the whole time it runs. Stops on a redstone signal.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="light_transfer_lens" />
  ### <Color id="aqua">Light Transfer Lens</Color>
</Row>

Redirects a ray around corners so it can reach a pedestal the emitter cannot see. Also stops on a redstone signal.

<Color id="yellow">Rays fade with distance</Color>, so very long lens chains will not work. Keep the emitter reasonably close to the crystal.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="runic_pedestal" />
  ### <Color id="aqua">Runic Pedestal</Color>
</Row>

The heart of a ritual. Open it to slot a <ItemLink id="runic_wisestone_plate" /> inside, then place a Crystal on top. Neither is consumed when the ritual runs.

<ItemImage id="minecraft:air" scale="0.25"/>

<Row>
  <ItemImage id="arcane_pedestal" />
  ### <Color id="aqua">Arcane Pedestal</Color>
</Row>

Holds the ingredient items a ritual consumes. For Crystal Infusion, place them <Color id="aqua">within 4 blocks</Color> of the crystal in every direction.

These are the same pedestals the Arcane Iterator uses, so they are worth keeping a stack of.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Performing Rituals</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>

To perform a ritual:

1. Craft a <ItemLink id="runic_pedestal" />, and a <ItemLink id="runic_wisestone_plate" /> with the desired ritual (such as <Color id="aqua">Crystal Infusion</Color>) crafted at the Arcane Iterator
2. Place the Runic Wisestone Plate inside the Runic Pedestal and place a Crystal on top of it
3. Redirect light to the Crystal using a <ItemLink id="light_emitter" /> and <ItemLink id="light_transfer_lens" /> as needed
4. Place the required items on <ItemLink id="arcane_pedestal" /> blocks around the Runic Pedestal
5. Start it by using the <ItemLink id="wissen_wand" /> in <Color id="aqua">Functional Mode</Color> on the Crystal

To stop a ritual, use the wand on the crystal again in <Color id="aqua">Reload Mode</Color>.

<ItemImage id="minecraft:air" scale="0.25"/>

The light ray is what drives the ritual, so it only makes progress while the beam is actually landing on the crystal. Break the beam and the ritual simply stalls until you restore it.

Only the items on the Arcane Pedestals are consumed. The plate, the pedestals and the Crystal are all reusable, and the crystal's <Color id="aqua">Resonance</Color> stat determines how powerful the ritual is, so it is worth putting a good one in.
