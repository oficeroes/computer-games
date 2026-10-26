import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout

from destiny_bonds_rpg import enemy_intent_text, enemy_turn


class EnemyIntentTests(unittest.TestCase):
    def test_poison_intent_includes_damage_and_duration(self):
        text = enemy_intent_text(
            {"name": "哥布林", "attack": 15},
            {"type": "poison", "damage": 12, "dot_turns": 3},
        )
        self.assertIn("毒液攻击", text)
        self.assertIn("中毒 3 回合", text)
        self.assertIn("12", text)

    def test_physical_intent_warns_that_companion_may_be_targeted(self):
        text = enemy_intent_text(
            {"name": "狼", "attack": 18}, {"type": "physical", "damage": 18}
        )
        self.assertIn("普通攻击", text)
        self.assertIn("你或同伴", text)

    def test_enemy_turn_uses_the_previewed_move(self):
        player = {"hp": 100, "defense": 0, "buffs": [], "debuffs": []}
        companion = {"name": "同伴", "hp": 50, "defense": 0}
        enemy = {
            "name": "敌人",
            "attack": 10,
            "attacks": [{"type": "physical", "damage": 10}],
        }
        previewed = {"type": "poison", "damage": 12, "dot_turns": 3}
        output = io.StringIO()

        with patch("destiny_bonds_rpg.random.choice", return_value="player") as choose:
            with redirect_stdout(output):
                enemy_turn(player, companion, enemy, planned_attack=previewed)

        choose.assert_called_once_with(["player", "companion"])
        self.assertIn("敌人·毒素", output.getvalue())
        self.assertEqual(player["debuffs"][0]["type"], "poison")


if __name__ == "__main__":
    unittest.main()
