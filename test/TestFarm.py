__author__ = 'Nazar Ner'

def test_scalr_farm(app):

    containerid = '8104b4ffeb57'
    farmid = '9800012'

    app.farm.go_to_container(containerid)
    app.farm.login_user_accaunt()
    app.farm.goto_list()
    app.farm.search(containerid, farmid)
    app.farm.add_role()
    app.farm.launch(containerid, farmid)


