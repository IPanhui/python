has_ticket = True
knife_length = 30
if has_ticket:
    print("进站安检")
    if knife_length >= 20:
        print("刀的长度是%scm长" %knife_length)
        print("不允许上车")
    else:
        print("安检通过，请进站")





else:
    print("去买票")