import random


def test_delete_project_by_id(app, db):
    old_project = db.get_project_list()
    project = random.choice(old_project)
    app.project.delete_project_by_id(project.id)
    new_project = db.get_project_list()
    print()
    print("--------------", old_project, "--------------------")
    print("--------------", new_project, "--------------------")
    old_project.remove(project)
    print("--------------", old_project, "--------------------")