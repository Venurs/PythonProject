"""
列表：存储一组数据：[10, 20, 30]
元组：存储一组数据：(10, 20, 30)
字典：dict
    dictionary：字典，使用key-value来进行存储数据。
    生活中字典：前几页目录，根据目录找具体的数据
    手机电话本：人名-->手机号码

    字典：可以理解为一组无序的键值对的组合。
        容器中：成对儿(key，value)的数据。

    字典的语法：{}
    {key:value,key:value,key:value....}
        key:键，名
        value：值，
        :
        没有index的概念

    字典注意事项：
        1.key必须是唯一的
        2.key的数据类型：是不可变的数据类型：字符串，数值，元组，而列表不可以
        3.value没有类型要求，可以是任意类型

"""
# 1.直接定义字典
# tels = {
#     "王二狗": "13810109898",
#     "李小花": "13912345678",
#     "Rose": "13245678956",
#     "Jack": "13173737373"
# }
#
# print(tels)
# print(type(tels))  # <class 'dict'>
#
# dict1 = {}  # 空的字典

# 2.可以使用dict()函数来创建字典
"""
可以使用dict()函数来创建字典
需要参数：需要一个列表
dict([[],(),[],[]])
    列表中存储的是列表或元组用于表示名值对
        [name，小小雪]-->2个元素：第一个元素会被认为key，第二个元素被认为value
        (age,18)
[
    [元素1，元素2],
    [元素1，元素2],
    [元素1，元素2],
    (元素1，元素2),
    (元素2，元素2)
]
"""
# dict2 = dict([["name", "小小雪"], ("age", 18), ["sex", "女"]])
# print(dict2)

# 3.使用dict()，配合关键字参数：来创建字典
"""
dict(key=value,key=value,key=value...)
"""
# dict3 = dict(name="王二狗", age=30, sex="男",address="南京市")
# print(dict3)
#
# print("-----")
"""
字典中的key：1必须是唯一的
key：使用数字，字符串，元组，不允许使用列表。
    元组中也不允许使用列表。
# """
# dict4 = {
#     2: "我是一个数字2",
#     2: "我也是一个数字2，啦啦啦啦",
#     "abc": "我是一个字符串",
#     (10, 20): "我是一个元组",
#     (10, 20): "我也是一个元组",
#     # [10, 20]: "我偷偷的是一个列表"
#     (["a", "b"]): "试一下"
# }
# print(dict4)

"""
练习1：创建2个字典：
    存储两个宠物狗的信息：狗名字，狗年龄，狗的品种，狗的颜色
    
练习2：创建1个字典：
    小小雪：
        姓名，年龄，婚否，妈妈(姓名，年龄)，朋友们(王二狗，李小花，三胖，Rose)
"""


animal1 = {"name": "王二狗",
           "dog_age": 18,
           "品种": "吉娃娃",
           "颜色": "白色"}
animal2 = {"name": "王三狗",
           "dog_age": 12,
           "品种": "哈士奇",
           "颜色": "黑色"}
very_small_snow = dict(name="小小雪",
                       age=18,
                       婚否="已婚",
                       her_mother=dict(mother_name="她妈妈", mother_age=18),
                       friend=("王二狗", "李小花", "三胖", "Rose",)
                       )
print(animal1)
print(animal2)
print(very_small_snow)



