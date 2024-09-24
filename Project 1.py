def filter_popular(reacts_2D, names, threshold):
    # Return users whose total engagement is greater than or equal to threshold.
    # i represents the index for lists in reacts_2D and also the index of names.
    popular_users = []
    for i in range(len(reacts_2D)):
        total_engagement = 0
        for engagement in reacts_2D[i]:
            total_engagement += engagement
        if total_engagement >= threshold:
            popular_users.append(names[i])
    return popular_users


def gather_engagement(names, reacts, grouping):
    # Return a 2D list with the names and engagement data for each of the users.
    # i represents the index of names and also represents the index of grouping.
    # j represents the index of all of the numbers in grouping iterated through.
    groups = []
    for i in range(len(names)):
        engagement_data = [names[i]]
        for j in range(grouping[i]):
            engagement_data.append(reacts.pop(0))
        groups.append(engagement_data)
    return groups


def clear_zeros(reacts_2D):
    # Return a 2D list which is clear of all zeros and empty lists in reacts_2D.
    # i represents the index of reacts_2D which contains many lists of integers.
    for i in range(len(reacts_2D)):
        while 0 in reacts_2D[i]:
            reacts_2D[i].remove(0)
    while [] in reacts_2D:
        reacts_2D.remove([])
    return reacts_2D


def form_reactions_list(react_dict1, react_dict2):
    # Return a 2D list which contains one of each reaction in both dictionaries.
    # If a reaction appears in both dictionaries, combine both of the reactions.
    reactions = []
    for reaction in react_dict1.keys():
        if reaction in react_dict2.keys():
            reaction_value = react_dict1[reaction] + react_dict2[reaction]
            reactions.append([reaction, reaction_value])
        else:
            reactions.append([reaction, react_dict1[reaction]])
    for reaction in react_dict2.keys():
        if reaction not in react_dict1.keys():
            reactions.append([reaction, react_dict2[reaction]])
    return reactions


def form_reactions_dict(reacts_2D):
    # Return a dictionary which contains the reactions from the list as keys and
    # their counts as values and also a total key that represents all reactions.
    # reaction[0] represents the key for reactions and reaction[1] is the value.
    reactions = {}
    total = 0
    for reaction in reacts_2D:
        reactions[reaction[0]] = reaction[1]
        total += reaction[1]
    reactions['total'] = total
    return reactions
