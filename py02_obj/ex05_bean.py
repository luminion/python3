
class Student(object):
    def __init__(self, name, age , sex):
        self.name = name # 公有属性, 任何地方都可以访问/修改 
        self._age = age # 保护属性 仅作为规范,提示该变量不要直接使用, 实际还是能访问/修改
        self.__sex = sex # 私有属性, 仅有本类可以访问, 实际上该类会自动生成一个属性, 名为 _Student__sex, 可以通过该属性访问/修改
    # getter, 使用@property装饰器, 可以将方法当做属性使用, 可以在方法中添加逻辑, 例如判断参数是否合法
    @property 
    def age(self):
        return self.__sex
    # setter,格式 : @getter的方法名.setter, 且该方法名需要与getter的方法名相同
    @age.setter
    def age(self, sex):
        self.__sex = sex


stu1 = Student("张三", 18, "男")
print(stu1.name)
# print(stu1._age) # 不建议直接访问/修改
# print(stu1.__sex) # 报错, 私有属性不能直接访问
# print(stu1._Student__sex) # 可以通过该属性访问/修改

# print(stu1.get_sex()) # 报错, 无该方法

print(stu1.age) # 可以通过getter访问/修改, getter会被认为是属性
stu1.age= "女" # 可以通过setter访问/修改, setter会被认为是属性
print(stu1.age) # 可以通过getter访问/修改, getter会被认为是属性


