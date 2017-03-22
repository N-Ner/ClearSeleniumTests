__author__ = 'Nazar Ner'

def test_scalr_farm(app):

    login = 'test@scalr.com'
    passw = '**********'
    containerid = '8104b4ffeb57'
    farmid = '9800012'

    app.farm.go_to_container(containerid)
    app.farm.login_user_accaunt(login, passw)
    app.farm.search(containerid, farmid)
    app.farm.search_quick_start()
    app.farm.add_role()
    app.farm.launch(containerid, farmid)
    
