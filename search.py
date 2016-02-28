from pprint import pprint


def search(all_courses, user_courses, last_name):

    def name_in_section(name, section):
        # TODO parsing for course sections that include
        # section code i.e. L5101 WE - Z
        if '-' in section:
            section = section.split(' - ')
            if len(section) == 2:
                return section[0] <= name.upper() <= section[1]
        return True

    def is_match(c, ln=last_name):
        return c[1] in c[0]['course'].upper() \
               and name_in_section(ln, c[0]['section'])

    def remove_dupes(l):
        new = []
        [new.append(obj) for obj in l if obj not in new]
        return new

    return remove_dupes([c0
                        for c0, c1 in
                        filter(is_match, [(c0, c1)
                               for c1 in user_courses
                               for c0 in all_courses])])
