from model.project import Project


# def test_add_group_bd(app, db):
#     project = Project(project_name="test1", status="development", view_status="public", description="test")
#     old_project = db.get_project_list()
#     search_project = next((i for i in old_project if i.project_name == project.project_name), None)
#     if search_project:
#         app.project.delete_project_by_id(search_project.id)
#     else:
#         old_project.append(project)
#     app.project.add_project(project)
#     new_project = db.get_project_list()
#     assert old_project == new_project

def test_add_group_soap(app):
    project = Project(project_name="test1", status="development", view_status="public", description="test")
    old_project = app.soap.get_project_list()
    search_project = next((i for i in old_project if i.project_name == project.project_name), None)
    if search_project:
        app.project.delete_project_by_id(search_project.id)
    else:
        old_project.append(project)
    app.project.add_project(project)
    new_project = app.soap.get_project_list()
    assert old_project == new_project
