from model.project import Project


def test_add_group(app, db):
    # app.session.login("administrator", "root")
    project = Project(project_name="test4", status="development", view_status="public", description="test")
    old_project = db.get_project_list()
    app.project.add_project(project)
    print()
    print("--------------", old_project, "--------------------")
    new_project = db.get_project_list()
    print("--------------", new_project, "--------------------")
    old_project.append(project)
    print("--------------", old_project, "--------------------")
  #  assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
