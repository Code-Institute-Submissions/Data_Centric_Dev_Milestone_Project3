{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":28,"position":28,"stack":[[{"start":{"row":12,"column":30},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":3902}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":52},"action":"insert","lines":["from flask_login import login_required, current_user"],"id":3903}],[{"start":{"row":95,"column":26},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":3904}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":15},"action":"insert","lines":["@login_required"],"id":3905}],[{"start":{"row":21,"column":20},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":3906}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":30},"action":"insert","lines":["login_manager = LoginManager()"],"id":3907}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["a"],"id":3908},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["p"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["p"]}],[{"start":{"row":13,"column":52},"end":{"row":13,"column":53},"action":"insert","lines":[","],"id":3909}],[{"start":{"row":13,"column":53},"end":{"row":13,"column":54},"action":"insert","lines":[" "],"id":3910},{"start":{"row":13,"column":54},"end":{"row":13,"column":55},"action":"insert","lines":["L"]},{"start":{"row":13,"column":55},"end":{"row":13,"column":56},"action":"insert","lines":["o"]},{"start":{"row":13,"column":56},"end":{"row":13,"column":57},"action":"insert","lines":["g"]},{"start":{"row":13,"column":57},"end":{"row":13,"column":58},"action":"insert","lines":["i"]},{"start":{"row":13,"column":58},"end":{"row":13,"column":59},"action":"insert","lines":["n"]}],[{"start":{"row":13,"column":54},"end":{"row":13,"column":59},"action":"remove","lines":["Login"],"id":3911},{"start":{"row":13,"column":54},"end":{"row":13,"column":66},"action":"insert","lines":["LoginManager"]}],[{"start":{"row":22,"column":33},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":3912}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":20},"action":"insert","lines":[".login_view = 'login"],"id":3913}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":13},"action":"insert","lines":["login_manager"],"id":3914}],[{"start":{"row":23,"column":33},"end":{"row":23,"column":34},"action":"insert","lines":["'"],"id":3915}],[{"start":{"row":13,"column":54},"end":{"row":13,"column":78},"action":"insert","lines":["login_user, logout_user,"],"id":3916}],[{"start":{"row":13,"column":78},"end":{"row":13,"column":79},"action":"insert","lines":[" "],"id":3917}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["£"],"id":3918}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["£"],"id":3919}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":3920}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["#"],"id":3921}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["#"],"id":3922}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"insert","lines":["#"],"id":3923}],[{"start":{"row":210,"column":3},"end":{"row":211,"column":74},"action":"remove","lines":[" if 'user_id' in session:   ","        _user = users_coll.find_one({\"_id\": ObjectId(session['user_id'])})"],"id":3924},{"start":{"row":210,"column":3},"end":{"row":211,"column":74},"action":"insert","lines":["if 'user_id' in session:   ","        _user = users_coll.find_one({\"_id\": ObjectId(session['user_id'])})"]}],[{"start":{"row":210,"column":3},"end":{"row":210,"column":4},"action":"insert","lines":[" "],"id":3925}],[{"start":{"row":210,"column":4},"end":{"row":211,"column":74},"action":"remove","lines":["if 'user_id' in session:   ","        _user = users_coll.find_one({\"_id\": ObjectId(session['user_id'])})"],"id":3926},{"start":{"row":210,"column":4},"end":{"row":211,"column":74},"action":"insert","lines":["if 'user_id' in session:   ","        _user = users_coll.find_one({\"_id\": ObjectId(session['user_id'])})"]}],[{"start":{"row":213,"column":68},"end":{"row":213,"column":69},"action":"insert","lines":[","],"id":3927}],[{"start":{"row":213,"column":69},"end":{"row":213,"column":70},"action":"insert","lines":[" "],"id":3928},{"start":{"row":213,"column":70},"end":{"row":213,"column":71},"action":"insert","lines":["u"]},{"start":{"row":213,"column":71},"end":{"row":213,"column":72},"action":"insert","lines":["s"]},{"start":{"row":213,"column":72},"end":{"row":213,"column":73},"action":"insert","lines":["e"]},{"start":{"row":213,"column":73},"end":{"row":213,"column":74},"action":"insert","lines":["r"]},{"start":{"row":213,"column":74},"end":{"row":213,"column":75},"action":"insert","lines":["="]}],[{"start":{"row":213,"column":75},"end":{"row":213,"column":76},"action":"insert","lines":["_"],"id":3929},{"start":{"row":213,"column":76},"end":{"row":213,"column":77},"action":"insert","lines":["u"]},{"start":{"row":213,"column":77},"end":{"row":213,"column":78},"action":"insert","lines":["s"]},{"start":{"row":213,"column":78},"end":{"row":213,"column":79},"action":"insert","lines":["e"]},{"start":{"row":213,"column":79},"end":{"row":213,"column":80},"action":"insert","lines":["r"]}],[{"start":{"row":78,"column":17},"end":{"row":78,"column":18},"action":"remove","lines":["4"],"id":3930},{"start":{"row":78,"column":17},"end":{"row":78,"column":18},"action":"insert","lines":["3"]}]]},"ace":{"folds":[],"scrolltop":5621.3333740234375,"scrollleft":0,"selection":{"start":{"row":78,"column":18},"end":{"row":78,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1582114582739,"hash":"e57ab544c803404022803d81503e2d6b72555c95"}