from model.project import Project


def test_add_group(app):
    app.session.login("administrator", "root")
    project = Project(project_name="test", status="development", view_status="public", description="test")
  #  old_project = db.get_project_list()
    app.project.add_project(project)
  #  new_project = db.get_project_list()
  #  old_project.append(project)
  #  assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
