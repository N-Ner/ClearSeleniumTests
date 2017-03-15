__author__ = 'Nazar Ner'

def test_scalr_farm(app):
    login = 'test@scalr.com'
    passw = '**********'
    containerid = '8104b4ffeb57'
    farmid = '9800012'
    farmrole = 'base-ubuntu1404'
    #Uncomment the line for Scope settings
    #scope = "img[data-qtip='This Role is defined in the Scalr Scope']"
    #scope = "img[data-qtip='TThis Role is defined in the Account Scope']"
    scope = "img[data-qtip='This Role is defined in the Environment Scope']"

    app.farm.go_to_container(containerid)
    app.farm.login_user_accaunt(login, passw)
    app.farm.search(containerid, farmid)
    app.farm.search_by_field(farmrole, scope)
    app.farm.add_role()
    app.farm.launch(containerid, farmid)