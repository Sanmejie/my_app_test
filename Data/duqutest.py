import os
import yaml


class Op_Data:

    def __init__(self, file_name):
        self.file_path = os.getcwd() + os.sep + file_name

    def read_yaml(self):
        # 读yaml
        with open(self.file_path, "r", ) as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def write_yaml(self, data):
        # 写yaml
        with open(self.file_path, "w") as f:
            return yaml.dump(data, f)


def get_data():
    # 读取返回数据
    data_list = []
    # data数据为大列表包含大字典包小字典
    data = Op_Data("data.yml").read_yaml().get("Login_data")
    for i in data:
        for o in i.keys():
            data_list.append((o, i.get(o).get("phone"), i.get(o).get("passwd"),
                              i.get(o).get("get_mess"), i.get(o).get("expect_message"),
                              i.get(o).get("tag")))
    return data_list


print(Op_Data("data.yml").read_yaml().get("Login_data"))
print(get_data())
print(os.getcwd())
