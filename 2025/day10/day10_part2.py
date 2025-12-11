import re
from itertools import combinations_with_replacement

def parse_light_diagram(str):
    return [c == "#" for c in str]


def parse_button_schematic(str):
    schematics = str.split(" ")
    schematics = [s.strip("()") for s in schematics]
    button_schematics = []
    for schematic in schematics:
        button_schematics.append(tuple([int(x) for x in schematic.split(",")]))
    return button_schematics


def parse_joltage_requirement(str):
    return tuple([int(x) for x in str.split(",")])


all_light_diagrams = []
all_button_schematics = []
all_joltage_reqs = []
pattern = r"\[(.+)\]\s*\((.+)\)\s*\{(.*)\}"
with open("example.txt", "r") as f:
    for line in f:
        match = re.search(pattern, line.strip())
        if not match:
            continue
        all_light_diagrams.append(parse_light_diagram(match.group(1)))
        all_button_schematics.append(parse_button_schematic(match.group(2)))
        all_joltage_reqs.append(parse_joltage_requirement(match.group(3)))


def press_button(light_diagram, button_schematic):
    for button in button_schematic:
        light_diagram[button] = not light_diagram[button]
    return light_diagram


def press_buttons(light_diagram, button_schematics):
    new_light_diagram = light_diagram.copy()
    for button_schematic in button_schematics:
        new_light_diagram = press_button(new_light_diagram, button_schematic)
    return new_light_diagram


def get_shortest_button_presses(light_diagram, button_schematics):
    for j in range(len(button_schematics)):
        for button_presses in combinations_with_replacement(button_schematics, j):
            new_light_diagram = press_buttons(light_diagram, button_presses)
            if new_light_diagram == [False] * len(new_light_diagram):
                return j, button_presses
    return -1, []

N = len(all_light_diagrams)
total_num_buttons = 0
for i in range(N):
    light_diagram = all_light_diagrams[i]
    button_schematics = all_button_schematics[i]
    joltage_requirement = all_joltage_reqs[i]
    # print(
    #     f"\nLight Diagram: {light_diagram}, \nButton Schematics: {button_schematics}, \nJoltage Requirement: {joltage_requirement}"
    # )
    num_buttons, button_presses = get_shortest_button_presses(light_diagram, button_schematics)
    # print(f"{num_buttons} Button Presses: {button_presses}")
    total_num_buttons += num_buttons

print(f"Total Number of Buttons: {total_num_buttons}")

import numpy as np
from scipy.optimize import linprog

A_eq = np.array([
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 0],
])
b_eq = np.array([3, 5, 4, 7])
c = np.ones(6)  # minimize sum of x

result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
print(result.x)
print(f"Minimum sum: {result.fun}")
