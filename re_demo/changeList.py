# -*- coding: utf-8 -*-
# @Author       :junjie    
# @Time         :2019/12/4 16:29
# @FileName     :changeList.py
#IDE            :PyCharm


#给定一个list,把里面的数字处理成偶数在左边,奇数在右边。
def listto(insert_list):
    if type(insert_list)==list:
        if len(insert_list)==1 :
            if type(insert_list[0]) is not int:
                return False
            return insert_list
        for item in insert_list:
            try:
                if item%2==0:
                    insert_list.remove(item)
                    insert_list.insert(0,item)
            except :
                return False
        return  insert_list
    else:
        return False
if __name__ == '__main__':
    list1=[0,-1342,3232,23231,45,78,89]
    print(listto(list1))