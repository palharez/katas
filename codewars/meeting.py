def meeting(s):
    names = s.upper().split(';')

    inverted_by_last_name = []

    for name in names:
        splited_name = name.split(':')
        inverted_by_last_name.append((splited_name[-1], splited_name[0]))

    sorted_by_last_name = sorted(inverted_by_last_name, key=lambda name: name[0])

    parsed_names = []

    for name in sorted_by_last_name:
        parsed_names.append("(%s, %s)" % (name[0], name[1]))

    return "".join(parsed_names)



if __name__ == '__main__':
    # print(meeting("Alex:Arno;Alissa:Cornwell;Sarah:Bell;Andrew:Dorries;Ann:Kern;Haley:Arno;Paul:Dorny;Madison:Kern"),
    #     "(ARNO, ALEX)(ARNO, HALEY)(BELL, SARAH)(CORNWELL, ALISSA)(DORNY, PAUL)(DORRIES, ANDREW)(KERN, ANN)(KERN, MADISON)")

    print(meeting("Michael:Steve;Ann:Dorny;Megan:Arno;Emily:Arno;Victoria:Gates;Jacob:Meta;Abba:Kern;Sarah:Korn;Elizabeth:Bel"))