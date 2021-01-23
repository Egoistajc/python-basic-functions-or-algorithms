from pyecharts import Bar
from pyecharts import Line
from pyecharts import Overlap
city_main=city_com.sort_values('count',ascending=False)[0:20]
attr=city_main['city']
v1=city_main['count']
v2=city_main['mean']
line=Line("主要城市评分")
line.add("城市", attr, v2, is_stack=True,xaxis_rotate=30,yaxis_min=4.2,
         mark_point=['min','max'],xaxis_interval =0,line_color='lightblue',
         line_width=4,mark_point_textcolor='black',
         mark_point_color='lightblue',
         is_splitline_show=False)
bar = Bar("主要城市评论数")
bar.add("城市", attr, v1, is_stack=True,xaxis_rotate=30,yaxis_min=4.2,
         xaxis_interval =0,is_splitline_show=False)
overlap=Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render('主要城市评论数_平均分.html')


