from model.project import Project
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_proj_create_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_create_page.php")):
            wd.find_element(By.LINK_TEXT, "Manage").click()
            wd.find_element(By.LINK_TEXT, "Manage Progects").click()
            wd.find_element(By.CSS_SELECTOR, "input.button-small[value='Create New Project']").click()

    def filling_project_form(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, "name").click()
            wd.find_element(By.NAME, "name").clear()
            wd.find_element(By.NAME, "name").send_keys(text)

    def fild_select_list(self, fild_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, fild_name).click()
            Select(wd.find_element(By.NAME, fild_name)).select_by_visible_text(text)

    def clic_chackbox(self, inherit_global_categories):
        wd = self.app.wd
        checkbox = wd.find_element(By.NAME, "inherit_global")
        if inherit_global_categories and not checkbox.is_selected():
            wd.find_element(By.NAME, "inherit_global").click()

    def filling_fields(self, project):
        wd = self.app.wd
        self.filling_project_form("name", project.project_name)
        self.fild_select_list("status", project.status)
        self.clic_chackbox(project.inherit_global_categories)
        self.fild_select_list("view_state", project.view_status)
        self.filling_project_form("description", project.description)

    def add_project(self, project):
        wd = self.app.wd
        self.open_manage_proj_create_page()
        self.filling_fields(project)
        wd.find_element(By.CSS_SELECTOR, "input.button[value='Add Project']").click()
