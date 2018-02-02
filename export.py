# coding=utf-8
from __future__ import unicode_literals
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot

# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
# v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# bar = Bar("Bar chart", "precipitation and evaporation one year")
# bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
# bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
# bar.render('test.html')
# make_a_snapshot('test.html','test.png')

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render()

print ('start')

make_a_snapshot('render.html', 'snapshot.png')

print ('end')