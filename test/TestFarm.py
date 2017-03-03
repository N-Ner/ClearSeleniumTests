__author__ = 'Nazar Ner'

def test_scalr_farm(app):

    containerid = '8104b4ffeb57'
    farmid = '9800012'

    app.farm.go_to_container(containerid)
    app.farm.login_user_accaunt()
    app.farm.goto_farms_list()
    app.farm.search_farm(containerid, farmid)
    app.farm.add_farm_role()
    app.farm.launch_farm(containerid, farmid)


