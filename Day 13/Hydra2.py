input1 = """Nick Fury : Tony Stark, Maria Hill, Norman Osborn
Hulk : Tony Stark, HawkEye, Rogers
Rogers : Thor
Tony Stark: Pepper Potts, Nick Fury
Agent_13 : Agent-X, Nick Fury, Hitler
Thor: HawkEye, BlackWidow
BlackWidow:Hawkeye
Maria Hill : Hulk, Rogers, Nick Fury
Agent-X : Agent_13, Rogers
Norman Osborn: Tony Stark, Thor"""

lv10 = "Nick Fury"
dataset = {}
for each in input1.split("\n"):
    tmp = each.split(":")
    dataset[tmp[0].strip()] = tmp[1].strip().split(", ")
# print(dataset)


def hydra_agents(d1, lvl):
    hydra_members, shield_members, agents = set(), set(), [lvl]

    while len(agents) > 0:
        current = agents.pop()
        shield_members.add(current)

        if current in d1:
            for agent in d1[current]:
                if agent not in shield_members:
                    agents.append(agent)

    for sender in d1.keys():
        if sender not in shield_members:
            hydra_members.add(sender)

        for receiver in d1[sender]:
            if receiver not in shield_members:
                hydra_members.add(receiver)

    return hydra_members


x = (hydra_agents(dataset, lv10))

list1 = list(x)

for each in list1:
    print(each, end=", ")
