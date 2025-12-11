import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


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
with open("input.txt", "r") as f:
    for line in f:
        match = re.search(pattern, line.strip())
        if not match:
            continue
        all_light_diagrams.append(parse_light_diagram(match.group(1)))
        all_button_schematics.append(parse_button_schematic(match.group(2)))
        all_joltage_reqs.append(parse_joltage_requirement(match.group(3)))


def build_A_eq(button_schematics, m, n):
    A_eq = np.zeros((n, m))
    for i, button_schematic in enumerate(button_schematics):
        for button in button_schematic:
            A_eq[i, button] = 1
    return A_eq.T


N = len(all_light_diagrams)
total_num_buttons = 0
for i in range(N):
    light_diagram = all_light_diagrams[i]
    button_schematics = all_button_schematics[i]
    joltage_requirement = all_joltage_reqs[i]
    # print(
    #     f"\nLight Diagram: {light_diagram}, \nButton Schematics: {button_schematics}, \nJoltage Requirement: {joltage_requirement}"
    # )
    m = len(joltage_requirement)
    n = len(button_schematics)
    A_eq = build_A_eq(button_schematics, m, n)
    b_eq = np.array(joltage_requirement)
    c = np.ones(n)
    constraints = [LinearConstraint(A_eq, b_eq, b_eq)]
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(n)
    button_presses = milp(
        c, constraints=constraints, bounds=bounds, integrality=integrality
    )
    num_buttons = button_presses.fun
    # print(f"{num_buttons} Button Presses: {button_presses.x}")
    total_num_buttons += num_buttons

print(f"Total Number of Buttons: {total_num_buttons}")
