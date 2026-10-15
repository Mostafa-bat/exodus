---
navigation:
  title: Living Armor
  icon: bloodmagic:livinghelmet
  parent: index.md
  position: 8
item_ids:
  - bloodmagic:livinghelmet
  - bloodmagic:livingplate
  - bloodmagic:livingleggings
  - bloodmagic:livingboots
  - bloodmagic:upgradetrainer
  - bloodmagic:reagentbinding
  - bloodmagic:arcaneashes
  - bloodmagic:upgradetome
---
# <Color id="red">Living Armor</Color>

<Column alignItems="center" fullWidth={true}>
  # <Color id="red">Living Armor</Color>
  <ItemImage id="bloodmagic:livinghelmet" scale="2" />
  Living Armor <Color id="light_purple">trains itself as you use it</Color>. It starts out no better than iron, but everything you do while wearing it teaches it something, and a well-trained set eventually outclasses anything you can enchant.
</Column>

<ItemImage id="minecraft:air" scale="0.25" />

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">Crafting Living Armor</Color>
</Column>

You need <Color id="aqua">Iron armour</Color>, <ItemLink id="bloodmagic:arcaneashes" />, and <ItemLink id="bloodmagic:reagentbinding" /> for each piece. Binding Reagent is made in the Alchemy Table and costs enough Demon Will that you will want a <Color id="green">Common Tartaric Gem</Color> before you start.

Draw an Alchemy Array with the ashes, apply the Binding Reagent, then drop in an Iron Helmet, Chestplate, Leggings or Boots and stand back.

<ItemImage id="minecraft:air" scale="0.05" />

### <Color id="aqua">Full Set</Color>

<ItemGrid>
  <ItemIcon id="bloodmagic:livinghelmet" />
  <ItemIcon id="bloodmagic:livingplate" />
  <ItemIcon id="bloodmagic:livingleggings" />
  <ItemIcon id="bloodmagic:livingboots" />
</ItemGrid>

<ItemImage id="minecraft:air" scale="0.25" />

The finished armour has <Color id="green">Diamond-level durability</Color> but only <Color id="yellow">Iron-level protection</Color> until it starts levelling up. Repair it in an anvil with more Binding Reagent. Hold sneak and look at a piece to see what it has learned so far.

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">Upgrade System</Color>
</Column>

The armour has <Color id="red">100 upgrade points</Color> to spend, and each upgrade level costs points. You cannot have everything, which is the whole design. Most players end up with several specialised sets rather than one do-everything set.

Upgrades train themselves by watching what you do:

| Upgrade | Trained by | Max | Effect |
|---------|-----------|-----|--------|
| Quick Feet | Running around | 10 | Up to +150% movement speed |
| Fierce Strike | Melee attacks | 10 | Extra melee damage |
| Dwarven Might | Mining | 10 | Faster mining on repeated blocks, later a Haste buff after breaking one |
| Healthy | Healing, including potions | 10 | Up to 25 extra hearts |
| Tough | Taking non-projectile damage | 10 | Reduces non-projectile harm |
| Pin Cushion | Being shot | 10 | Reduces arrow damage |
| Experienced | Collecting XP | 10 | Up to +150% XP from kills |
| Strong Legs | Jumping | 10 | Up to +7.5 blocks jump height and 83% fall resistance. Hold sneak to jump normally. |
| Tough Palms | Self-sacrifice with the knife | 10 | Up to +150% LP from self-sacrifice |
| Body Builder | Eating | 5 | Up to 100% knockback resistance and 5 extra hearts |
| Soft Fall | Taking fall damage | 5 | Up to complete fall immunity |
| Gift of Ignis | Being on fire | 5 | Fire Resistance, longer and faster recharging with level |
| Poison Resistance | Being poisoned | 5 | Cures Poison on a cooldown |
| Charging Strike | Hitting things while sprinting | 5 | Up to +50% sprint attack damage and knockback |
| Repair | Repairing your chestplate | 1 | Repairs a random worn piece every 5 seconds |
| Gilded | Handing a Piglin a Gold Ingot | 1 | Piglins ignore you as if you wore gold |

A few cannot be trained at all and have to be crafted as <ItemLink id="bloodmagic:upgradetome" />:

* <Color id="aqua">Brilliance</Color> improves armour and toughness, one level per tome, up to 5.
* <Color id="aqua">Elytra</Color> adds an Elytra to the chestplate, draining durability at half the normal rate.
* <Color id="aqua">Socketed</Color> adds Living Armour Socket curio slots, one per tome.

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">Downgrades</Color>
</Column>

The armour can also pick up <Color id="red">downgrades</Color>, deliberately applied through the <Color id="light_purple">Penance of the Leadened Soul</Color> ritual. Accepting a drawback buys you upgrade points to spend elsewhere, so this is how you get past the 100-point ceiling on a specialised set.

They are not subtle. Examples include <Color id="red">Crippled Arm</Color> (your offhand stops working entirely, no shields, no torch placing), <Color id="red">Quenched</Color> (you cannot drink potions), <Color id="red">Diseased</Color> (all healing cut by up to 80%), <Color id="red">Limp Leg</Color> (up to 70% slower), <Color id="red">Storm Trooper</Color> (bows and crossbows become wildly inaccurate), and <Color id="red">Battle Hungry</Color> (hunger if you have not attacked something recently).

Pick ones you can live with. A miner does not care about Storm Trooper.

***

<Column alignItems="center" fullWidth={true}>
## <Color id="gold">Controlling Growth</Color>
</Column>

<Row>
  <ItemImage id="bloodmagic:upgradetrainer"/>
  <Column>
    ### <Color id="aqua">Training Bracelet</Color>
  </Column>
</Row>

Right-click the <ItemLink id="bloodmagic:upgradetrainer"/> to open its menu and set a <Color id="green">level cap</Color> per upgrade, so the armour stops wasting points on skills you do not want. You need a copy of that upgrade's Tome in hand to add it to the list.

It tracks up to <Color id="green">16</Color> upgrades at once and can be set to either allow or block everything not on the list. To ban a single upgrade, add it in "allow others" mode with its cap set to 0.

Only one bracelet works at a time. It looks in this order: offhand, then Curios, then your main inventory, then add-on inventories.

<ItemImage id="minecraft:air" scale="0.25" />

### <Color id="aqua">Useful Rituals</Color>

* <Color id="light_purple">Ritual of Living Evolution</Color> raises the armour's upgrade point ceiling.
* <Color id="light_purple">Sound of the Cleansing Soul</Color> strips upgrades back out so you can respec.
* <Color id="light_purple">Penance of the Leadened Soul</Color> applies downgrades on purpose.
