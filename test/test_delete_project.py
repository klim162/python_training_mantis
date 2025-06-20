import random
from model.project import Project


def test_delete_project_by_id(app, db):
    if len(db.get_project_list()) == 0:
        app.project.add_project(Project(project_name="test"))
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    old_project.remove(project)
    new_project = db.get_project_list()
    assert old_project == new_project
