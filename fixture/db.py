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
        else: return None

    def meeting_viev_status(self, status):
        if status == 10: return "public"
        elif status == 50: return "private"
        else: return None

    def meeting_inherit_global_categories(self, status):
        if status == 1: return True
        else: return False

    def get_project_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, enabled, view_state, description from mantis_project_table")
            for row in cursor:
                (id, name, status, enabled, view_state, description) = row
                list.append(Project(id=str(id), project_name=name, status=self.meeting_status(status),
                                    inherit_global_categories=self.meeting_inherit_global_categories(enabled),
                                    view_status=self.meeting_viev_status(view_state), description=description))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
