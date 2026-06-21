#Editor 2025 Gilbert_Hoi RPG Game
import random #導入隨機數庫

# 定義怪物"列表/串列list"(使用"字典dictionary"對應名稱及相關屬性)
monsters = [
    {"名稱": "IT史萊姆", "生命": 20, "攻擊": 5, "閃避": 0.3},
    {"名稱": "IT哥布林", "生命": 50, "攻擊": 15, "閃避": 0.1},
    {"名稱": "IT巨魔", "生命": 100, "攻擊": 20, "閃避": 0.05}
]

# 玩家初始屬性
player_life = 100  #生命值
player_attack = 20  #攻擊力
player_defense = 0.1  #防禦值
player_dodge = 0.15  #閃避值

# 遊戲開始
print("一隻可怕的怪物出現了！")
print("^^|___|^^")
print(" !|-_-|! ")
print("  |~~~|  ")
print("你要與之戰鬥嗎？")

while True:  #使用while True進入遊戲的循環中
    monster = random.choice(monsters) # 從列表/串列list中，隨機取出一個項目隨機選擇一個值"怪物"
    # 以下是玩家回合內容
    print("\n你的回合到了：")
    print("你的生命值：", player_life)
    print("敵人:",monster["名稱"])
    print("怪物的生命值：", monster["生命"])
    print("1. 攻擊")
    print("2. 防禦")
    print("3. 逃跑")
    
    Pchoice = input("請選擇你的行動：")
    
    if Pchoice == "1":
        # player選擇攻擊
        if random.random() > monster["閃避"]:   # 使用random.random()產生0.1-1的隨機數
            damage = player_attack - (player_attack * monster["閃避"])   #傷害值的計算
            monster["生命"] -= damage
            print("你對怪物造成了", damage, "點傷害！")
        else:
            print("怪物閃避了你的攻擊！")       #如果數值少於閃避值則完全閃避攻擊
    elif Pchoice == "2":
        # player選擇防禦
        player_defense += 0.1
        print("你進入防禦狀態，你的防禦力提升！")
    elif Pchoice == "3":
        print("你逃跑了，遊戲結束！")
        break
    else:
        print("請輸入有效的選項！")
        continue
    
    if monster["生命"] <= 0:
        print("你擊敗了IT怪物，獲得勝利！Y^_^Y ")
        break
    
    # 怪物回合
    print("\n怪物回合：")
    print("你的生命值：", player_life)
    print("怪物的生命值：", monster["生命"])
    
    if random.random() > player_dodge:   # 使用random.random()產生0.1-1的隨機數
        damage = monster["攻擊"] - (monster["攻擊"] * player_defense)   #Player受傷害計算,當player防禦力高於1時,則不會再受傷害
        player_life -= damage
        print("怪物對你造成了", damage, "點傷害！")
    else:
        print("你閃避了怪物的攻擊！")     #如果數值少於閃避值則完全閃避攻擊
    print("="*30)
    if player_life <= 0:
        print("你被怪物擊敗了，遊戲結束！X_X ")
        print("="*30)
        break