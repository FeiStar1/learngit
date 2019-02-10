std1 = {'name':'weihong','score':98}
std2 = {'name':'fujun','score':81}
class student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))

    def splitmx(self):
        self.xing = self.name.split()[1]
        self.ming = self.name.split()[0]
        print('xing is %s,ming is %s'%(self.xing,self.ming))


fujun = student('fujun zhao',59)
weihong = student('weihong ye',87)
fujun.print_score()
weihong.print_score()
fujun.splitmx()
