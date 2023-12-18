with open('students.txt', 'r') as rf:
        names = rf.readlines()
        sorted_names = sorted(names)
        
        with open('students.txt', 'w') as wf:
            for name in sorted_names:
                 wf.writelines(name)