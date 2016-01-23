class Component(object):
    def __init__(self, c_name, c_data={}, **kwargs):

        self.dict = {}
        self.dict["name"] = c_name

        self.dict["data"] = c_data
        for key, value in kwargs.iteritems():
            self.dict["data"][key] = value

    def to_dict(self):
        return self.dict
