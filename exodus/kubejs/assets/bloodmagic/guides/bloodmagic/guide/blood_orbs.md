---
navigation:
  title: Blood Orbs
  icon: bloodmagic:weakbloodorb
  parent: index.md
  position: 2
item_ids:
  - bloodmagic:weakbloodorb
  - bloodmagic:apprenticebloodorb
  - bloodmagic:magicianbloodorb
  - bloodmagic:masterbloodorb
  - bloodmagic:archmagebloodorb
  - animus:blood_orb_transcendent
  - bloodmagic:speedrune
  - bloodmagic:orbcapacityrune
---
# <Color id="red">Blood Orbs</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Blood Orbs</Color>
  <ItemImage id="bloodmagic:weakbloodorb" scale="2" />
  Blood Orbs give you a pool of LP, called a Soul Network, which is used to power [Rituals](rituals.md) and [Sigils](sigils.md). Each tier of orb holds more LP than the last.
</Column>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Orb Comparison</Color>
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
| Orb | LP Capacity | Tier |
|-----|-------------|------|
| <ItemImage id="bloodmagic:weakbloodorb" scale="0.5" /> <Color id="red"><ItemLink id="bloodmagic:weakbloodorb" /></Color> | 5,000 | I
| <ItemImage id="bloodmagic:apprenticebloodorb" scale="0.5" /> <Color id="dark_green"><ItemLink id="bloodmagic:apprenticebloodorb" /></Color> | 25,000 | II
| <ItemImage id="bloodmagic:magicianbloodorb" scale="0.5" /> <Color id="aqua"><ItemLink id="bloodmagic:magicianbloodorb" /></Color> | 150,000 | III
| <ItemImage id="bloodmagic:masterbloodorb" scale="0.5" /> <Color id="yellow"><ItemLink id="bloodmagic:masterbloodorb" /></Color> | 1,000,000 | IV
| <ItemImage id="bloodmagic:archmagebloodorb" scale="0.5" /> <Color id="dark_purple"><ItemLink id="bloodmagic:archmagebloodorb" /></Color> | 10,000,000 | V
| <ItemImage id="animus:blood_orb_transcendent" scale="0.5" /> <Color id="light_purple"><ItemLink id="animus:blood_orb_transcendent" /></Color> | 30,000,000 | VI

The Transcendent Blood Orb comes from <Color id="dark_red">Animus</Color>. Every other orb is vanilla Blood Magic, and each one is crafted in an Altar of the matching tier.

<ItemImage id="minecraft:air" scale="0.25"/>

***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">Binding and Filling</Color>
</Column>

The first time you right-click with an orb it <Color id="green">binds</Color> to you, and from then on that orb draws from and fills your Soul Network. Anything else that binds to you, sigils included, shares the same pool.

There are two ways to put LP into it:

* **Right-click the orb.** This spends one heart of your health for <Color id="red">200 LP</Color>. Fine in a pinch, slow for real work.
* **Drop the orb in a Blood Altar.** It soaks up Life Essence as fast as the Altar can push it, which is set by your <ItemLink id="bloodmagic:speedrune" />. This is the normal way to fill a network.

<ItemImage id="minecraft:air" scale="0.25"/>

><Color id="yellow">Tip:</Color> If the highest orb still is not enough storage, <ItemLink id="bloodmagic:orbcapacityrune" /> around the Altar raises the capacity of whichever orb is sitting inside it.

><Color id="red">Careful:</Color> When something bound to you runs your network dry it will usually take the cost straight out of your health instead. A ritual that outruns your income will just leave you permanently nauseous until you shut it off or refill.
