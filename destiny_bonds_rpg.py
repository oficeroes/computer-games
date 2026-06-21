"""
╔══════════════════════════════════════════════════════════════╗
║                    命运之契 — 羁绊冒险                        ║
║                  Destiny Bonds - RPG Game                    ║
║                                                              ║
║  一款轻松幽默的回合制文字RPG。选择性别与职业，               ║
║  与同性伙伴并肩作战，在冒险中收获友情与成长。               ║
║                                                              ║
║  Editor: 2026 Python RPG Project                             ║
╚══════════════════════════════════════════════════════════════╝
"""

import random
import time
import os
import sys
import io

if sys.platform == "win32":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    except (AttributeError, OSError):
        pass

# ============================================================
# ============================================================

def slow_print(text, delay=0.03):
    """逐字打印文字，营造打字机效果"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def divider(char="═", length=50):
    """打印分隔线"""
    print(char * length)

def press_enter():
    """等待玩家按回车继续"""
    input("\n  [ 按 Enter 键继续... ]")

def clear_screen():
    """清屏 (Windows)"""
    os.system("cls" if os.name == "nt" else "clear")

def get_int_input(prompt, min_val=None, max_val=None):
    """安全获取整数输入"""
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"  !! 请输入不小于 {min_val} 的数字！")
                continue
            if max_val is not None and val > max_val:
                print(f"  !! 请输入不大于 {max_val} 的数字！")
                continue
            return val
        except ValueError:
            print("  !! 请输入有效的数字！")

# ============================================================
# ============================================================

MEMES = {
    "amazing": "绝绝子",
    "doomed": "芭比Q了",
    "thanks_sarcastic": "栓Q",
    "far_ahead": "遥遥领先",
    "too_cool": "泰裤辣",
    "whatever": "啊对对对",
    "lying_flat": "躺平",
    "giving_up": "摆烂",
    "involution": "内卷",
    "mental_state": "精神状态美丽",
    "emotionally_broken": "破防了",
    "introvert": "i人",
    "extrovert": "e人",
    "show_off": "显眼包",
    "buddy": "搭子",
    "emotional_value": "情绪价值",
    "family_who_knows": "家人们谁懂啊",
    "six": "6",
    "crushed": "被碾压了",
    "carried": "被带飞了",
    "gg": "GG",
}

def meme(key):
    """获取热梗，如果key不存在则返回原key（兼容未来替换）"""
    return MEMES.get(key, key)

# ============================================================
# ============================================================

MONSTER_ART = {
    "史莱姆": [
        ["     ___   ", "    / o \\  ", "   |_____| ", "   \\_____/ "],
        ["       ___   ", "      / o \\  ", "     |_____| ", "     \\_____/ "],
        ["   ___   ", "  / o \\  ", " |_____| ", " \\_____/ "],
    ],
    "哥布林": [
        ["   .---.  ", "  ( o o ) ", "   \\_-_/  ", "   /   \\  "],
        ["     .---.  ", "    ( o o ) ", "     \\_-_/  ", "     /   \\  "],
        [" .---.  ", "( o o ) ", " \\_-_/  ", " /   \\  "],
    ],
    "狼": [
        ["    /\\_/\\   ", "   ( o.o )  ", "    > ^ <   ", "   /     \\  "],
        ["      /\\_/\\   ", "     ( o.o )  ", "      > ^ <   ", "     /     \\  "],
        ["  /\\_/\\   ", " ( o.o )  ", "  > ^ <   ", " /     \\  "],
    ],
    "骷髅": [
        ["    .---.   ", "   ( o o )  ", "    | - |   ", "    |___|   ", "   /|   |\\  "],
        ["      .---.   ", "     ( o o )  ", "      | - |   ", "      |___|   ", "     /|   |\\  "],
        ["  .---.   ", " ( o o )  ", "  | - |   ", "  |___|   ", " /|   |\\  "],
    ],
    "暗影法师": [
        ["     _/\\_   ", "    ( oo )  ", "     \\/\\/   ", "     /||\\   ", "    / || \\  "],
        ["       _/\\_   ", "      ( oo )  ", "       \\/\\/   ", "       /||\\   ", "      / || \\  "],
        ["   _/\\_   ", "  ( oo )  ", "   \\/\\/   ", "   /||\\   ", "  / || \\  "],
    ],
    "神殿守护者": [
        ["    .=====.   ", "   || O O ||  ", "   ||  _  ||  ", "   ||_____||  ", "   /|||||||\\  "],
        ["      .=====.   ", "     || O O ||  ", "     ||  _  ||  ", "     ||_____||  ", "     /|||||||\\  "],
        ["  .=====.   ", " || O O ||  ", " ||  _  ||  ", " ||_____||  ", " /|||||||\\  "],
    ],
    "暗影之主": [
        ["     ./\\\\.    ", "    / == \\   ", "   | (( )) |  ", "   | _||_ |   ", "   /  ||  \\   "],
        ["       ./\\\\.    ", "      / == \\   ", "     | (( )) |  ", "     | _||_ |   ", "     /  ||  \\   "],
        ["   ./\\\\.    ", "  / == \\   ", " | (( )) |  ", " | _||_ |   ", " /  ||  \\   "],
    ],
}

def get_monster_art_key(enemy_name):
    """根据敌人名称匹配ASCII艺术key"""
    name_map = {
        "新手史莱姆": "史莱姆", "森林史莱姆": "史莱姆",
        "哥布林小兵": "哥布林",
        "森林巨狼": "狼",
        "骷髅士兵": "骷髅",
        "暗影法师": "暗影法师",
        "神殿守护者": "神殿守护者",
        "暗影之主": "暗影之主",
    }
    return name_map.get(enemy_name, None)

def animate_monster(enemy_name, duration=1.5):
    """怪物出场动画：左右摆动"""
    art_key = get_monster_art_key(enemy_name)
    if not art_key or art_key not in MONSTER_ART:
        return
    frames = MONSTER_ART[art_key]
    sequence = [0, 1, 0, 2, 0, 1, 0, 2, 0]
    frame_time = duration / len(sequence)
    for frame_idx in sequence:
        clear_screen()
        print()
        print(f"  [ {enemy_name} 出现了！]")
        print()
        for line in frames[frame_idx]:
            print("      " + line)
        print()
        time.sleep(frame_time)

def draw_monster(enemy_name):
    """静态绘制怪物（用于战斗界面）"""
    art_key = get_monster_art_key(enemy_name)
    if not art_key or art_key not in MONSTER_ART:
        return
    frames = MONSTER_ART[art_key]
    print()
    for line in frames[0]:
        print("      " + line)
    print()

# ============================================================
# ============================================================

CLASSES = {
    "战士": {
        "name": "战士",
        "label": "[盾]",
        "hp": 150,
        "attack": 18,
        "defense": 12,
        "speed": 5,
        "skills": {
            "盾击": {"damage_mult": 1.5, "cooldown": 2, "desc": "用盾牌猛击敌人，造成1.5倍伤害"},
            "战吼": {"damage_mult": 1.0, "cooldown": 3, "desc": "发出战吼提升士气，攻击+5持续2回合", "buff_attack": 5, "buff_turns": 2},
            "泰山压顶": {"damage_mult": 2.5, "cooldown": 5, "desc": "跳起全力砸下！造成2.5倍伤害"},
        },
        "desc": "高生命，高防御，团队的坚实后盾。\n       「躺平？不存在的，我就是团队的承重墙！」",
    },
    "法师": {
        "name": "法师",
        "label": "[法]",
        "hp": 90,
        "attack": 30,
        "defense": 6,
        "speed": 8,
        "skills": {
            "火球术": {"damage_mult": 1.8, "cooldown": 2, "desc": "发射灼热火球，造成1.8倍伤害"},
            "冰霜护盾": {"damage_mult": 0, "cooldown": 4, "desc": "凝聚冰盾，防御力+8持续2回合", "buff_defense": 8, "buff_turns": 2},
            "奥术风暴": {"damage_mult": 3.0, "cooldown": 5, "desc": "释放奥术能量风暴！造成3.0倍伤害"},
        },
        "desc": "超高攻击，低防御，知识就是力量。\n       「卷不动了？那就用火力覆盖解决问题！」",
    },
    "游侠": {
        "name": "游侠",
        "label": "[弓]",
        "hp": 110,
        "attack": 22,
        "defense": 8,
        "speed": 12,
        "skills": {
            "连射": {"damage_mult": 1.3, "cooldown": 1, "desc": "快速射出两箭，每箭0.65倍伤害（总1.3倍）"},
            "陷阱": {"damage_mult": 1.0, "cooldown": 3, "desc": "设置陷阱，敌人下回合受到额外伤害", "trap_damage": 30},
            "致命一击": {"damage_mult": 2.8, "cooldown": 5, "desc": "瞄准要害！造成2.8倍伤害"},
        },
        "desc": "高速度，均衡属性，先发制人。\n       「天下武功，唯快不破——" + meme("far_ahead") + "！」",
    },
}

ENEMIES_BY_CHAPTER = {
    "prologue": [
        {"name": "新手史莱姆", "hp": 30, "attack": 8, "defense": 0, "exp": 20, "gold": 15, "desc": "一只看起来不太聪明的史莱姆，适合练手。"},
    ],
    "chapter1": [
        {"name": "森林史莱姆", "hp": 50, "attack": 10, "defense": 2, "exp": 30, "gold": 20, "desc": "比新手村的大了一圈，但还是个憨憨。"},
        {"name": "哥布林小兵", "hp": 70, "attack": 15, "defense": 4, "exp": 45, "gold": 30, "desc": "哥布林界的" + meme("lying_flat") + "选手，混日子的。",
         "attacks": [{"type": "physical", "damage": 15}, {"type": "poison", "damage": 12, "dot_turns": 3}]},
        {"name": "森林巨狼", "hp": 90, "attack": 18, "defense": 5, "exp": 60, "gold": 40, "desc": "眼神凶狠，但它其实只是想找你玩。",
         "attacks": [{"type": "physical", "damage": 18}, {"type": "physical", "damage": 22}]},
    ],
    "chapter2": [
        {"name": "骷髅士兵", "hp": 100, "attack": 20, "defense": 8, "exp": 70, "gold": 50, "desc": "只剩骨头还在" + meme("involution") + "的打工人。"},
        {"name": "暗影法师", "hp": 80, "attack": 28, "defense": 5, "exp": 80, "gold": 55, "desc": "研究黑暗魔法的卷王，法力高强。",
         "attacks": [{"type": "magic", "damage": 28}, {"type": "burn", "damage": 18, "dot_turns": 2}]},
    ],
    "boss_chapter2": [
        {"name": "神殿守护者", "hp": 200, "attack": 28, "defense": 12, "exp": 200, "gold": 150, "desc": "远古神殿的守护石像，" + meme("too_cool") + "！",
         "attacks": [{"type": "physical", "damage": 28}, {"type": "magic", "damage": 22}, {"type": "burn", "damage": 20, "dot_turns": 2}]},
    ],
    "final_boss": [
        {"name": "暗影之主", "hp": 350, "attack": 35, "defense": 15, "exp": 500, "gold": 300, "desc": "黑暗的化身，全服最强的" + meme("show_off") + "。",
         "attacks": [{"type": "physical", "damage": 35}, {"type": "magic", "damage": 30}, {"type": "poison", "damage": 25, "dot_turns": 3}, {"type": "burn", "damage": 28, "dot_turns": 2}]},
    ],
}

ITEMS = {
    "生命药水": {"type": "heal", "value": 50, "price": 30, "label": "[生命+]", "desc": "恢复50点生命值"},
    "大生命药水": {"type": "heal", "value": 100, "price": 55, "label": "[生命++]", "desc": "恢复100点生命值"},
    "力量卷轴": {"type": "buff_attack", "value": 10, "turns": 3, "price": 50, "label": "[攻击+]", "desc": "攻击力+10，持续3回合"},
    "护盾符文": {"type": "buff_defense", "value": 10, "turns": 3, "price": 50, "label": "[防御+]", "desc": "防御力+10，持续3回合"},
    "速度卷轴": {"type": "buff_speed", "value": 5, "turns": 3, "price": 45, "label": "[速度+]", "desc": "速度+5，持续3回合"},
    "暴击符文": {"type": "buff_crit", "value": 0.25, "turns": 3, "price": 60, "label": "[暴击+]", "desc": "暴击率+25%，持续3回合"},
    "解毒药剂": {"type": "cure_debuff", "value": 1, "price": 35, "label": "[解毒]", "desc": "清除中毒/灼烧等负面状态"},
    "吸血之刃": {"type": "buff_lifesteal", "value": 0.3, "turns": 3, "price": 70, "label": "[吸血]", "desc": "攻击回复30%伤害为生命，3回合"},
    "复活羽毛": {"type": "revive", "value": 0.5, "price": 120, "label": "[复活]", "desc": "阵亡时自动以50%HP复活"},
    "逃脱卷轴": {"type": "escape", "value": 1, "price": 40, "label": "[逃脱]", "desc": "战斗中100%逃脱"},
}

SHOP_ITEMS = [
    {"name": "生命药水", "price": ITEMS["生命药水"]["price"], "label": ITEMS["生命药水"]["label"]},
    {"name": "大生命药水", "price": ITEMS["大生命药水"]["price"], "label": ITEMS["大生命药水"]["label"]},
    {"name": "力量卷轴", "price": ITEMS["力量卷轴"]["price"], "label": ITEMS["力量卷轴"]["label"]},
    {"name": "护盾符文", "price": ITEMS["护盾符文"]["price"], "label": ITEMS["护盾符文"]["label"]},
    {"name": "速度卷轴", "price": ITEMS["速度卷轴"]["price"], "label": ITEMS["速度卷轴"]["label"]},
    {"name": "暴击符文", "price": ITEMS["暴击符文"]["price"], "label": ITEMS["暴击符文"]["label"]},
    {"name": "解毒药剂", "price": ITEMS["解毒药剂"]["price"], "label": ITEMS["解毒药剂"]["label"]},
    {"name": "吸血之刃", "price": ITEMS["吸血之刃"]["price"], "label": ITEMS["吸血之刃"]["label"]},
    {"name": "复活羽毛", "price": ITEMS["复活羽毛"]["price"], "label": ITEMS["复活羽毛"]["label"]},
    {"name": "逃脱卷轴", "price": ITEMS["逃脱卷轴"]["price"], "label": ITEMS["逃脱卷轴"]["label"]},
]

RANDOM_EVENTS = [
    {
        "title": "[宝箱] 神秘宝箱",
        "desc": "路边发现一个闪闪发光的宝箱！",
        "effect": "treasure",
        "gold": (30, 80),
        "text_good": "打开宝箱，获得了一笔金币！欧气爆棚！",
        "text_bad": None,
    },
    {
        "title": "[温泉] 回复温泉",
        "desc": "森林深处发现一处冒着热气的温泉…",
        "effect": "heal",
        "heal_amount": 60,
        "text_good": "泡了个温泉，全身舒爽！恢复了60点生命值。",
        "text_bad": None,
    },
    {
        "title": "[商人] 神秘商人",
        "desc": "一个背着大包的商人突然出现：「嘿！要看看我的好东西吗？」",
        "effect": "discount_shop",
        "text_good": "神秘商人给了你一个折扣券！",
        "text_bad": None,
    },
    {
        "title": "[陷阱] 哥布林陷阱",
        "desc": "你没注意脚下…踩到了一个陷阱！",
        "effect": "trap",
        "damage": 25,
        "text_good": None,
        "text_bad": "触发了哥布林的陷阱，受到了25点伤害！" + meme("doomed") + "！",
    },
    {
        "title": "[石碑] 古老石碑",
        "desc": "路边有一块刻满文字的石碑，散发着微弱的光芒…",
        "effect": "exp_bonus",
        "exp": 50,
        "text_good": "你从石碑上学到了古老的战斗技巧！获得了50点经验值。" + meme("too_cool") + "！",
        "text_bad": None,
    },
    {
        "title": "[旅人] 迷路的旅人",
        "desc": "一个迷路的旅人向你求助…",
        "effect": "choice",
        "choice_help": {"gold": 50, "text": "旅人感激地给了你50金币作为谢礼！"},
        "choice_ignore": {"text": "你装作没看见走开了…（无事发生）"},
    },
]

ACHIEVEMENTS_DEF = {
    "first_blood": {"name": "[首胜] 第一滴血", "desc": "赢得第一场战斗"},
    "level5": {"name": "[成长] 初出茅庐", "desc": "达到5级"},
    "rich": {"name": "[财富] 财大气粗", "desc": "拥有超过200金币"},
    "collector": {"name": "[收藏] 收藏家", "desc": "背包拥有5件以上道具"},
    "boss_slayer": {"name": "[屠龙] Boss终结者", "desc": "击败神殿守护者"},
    "final_victory": {"name": "[通关] 命运之契", "desc": "通关游戏"},
    "bond_master": {"name": "[羁绊] 最佳搭子", "desc": "羁绊值达到8以上"},
    "meme_king": {"name": "[梗王] 名梗收集者", "desc": "遇到了所有类型的随机事件"},
}

CHAPTERS = (
    {
        "id": "prologue",
        "title": "序章：命运的齿轮开始转动",
        "subtitle": "— 冒险者公会，新人报到 —",
        "has_shop": False,
        "has_event": False,
        "num_battles": 1,
        "enemy_pool": "prologue",
        "has_boss": False,
        "boss_pool": None,
        "intro_text": "你来到了冒险者公会，准备接受你的第一个任务。\n公会会长看了看你：「新人？先证明你的实力吧！」",
    },
    {
        "id": "chapter1",
        "title": "第一章：这森林谁爱来谁来",
        "subtitle": "— 迷雾森林的试炼 —",
        "has_shop": True,
        "has_event": True,
        "num_battles": 2,
        "enemy_pool": "chapter1",
        "has_boss": False,
        "boss_pool": None,
        "intro_text": "踏入迷雾森林，四周弥漫着诡异的气息。\n远处传来哥布林的怪笑声…",
    },
    {
        "id": "chapter2",
        "title": "第二章：神殿の" + meme("amazing"),
        "subtitle": "— 远古遗迹的挑战 —",
        "has_shop": True,
        "has_event": True,
        "num_battles": 2,
        "enemy_pool": "chapter2",
        "has_boss": True,
        "boss_pool": "boss_chapter2",
        "intro_text": "远古神殿的大门轰然打开。\n一股强大的魔力从深处传来…守护者苏醒了！",
    },
    {
        "id": "final",
        "title": "终章：" + meme("buddy") + "一生一起走",
        "subtitle": "— 最终决战 —",
        "has_shop": True,
        "has_event": False,
        "num_battles": 0,
        "enemy_pool": None,
        "has_boss": True,
        "boss_pool": "final_boss",
        "intro_text": "黑暗的最深处，暗影之主等待着你的到来。\n「终于来了…让我看看你的羁绊之力吧！」",
    },
)

# ============================================================
# ============================================================

COMPANION_NAMES = ("大壮", "小晴")

COMPANION_STATS = {
    "大壮": {"hp": 130, "attack": 16, "defense": 10, "speed": 6,
             "tagline": "热血憨厚的战士，嘴上爱说大话，但关键时刻绝对靠谱。\n       「兄弟！冲就完了！」"},
    "小晴": {"hp": 105, "attack": 22, "defense": 7, "speed": 10,
             "tagline": "毒舌吐槽担当，外表高冷内心火热，战斗力爆表。\n       「你可真行啊…不过，还行。」"},
}

DIALOGUES = {
    "male": {
        "first_meet": {
            "speaker": "大壮",
            "text": "「嘿！你也是来冒险的？我叫大壮，梦想是成为最强的冒险者！" + meme("too_cool") + "！\n　怎么样，要不要组个" + meme("buddy") + "一起闯？」",
            "options": [
                {"text": "「" + meme("too_cool") + "！一起组队吧！」", "bond": 2,
                 "response": "大壮咧嘴一笑：「有眼光！咱们就是最强" + meme("buddy") + "了！\n　以后有我在，稳得一批！」"},
                {"text": "「……你" + meme("mental_state") + "真的" + meme("amazing") + "。」", "bond": 1,
                 "response": "大壮挠挠头：「嘿嘿，我" + meme("extrovert") + "实锤，你肯定是" + meme("introvert") + "吧？\n　没事！跟我混，保证把你带成" + meme("extrovert") + "！」"},
            ],
        },
        "after_chapter1": {
            "speaker": "大壮",
            "text": "「兄弟！这森林也太阴间了吧！不过咱们配合越来越默契了！\n　话说，你觉得我这个" + meme("buddy") + "怎么样？」",
            "options": [
                {"text": "「靠谱！有你在真好！」", "bond": 2,
                 "response": "大壮眼睛一亮：「真的吗！那必须的！\n　以后不管遇到什么，咱们一起扛！」"},
                {"text": "「嗯…还行吧，至少没拖后腿。」", "bond": 1,
                 "response": "大壮假装生气：「什么叫还行！我这叫稳中带秀好吗！\n　算了算了，反正我知道你心里是认可我的！」"},
            ],
        },
        "before_boss": {
            "speaker": "大壮",
            "text": "「兄弟，前面就是神殿守护者了。说实话我有点紧张…\n　但是！有你在，我觉得没什么好怕的。」",
            "options": [
                {"text": "「一起上！我们是最强组合！」", "bond": 2,
                 "response": "大壮举起拳头：「对！最强组合！让那个石头人见识下\n　什么叫真正的羁绊之力！冲啊！！」"},
                {"text": "「别怕，我罩着你！」", "bond": 1,
                 "response": "大壮愣了一下，然后大笑：「哈哈哈！好！\n　今天就看咱俩怎么把这个Boss给办了！」"},
            ],
        },
        "ending": {
            "speaker": "大壮",
            "text": "「我们…真的做到了！兄弟！」\n大壮激动得声音都在颤抖。",
            "options": [
                {"text": "「这是我们共同的胜利！」", "bond": 2,
                 "response": "大壮给了你一个兄弟式的拥抱：「这辈子最好的" + meme("buddy") + "！\n　以后还有很多冒险，咱们继续一起走！」"},
                {"text": "「嗯，谢谢你一路的陪伴。」", "bond": 1,
                 "response": "大壮用力拍了拍你的肩膀：「说啥谢谢！\n　都是兄弟！走吧，回去好好庆祝一下！」"},
            ],
        },
    },
    "female": {
        "first_meet": {
            "speaker": "小晴",
            "text": "「……你也是来冒险的？我叫小晴。\n　别拖我后腿就行。不过我眼光向来不错，你应该还行。」",
            "options": [
                {"text": "「放心，绝对不会" + meme("giving_up") + "！」", "bond": 2,
                 "response": "小晴嘴角微微上扬：「哼，希望你说到做到。\n　那就一起吧，多个" + meme("buddy") + "也不是坏事。」"},
                {"text": "「好家伙，你这高冷人设" + meme("amazing") + "。」", "bond": 1,
                 "response": "小晴白了你一眼：「……信不信我现在就让你" + meme("doomed") + "了。\n　算了，不跟你计较。走了，菜鸟。」"},
            ],
        },
        "after_chapter1": {
            "speaker": "小晴",
            "text": "「呼…这森林真是够了。不过嘛…\n　你的表现比我预想的要好一点。就一点点。」",
            "options": [
                {"text": "「能得到你的认可，" + meme("emotionally_broken") + "了！」", "bond": 2,
                 "response": "小晴差点笑出声：「谁认可你了！…不过，\n　和你组队确实没那么无聊。继续保持。」"},
                {"text": "「你也挺厉害的，不愧是实力派。」", "bond": 1,
                 "response": "小晴别过脸去：「……突然这么正经干嘛。\n　快走吧，前面还有路要赶。」（但你看到她嘴角在笑）"},
            ],
        },
        "before_boss": {
            "speaker": "小晴",
            "text": "「前面就是神殿守护者…看起来很不好对付。\n　你…准备好了吗？」",
            "options": [
                {"text": "「有你在，我什么都不怕！」", "bond": 2,
                 "response": "小晴沉默了一秒，然后抬起头：「…笨蛋。\n　那就一起上吧，让这个石头看看什么叫团队！」"},
                {"text": "「准备完毕！一起解决它！」", "bond": 1,
                 "response": "小晴点了点头：「好。记住，打不过就跑，\n　" + meme("giving_up") + "有时候也是一种智慧…开玩笑的！上吧！」"},
            ],
        },
        "ending": {
            "speaker": "小晴",
            "text": "「……赢了。」\n小晴的声音难得有些微微发颤。",
            "options": [
                {"text": "「是我们一起赢的！」", "bond": 2,
                 "response": "小晴看着你，终于露出了一个真正的笑容：「嗯。\n　谢谢你，最好的" + meme("buddy") + "。以后也请多指教。」"},
                {"text": "「你真的很厉害，小晴。」", "bond": 1,
                 "response": "小晴轻轻踢了你一下：「少来这套。\n　…不过，跟你的这次冒险，我会记住的。」"},
            ],
        },
    },
}

# ============================================================
# ============================================================

def create_character():
    """创建玩家角色，返回 player (dict)"""
    clear_screen()
    divider("★", 50)
    print("            命运之契")
    divider("★", 50)
    print()
    slow_print("欢迎来到冒险者公会！在开始冒险之前，先来创建你的角色吧。")
    print()

    while True:
        name = input("  > 请输入你的名字：").strip()
        if name:
            break
        print("  !! 名字不能为空哦！")

    print("\n  > 请选择你的性别：")
    print("    1. 男性")
    print("    2. 女性")
    gender_choice = get_int_input("  >> 请输入 (1/2)：", 1, 2)
    gender = "male" if gender_choice == 1 else "female"
    companion_name = COMPANION_NAMES[0] if gender == "male" else COMPANION_NAMES[1]

    print(f"\n  > 请选择你的职业：")
    for i, (class_name, class_data) in enumerate(CLASSES.items(), 1):
        print(f"    {i}. {class_data['label']} {class_name}")
        print(f"       {class_data['desc']}")
    class_choice = get_int_input("  >> 请输入 (1/2/3)：", 1, 3)
    class_name = list(CLASSES.keys())[class_choice - 1]
    class_data = CLASSES[class_name]

    player = {
        "name": name,
        "gender": gender,
        "class": class_name,
        "class_data": class_data,
        "hp": class_data["hp"],
        "max_hp": class_data["hp"],
        "attack": class_data["attack"],
        "defense": class_data["defense"],
        "speed": class_data["speed"],
        "level": 1,
        "exp": 0,
        "gold": 50,
        "inventory": [],
        "skill_cooldowns": {},
        "buffs": [],
        "debuffs": [],
        "achievements": set(),
        "events_triggered": set(),
        "bond": 0,
        "chapter": 0,
    }

    for skill_name in class_data["skills"]:
        player["skill_cooldowns"][skill_name] = 0

    clear_screen()
    divider("*", 50)
    print(f"  [+] 角色创建完成！")
    divider("*", 50)
    print(f"  姓名：{player['name']}")
    print(f"  职业：{class_data['label']} {class_name}")
    print(f"  生命：{player['hp']}/{player['max_hp']}")
    print(f"  攻击：{player['attack']}  防御：{player['defense']}  速度：{player['speed']}")
    print(f"  金币：{player['gold']} 元")
    print(f"  同伴：{companion_name}")
    divider("★", 50)
    press_enter()

    return player

def init_companion(player):
    """初始化同伴"""
    companion_name = COMPANION_NAMES[0] if player["gender"] == "male" else COMPANION_NAMES[1]
    stats = COMPANION_STATS[companion_name]
    companion = {
        "name": companion_name,
        "hp": stats["hp"],
        "max_hp": stats["hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "speed": stats["speed"],
    }
    return companion

# ============================================================
# ============================================================

def show_status(player, companion):
    """显示玩家和同伴的状态"""
    divider()
    print(f"  {player['name']} | {player['class_data']['label']} {player['class']} | Lv.{player['level']}")
    print(f"  生命: {max(0, player['hp'])}/{player['max_hp']} | 攻击: {player['attack']} | 防御: {player['defense']}")
    print(f"  经验: {player['exp']} | 金币: {player['gold']}元 | 羁绊: {player['bond']}/10")
    if player["buffs"]:
        buff_str = " | ".join([f"{b['type']}+{b['value']}({b['turns']}回合)" for b in player["buffs"]])
        print(f"  Buff: {buff_str}")
    print(f"  {companion['name']} | 生命: {max(0, companion['hp'])}/{companion['max_hp']} | 攻击: {companion['attack']}")
    if player["inventory"]:
        inv_str = " | ".join([f"{ITEMS[item['name']]['label']}{item['name']}x{item['qty']}" for item in player["inventory"]])
        print(f"  [背包]: {inv_str}")
    else:
        print(f"  [背包]: 空空如也~")
    divider()

# ============================================================
# ============================================================

MAX_INVENTORY = 8

def add_item(player, item_name, qty=1):
    """添加道具到背包"""
    inventory = player["inventory"]

    for item in inventory:
        if item["name"] == item_name:
            item["qty"] += qty
            print(f"  [+] 获得 {ITEMS[item_name]['label']} {item_name} x{qty}！（现有 {item['qty']} 个）")
            return True

    if len(inventory) >= MAX_INVENTORY:
        print(f"  !! 背包已满（{MAX_INVENTORY}格）！无法获得 {item_name}。")
        return False

    inventory.append({"name": item_name, "qty": qty})
    print(f"  [+] 获得 {ITEMS[item_name]['label']} {item_name} x{qty}！")
    return True

def use_item(player, item_name, target="player", companion=None):
    """使用道具 - target: 'player' 或 'companion'"""
    inventory = player["inventory"]
    item_data = ITEMS.get(item_name)
    if not item_data:
        print(f"  !! 未知道具：{item_name}")
        return False

    for item in inventory:
        if item["name"] == item_name and item["qty"] > 0:
            break
    else:
        print(f"  !! 背包中没有 {item_name}！")
        return False

    item_type = item_data["type"]
    actual_target = player if target == "player" else companion
    target_name = "你" if target == "player" else companion["name"] if companion else "同伴"

    if item_type == "heal":
        if not actual_target:
            print(f"  !! 目标无效！")
            return False
        heal_amount = min(item_data["value"], actual_target["max_hp"] - actual_target["hp"])
        if heal_amount <= 0:
            print(f"  !! {target_name} 生命值已满！")
            return False
        actual_target["hp"] += heal_amount
        print(f"  [+] 对 {target_name} 使用 {item_data['label']} {item_name}，恢复了 {heal_amount} 点生命！")

    elif item_type == "buff_attack":
        player["buffs"].append({"type": "attack", "value": item_data["value"], "turns": item_data["turns"]})
        print(f"  [+] 使用 {item_data['label']} {item_name}，攻击 +{item_data['value']}，持续 {item_data['turns']} 回合！")

    elif item_type == "buff_defense":
        player["buffs"].append({"type": "defense", "value": item_data["value"], "turns": item_data["turns"]})
        print(f"  [+] 使用 {item_data['label']} {item_name}，防御 +{item_data['value']}，持续 {item_data['turns']} 回合！")

    elif item_type == "buff_speed":
        player["buffs"].append({"type": "speed", "value": item_data["value"], "turns": item_data["turns"]})
        print(f"  [+] 使用 {item_data['label']} {item_name}，速度 +{item_data['value']}，持续 {item_data['turns']} 回合！")

    elif item_type == "buff_crit":
        player["buffs"].append({"type": "crit", "value": item_data["value"], "turns": item_data["turns"]})
        print(f"  [+] 使用 {item_data['label']} {item_name}，暴击率 +{int(item_data['value']*100)}%，持续 {item_data['turns']} 回合！")

    elif item_type == "buff_lifesteal":
        player["buffs"].append({"type": "lifesteal", "value": item_data["value"], "turns": item_data["turns"]})
        print(f"  [+] 使用 {item_data['label']} {item_name}，攻击吸血 {int(item_data['value']*100)}%，持续 {item_data['turns']} 回合！")

    elif item_type == "cure_debuff":
        if not player["debuffs"]:
            print(f"  !! 没有负面状态，不需要使用 {item_name}！")
            return False
        cleared = [d for d in player["debuffs"]]
        player["debuffs"].clear()
        names = "、".join(["中毒" if d['type']=='poison' else "灼烧" if d['type']=='burn' else d['type'] for d in cleared])
        print(f"  [+] 使用 {item_data['label']} {item_name}，清除了「{names}」状态！")

    elif item_type == "revive":
        player["hp"] = min(player["max_hp"], player["hp"] + int(player["max_hp"] * item_data["value"]))
        print(f"  [+] 使用 {item_data['label']} {item_name}，恢复了大量生命！")

    elif item_type == "escape":
        print(f"  !! {item_name} 只能在战斗中使用！")
        return False

    item["qty"] -= 1
    if item["qty"] <= 0:
        inventory.remove(item)
    return True

def show_inventory(player):
    """查看背包"""
    inventory = player["inventory"]
    if not inventory:
        print("\n  [背包] 空空如也~")
        return

    print("\n  [背包] ====== 你的背包 ======")
    for i, item in enumerate(inventory, 1):
        item_data = ITEMS[item["name"]]
        print(f"  {i}. {item_data['label']} {item['name']} x{item['qty']} -- {item_data['desc']}")
    print(f"  （容量：{len(inventory)}/{MAX_INVENTORY}）")
    print("=" * 30)

def use_item_from_inventory(player):
    """从背包使用道具"""
    show_inventory(player)
    inventory = player["inventory"]
    if not inventory:
        return False

    print("\n输入道具编号来使用，输入 0 返回：")
    choice = get_int_input("  >> ", 0, len(inventory))
    if choice == 0:
        return False

    item_name = inventory[choice - 1]["name"]
    return use_item(player, item_name)

# ============================================================
# ============================================================

def enter_shop(player, companion):
    """进入商店"""
    clear_screen()
    print()
    divider("=", 52)
    print("  [ 商店 ]  冒险者杂货铺")
    divider("=", 52)

    print(f"  ┌─ 你的当前状态 ─────────────────────────┐")
    print(f"  │ {player['class_data']['label']} {player['name']}  │  Lv.{player['level']}  │  {player['class']}")
    print(f"  │ 生命：{player['hp']:>4} / {player['max_hp']:<4}  │  攻击：{player['attack']:>3}  │  防御：{player['defense']:>3}")
    print(f"  │ 同伴 {companion['name']}  │  生命：{companion['hp']:>4} / {companion['max_hp']:<4}")
    print(f"  │ 金币：{player['gold']:>4} 元  │  背包：{len(player['inventory'])} / {MAX_INVENTORY}")
    if player['inventory']:
        inv_items = "  ".join([f"{ITEMS[i['name']]['label']}{i['name']}x{i['qty']}" for i in player['inventory']])
        print(f"  │ 道具：{inv_items}")
    print(f"  └──────────────────────────────────────────┘")
    divider("-", 52)

    slow_print(f"老板：「哟！{player['name']}和{companion['name']}！看看需要啥？」")
    print()

    while True:
        print("  商品列表：")
        for i, item in enumerate(SHOP_ITEMS, 1):
            item_data = ITEMS[item["name"]]
            hint = ""
            if item_data["type"] == "heal" and player["hp"] < player["max_hp"]:
                missing = player["max_hp"] - player["hp"]
                hint = f"  << 还差 {missing} 生命，推荐购买！"
            print(f"  {i}. {item['label']} {item['name']}  --  {item_data['desc']}  |  {item['price']:>3} 元{hint}")
        print(f"  0. 离开商店")
        print(f"  S. 卖出道具 (半价回收)")

        choice = input("\n  >> 请输入选项：").strip().lower()

        if choice == "0":
            slow_print("老板：「欢迎下次光临！加油啊冒险者！」")
            press_enter()
            break
        elif choice == "s":
            sell_item(player)
            continue

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(SHOP_ITEMS):
                item = SHOP_ITEMS[idx]
                if player["gold"] >= item["price"]:
                    if len(player["inventory"]) >= MAX_INVENTORY:
                        print(f"  !! 背包已满！请先清理背包。")
                        continue
                    player["gold"] -= item["price"]
                    add_item(player, item["name"], 1)
                    print(f"  [+] 购买了 {item['label']} {item['name']}！剩余金币：{player['gold']} 元")
                else:
                    print(f"  !! 金币不足！需要 {item['price']} 元，你只有 {player['gold']} 元。")
                    slow_print(f"老板：「" + meme("whatever") + "，没钱就别看啦~」")
            else:
                print("  !! 无效选项！")
        except ValueError:
            print("  !! 无效选项！")

def sell_item(player):
    """卖出道具（半价）"""
    inventory = player["inventory"]
    if not inventory:
        print("  !! 背包是空的，没有东西可卖！")
        return

    show_inventory(player)
    print("\n输入道具编号来卖出（半价回收），输入 0 返回：")
    choice = get_int_input("  >> ", 0, len(inventory))
    if choice == 0:
        return

    item = inventory[choice - 1]
    sell_price = ITEMS[item["name"]]["price"] // 2
    player["gold"] += sell_price
    print(f"  [+] 卖出了 {ITEMS[item['name']]['label']} {item['name']}，获得 {sell_price} 元！")

    item["qty"] -= 1
    if item["qty"] <= 0:
        inventory.remove(item)

# ============================================================
# ============================================================

def exp_to_level(level):
    """计算升级所需经验"""
    return level * 50 + 50

def check_level_up(player):
    """检查并处理升级"""
    while True:
        needed = exp_to_level(player["level"])
        if player["exp"] >= needed:
            player["exp"] -= needed
            player["level"] += 1
            player["max_hp"] += 15
            player["hp"] = player["max_hp"]
            player["attack"] += 3
            player["defense"] += 2
            player["speed"] += 1

            print()
            divider("*", 40)
            print(f"  [升级!] {player['name']} 升到了 Lv.{player['level']}！")
            print(f"  HP上限 +15 | 攻击 +3 | 防御 +2 | 速度 +1")
            divider("*", 40)

            if player["level"] % 5 == 0:
                print(f"  [里程碑] 你已成为更强大的冒险者！")
                slow_print(f"     {player['class_data']['label']} 「" + meme("far_ahead") + "！」")

            if player["level"] >= 5 and "level5" not in player["achievements"]:
                player["achievements"].add("level5")
                print(f"  [成就] 解锁：{ACHIEVEMENTS_DEF['level5']['name']}！")
            time.sleep(1)
        else:
            break

# ============================================================
# ============================================================

def calculate_damage(attacker_atk, defender_def):
    """计算伤害值"""
    raw = attacker_atk - defender_def * 0.6
    return max(1, int(raw))

def apply_buffs(player):
    """应用Buff加成"""
    bonus_atk = 0
    bonus_def = 0
    for buff in player["buffs"]:
        if buff["type"] == "attack":
            bonus_atk += buff["value"]
        elif buff["type"] == "defense":
            bonus_def += buff["value"]
    return bonus_atk, bonus_def

def tick_buffs(player):
    """减少Buff回合数，移除过期Buff"""
    expired = []
    for buff in player["buffs"]:
        buff["turns"] -= 1
        if buff["turns"] <= 0:
            expired.append(buff)
    for b in expired:
        player["buffs"].remove(b)
        type_cn = "攻击" if b['type'] == 'attack' else "防御" if b['type'] == 'defense' else b['type']
        print(f"  [Buff] 「{type_cn}+{b['value']}」效果已消失。")

def tick_debuffs(player):
    """处理DOT持续性伤害"""
    expired = []
    for debuff in player["debuffs"]:
        type_cn = "中毒" if debuff['type'] == 'poison' else "灼烧" if debuff['type'] == 'burn' else debuff['type']
        player["hp"] -= debuff["damage"]
        print(f"  [DOT] 「{type_cn}」造成 {debuff['damage']} 点伤害！（剩余 {debuff['turns']-1} 回合）")
        debuff["turns"] -= 1
        if debuff["turns"] <= 0:
            expired.append(debuff)
    for d in expired:
        player["debuffs"].remove(d)
        type_cn = "中毒" if d['type'] == 'poison' else "灼烧" if d['type'] == 'burn' else d['type']
        print(f"  [Debuff] 「{type_cn}」状态已解除。")

def tick_cooldowns(player):
    """减少技能冷却"""
    for skill in player["skill_cooldowns"]:
        if player["skill_cooldowns"][skill] > 0:
            player["skill_cooldowns"][skill] -= 1

def companion_assist(player, companion, enemy):
    """同伴协助攻击（基于羁绊值概率触发）"""
    bond = player["bond"]
    if companion["hp"] <= 0:
        return False
    chance = bond * 8
    if random.randint(1, 100) <= chance:
        assist_dmg = calculate_damage(
            int(companion["attack"] * (0.5 + bond * 0.05)),
            enemy["defense"]
        )
        enemy["hp"] -= assist_dmg
        print(f"  [协助] {companion['name']} 协助攻击！造成 {assist_dmg} 点伤害！")
        if bond >= 8:
            slow_print(f"     「这就是" + meme("buddy") + "的羁绊之力！」")
        return True
    return False

def use_combo_skill(player, companion, enemy):
    """羁绊合体技（羁绊≥6解锁）"""
    if player["bond"] < 6:
        return False

    bonus_atk, _ = apply_buffs(player)
    total_atk = player["attack"] + companion["attack"] + bonus_atk
    combo_dmg = calculate_damage(int(total_atk * 2.5), enemy["defense"])
    enemy["hp"] -= combo_dmg

    print()
    divider("#", 45)
    print(f"  *** 羁绊合击·命运之契 ***")
    slow_print(f"  {player['name']} 与 {companion['name']} 的力量合而为一！")
    print(f"  造成 {combo_dmg} 点巨额伤害！！")
    divider("#", 45)
    return True

def player_turn(player, companion, enemy):
    """玩家回合"""
    bonus_atk, bonus_def = apply_buffs(player)
    show_status(player, companion)
    print(f"\n  >> {enemy['name']} | 生命: {max(0, enemy['hp'])}")
    print(f"  \"{enemy['desc']}\"")
    print()

    print("  你的行动：")
    print("  1. 攻击      2. 技能      3. 防御      4. 道具")
    if player["bond"] >= 6:
        print(f"  5. [羁绊合击·命运之契] (每场限1次)")
        max_choice = 5
    else:
        max_choice = 4

    choice = get_int_input("  >> 选择：", 1, max_choice)

    if choice == 1:
        dmg = calculate_damage(player["attack"] + bonus_atk, enemy["defense"])
        crit_buff = next((b for b in player["buffs"] if b["type"] == "crit"), None)
        is_crit = crit_buff and random.random() < crit_buff["value"]
        if is_crit:
            dmg = int(dmg * 1.5)
            print(f"\n  [攻击·暴击!!] 你攻击了 {enemy['name']}，暴击造成 {dmg} 点伤害！")
        else:
            print(f"\n  [攻击] 你攻击了 {enemy['name']}，造成 {dmg} 点伤害！")
        enemy["hp"] -= dmg
        lifesteal_buff = next((b for b in player["buffs"] if b["type"] == "lifesteal"), None)
        if lifesteal_buff:
            heal_amt = int(dmg * lifesteal_buff["value"])
            player["hp"] = min(player["max_hp"], player["hp"] + heal_amt)
            if heal_amt > 0:
                print(f"  [吸血] 回复了 {heal_amt} 点生命！")

    elif choice == 2:
        skills = player["class_data"]["skills"]
        available = [(name, data) for name, data in skills.items()
                     if player["skill_cooldowns"][name] == 0]

        if not available:
            print("  !! 所有技能都在冷却中！请重新选择。")
            return player_turn(player, companion, enemy)

        print("\n  可用技能：")
        for i, (name, data) in enumerate(available, 1):
            cd_info = f"冷却{data['cooldown']}回合" if data['cooldown'] > 0 else "无冷却"
            print(f"  {i}. {name} -- {data['desc']} ({cd_info})")
        print(f"  0. 返回")

        skill_choice = get_int_input("  >> 选择技能：", 0, len(available))
        if skill_choice == 0:
            return player_turn(player, companion, enemy)

        skill_name, skill_data = available[skill_choice - 1]

        if "buff_attack" in skill_data:
            player["buffs"].append({"type": "attack", "value": skill_data["buff_attack"], "turns": skill_data["buff_turns"]})
            print(f"\n  [技能] {skill_name}！ATK +{skill_data['buff_attack']}，持续 {skill_data['buff_turns']} 回合！")
        elif "buff_defense" in skill_data:
            player["buffs"].append({"type": "defense", "value": skill_data["buff_defense"], "turns": skill_data["buff_turns"]})
            print(f"\n  [技能] {skill_name}！DEF +{skill_data['buff_defense']}，持续 {skill_data['buff_turns']} 回合！")
        elif "trap_damage" in skill_data:
            enemy["hp"] -= skill_data["trap_damage"]
            print(f"\n  [技能] {skill_name}！陷阱触发，敌人受到 {skill_data['trap_damage']} 点伤害！")
        else:
            dmg = calculate_damage(int((player["attack"] + bonus_atk) * skill_data["damage_mult"]), enemy["defense"])
            enemy["hp"] -= dmg
            print(f"\n  [技能] {skill_name}！造成 {dmg} 点伤害！")

        player["skill_cooldowns"][skill_name] = skill_data["cooldown"]

    elif choice == 3:
        player["buffs"].append({"type": "defense", "value": player["defense"], "turns": 1})
        print(f"\n  [防御] 进入防御姿态！本回合 DEF 翻倍！")

    elif choice == 4:
        if not player["inventory"]:
            print("  !! 背包是空的！")
            return player_turn(player, companion, enemy)
        show_inventory(player)
        inv = player["inventory"]
        print("输入道具编号使用，0 返回：")
        item_choice = get_int_input("  >> ", 0, len(inv))
        if item_choice == 0:
            return player_turn(player, companion, enemy)
        item_name = inv[item_choice - 1]["name"]
        if ITEMS[item_name]["type"] == "escape":
            use_item(player, item_name)
            return "escaped"
        elif ITEMS[item_name]["type"] == "heal":
            print(f"\n  对谁使用 {item_name}？")
            print("  1. 自己")
            print(f"  2. 同伴 {companion['name']}（生命: {companion['hp']}/{companion['max_hp']}）")
            t_choice = get_int_input("  >> ", 1, 2)
            if t_choice == 2 and companion["hp"] <= 0:
                print("  !! 同伴已失去战斗力，无法使用！")
                return player_turn(player, companion, enemy)
            target = "companion" if t_choice == 2 else "player"
            use_item(player, item_name, target, companion)
        else:
            use_item(player, item_name)

    elif choice == 5 and player["bond"] >= 6:
        use_combo_skill(player, companion, enemy)
        player["_combo_used"] = True

    if enemy["hp"] > 0:
        companion_assist(player, companion, enemy)

    return None

def enemy_turn(player, companion, enemy):
    """敌人回合 - 支持物理/魔法/毒素攻击"""
    bonus_atk, bonus_def = apply_buffs(player)

    attacks = enemy.get("attacks", [{"type": "physical", "damage": enemy["attack"]}])
    if not attacks:
        attacks = [{"type": "physical", "damage": enemy["attack"]}]
    atk = random.choice(attacks)
    atk_type = atk.get("type", "physical")
    atk_dmg = atk.get("damage", enemy["attack"])

    targets = ["player"]
    if companion["hp"] > 0:
        targets.append("companion")
    target = random.choice(targets)

    if target == "player":
        if atk_type == "magic":
            dmg = calculate_damage(atk_dmg, player["defense"] * 0.5 + bonus_def * 0.5)
            player["hp"] -= dmg
            print(f"\n  [敌人·魔法] {enemy['name']} 释放魔法攻击！造成 {dmg} 点伤害！（无视部分防御）")
        elif atk_type == "poison":
            dmg = calculate_damage(atk_dmg * 0.6, player["defense"] + bonus_def)
            player["hp"] -= dmg
            dot_turns = atk.get("dot_turns", 3)
            player["debuffs"].append({"type": "poison", "damage": atk_dmg // 3, "turns": dot_turns})
            print(f"\n  [敌人·毒素] {enemy['name']} 喷射毒液！造成 {dmg} 点伤害，附加中毒 {dot_turns} 回合！")
        elif atk_type == "burn":
            dmg = calculate_damage(atk_dmg * 0.7, player["defense"] + bonus_def)
            player["hp"] -= dmg
            dot_turns = atk.get("dot_turns", 2)
            player["debuffs"].append({"type": "burn", "damage": atk_dmg // 4, "turns": dot_turns})
            print(f"\n  [敌人·灼烧] {enemy['name']} 喷出火焰！造成 {dmg} 点伤害，附加灼烧 {dot_turns} 回合！")
        else:
            dmg = calculate_damage(atk_dmg, player["defense"] + bonus_def)
            player["hp"] -= dmg
            print(f"\n  [敌人·物理] {enemy['name']} 攻击了你！造成 {dmg} 点伤害！")
    else:
        dmg = calculate_damage(atk_dmg, companion["defense"])
        companion["hp"] -= dmg
        print(f"\n  [敌人] {enemy['name']} 攻击了 {companion['name']}！造成 {dmg} 点伤害！")

def has_revive_item(player):
    """检查是否有复活道具"""
    for item in player["inventory"]:
        if ITEMS[item["name"]]["type"] == "revive" and item["qty"] > 0:
            return item["name"]
    return None

def battle(player, companion, enemy):
    """主战斗循环（刷新式界面）"""
    clear_screen()
    print()
    divider("!", 50)
    slow_print(f"  !! 遭遇敌人：{enemy['name']}！！")
    print(f"  \"{enemy['desc']}\"")
    divider("!", 50)
    draw_monster(enemy["name"])
    press_enter()

    player["_combo_used"] = False
    turn = 1

    while player["hp"] > 0 and enemy["hp"] > 0:
        clear_screen()
        print()
        divider("=", 50)
        print(f"  [战斗] 第 {turn} 回合")
        divider("=", 50)

        draw_monster(enemy["name"])

        print(f"  >> {enemy['name']} <<")
        print(f"  生命: {max(0, enemy['hp'])}  |  攻击: {enemy['attack']}  |  防御: {enemy['defense']}")
        print(f"  \"{enemy['desc']}\"")

        hp_bar_len = 20
        enemy_hp_pct = max(0, enemy["hp"]) / max(1, enemy.get("_initial_hp", enemy["hp"]))
        filled = int(hp_bar_len * min(1, enemy_hp_pct))
        print(f"  生命: [{'#' * filled}{'.' * (hp_bar_len - filled)}]")

        print()
        divider("-", 50)

        bns_atk, bns_def = apply_buffs(player)
        print(f"  {player['class_data']['label']} {player['name']} | Lv.{player['level']} | {player['class']}")
        print(f"  生命: {max(0, player['hp'])}/{player['max_hp']}  |  攻击: {player['attack']}{' +'+str(bns_atk) if bns_atk else ''}  |  防御: {player['defense']}{' +'+str(bns_def) if bns_def else ''}")
        print(f"  同伴 {companion['name']}  |  生命: {max(0, companion['hp'])}/{companion['max_hp']}  |  攻击: {companion['attack']}")
        if player["buffs"]:
            buff_names = []
            for b in player["buffs"]:
                t = b['type']
                tn = "攻击" if t=='attack' else "防御" if t=='defense' else "速度" if t=='speed' else "暴击" if t=='crit' else "吸血" if t=='lifesteal' else t
                buff_names.append(f"{tn}+{b['value']}({b['turns']}回合)")
            print(f"  [增益]: {' | '.join(buff_names)}")
        if player["debuffs"]:
            debuff_names = []
            for d in player["debuffs"]:
                tn = "中毒" if d['type']=='poison' else "灼烧" if d['type']=='burn' else d['type']
                debuff_names.append(f"{tn}(每回合-{d['damage']},剩{d['turns']}回合)")
            print(f"  [负面]: {' | '.join(debuff_names)}")

        if player["inventory"]:
            inv_str = " | ".join([f"{ITEMS[i['name']]['label']}{i['name']}x{i['qty']}" for i in player["inventory"]])
            print(f"  [背包]: {inv_str}")
        else:
            print(f"  [背包]: 空空如也~")

        cds = [f"{s}:{c}" for s, c in player["skill_cooldowns"].items() if c > 0]
        if cds:
            print(f"  技能冷却: {' | '.join(cds)}")

        divider("-", 50)

        if player["debuffs"]:
            tick_debuffs(player)
            if player["hp"] <= 0:
                revive_item = has_revive_item(player)
                if revive_item:
                    player["hp"] = int(player["max_hp"] * 0.5)
                    for item in player["inventory"]:
                        if item["name"] == revive_item:
                            item["qty"] -= 1
                            if item["qty"] <= 0: player["inventory"].remove(item)
                            break
                    print(f"  [+] 复活羽毛触发！以 50% 生命复活！")
                    press_enter()
                else:
                    print(f"  {companion['name']}：「不！！！」")
                    slow_print(f"  {meme('doomed')}... Game Over...")
                    press_enter()
                    return "dead"
            print()
            press_enter()

        result = player_turn(player, companion, enemy)
        if result == "escaped":
            print()
            slow_print("[逃脱] 你使用了逃脱卷轴，成功逃离战斗！")
            press_enter()
            return "escaped"

        if enemy["hp"] <= 0:
            clear_screen()
            print()
            divider("=", 50)
            print(f"  [胜利] {enemy['name']} 被击败了！")
            divider("=", 50)
            draw_monster(enemy["name"])
            break

        print()
        press_enter()

        clear_screen()
        print()
        divider("=", 50)
        print(f"  [战斗] 第 {turn} 回合 -- 敌人行动")
        divider("=", 50)
        draw_monster(enemy["name"])
        print(f"  >> {enemy['name']} <<  生命: {max(0, enemy['hp'])}")
        print()
        enemy_turn(player, companion, enemy)

        if player["hp"] <= 0:
            revive_item = has_revive_item(player)
            if revive_item:
                print(f"\n  [阵亡] 你被击倒了...")
                slow_print(f"  [复活] 复活羽毛发出了光芒！")
                player["hp"] = int(player["max_hp"] * 0.5)
                for item in player["inventory"]:
                    if item["name"] == revive_item:
                        item["qty"] -= 1
                        if item["qty"] <= 0:
                            player["inventory"].remove(item)
                        break
                print(f"  [+] 你以 50% HP 复活了！继续战斗！")
            else:
                print(f"\n  [阵亡] {player['name']} 倒下了...")
                print(f"  {companion['name']}：「不！！！」")
                slow_print(f"  {meme('doomed')}... Game Over...")
                press_enter()
                return "dead"

        tick_buffs(player)
        tick_cooldowns(player)
        turn += 1
        print()
        press_enter()

        if turn > 30:
            slow_print(f"\n  [超时] 战斗时间过长，敌人逃跑了！")
            press_enter()
            return "timeout"

    if enemy["hp"] <= 0:
        print()
        divider("=", 50)
        print(f"  *** 战斗胜利！***")
        divider("=", 50)
        exp_gain = enemy["exp"] + random.randint(-5, 10)
        gold_gain = enemy["gold"] + random.randint(-5, 15)
        player["exp"] += max(1, exp_gain)
        player["gold"] += max(1, gold_gain)
        print(f"  EXP +{max(1, exp_gain)}  |  金币 +{max(1, gold_gain)}元")

        if random.random() < 0.3:
            drop_item = random.choice(["生命药水", "力量卷轴"])
            add_item(player, drop_item)

        if "first_blood" not in player["achievements"]:
            player["achievements"].add("first_blood")
            print(f"  [成就] 解锁：{ACHIEVEMENTS_DEF['first_blood']['name']}！")

        check_level_up(player)
        press_enter()
        return "victory"

    return "dead"

# ============================================================
# ============================================================

def dialogue_choice(player, companion, dialogue_key):
    """执行对话选择分支"""
    gender = player["gender"]
    dialogs = DIALOGUES.get(gender, {})
    dialogue = dialogs.get(dialogue_key)

    if not dialogue:
        return

    clear_screen()
    print()
    divider("-", 45)
    slow_print(f"[{dialogue['speaker']}]：")
    slow_print(dialogue["text"])
    divider("-", 45)

    print()
    for i, opt in enumerate(dialogue["options"], 1):
        print(f"  {i}. {opt['text']}")
    print()

    choice = get_int_input("  >> 你的回答 (1/2)：", 1, 2)
    chosen = dialogue["options"][choice - 1]

    print()
    slow_print(f"[{dialogue['speaker']}]：")
    slow_print(chosen["response"])

    player["bond"] += chosen["bond"]
    if player["bond"] > 10:
        player["bond"] = 10
    print(f"\n  [羁绊] +{chosen['bond']}（当前：{player['bond']}/10）")

    if player["bond"] >= 8 and "bond_master" not in player["achievements"]:
        player["achievements"].add("bond_master")
        print(f"  [成就] 解锁：{ACHIEVEMENTS_DEF['bond_master']['name']}！")

    press_enter()

# ============================================================
# ============================================================

def trigger_random_event(player, companion):
    """触发随机事件"""
    available_events = [e for e in RANDOM_EVENTS if e["title"] not in player["events_triggered"]]
    if not available_events:
        return

    event = random.choice(available_events)
    player["events_triggered"].add(event["title"])

    clear_screen()
    print()
    divider("*", 40)
    print(f"  {event['title']}")
    slow_print(f"  {event['desc']}")
    divider("*", 40)

    effect = event["effect"]

    if effect == "treasure":
        gold = random.randint(*event["gold"])
        player["gold"] += gold
        slow_print(f"  {event['text_good']} (+{gold}G)")

    elif effect == "heal":
        heal_amt = min(event["heal_amount"], player["max_hp"] - player["hp"])
        player["hp"] += heal_amt
        slow_print(f"  {event['text_good']}")

    elif effect == "discount_shop":
        slow_print(f"  {event['text_good']}")
        bonus_gold = 40
        player["gold"] += bonus_gold
        print(f"  [+] 获得折扣等值金币 +{bonus_gold}G！")

    elif effect == "trap":
        player["hp"] -= event["damage"]
        slow_print(f"  {event['text_bad']}")
        if player["hp"] <= 0:
            player["hp"] = 1
            print(f"  !! 你勉强撑住了！（HP保留1点）")

    elif effect == "exp_bonus":
        player["exp"] += event["exp"]
        slow_print(f"  {event['text_good']}")
        check_level_up(player)

    elif effect == "choice":
        print("\n  你会怎么做？")
        print("  1. 帮助他/她")
        print("  2. 装作没看见")
        sub_choice = get_int_input("  >> ", 1, 2)
        if sub_choice == 1:
            player["gold"] += event["choice_help"]["gold"]
            slow_print(f"  {event['choice_help']['text']}")
        else:
            slow_print(f"  {event['choice_ignore']['text']}")

    meme_titles = {"[宝箱] 神秘宝箱", "[温泉] 回复温泉", "[商人] 神秘商人", "[陷阱] 哥布林陷阱", "[石碑] 古老石碑", "[旅人] 迷路的旅人"}
    if meme_titles.issubset(player["events_triggered"]) and "meme_king" not in player["achievements"]:
        player["achievements"].add("meme_king")
        print(f"\n  [成就] 解锁：{ACHIEVEMENTS_DEF['meme_king']['name']}！")

    press_enter()

# ============================================================
# ============================================================

def play_chapter(player, companion, chapter_index):
    """执行一个章节"""
    chapter = CHAPTERS[chapter_index]
    player["chapter"] = chapter_index

    clear_screen()
    print()
    divider("◆", 50)
    print(f"  {chapter['title']}")
    print(f"  {chapter['subtitle']}")
    divider("◆", 50)
    print()
    slow_print(chapter["intro_text"])
    press_enter()

    if chapter["num_battles"] > 0 and chapter["enemy_pool"]:
        for battle_num in range(chapter["num_battles"]):
            enemy_template = random.choice(ENEMIES_BY_CHAPTER[chapter["enemy_pool"]])
            enemy = enemy_template.copy()
            result = battle(player, companion, enemy)

            if result == "dead":
                return "dead"
            elif result == "escaped":
                slow_print("你逃跑了，但这个敌人还在前方等着你…")
            elif result == "timeout":
                pass

            check_level_up(player)

    if chapter["has_shop"]:
        print()
        slow_print(f"[商店] 前方发现了一家冒险者商店！")
        print(f"{companion['name']}：「去看看有什么好东西吧！」")
        press_enter()
        enter_shop(player, companion)

    if chapter["has_event"]:
        trigger_random_event(player, companion)

    if chapter["has_boss"] and chapter["boss_pool"]:
        if chapter["id"] == "chapter2":
            dialogue_choice(player, companion, "before_boss")

        print()
        divider("!", 50)
        slow_print(f"!! Boss 战即将开始...")
        divider("!", 50)
        press_enter()

        boss_template = random.choice(ENEMIES_BY_CHAPTER[chapter["boss_pool"]])
        boss = boss_template.copy()
        result = battle(player, companion, boss)

        if result == "dead":
            return "dead"

        if chapter["id"] == "chapter2" and "boss_slayer" not in player["achievements"]:
            player["achievements"].add("boss_slayer")
            print(f"  [成就] 解锁：{ACHIEVEMENTS_DEF['boss_slayer']['name']}！")
            press_enter()

        if chapter["id"] == "chapter1":
            dialogue_choice(player, companion, "after_chapter1")

    return "continue"

# ============================================================
# ============================================================

def show_ending(player, companion):
    """显示结局"""
    clear_screen()
    print()
    divider("*", 55)
    print(f"           命运之契")
    divider("*", 55)
    print()
    slow_print(f"暗影之主在{player['name']}与{companion['name']}的羁绊之力面前…")
    slow_print("化为了一缕轻烟，彻底消散。")
    print()
    slow_print("光明重新照耀大地。")
    slow_print(f"两个" + meme("buddy") + "肩并肩站着，望着远方的日出。")
    print()

    dialogue_choice(player, companion, "ending")

    if "final_victory" not in player["achievements"]:
        player["achievements"].add("final_victory")
    if player["gold"] >= 200 and "rich" not in player["achievements"]:
        player["achievements"].add("rich")
    if len(player["inventory"]) >= 5 and "collector" not in player["achievements"]:
        player["achievements"].add("collector")

    print()
    if player["bond"] >= 8:
        divider("#", 50)
        slow_print(f"[彩蛋] 羁绊之力达到 {player['bond']}/10！")
        if player["gender"] == "male":
            slow_print(f"大壮：「兄弟！这辈子最好的冒险！下次咱们去更远的地方！」")
        else:
            slow_print(f"小晴：「……这次冒险，还不错。下次别让我等太久。」")
        divider("#", 50)
    else:
        slow_print(f"（羁绊值 {player['bond']}/10 - 友情的力量还在成长中…）")

    print()
    divider("-", 45)
    print("  [冒险成就]：")
    for ach_id in sorted(player["achievements"]):
        ach = ACHIEVEMENTS_DEF.get(ach_id)
        if ach:
            print(f"     [+] {ach['name']} -- {ach['desc']}")
    if not player["achievements"]:
        print("     （无）")
    divider("-", 45)

    print()
    divider("=", 45)
    print("  [最终统计]：")
    print(f"     角色：{player['class_data']['label']} {player['class']} Lv.{player['level']}")
    print(f"     羁绊：{player['bond']}/10 -- {companion['name']}")
    print(f"     金币：{player['gold']} 元")
    print(f"     背包道具：{len(player['inventory'])} 件")
    print(f"     成就：{len(player['achievements'])} 个")
    divider("=", 45)

    print()
    slow_print("╔══════════════════════════════════════╗")
    slow_print("║     感谢游玩《命运之契》！          ║")
    slow_print("║   " + meme("buddy") + "一生一起走，友谊长存！  ║")
    slow_print("╚══════════════════════════════════════╝")
    print()
    press_enter()

# ============================================================
# ============================================================

ENDLESS_ENEMIES = [
    {"name": "深渊史莱姆", "hp": 80, "attack": 18, "defense": 5, "exp": 50, "gold": 35, "desc": "来自深渊的变异史莱姆。",
     "attacks": [{"type": "physical", "damage": 18}, {"type": "poison", "damage": 14, "dot_turns": 3}]},
    {"name": "地狱哥布林", "hp": 120, "attack": 25, "defense": 8, "exp": 70, "gold": 50, "desc": "被地狱火淬炼过的哥布林战士。",
     "attacks": [{"type": "physical", "damage": 25}, {"type": "burn", "damage": 20, "dot_turns": 2}]},
    {"name": "暗影骑士", "hp": 180, "attack": 32, "defense": 12, "exp": 100, "gold": 80, "desc": "堕入黑暗的亡灵骑士。",
     "attacks": [{"type": "physical", "damage": 32}, {"type": "magic", "damage": 28}]},
    {"name": "炎魔", "hp": 250, "attack": 40, "defense": 15, "exp": 150, "gold": 120, "desc": "地狱深处的火焰恶魔。",
     "attacks": [{"type": "burn", "damage": 35, "dot_turns": 3}, {"type": "magic", "damage": 40}]},
    {"name": "毒龙", "hp": 300, "attack": 45, "defense": 18, "exp": 200, "gold": 160, "desc": "喷吐剧毒的远古龙族。",
     "attacks": [{"type": "poison", "damage": 38, "dot_turns": 4}, {"type": "physical", "damage": 45}]},
    {"name": "地狱之主", "hp": 500, "attack": 55, "defense": 25, "exp": 400, "gold": 300, "desc": "地狱门的最终统治者！",
     "attacks": [{"type": "physical", "damage": 55}, {"type": "magic", "damage": 48}, {"type": "burn", "damage": 42, "dot_turns": 3}, {"type": "poison", "damage": 38, "dot_turns": 4}]},
]

def endless_mode(player, companion):
    """无尽模式 - 地狱门"""
    clear_screen()
    print()
    divider("#", 55)
    print("          !! 地 狱 门 !!")
    divider("#", 55)
    print()
    slow_print("眼前的黑暗中，一道燃烧着的地狱之门缓缓打开...")
    slow_print(f"{companion['name']}：「这...这是什么东西？！太恐怖了吧！」")
    slow_print("你深吸一口气，握紧了武器。")
    slow_print("「既然来了，那就杀穿它！」")
    press_enter()

    wave = 1
    while True:
        enemy_template = random.choice(ENDLESS_ENEMIES)
        enemy = enemy_template.copy()
        scale = 1 + wave * 0.15
        enemy["hp"] = int(enemy["hp"] * scale)
        enemy["attack"] = int(enemy["attack"] * scale)
        enemy["defense"] = int(enemy["defense"] * scale)
        enemy["exp"] = int(enemy["exp"] * scale)
        enemy["gold"] = int(enemy["gold"] * scale)
        if "attacks" in enemy:
            for atk in enemy["attacks"]:
                atk["damage"] = int(atk["damage"] * scale)

        clear_screen()
        print()
        divider("!", 50)
        print(f"  无尽模式 - 第 {wave} 波")
        divider("!", 50)
        print(f"  敌人强度: x{scale:.1f}")
        press_enter()

        result = battle(player, companion, enemy)
        if result == "dead":
            print()
            divider("=", 45)
            slow_print(f"你在地狱门中坚持了 {wave} 波...")
            slow_print(f"最终等级: Lv.{player['level']} | 金币: {player['gold']} 元")
            slow_print("地狱之门缓缓关闭，但你知道——它还会再开的。")
            divider("=", 45)
            press_enter()
            return

        check_level_up(player)
        wave += 1

        heal_pct = random.randint(15, 30)
        player["hp"] = min(player["max_hp"], player["hp"] + int(player["max_hp"] * heal_pct / 100))
        companion["hp"] = min(companion["max_hp"], companion["hp"] + int(companion["max_hp"] * heal_pct / 100))
        print(f"\n  [+] 战后喘息：恢复了 {heal_pct}% 生命。")

        print()
        slow_print("一个神秘的旅商从虚空中出现...")
        print(f"{companion['name']}：「嘿！这里居然还有商人？？」")
        print("\n是否召唤商人购买补给？")
        print("  1. 是（随机商品）")
        print("  2. 否，继续战斗")
        shop_choice = get_int_input("  >> ", 1, 2)

        if shop_choice == 1:
            endless_shop(player, companion)

def endless_shop(player, companion):
    """无尽模式随机商店"""
    clear_screen()
    all_items = list(SHOP_ITEMS)
    random.shuffle(all_items)
    num_items = random.randint(4, min(8, len(all_items)))
    shop_pool = all_items[:num_items]

    print()
    divider("=", 50)
    print("  [虚空商人]  想要点什么？嘿嘿...")
    divider("=", 50)
    print(f"  {player['class_data']['label']} {player['name']}  Lv.{player['level']}")
    print(f"  生命: {player['hp']}/{player['max_hp']}  |  同伴: {companion['hp']}/{companion['max_hp']}")
    print(f"  金币: {player['gold']} 元  |  背包: {len(player['inventory'])}/{MAX_INVENTORY}")
    divider("-", 50)

    while True:
        print("  今日随机商品：")
        for i, item in enumerate(shop_pool, 1):
            item_data = ITEMS[item["name"]]
            print(f"  {i}. {item['label']} {item['name']}  --  {item_data['desc']}  |  {item['price']} 元")
        print(f"  0. 离开（继续战斗）")

        choice = input("\n  >> ").strip()
        if choice == "0":
            slow_print("商人：「下次再来哦，冒险者~」")
            press_enter()
            break

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(shop_pool):
                item = shop_pool[idx]
                if player["gold"] >= item["price"]:
                    if len(player["inventory"]) >= MAX_INVENTORY:
                        print(f"  !! 背包已满！")
                        continue
                    player["gold"] -= item["price"]
                    add_item(player, item["name"], 1)
                    print(f"  [+] 购买了 {item['label']} {item['name']}！剩余: {player['gold']} 元")
                else:
                    print(f"  !! 金币不足！需要 {item['price']} 元。")
            else:
                print("  !! 无效选项！")
        except ValueError:
            print("  !! 无效选项！")

# ============================================================
# ============================================================

def main():
    """主程序入口"""
    clear_screen()

    print()
    divider("★", 55)
    print(r"""
          ╔══════════════════════════════════╗
          ║    命  运  之  契                ║
          ║    Destiny Bonds                 ║
          ║                                  ║
          ║  一场关于友情与冒险的旅程…       ║
          ║  轻松幽默 · 回合制战斗 · 双线故事 ║
          ╚══════════════════════════════════╝
    """)
    divider("★", 55)
    print()
    slow_print("欢迎来到《命运之契》！")
    slow_print(f"在这里，你将遇到一生中最好的" + meme("buddy") + "。")
    slow_print("准备好了吗？冒险即将开始！")
    press_enter()

    player = create_character()

    companion = init_companion(player)
    companion_name = companion["name"]
    print()
    slow_print(f"\n{companion_name} 加入了你的队伍！")
    slow_print(f"   {COMPANION_STATS[companion_name]['tagline']}")
    press_enter()

    dialogue_choice(player, companion, "first_meet")

    for i in range(len(CHAPTERS)):
        result = play_chapter(player, companion, i)
        if result == "dead":
            print()
            divider("=", 40)
            slow_print("Game Over... 但冒险者的故事不会就此结束。")
            slow_print("重新开始，培养更强的羁绊吧！")
            divider("=", 40)
            press_enter()
            return

    show_ending(player, companion)

    print()
    divider("#", 50)
    slow_print("突然，地面剧烈震动...")
    slow_print("一道燃烧着的地狱之门在你面前缓缓打开！")
    slow_print(f"{companion['name']}：「这...这是传说中的地狱门？！」")
    divider("#", 50)
    print()
    print("是否进入无尽模式「地狱门」？")
    print("  1. 进入地狱门，挑战无尽深渊！")
    print("  2. 就此结束冒险")
    endless_choice = get_int_input("  >> ", 1, 2)

    if endless_choice == 1:
        endless_mode(player, companion)

# ============================================================
# ============================================================

if __name__ == "__main__":
    main()
