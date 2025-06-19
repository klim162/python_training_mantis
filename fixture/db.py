import pymysql.cursors
from model.project import Project


class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def meeting_status(self, status):
        if status == 10: return "development"
        elif status == 30: return "release"
        elif status == 50: return "stable"
        elif status == 70: return "obsolete"
        else: renurn None

    def meeting_viev_status(self, status):
        if status == 10: return "public"
        elif status == 30: return "release"
        elif status == 50: return "stable"
        elif status == 70: return "obsolete"
        else: renurn None

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, enabled, view_state, access_min from mantis_project_table")
            for row in cursor:
                (id, name, status, enabled, view_state, access_min) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()