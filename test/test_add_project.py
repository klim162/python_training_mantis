from model.project import Project


def test_add_group(app):
    project = Project(project_name="test", status="developmen", view_status="public", description="test")
  #  old_project = db.get_project_list()
    app.project.create(project)
  #  new_project = db.get_project_list()
  #  old_project.append(project)
  #  assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
