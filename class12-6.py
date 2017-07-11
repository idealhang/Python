list1 = ['1.Just Do It!','2.一切皆有可能！','3.让编程改变世界','4.Impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [brand + ':' + slogan[2:] for brand in list2 for slogan in list1 if brand[0]==slogan[0]]
list3.sort()
for each in list3:
        print(each)
