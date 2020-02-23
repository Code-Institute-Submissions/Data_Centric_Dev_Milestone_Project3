{"filter":false,"title":"models.py","tooltip":"/models.py","undoManager":{"mark":52,"position":52,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":73},"action":"insert","lines":["from . import db","from flask_login import UserMixin","from werkzeug.security import generate_password_hash, check_password_hash"],"id":1}],[{"start":{"row":2,"column":73},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":16},"action":"remove","lines":["from . import db"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":3,"column":0},"end":{"row":5,"column":32},"action":"insert","lines":["class User:","    def __init__(self, username):","        self.username = username"],"id":6}],[{"start":{"row":5,"column":32},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":6,"column":0},"end":{"row":6,"column":8},"action":"insert","lines":["        "]},{"start":{"row":6,"column":8},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":7,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "],"id":8},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "],"id":9}],[{"start":{"row":7,"column":4},"end":{"row":8,"column":19},"action":"insert","lines":["def is_authenticated():","        return True"],"id":10}],[{"start":{"row":7,"column":25},"end":{"row":7,"column":26},"action":"insert","lines":["s"],"id":11},{"start":{"row":7,"column":26},"end":{"row":7,"column":27},"action":"insert","lines":["e"]},{"start":{"row":7,"column":27},"end":{"row":7,"column":28},"action":"insert","lines":["l"]},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["f"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"remove","lines":[" "],"id":12}],[{"start":{"row":6,"column":4},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":14},"action":"insert","lines":[" @property"],"id":14}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":[" "],"id":15}],[{"start":{"row":9,"column":19},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]},{"start":{"row":10,"column":8},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":17}],[{"start":{"row":11,"column":4},"end":{"row":17,"column":20},"action":"insert","lines":[" @staticmethod","    def is_active():","        return True","","    @staticmethod","    def is_anonymous():","        return False"],"id":18}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":[" "],"id":19}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":17},"action":"remove","lines":["staticmethod"],"id":20},{"start":{"row":11,"column":5},"end":{"row":11,"column":17},"action":"insert","lines":["staticmethod"]}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":17},"action":"remove","lines":["staticmethod"],"id":21},{"start":{"row":11,"column":5},"end":{"row":11,"column":13},"action":"insert","lines":["property"]}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":17},"action":"remove","lines":["staticmethod"],"id":22},{"start":{"row":15,"column":5},"end":{"row":15,"column":13},"action":"insert","lines":["property"]}],[{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"insert","lines":["s"],"id":23},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"insert","lines":["e"]},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"insert","lines":["l"]},{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"insert","lines":["f"]}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["s"],"id":24},{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["e"]},{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"insert","lines":["l"]},{"start":{"row":16,"column":24},"end":{"row":16,"column":25},"action":"insert","lines":["f"]}],[{"start":{"row":17,"column":20},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]},{"start":{"row":18,"column":8},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":19,"column":4},"end":{"row":19,"column":8},"action":"remove","lines":["    "],"id":26}],[{"start":{"row":19,"column":4},"end":{"row":20,"column":28},"action":"insert","lines":["def get_id(self):","        return self.username"],"id":27}],[{"start":{"row":20,"column":28},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]},{"start":{"row":21,"column":8},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":8},"action":"remove","lines":["    "],"id":29}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":[" "],"id":30},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["#"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["U"],"id":31},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["s"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["e"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["r"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["m"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["i"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["x"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["i"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":["m"],"id":32},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["M"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"],"id":33}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["("],"id":34}],[{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":[")"],"id":35}],[{"start":{"row":22,"column":1},"end":{"row":22,"column":2},"action":"remove","lines":[" "],"id":36}],[{"start":{"row":22,"column":1},"end":{"row":28,"column":59},"action":"insert","lines":[" def set_password(self, password):","        \"\"\"Create hashed password.\"\"\"","        self.password = generate_password_hash(password, method='sha256')","","    def check_password(self, password):","        \"\"\"Check hashed password.\"\"\"","        return check_password_hash(self.password, password)"],"id":37}],[{"start":{"row":22,"column":2},"end":{"row":22,"column":4},"action":"insert","lines":["  "],"id":38}],[{"start":{"row":21,"column":3},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":22,"column":0},"end":{"row":22,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":22,"column":3},"end":{"row":22,"column":5},"action":"insert","lines":["\"\""],"id":40}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":6},"action":"remove","lines":["   ","   \"\" "],"id":45}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["#"],"id":46}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["\"\""],"id":48}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["\""],"id":49}],[{"start":{"row":30,"column":61},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":50},{"start":{"row":31,"column":0},"end":{"row":31,"column":8},"action":"insert","lines":["        "]},{"start":{"row":31,"column":8},"end":{"row":32,"column":0},"action":"insert","lines":["",""]},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["        "]},{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["\""]},{"start":{"row":32,"column":9},"end":{"row":32,"column":10},"action":"insert","lines":["\""]},{"start":{"row":32,"column":10},"end":{"row":32,"column":11},"action":"insert","lines":["\""]}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"remove","lines":["    "],"id":51},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["#"],"id":52}],[{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["#"],"id":53}],[{"start":{"row":25,"column":9},"end":{"row":25,"column":12},"action":"remove","lines":["\"\"\""],"id":54}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":35},"action":"remove","lines":["\"\"\""],"id":55}],[{"start":{"row":29,"column":9},"end":{"row":29,"column":11},"action":"remove","lines":["\"\""],"id":56}],[{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"remove","lines":["\""],"id":57}],[{"start":{"row":29,"column":31},"end":{"row":29,"column":34},"action":"remove","lines":["\"\"\""],"id":58}]]},"ace":{"folds":[],"scrolltop":90,"scrollleft":0,"selection":{"start":{"row":32,"column":3},"end":{"row":32,"column":3},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":4,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1581533872425,"hash":"0f7112dc16c753dd839e35dc8d1a1360a315dfb8"}