# imported libraries
import random
import time

# global variable
project = []
spotlight_showcase_list = []
dict_points = {}
projectid_list = []
top_project_detail = []
password = 'sarah123'
catagory = []


def option():  # to choice the options
    try:
        flag = True
        while flag:
            print('1-Adding Project Details (APD)', '2-Updating Project Details (UPD)',
                  '3-Deleting Project Details (DPD)',
                  '4-Viewing Project Details (VPD)', '5-Random Spotlight Selection (RSS)',
                  '6-Recording Awards and Recognitions (AWP)', '7-Exiting the Program (EXIT)', sep="\n")
            choice = int(input('enter the option: '))
            if choice == 1:
                apd()
            elif choice == 2:
                upd()
                continue
            elif choice == 3:
                dpd()
                continue
            elif choice == 4:
                vpd()
                continue
            elif choice == 5:
                rss()
                flag = False
            elif choice == 6:
                print('you can\'t select this option before random spot light selection ')
                continue
            elif choice == 7:
                exit_option = input('if you exit then you can\'t edit  or add the projects:(input yes or no): ').lower()
                print(exit_option)
                if exit_option == 'y' or exit_option == 'yes':
                    print('your going to exit from this command line menu')
                    time.sleep(1)
                    print('exited')
                    print('datas are stored in project_detail.text file  ')
                    break
                elif exit_option == 'n' or exit_option == 'no':
                    continue

            else:
                print('')
                print('option not available')
                print('')
        else:
            flag_2 = True
            while flag_2:
                print('1-Adding Project Details (APD)', '2-Updating Project Details (UPD)',
                      '3-Deleting Project Details (DPD)', '4-Viewing Project Details (VPD)',
                      '5-Random Spotlight Selection (RSS)', '6-Recording Awards and Recognitions (AWP)',
                      '7-Exiting the Program (EXIT)', sep="\n")
                choice = int(input('enter the option: '))
                if choice in [1, 2, 3, 4, 5]:
                    print('you can\'t select this option after random spot light selection ')
                elif choice == 6:
                    awp()

                elif choice == 7:
                    exit_option = input(
                        'if you exit then you can\'t edit  or add the projects:(input yes or no): ').lower()
                    print(exit_option)
                    if exit_option == 'y' or exit_option == 'yes':
                        print('your going to exit from this command line menu')
                        time.sleep(1)
                        print('exited')
                        print('datas are stored in project_detail.text file  ')
                        break
                    elif exit_option == 'n' or exit_option == 'no':
                        continue
                else:
                    print('')
                    print('option not available')
                    print('')
                    continue
    except Exception as e:
        print(f'the error is : {e}')
        option()


def short_nested_list():  # short
    for i in range(len(project)):
        for j in range(len(project) - 1):
            if int(project[j][0]) > int(project[j + 1][0]):
                store = project[j]
                project[j] = project[j + 1]
                project[j + 1] = store
    return project


def spd():  # save the project details into a text file
    try:
        if len(project) == 0:
            print('no project are added ')
            option()
        else:

            [catagory.append(project[pro][2]) for pro in range(len(project)) if project[pro][2] not in catagory]
            print(f'list of catagories: {catagory}')
            with open('project_detail.txt', 'w') as f:
                f.write('')

            for cat in range(len(catagory)):
                with open('project_detail.txt', 'a') as f:
                    f.write(' \n')
                    f.write(catagory[cat])
                    f.write('\n')

                    for i in range(len(project)):
                        if project[i][2] == catagory[cat]:
                            project_detail = f'projectID: {project[i][0]} | project_name: {project[i][1]} | category: {project[i][2]}| members_name: {project[i][3]}| description: {project[i][4]}  | country: {project[i][5]}'
                            f.write(project_detail)
                            f.write('\n')
    except Exception as e:
        print(f'the error is : {e}')
        option()


def apd():  # add the project detail
    try:
        project_id = input('enter the project ID: (ID must be 3 digits: 001-999): ')
        if len(project_id) == 3 and 1 <= int(project_id) <= 999:
            if project_id in projectid_list:
                print('project id already exist')
                apd()
            else:
                projectid_list.append(project_id)
        else:
            print('project ID must be 3 digits and it can\'t be null: 001-999')
            apd()
        # get project name (not null)
        times = 0
        while times < 1:
            project_name = input('enter the project name: ')
            times += 1
            if project_name == '':
                print('field can\'t be null')
                times -= 1
        # get project category (not null)
        times = 0
        while times < 1:
            category = input('enter the category of the project: ').lower()
            times += 1
            if category == '':
                print('field can\'t be null')
                times -= 1
        # get team member (not null)
        times = 0
        while times < 1:
            team_member = input('enter the team name of team members: (separated by coma) ').split(',')
            times += 1
            if team_member == '':
                print('field can\'t be null')
                times -= 1
        # get project description (not null)
        times = 0
        while times < 1:
            description = input('enter the description about the project: ')
            times += 1
            if description == '':
                print('field can\'t be null')
                times -= 1
        # get country (not null)
        times = 0
        while times < 1:
            country = input('enter the country: ')
            times += 1
            if country == '':
                print('field can\'t be null')
                times -= 1

        temp = [project_id, project_name, category, team_member, description, country]
        project.append(temp)
        short_nested_list()
        print(f'project detail is saving into text file ')
        print(f'adding to text file is progressing wait for 2 seconds')
        spd()
        print(f'project {project_id} added')
        time.sleep(2)
        print(project)
        print('')
        option()
    except Exception as e:
        print(f'the error is : {e}')
        option()


# deleting the project detail
def dpd():
    try:
        input_password = input('enter the password: ')
        if input_password == password:
            dlt_project_id = input('enter the ID of the project which you need to delete: ')
            for i in range(len(project)):
                if project[i][0] == dlt_project_id:
                    catagory.remove(project[i][2])
                    project.pop(i)
                    projectid_list.remove(dlt_project_id)
                    print(f'project detail is saving into text file ')
                    print(f'deleting from text file is progressing wait for 2 seconds')
                    spd()
                    print(f'project {dlt_project_id} deleted')
                    time.sleep(2)
                    print(project)
                    print('')

        else:
            print('invalid password')
            option()
            print('')
    except Exception as e:
        print(f'the error is: {e}')
        option()


def upd():  # update the project detail.
    try:
        input_password = input('enter the password: ')
        if input_password == password:
            upd_project_id = input('enter the ID of the project which you need to update: ')
            short_nested_list()
            for i in range(len(project)):
                if project[i][0] == upd_project_id:
                    project.pop(i)
                    project_id = upd_project_id
                    print(f'project id is {upd_project_id}')

                    times = 0
                    while times < 1:
                        project_name = input('enter the project name: ')
                        times += 1
                        if project_name == '':
                            print('field can\'t be null')
                            times -= 1

                    times = 0
                    while times < 1:
                        category = input('enter the category of the project: ').lower()
                        times += 1
                        if category == '':
                            print('field can\'t be null')
                            times -= 1

                    times = 0
                    while times < 1:
                        team_member = input('enter the team name of team members: (separated by coma) ').split(',')
                        times += 1
                        if team_member == '':
                            print('field can\'t be null')
                            times -= 1

                    times = 0
                    while times < 1:
                        description = input('enter the description about the project: ')
                        times += 1
                        if description == '':
                            print('field can\'t be null')
                            times -= 1

                    times = 0
                    while times < 1:
                        country = input('enter the country: ')
                        times += 1
                        if country == '':
                            print('field can\'t be null')
                            times -= 1

                    temp = [project_id, project_name, category, team_member, description, country]
                    project.insert(i, temp)
                    print(f'project detail is saving into text file ')
                    print(f'Updating  the text file is progressing wait for 2 seconds')
                    spd()
                    print(f'project {upd_project_id} updated')

                    time.sleep(2)
                    print(project)
                    print('')

        else:
            print('invalid password')
            print('')
            option()
    except Exception as e:
        print(f'the error is: {e}')
        option()


def vpd():  # view the data

    try:
        print('1 - view every projects details\n''2 - view particular project details')
        vdp_choice = int(input('enter your choice '))
        if vdp_choice == 1:
            with open('project_detail.txt', 'r') as f:
                for i in f:
                    if 'projectID: ' in i:
                        print(i)
            print(f'all project details are displayed')

        elif vdp_choice == 2:
            vpd_id = input('enter the project ID which you need to view: ')
            with open('project_detail.txt', 'r') as f:
                for i in f:
                    project_indexing = 'projectID: ' + vpd_id
                    if project_indexing in i:
                        print(i)


        else:
            print('invalid choice')

        time.sleep(2)
        print('')
    except Exception as e:
        print(f'the error is: {e}')
        option()


def rss():  # random select spotlight

    try:

        catagory_list = []
        catagories_projects_id = []

        # read the text file and group them according to there project catagories
        with open('project_detail.txt', 'r') as f:
            for i in f:
                if 'projectID: ' in i:
                    listofoneproject = i.split('|')
                    cat = listofoneproject[2][11::]
                    catagory_list.append(cat)

        # to remove the duplication
        catagories_of_project = []
        [catagories_of_project.append(i) for i in catagory_list if
         i not in catagories_of_project]  # list comprehension methode

        if len(catagories_of_project) >= 3:
            # create a  temp list and store same catagories program ID
            for i in catagories_of_project :
                temp_id = []
                with open('project_detail.txt', 'r') as f:
                    for j in f:
                        if 'projectID: ' in j:
                            listofoneproject = j.split('|')
                            if listofoneproject[2][11::] == i:
                                temp_id.append(listofoneproject[0][11::])
                # append to the nested list where we save project ID sort by project catagories
                catagories_projects_id.append(temp_id)

            # select the one random project id and make it into spotlight showcase
            for i in range(len(catagories_projects_id)):
                random_showcase_ID = random.choice(catagories_projects_id[i])
                spotlight_showcase_list.append(random_showcase_ID)
            print(f'selection on progress please waite for 2 seconds.......')
            time.sleep(2)
            print(f'selected projects ID for spotlight showcase are {spotlight_showcase_list}')
            print('')
            print('visualizing the leaderboard ')
        else:
            print('to do a further process we need at least 3 catagories')
            option()
    except Exception as e:
        print(f'the error is: {e}')
        option()


def awp():  # calculating points for selected project
    try:

        for p_id in spotlight_showcase_list:  # select one project from spotlight case to give points.
            tot_points = 0
            entry = 0
            judge_no = 0
            while entry < 4:  # get input from 4 judges and calculate tha point
                judge_point = 0
                judge_no += 1
                entry += 1
                points = input(f'enter the points of judge {judge_no} for project {p_id}: ')
                for i in points:
                    if i == '*' and len(points) <= 5:  # input must be "*" and maximum input = 5
                        judge_point += 1
                    else:
                        print('invalid points re enter it(input must be \'*\' and maximum number = 5)')
                        entry -= 1
                        judge_no -= 1
                        break
                tot_points += judge_point
            print(f'total points of project {p_id} is {tot_points} ')
            print('')
            time.sleep(2)
            dict_points[p_id] = tot_points

        list_item = list(dict_points.items())

        for i in range(len(list_item)):  # order the project according to their points
            for j in range(len(list_item) - 1):
                if int(list_item[j][1]) < int(list_item[j + 1][1]):
                    store = list_item[j]
                    list_item[j] = list_item[j + 1]
                    list_item[j + 1] = store

        print('calculating the points...')
        time.sleep(2)
        print('the  first, second and third place are goes to.....')
        time.sleep(1)
        print(f'3 rd place: {list_item[2][0]}')
        time.sleep(1)
        print(f'2 nd place: {list_item[1][0]}')
        time.sleep(2)
        print(f'1 st place: {list_item[0][0]}')
        time.sleep(2)
        print('')
        vap()
    except Exception as e:
        print(f'the error is: {e}')
        option()


def vap():
    try:
        # short the list_item list
        list_item = list(dict_points.items())
        for i in range(len(list_item)):  # order the project according to their points
            for j in range(len(list_item) - 1):
                if int(list_item[j][1]) < int(list_item[j + 1][1]):
                    store = list_item[j]
                    list_item[j] = list_item[j + 1]
                    list_item[j + 1] = store
        # retrieve the project details from text file and list the top 3 projects
        for p in range(3):
            with open('project_detail.txt', 'r') as f:
                for i in f:
                    project_indexing = 'projectID: ' + list_item[p][0]
                    if project_indexing in i:
                        top_project_detail.append(i.split('|'))
        space = 80
        # print the required things to visualisation
        for index in range(3):
            for r in range(int(list_item[index][1])):
                print(' ' * space + '*')

            for nested_index in range(1):

                print(
                    f'{' ' * (space - len(top_project_detail[index][1]) // 2)}{top_project_detail[index][1]}')
                print(
                    f'{' ' * (space - len(top_project_detail[index][5]) // 2)}{top_project_detail[index][5]}')
                if index == 0:
                    print(f'{" " * (space - len('1 st place') // 2)}1 st place')
                elif index == 1:
                    print(f'{" " * (space - len('2 nd place') // 2)}2 nd place')
                else:
                    print(f'{" " * (space - len('3 rd place') // 2)}3 rd place')
            print('')
            time.sleep(2)
    except Exception as e:
        print(f'the error is: {e}')
        option()


option()
