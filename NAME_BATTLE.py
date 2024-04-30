def name_battle(attacker, target):
    """
    The purpose of this function is to simulate a battle in a
    parallel universe in which, when a person attacks another person (the
    target) by absorbing letters in the target's name that match the
    attacker's name, and the percentage of letters left over gives
    the current life-force level of the target
    """

    target_list = list(target)

    for l in list(attacker):
        if l in target_list: target_list.remove(l)

    health = 100.0*len(target_list)/len(target)

    return (target_list, health)


