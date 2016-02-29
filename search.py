from pprint import pprint


def search(all_courses, user_courses, last_name):

    def in_course(course_code, user_course):
        return user_course.upper() in course_code.upper()

    def name_in_section(name, section):
        if '-' in section:
            sec = section.split(' - ')  # section = 'K - SH'
            # some sections may have lecture code too (i.e. 'L0201 K - SH')
            sec[0] = sec[0].split('  ')[1] if '  ' in sec[0] else sec[0]
            return sec[0] <= name.upper() <= sec[1]
        return True

    def lecture_in_section(course_code, section):
        # sections with lecture codes have a double space
        # sections without names have no dash
        # course codes with a specified lecture will have a dash
        if ('  ' in section or '-' not in section) and '-' in course_code:
            lecture, user_lecture = section.split('  ')[0], \
                course_code.split('-')[1]
            return lecture.lower() == user_lecture.lower()
        return True

    def is_match(c, ln=last_name):
        return in_course(c[0]['course'], c[1].split('-')[0]) \
               and name_in_section(ln, c[0]['section']) \
               and lecture_in_section(c[1], c[0]['section'])

    return [c0
            for c0, c1 in
            filter(is_match, [(c0, c1)
                   for c1 in user_courses
                   for c0 in all_courses])]
