# You are given an array power[] where each element represents the damage of an attack.
# You are also given a single-use armor with a value armor that can block up to min(armor, damage) for one attack.
# The goal is to calculate the minimum initial health required to survive all attacks.

# 1. Without using the armor, the total health required is the sum of all attack values in power[].
#
# 2. Using the armor optimally:
#
# It should block the maximum possible damage. Hence, we apply it to the attack with the largest damage.
# Subtract min(armor, max_damage) from the total health requirement.
# Formula:
#
# 3. Minimum Initial Health = sum(power) - min(armor, max(power))

def minimum_initial_health(power, armor):
    total_damage = sum(power)
    max_damage = max(power)
    blocked_damage = min(armor, max_damage)

    return total_damage - blocked_damage


# Example usage
power = [1, 2, 6, 7]
armor = 5
print(minimum_initial_health(power, armor))  # Output: 11
