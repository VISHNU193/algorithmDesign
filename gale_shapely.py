# Preference lists for men
men_preferences = {
    'Victor': ['Bertha', 'Amy', 'Diane', 'Erika', 'Clare'],
    'Wyatt': ['Diane', 'Bertha', 'Amy', 'Clare', 'Erika'],
    'Xavier': ['Bertha', 'Erika', 'Clare', 'Diane', 'Amy'],
    'Yancey': ['Amy', 'Diane', 'Clare', 'Bertha', 'Erika'],
    'Zeus': ['Bertha', 'Diane', 'Amy', 'Erika', 'Clare']
}

# Preference lists for women
women_preferences = {
    'Amy': ['Zeus', 'Victor', 'Wyatt', 'Yancey', 'Xavier'],
    'Bertha': ['Xavier', 'Wyatt', 'Yancey', 'Victor', 'Zeus'],
    'Clare': ['Wyatt', 'Xavier', 'Yancey', 'Zeus', 'Victor'],
    'Diane': ['Victor', 'Zeus', 'Yancey', 'Xavier', 'Wyatt'],
    'Erika': ['Yancey', 'Wyatt', 'Zeus', 'Xavier', 'Victor']
}


def gale_shapely(m_pref:dict[str,list[str]],w_pref:dict[str,list[str]])->dict[str,str]:
    men_engaged=dict()
    women_engaged=dict()
    free_men= set(m_pref.keys())

    while free_men:
        man = free_men.pop()

        for woman in m_pref[man]:
            if woman not in women_engaged:
                men_engaged[man]=woman
                women_engaged[woman]=man

                break
            else:
                current_partner = women_engaged[woman]
                woman_pref = w_pref[woman]

                if woman_pref.index(current_partner) > woman_pref.index(man):

                    men_engaged[man]=woman
                    women_engaged[woman]=man

                    free_men.add(current_partner)

                    break
    return men_engaged
result = gale_shapely(men_preferences,women_preferences)
result = {key:result[key] for key in sorted(result.keys())}
print(result)



# def gale(m_pref:dict,w_pref:dict):
#     m_e = dict()
#     w_e = dict()
#     free_m = set(m_pref.keys())

#     while free_m:
#         man = free_m.pop()
        
#         for woman in m_pref[man]:
#             if woman not in w_e:
#                 m_e[man]=woman
#                 w_e[woman]=man
#                 break
#             else:
#                 c_p = w_e[woman]
#                 woman_pref = w_pref[woman]

#                 if woman_pref.index(c_p) > woman_pref.index(man):
#                     m_e[man]=woman
#                     w_e[woman]=man
#                     free_m.add(c_p)
#                     break


