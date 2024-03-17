import os
import yaml


class Handleyaml(object):
    def __init__(self, yaml_file):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 基础路径
        self.yaml_path = os.path.join(self.base_dir, 'main', yaml_file)

    def read_yaml(self, section, option):
        """读取配置文件中的数据"""
        with open(self.yaml_path, encoding='utf-8') as one_file:
            self.res_data = yaml.full_load(one_file)
            return self.res_data[section][option]

    @staticmethod
    def write_yaml(yamlname, YamlDatas):
        yaml_path = os.path.join(CONFIGS_DIR,yamlname)
        """使用yaml方法将数据写入到配置文件中"""
        with open(yaml_path, 'w', encoding='utf-8') as w_file:
            yaml.dump(YamlDatas, w_file, allow_unicode=True)

    def change_yaml(self,section, option,up_data):
        """
        修改yaml文件中的某个参数
        :param section:
        :param option:
        :param up_data:
        :return:
        """
        self.read_yaml(section, option)
        content = self.res_data
        content[section][option] = up_data
        with open(self.yaml_path, 'w', encoding="utf-8") as nf:
            yaml.dump(content, nf, allow_unicode=True)



if __name__ == "__main__":
    data = {
            'Europe':{"country": "奥地利"},
            'city':{'cityname': '维也纳','celebrity': '莫扎特','telent': '音乐'}
          }
    do_yaml = Handleyaml(r'config.yaml')
    a = do_yaml.read_yaml('path', 'images_file')
    print(a)
