def search(all_courses, student_courses, last_name):

    def in_course(student_course, course):
        return student_course.upper() in course.upper()

    def name_in_section(section, ln=last_name):
        if '-' in section:
            n = section.split(' - ')  # section = 'K - SH'
            # some sections may have lecture code too (i.e. 'L0201  K - SH')
            n[0] = n[0].split('  ')[1] if '  ' in n[0] else n[0]
            return n[0].upper() <= ln.upper() <= n[1].upper()
        return True

    def lecture_in_section(student_course, section):
        # section has a lecture code if
        #   it has a name range (a dash) and a double space, 'L0201  K - SH'
        #   it has no name range (no dash), 'L0201'
        # student_course has a lecture code if it has a dash, 'ECO100-L0201'
        if ('  ' in section or '-' not in section) and '-' in student_course:
            section_lecture, student_lecture = \
                section.split('  ')[0], student_course.split('-')[1]
            return section_lecture.lower() == student_lecture.lower()
        return True

    def in_section(student_course, section):
        return name_in_section(section) \
            and lecture_in_section(student_course, section)

    def is_match(c):
        return in_course(c[1].split('-')[0], c[0]['course']) \
            and in_section(c[1], c[0]['section'])

    return [course
            for course, student_course in
            filter(is_match, [(c, sc)
                   for sc in student_courses
                   for c in all_courses])]
