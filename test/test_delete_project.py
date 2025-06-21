import random
from model.project import Project


# def test_delete_project_by_id_db(app, db):
#     if len(db.get_project_list()) == 0:
#         app.project.add_project(Project(project_name="test"))
#     old_project = db.get_project_list()
#     project = random.choice(old_project)
#     app.project.delete_project_by_id(project.id)
#     old_project.remove(project)
#     new_project = db.get_project_list()
#     assert old_project == new_project

def test_delete_project_by_id_soap(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.add_project(Project(project_name="test"))
    old_project = app.soap.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    old_project.remove(project)
    new_project = app.soap.get_project_list()
    assert old_project == new_project
