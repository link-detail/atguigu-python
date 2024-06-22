#
# # 用户输入账号，密码后，根据用户是否已经注册，用户是否在黑名单中，提示用户是否登陆成功
#
# users = [
#     {"name": "jack", "pd": "123", "status": True},
#     {"name": "rose", "pd": "456", "status": True},
#     {"name": "mia", "pd": "789", "status": False}
#
# ]
#
#
# flag = False
#
# for i in range(3):
#     user = input("请输入你的用户名-->")
#     pwd = input("请输入你的密码-->")
#     for e in users:
#         if e["name"] == user:
#             if e["pd"] == pwd:
#                 print("hello")
#             else:
#                 print("密码错误!")
#             break
#     else:
#         print("用户不存在，请先注册")



list1 = [1, 2, 3]
print(sum(list1))