#Editor 2025 Gilbert_Hoi RPG Game
import random
#通過字典設定玩家角色屬性
player = {
    "name": "",
    "health": 100,    #生命值
    "attack": 10,     #攻擊力
    "defense": 5,     #基礎防御力
    "experience": 0,     #經驗值
    "special_attack": 20,   #強力攻擊
    "special_attack_countdown": 5     #大招倒計時
}
#通過串列和字典設定怪物角色屬性
enemies = [
    {"name": "IT小布林", "health": 50, "attack": 5, "defense": 0, "experience": 20},
    {"name": "大數據巨魔", "health": 120, "attack": 10, "defense": 5, "experience": 30},
    {"name": "AI魔龍", "health": 200, "attack": 15, "defense": 10, "experience": 50}
]
#列印角色狀態
def print_status():
    print("玩家:", player)
    print("怪物:")
    for enemy in enemies:
        print(enemy)
#隨機遇到怪物角色
def generate_random_enemy():
    return random.choice(enemies)
#運行一般攻擊及防御的生命值扣減
def perform_attack(attacker, defender):
    damage = max(0, attacker["attack"] - defender["defense"])  #使用 max的原因是減少if判斷防御力大過攻擊力,並且不會時做成反加血現象,
    defender["health"] -= damage
    return damage
#運行強力攻擊的生命值扣減
def special_attack(attacker, defender):
    damage = max(0, attacker["special_attack"] - defender["defense"])
    defender["health"] -= damage
    return damage
#運行戰鬥選項
def battle(enemy):
    while player["health"] > 0 and enemy["health"] > 0:
        print("--- 玩家 回合 ---")
        print("1. 攻擊")
        print("2. 防御")
        print("3. 閃避")
        if player["special_attack_countdown"] == 0:   #判斷是否可以使用強力攻擊
            print("4. 強力攻擊 (高傷害值)")
        choice = int(input("請選擇你的行動: "))

        if choice == 1:
            damage = perform_attack(player, enemy)
            print("你攻擊了", enemy["name"], "並做成", damage, "點傷害.")
        elif choice == 2:
            player["defense"] += 1
            print("你選擇了防御，防御值增加1.")
        elif choice == 3:
            evade_chance = random.randint(1, 10)
            if evade_chance <= 4:
                player["defense"] += 0.5
                print("你成功進行閃避怪物的攻擊，防御值增加0.5 .")
            else:
                damage = perform_attack(enemy, player)
                print("你閃避失敗. 怪物", enemy["name"], "攻擊你並做成,", damage, "點傷害.")
        elif choice == 4 and player["special_attack_countdown"] == 0:
            damage = special_attack(player, enemy)
            print("你使用了強力攻擊，並做成", damage, "點傷害.")
            player["special_attack_countdown"] = 5
        else:
            print("選擇錯誤. 請重選一遍.")
            continue
        #強力攻擊倒數減少1
        player["special_attack_countdown"] = max(0, player["special_attack_countdown"] - 1)
        #怪物被消滅
        if enemy["health"] <= 0:
            print("你打敗了", enemy["name"], "並獲得了", enemy["experience"], "點經驗值.")
            player["experience"] += enemy["experience"]
            enemies.remove(enemy)   # 在串列中刪除一個怪物
            break

        print("--- 怪物 回合 ---")
        damage = perform_attack(enemy, player)
        print(enemy["name"], "攻擊你並對你做成", damage, "點傷害.")
        #判定失敗條件
        if player["health"] <= 0:
            print("Game over! 你被怪物打敗!!")
            break
        print("\n--- 回合 結束 ---")
        print("玩家:", player)
        print("怪物:", enemy)
#用於循環執行的主程序函數/式
def main():
    player["name"] = input("請先輸入你的名字: ")
    while True:
        print("\n--- RPG Game ---")
        print_status()  #顯示狀態子程序

        if not enemies:
            print("恭喜你通關! 你擊敗了所有怪物，成功通關.")
            break

        print("\n按 'b' 鍵隨機出現一隻怪物並做行戰鬥　或'q'鍵退出戲.")
        choice = input("請輸入你的選擇: ")

        if choice == "b":
            enemy = generate_random_enemy()
            print("\n你遇到了一隻", enemy["name"], ". 開始進行戰鬥!")
            battle(enemy)    #戰鬥子程序
        elif choice == "q":
            print("離開遊戲...")
            break
        else:
            print("輸入錯誤，請重新輸入.")

if __name__ == "__main__":   # __main__執行主程式入口程序
    main()  #進入主子程序
