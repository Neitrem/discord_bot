from typing import *


class ITEM:
    """for any object that can be stored in the inventory"""

    def __init__(self, id_: int, type_: str, rarity: str, amount: int, is_stackable: bool, lvl: int):
        self.id_ = id_
        "uniq number of this type of items"
        self.type_ = type_
        "full line of current type (item.tool.sword.common_sword)"
        self.rarity = rarity
        "the rarity of the item (common, non-common, rare, super, legendary)"
        self.amount = amount
        "current amount of this items in the inventory (1, 3, 22 ...)"
        self.is_stackable = is_stackable
        "flag for recognize non-stackable item (True, False)"
        self.lvl = lvl
        "the lvl of this item (1 ,5 , 55, ...)"

    def get_string(self) -> dict:
        """Returns all variables dict for this item"""
        return self.__dict__

    def GetName(self) -> str:
        """Returns name of this item"""
        return self.type_.split('.')[1]


class FOOD(ITEM):
    """for any food item"""

    def __init__(self, id_: int, type_: str, rarity: str, amount: int, is_stackable: bool, lvl: int,
                 amount_hp_reg: int, effect: list[dict] = None):
        ITEM.__init__(self, id_, type_, rarity, amount, is_stackable, lvl)
        self.amount_hp_reg = amount_hp_reg
        "the amount of hp that will be healed after using this item (1, 3, 3.5, 20 ...)"
        self.effect = effect
        "any boosts or debuffs that will be gained after using this item (increase.speed:10, decrease.intelligence:10 )"


class POTION(ITEM):
    """for any potion"""

    def __init__(self, id_: int, type_: str, rarity: str, amount: int, is_stackable: bool, lvl: int,
                 ban_use_time: int, toxin_lvl: int, effect: list[dict]):
        ITEM.__init__(self, id_, type_, rarity, amount, is_stackable, lvl)
        self.ban_use_time = ban_use_time
        "the timeout of using potion of one type (heal:20, power:10 ....)"
        self.toxin_lvl = toxin_lvl
        "the level of intoxication u will gain after using this potion (5, 10 ,40)"
        self.effect = effect
        "some extra effects of potion (power:2, speed:4 ...)"


class EQUIPMENT(ITEM):
    """for anything that can be equip"""

    def __init__(self, id_: int, type_: str, rarity: str, amount: int, is_stackable: bool,
                 lvl: int, is_breakable: bool, durability: int, max_durability: int,
                 enchant: list[dict] = None, bonuses: list[dict] = None):
        ITEM.__init__(self, id_, type_, rarity, amount, is_stackable, lvl)
        self.is_breakable = is_breakable
        "flag for recognize non_breakable item (True, False)"
        self.durability = durability
        "the current durability of item (189, 765, 23456 ...)"
        self.max_durability = max_durability
        "the max durability of item (200, 1000, 50000 ...)"
        self.bonuses = bonuses
        "bonuses that item gained after craft ({speed:2, slow:3}, {...} ...)"
        self.enchant = enchant
        "the enchants gained by enchanting by wizard or blacksmith"


class TOOL(EQUIPMENT):
    """for any tools like axe, pickaxe, sword, bowl and etc."""

    def __init__(self, id_: int, type_: str, rarity: str, amount: int, is_stackable: bool, lvl: int, is_breakable: bool,
                 durability: int, max_durability: int, damage: int, damage_type: str, damage_distance: str,
                 enchant: list[dict] = None, bonuses: list[dict] = None):
        EQUIPMENT.__init__(self, id_, type_, rarity, amount, is_stackable, lvl,
                           is_breakable, durability, max_durability, enchant, bonuses)
        self.damage = damage  # damage that item deals by one hit (2, 15 ,105 ...)
        self.damage_type = damage_type  # the damage type that this item deals (slash, crush, ...)
        self.damage_distance = damage_distance  # the distance when it can be used (short, medium, long)


class CLOTHES(EQUIPMENT):
    """for any type of armour and non-armour clothes"""

    def __init__(self, id_: int, type_: str, rarity: str, amount: int, is_stackable: bool, lvl: int, is_breakable: bool,
                 durability: int, max_durability: int, resist: int, body_part: str, resist_list: list[dict] = None,
                 enchant: list[dict] = None, bonuses: list[dict] = None):
        EQUIPMENT.__init__(self, id_, type_, rarity, amount, is_stackable, lvl, is_breakable, durability,
                           max_durability, enchant, bonuses)
        self.resist = resist
        self.body_part = body_part
        "the damage that will be ignored (1, 13, 100)"
        self.resist_list = resist_list
        "list of damage types that will be ignored more or lesser ({slash:2, crush:-3}, {...}, ...)"


class ENTITY:
    """for any living and deadly characters"""

    def __init__(self, hp: int, max_hp: int, lvl: int, type_: str, base_armour: int, stats: dict):
        self.hp = hp
        """the health point of this character (7, 45, 145, ...)"""
        self.max_hp = max_hp
        """max amount of hp (10, 100, 1000, ...)"""
        self.lvl = lvl
        """the current lvl (1, 5, 15, ...)"""
        self.type_ = type_
        """string variable that contains info about type of this character(wolf, villager, player, etc...)"""
        self.base_armour = base_armour
        """the base armour that character have without any shields and so-on (0, 1, 2 , 23, ...)"""
        self.stats = stats
        """the dictionary that contains all characteristics of character (strength, speed, etc) as integer"""


class HUMAN(ENTITY):
    """u can use it for every entities that has body like human and also have some intelligence)"""

    def __init__(self, hp: int, max_hp: int, lvl: int, type_: str, base_armour: int, stats: dict, name: str,
                 clothes: dict, tool: TOOL, coins: int):
        ENTITY.__init__(self, hp, max_hp, lvl, type_, base_armour, stats)
        self.name = name
        """the name or nickname of this character (Nikol, Neitrem, etc)"""
        self.clothes = clothes
        """the list of clothes that is on this character ({{name:t-short, ...}, {...}, ...}, {...})"""
        self.tool = tool
        """the tool that equipped now ({name: sword, damage: 12, ...})"""
        self.coins = coins
        """the money that character have with it (12, 34, 109089, ...)"""


class PLAYER(HUMAN):
    """use it only for players characters"""

    def __init__(self, hp: int, max_hp: int, lvl: int, type_: str, base_armour: int, stats: dict, name: str, coins: int,
                 inventory: list[Union[FOOD, POTION, CLOTHES, TOOL]], exp: int, clothes: dict, cur_loc: str,
                 visited_locs: dict, tool: Optional[TOOL] = None, death_debuffs: list[dict] = None,
                 professions: list[dict] = None):
        HUMAN.__init__(self, hp, max_hp, lvl, type_, base_armour, stats, name, clothes, tool, coins)
        self.inventory = inventory
        """the list of class objects [ITEM] that player has now ([class obj Apple, class obj, Potion, etc])"""
        self.exp = exp
        """the current amount of lvl points (123 ,450, ...)"""
        self.death_debuffs = death_debuffs
        """the debuffs that u got after death ({slow:3, weakness:4, ...}, {...}, ...)"""
        self.professions = professions
        """list of this player profession and its lvl ({{name: Gardener, ...}, {...}, ...}, {...})"""
        self.cur_loc = cur_loc
        """keeps the current player location"""
        self.visited_locs = visited_locs
        """dict with visited locs and visiting time for each loc"""

    def CreateCharacterInfoMessage(self) -> str:
        """Returns message with character main info formatted for discord"""
        res_str = f"```LVL: {self.lvl}```" \
                  f"```EXP: {self.exp} / {1000 + (100 * (1.1 ** self.lvl) * self.lvl)}```" \
                  f"```HP:  {self.hp} / {self.max_hp}```" \
                  f"```Tool: " + f"{self.tool.GetName() if self.tool is not None else 'Empty'}```" \
				  f"```Clothes:\n" \
				  f"--Head:  {self.clothes['head'].GetName() if self.clothes['head'] is not None else 'Empty'}\n" \
				  f"--Chest: {self.clothes['body'].GetName() if self.clothes['body'] is not None else 'Empty'}\n" \
				  f"--Legs:  {self.clothes['legs'].GetName() if self.clothes['legs'] is not None else 'Empty'}\n```"
        return res_str

    def CreateInventoryListMessage(self, page=1) -> str:
        """Returns message with list of ITEMs from inventory formatted for discord"""
        item_count = 0
        if len(self.inventory) <= (page - 1) * 10:
            return 'No more item!'
        res_str = ''
        for item in self.inventory:
            item_count += 1
            if item_count > (page - 1) * 10:
                res_str += "`[{count:-4}]` {name:10}  {0.lvl} lvl\n".format(item, count=item_count, name=item.GetName())
            if item_count == page * 10:
                break
        return res_str


class MOB(ENTITY):
    def __init__(self, hp: int, max_hp: int, lvl: int, type_: str, base_armour: int, stats: dict, damage_type: str,
                 resist_list: list[dict]):
        ENTITY.__init__(self, hp, max_hp, lvl, type_, base_armour, stats)
        self.damage_type = damage_type
        """the damage type that this mob deal (slash, crush, ...)"""
        self.resist_list = resist_list
        """list of damage types that will be ignored more or lesser ({slash:2, crush:-3}, {...}, ...)"""


class ANIMAL(MOB):
    """use it for any animals"""

    def __init__(self, hp: int, max_hp: int, lvl: int, type_: str, base_armour: int, stats: dict, damage_type: str,
                 resist_list: list[dict], agro: bool):
        MOB.__init__(self, hp, max_hp, lvl, type_, base_armour, stats, damage_type, resist_list)
        self.agro = agro
        """the flag for recognize aggressive or not animals"""


class MONSTER(MOB):
    """use it for always aggressive creatures and some other strange things"""

    def __init__(self, hp: int, max_hp: int, lvl: int, type_: str, base_armour: int, stats: dict, damage_type: str,
                 resist_list: list[dict]):
        MOB.__init__(self, hp, max_hp, lvl, type_, base_armour, stats, damage_type, resist_list)
