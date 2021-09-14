from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment, Preference
from users.models import Follow, Profile
import sys
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from .forms import NewCommentForm, NewPostForm
from django.contrib.auth.decorators import login_required

katie_ministry = [
    {
        'link': 'https://www.youtube.com/embed/JZbs0r9KGf8'
    },
    {
        'link': 'https://www.youtube.com/embed/cNqlvuIKWzc'
    },
    {
        'link': 'https://www.youtube.com/embed/3WC9C_8xFe4'
    },
    {
        'link': 'https://www.youtube.com/embed/CSRvkICzxgk'
    },
    {
        'link': 'https://www.youtube.com/embed/aWxygCMvJog'
    },
    {
        'link': 'https://www.youtube.com/embed/gBO0XAulWBQ'
    },
    {
        'link': 'https://www.youtube.com/embed/CD-9lYHZsYw'
    },
    {
        'link': 'https://www.youtube.com/embed/jdW7XgnBheg'
    },
    {
        'link': 'https://www.youtube.com/embed/ln19E_ybs7U'
    },
    {
        'link': 'https://www.youtube.com/embed/RUMbjgujDUY'
    },
    {
        'link': 'https://www.youtube.com/embed/CDDzEAtRwBM'
    },
    {
        'link': 'https://www.youtube.com/embed/JBfB7h5v9gM'
    },
    {
        'link': 'https://www.youtube.com/embed/G7dL-YMNUms'
    },
    {
        'link': 'https://www.youtube.com/embed/DAK6vephRko'
    },
    {
        'link': 'https://www.youtube.com/embed/zIbSzjjJ27Q'
    },
    {
        'link': 'https://www.youtube.com/embed/gwuf8wSmfBA'
    },
    {
        'link': 'https://www.youtube.com/embed/xBzGrCAZN3Y'
    },
    {
        'link': 'https://www.youtube.com/embed/qqOVd2B0R3Y'
    },
    {
        'link': 'https://www.youtube.com/embed/t5A9unRhROo'
    },
    {
        'link': 'https://www.youtube.com/embed/KE5-Ni2Db1g'
    },
    {
        'link': 'https://www.youtube.com/embed/4KNzUYZrSBk'
    },
    {
        'link': 'https://www.youtube.com/embed/Ona4sZUi42A'
    },
    {
        'link': 'https://www.youtube.com/embed/yXw9Yzzu-18'
    },
    {
        'link': 'https://www.youtube.com/embed/HKgFGmT6C-U'
    },
    {
        'link': 'https://www.youtube.com/embed/Brkv11Kxj4s'
    },
    {
        'link': 'https://www.youtube.com/embed/TGZyDHmxIBc'
    },
    {
        'link': 'https://www.youtube.com/embed/WxA_JyDVyH0'
    },
]

transformation_church = [
    {
        'link': 'https://www.youtube.com/embed/9L7BuD4lKH0'
    },
    {
        'link': 'https://www.youtube.com/embed/5g17mCpiCCo'
    },
    {
        'link': 'https://www.youtube.com/embed/oOH6prhdfRY'
    },
    {
        'link': 'https://www.youtube.com/embed/Indqj3OxWRg'
    },
    {
        'link': 'https://www.youtube.com/embed/0-6zYwaLTK8'
    },
    {
        'link': 'https://www.youtube.com/embed/uiR8TLiyfnc'
    },
    {
        'link': 'https://www.youtube.com/embed/wEbY3pLC5R8'
    },
    {
        'link': 'https://www.youtube.com/embed/ymaZ4WUnBFU'
    },
    {
        'link': 'https://www.youtube.com/embed/BF2mqj2Hwlk'
    },
    {
        'link': 'https://www.youtube.com/embed/dXusD3zQaBE'
    },
    {
        'link': 'https://www.youtube.com/embed/0-7Db04Te18'
    },
    {
        'link': 'https://www.youtube.com/embed/cJO5rE8QC0c'
    },
    {
        'link': 'https://www.youtube.com/embed/C6luWwIgkyc'
    },
    {
        'link': 'https://www.youtube.com/embed/lctbj9PiPt8'
    },
    {
        'link': 'https://www.youtube.com/embed/UMxvDH67N_Q'
    },
    {
        'link': 'https://www.youtube.com/embed/klz2_uERFo0'
    },
    {
        'link': 'https://www.youtube.com/embed/Red8ukUaFro'
    },
    {
        'link': 'https://www.youtube.com/embed/qGv-nu8SY80'
    },
    {
        'link': 'https://www.youtube.com/embed/lpSbIK04oOc'
    },
    {
        'link': 'https://www.youtube.com/embed/YLraZ7nny1k'
    },
    {
        'link': 'https://www.youtube.com/embed/QSXtKhtsCvc'
    },
    {
        'link': 'https://www.youtube.com/embed/PRcInxObbIE'
    },
    {
        'link': 'https://www.youtube.com/embed/LPLHVQ2BBno'
    },
    {
        'link': 'https://www.youtube.com/embed/5nqsTwEU3k0'
    },
    {
        'link': 'https://www.youtube.com/embed/Zt0bkaSrE5I'
    },
    {
        'link': 'https://www.youtube.com/embed/nVVVxD7_Hb4'
    },
    {
        'link': 'https://www.youtube.com/embed/6DoxE1_TWNA'
    },
    {
        'link': 'https://www.youtube.com/embed/KZkhnlf2jkY'
    },
    {
        'link': 'https://www.youtube.com/embed/N10me3vlxQc'
    },
    {
        'link': 'https://www.youtube.com/embed/nQYoD24T5Bg'
    },
    {
        'link': 'https://www.youtube.com/embed/JO568RCijvU'
    },
    {
        'link': 'https://www.youtube.com/embed/g0-BZNhsTqQ'
    },
    {
        'link': 'https://www.youtube.com/embed/t914_6XDQHY'
    },
    {
        'link': 'https://www.youtube.com/embed/Ia2nR4iZkXc'
    },
    {
        'link': 'https://www.youtube.com/embed/TRQxZmfvurI'
    },
    {
        'link': 'https://www.youtube.com/embed/qkz0k3I_XzY'
    },
    {
        'link': 'https://www.youtube.com/embed/dVBBPLqeAZg'
    },
    {
        'link': 'https://www.youtube.com/embed/6gdBxU8Na1o'
    },
    {
        'link': 'https://www.youtube.com/embed/a65p4ZvNVJs'
    },
    {
        'link': 'https://www.youtube.com/embed/ihwyLnfT-xc'
    },
    {
        'link': 'https://www.youtube.com/embed/hq9iTBtTSyw'
    },
    {
        'link': 'https://www.youtube.com/embed/P_N7q2lQ6-4'
    },
    {
        'link': 'https://www.youtube.com/embed/v7qWSXLKMCU'
    },
    {
        'link': 'https://www.youtube.com/embed/iA1U2f0l_fo'
    },
    {
        'link': 'https://www.youtube.com/embed/QslEzAs-tG4'
    },
    {
        'link': 'https://www.youtube.com/embed/_q7pf4pbB6M'
    },
]

afrika_ministry = [
    {
        'link': 'https://www.youtube.com/embed/p1g4AzmUM2o'
    },
    {
        'link': 'https://www.youtube.com/embed/saHOkR3I9xM'
    },
    {
        'link': 'https://www.youtube.com/embed/GvuwS3QqOeE'
    },
    {
        'link': 'https://www.youtube.com/embed/G7R3lWNrvso'
    },
    {
        'link': 'https://www.youtube.com/embed/_YZTmyJarsc'
    },
    {
        'link': 'https://www.youtube.com/embed/P0SKqzJJrds'
    },
    {
        'link': 'https://www.youtube.com/embed/jhEhxJ4Ry3M'
    },
    {
        'link': 'https://www.youtube.com/embed/1Zx5V7Ospj0'
    },
    {
        'link': 'https://www.youtube.com/embed/eUrumMz62Xc'
    },
    {
        'link': 'https://www.youtube.com/embed/VKQ0wl6YPcA'
    },
    {
        'link': 'https://www.youtube.com/embed/xZh_RQSHqlc'
    },
    {
        'link': 'https://www.youtube.com/embed/QGG7djSUvvw'
    },
    {
        'link': 'https://www.youtube.com/embed/shQM4kp-9NU'
    },
    {
        'link': 'https://www.youtube.com/embed/w8NJNkzzbIU'
    },
    {
        'link': 'https://www.youtube.com/embed/oBhgEeHTo0U'
    },
    {
        'link': 'https://www.youtube.com/embed/t3FGj_vL1dY'
    },
    {
        'link': 'https://www.youtube.com/embed/LuFy2sc59Cc'
    },
]

jl_bevere = [
    {
        'link': 'https://www.youtube.com/embed/GnVbOnHMNZQ'
    },
    {
        'link': 'https://www.youtube.com/embed/I2gySCGAQTQ'
    },
    {
        'link': 'https://www.youtube.com/embed/sURoE7gY7n0'
    },
    {
        'link': 'https://www.youtube.com/embed/brNzUs7NC0g'
    },
    {
        'link': 'https://www.youtube.com/embed/dyEBD8r5dF0'
    },
    {
        'link': 'https://www.youtube.com/embed/y1QF7MApv7I'
    },
    {
        'link': 'https://www.youtube.com/embed/SfNIx1QIge4'
    },
    {
        'link': 'https://www.youtube.com/embed/5hV1JE-nfx0'
    },
    {
        'link': 'https://www.youtube.com/embed/D21GNLJzHu0'
    },
    {
        'link': 'https://www.youtube.com/embed/ILrB-NMjKOk'
    },
    {
        'link': 'https://www.youtube.com/embed/4dKqrwl0EFk'
    },
    {
        'link': 'https://www.youtube.com/embed/8i3_9cUyZAQ'
    },
]

potters_house = [
    {
        'link': 'https://www.youtube.com/embed/Lt0yPOwHiNI'
    },
    {
        'link': 'https://www.youtube.com/embed/tVeKk3OEEek'
    },
    {
        'link': 'https://www.youtube.com/embed/vOguyvfItRs'
    },
    {
        'link': 'https://www.youtube.com/embed/7Pd8M6sgHOU'
    },
    {
        'link': 'https://www.youtube.com/embed/uawQ9Khue8k'
    },
    {
        'link': 'https://www.youtube.com/embed/3kONP_v-MgU'
    },
    {
        'link': 'https://www.youtube.com/embed/0IYPTYqPJP4'
    },
    {
        'link': 'https://www.youtube.com/embed/Bc1CMqQAKmk'
    },
    {
        'link': 'https://www.youtube.com/embed/9GKURgflL6Q'
    },
    {
        'link': 'https://www.youtube.com/embed/rh4n4W2k7qo'
    },
    {
        'link': 'https://www.youtube.com/embed/qi-tTUOzRxs'
    },
    {
        'link': 'https://www.youtube.com/embed/JAu95AkMyVg'
    },
    {
        'link': 'https://www.youtube.com/embed/mYBqFaV6qC4'
    },
    {
        'link': 'https://www.youtube.com/embed/UZNj7OmBTXc'
    },
    {
        'link': 'https://www.youtube.com/embed/X3Ru_h9m9zM'
    },
    {
        'link': 'https://www.youtube.com/embed/WbjgaezTjgA'
    },
    {
        'link': 'https://www.youtube.com/embed/0ujjBmVkYhg'
    },
    {
        'link': 'https://www.youtube.com/embed/cozdRqf2H7o'
    },
    {
        'link': 'https://www.youtube.com/embed/6C3zi26oR0E'
    },
    {
        'link': 'https://www.youtube.com/embed/itnoy6rhSHQ'
    },
    {
        'link': 'https://www.youtube.com/embed/0RoIU04x3_Y'
    },
    {
        'link': 'https://www.youtube.com/embed/ZBfD_5slFFM'
    },
    {
        'link': 'https://www.youtube.com/embed/aGHqLzxcM4w'
    },
    {
        'link': 'https://www.youtube.com/embed/h-zjZia34a4'
    },
    {
        'link': 'https://www.youtube.com/embed/BuRXu0Foc0M'
    },
    {
        'link': 'https://www.youtube.com/embed/vxFQh78r0WA'
    },
]

elevation = [
    {
        'link': 'https://www.youtube.com/embed/_rIoV9yaUaM'
    },
    {
        'link': 'https://www.youtube.com/embed/QgM-jiIfzIs'
    },
    {
        'link': 'https://www.youtube.com/embed/_NzBmo8SSBE'
    },
    {
        'link': 'https://www.youtube.com/embed/4G8LvFNbLYs'
    },
    {
        'link': 'https://www.youtube.com/embed/-ZJBo8dVAvg'
    },
    {
        'link': 'https://www.youtube.com/embed/wSCzYPsOFcY'
    },
    {
        'link': 'https://www.youtube.com/embed/m-eabvA4NLg'
    },
    {
        'link': 'https://www.youtube.com/embed/it4cDLBcn5E'
    },
    {
        'link': 'https://www.youtube.com/embed/1p9grcUN4lI'
    },
    {
        'link': 'https://www.youtube.com/embed/dd0necEx8xU'
    },
    {
        'link': 'https://www.youtube.com/embed/D7Foy9nkMV0'
    },
    {
        'link': 'https://www.youtube.com/embed/IkowSQWs8mM'
    },
    {
        'link': 'https://www.youtube.com/embed/5Vzfc3wwgf8'
    },
    {
        'link': 'https://www.youtube.com/embed/J7Pg4BW3j5o'
    },
    {
        'link': 'https://www.youtube.com/embed/Tk12DsbkB8A'
    },
    {
        'link': 'https://www.youtube.com/embed/uG8Rg0Sn1xM'
    },
    {
        'link': 'https://www.youtube.com/embed/7v572vNcbf8'
    },
    {
        'link': 'https://www.youtube.com/embed/QVWCjc-XUm8'
    },
    {
        'link': 'https://www.youtube.com/embed/VMeNTJoMH9M'
    },
    {
        'link': 'https://www.youtube.com/embed/dU0pVacQ_aE'
    },
    {
        'link': 'https://www.youtube.com/embed/MtfSpeLvwj4'
    },
    {
        'link': 'https://www.youtube.com/embed/hgB9p5ia8qo'
    },
    {
        'link': 'https://www.youtube.com/embed/Q4dZx69sero'
    },
    {
        'link': 'https://www.youtube.com/embed/PwimnqpGCf8'
    },
    {
        'link': 'https://www.youtube.com/embed/PwimnqpGCf8'
    },
    {
        'link': 'https://www.youtube.com/embed/sMSToT11ll8'
    },
    {
        'link': 'https://www.youtube.com/embed/CrIXfUJcjhk'
    },
    {
        'link': 'https://www.youtube.com/embed/oDp63iqIYdw'
    },
    {
        'link': 'https://www.youtube.com/embed/cBNGPsjvDmo'
    },
    {
        'link': 'https://www.youtube.com/embed/QjBSksFSIyU'
    },
    {
        'link': 'https://www.youtube.com/embed/JBH_SudUQoA'
    },
    {
        'link': 'https://www.youtube.com/embed/c8vodSF_k9A'
    },
    {
        'link': 'https://www.youtube.com/embed/Wnp_v83GsAo'
    },
    {
        'link': 'https://www.youtube.com/embed/Iojt-t9RufA'
    },
    {
        'link': 'https://www.youtube.com/embed/oLgheXUYIzw'
    },
    {
        'link': 'https://www.youtube.com/embed/ey883taZMac'
    },
    {
        'link': 'https://www.youtube.com/embed/HZhGARgXDhA'
    },
    {
        'link': 'https://www.youtube.com/embed/TcMp3uRzuX0'
    },
    {
        'link': 'https://www.youtube.com/embed/QhYA8aOFdT4'
    },
    {
        'link': 'https://www.youtube.com/embed/54jgesZlCQ8'
    },
    {
        'link': 'https://www.youtube.com/embed/tzxBm06lTbE'
    },
    {
        'link': 'https://www.youtube.com/embed/M755_miJKbI'
    },
    {
        'link': 'https://www.youtube.com/embed/PcHSk0hLEiA'
    },
    {
        'link': 'https://www.youtube.com/embed/9yoaNVFo-tI'
    },
    {
        'link': 'https://www.youtube.com/embed/9UnsX2lgEwg'
    },
    {
        'link': 'https://www.youtube.com/embed/CHYcKWHcDEE'
    },
    {
        'link': 'https://www.youtube.com/embed/GTk3etGzyTI'
    },
]

Todd = [
    {
        'link': 'https://www.youtube.com/embed/2zukM_R2xBA'
    },
    {
        'link': 'https://www.youtube.com/embed/Uxp8Ks--1f0'
    },
    {
        'link': 'https://www.youtube.com/embed/4YkgYYlVuX4'
    },
    {
        'link': 'https://www.youtube.com/embed/S6_A04CRKB0'
    },
    {
        'link': 'https://www.youtube.com/embed/Hm8ukj747A0'
    },
    {
        'link': 'https://www.youtube.com/embed/JzrzeLN0dkE'
    },
    {
        'link': 'https://www.youtube.com/embed/gdkCBzwyesM'
    },
    {
        'link': 'https://www.youtube.com/embed/kgnyBbe5nw8'
    },
    {
        'link': 'https://www.youtube.com/embed/Mq26gah1N2I'
    },
    {
        'link': 'https://www.youtube.com/embed/jGT2vW81gWQ'
    },
    {
        'link': 'https://www.youtube.com/embed/B3HlltljrwE'
    },
    {
        'link': 'https://www.youtube.com/embed/VsjG8ZYPJ_A'
    },
    {
        'link': 'https://www.youtube.com/embed/2cQD7UGFBpE'
    },
    {
        'link': 'https://www.youtube.com/embed/clr3uJl6Jic'
    },
    {
        'link': 'https://www.youtube.com/embed/oaPX5Qhnwqk'
    },
    {
        'link': 'https://www.youtube.com/embed/5DsP1xPiI5Y'
    },
    {
        'link': 'https://www.youtube.com/embed/hy1KPAR3g5A'
    },
    {
        'link': 'https://www.youtube.com/embed/witIJziYOCQ'
    },
    {
        'link': 'https://www.youtube.com/embed/QS464R4Y-5Q'
    },
    {
        'link': 'https://www.youtube.com/embed/8wfisChl-tg'
    },
    {
        'link': 'https://www.youtube.com/embed/7kYzs_kLXQo'
    },
    {
        'link': 'https://www.youtube.com/embed/TI15LOx4xko'
    },
    {
        'link': 'https://www.youtube.com/embed/OXXidY8WEGE'
    },
    {
        'link': 'https://www.youtube.com/embed/sOL4W8w5Zsw'
    },
    {
        'link': 'https://www.youtube.com/embed/1H8Ox-kChmo'
    },
    {
        'link': 'https://www.youtube.com/embed/XsV4QPSiQb0'
    },
    {
        'link': 'https://www.youtube.com/embed/wjnpTp85ZlA'
    },
    {
        'link': 'https://www.youtube.com/embed/B1CB1Tc3O8I'
    },
]

Joyce = [
    {
        'link': 'https://www.youtube.com/embed/nSSleJP4Ib0'
    },
    {
        'link': 'https://www.youtube.com/embed/L9r93TmmjTM'
    },
    {
        'link': 'https://www.youtube.com/embed/QhskWN4ItGY'
    },
    {
        'link': 'https://www.youtube.com/embed/ifV0XiuHEhw'
    },
    {
        'link': 'https://www.youtube.com/embed/p3UzTIz075o'
    },
    {
        'link': 'https://www.youtube.com/embed/IU1HVuCHiMg'
    },
]

john_gray = [
    {
        'link': 'https://www.youtube.com/embed/CgrN8JK37GM'
    },
    {
        'link': 'https://www.youtube.com/embed/yLTpvmRkl2M'
    },
    {
        'link': 'https://www.youtube.com/embed/pAGmFvYIb-I'
    },
    {
        'link': 'https://www.youtube.com/embed/gWXcAnxQbWE'
    },
    {
        'link': 'https://www.youtube.com/embed/jOfrOGEaC8w'
    },
    {
        'link': 'https://www.youtube.com/embed/EfiWHkYfByA'
    },
    {
        'link': 'https://www.youtube.com/embed/vGTpnugkHYo'
    },
    {
        'link': 'https://www.youtube.com/embed/jVxhzSIeZuk'
    },
    {
        'link': 'https://www.youtube.com/embed/ymIzdbHtY9s'
    },
    {
        'link': 'https://www.youtube.com/embed/LxLYzlx_438'
    },
    {
        'link': 'https://www.youtube.com/embed/avcK7PR0iiI'
    },
    {
        'link': 'https://www.youtube.com/embed/t4AvVqTxQm4'
    },
    {
        'link': 'https://www.youtube.com/embed/0V3W7YnAtFU'
    },
    {
        'link': 'https://www.youtube.com/embed/eLUOHacdrGE'
    },
    {
        'link': 'https://www.youtube.com/embed/nmgF5cS8j4c'
    },
    {
        'link': 'https://www.youtube.com/embed/3cGeo-e3jHI'
    },
    {
        'link': 'https://www.youtube.com/embed/srjvoQdbPwI'
    },
    {
        'link': 'https://www.youtube.com/embed/kiYNxSxMM78'
    },
    {
        'link': 'https://www.youtube.com/embed/Pd_MvBSKzlQ'
    },
    {
        'link': 'https://www.youtube.com/embed/PqXQSchlUkI'
    },
    {
        'link': 'https://www.youtube.com/embed/IvgJqMJNGsU'
    },
    {
        'link': 'https://www.youtube.com/embed/hJKCOpyQtFE'
    },
    {
        'link': 'https://www.youtube.com/embed/9VSEuZqYG6w'
    },
    {
        'link': 'https://www.youtube.com/embed/_crWozH4cvg'
    },
    {
        'link': 'https://www.youtube.com/embed/8QSVPnZynpo'
    },
    {
        'link': 'https://www.youtube.com/embed/JYvTdzD-SzE'
    },
    {
        'link': 'https://www.youtube.com/embed/AtXnofiLfVI'
    },
    {
        'link': 'https://www.youtube.com/embed/uJC-grn9cvQ'
    },
    {
        'link': 'https://www.youtube.com/embed/q5NDKBFu_hU'
    },
    {
        'link': 'https://www.youtube.com/embed/wNJ_qtM9OQI'
    },
    {
        'link': 'https://www.youtube.com/embed/jdtPF57BcnU'
    },
    {
        'link': 'https://www.youtube.com/embed/Ry_koNJNZMQ'
    },
    {
        'link': 'https://www.youtube.com/embed/RbKstbALJsk'
    },
    {
        'link': 'https://www.youtube.com/embed/j5mIqT2W2Mw'
    },
    {
        'link': 'https://www.youtube.com/embed/_9qIzyRmH1w'
    },
    {
        'link': 'https://www.youtube.com/embed/PKhcc7P_pgo'
    },
]

prince = [
    {
        'link': 'https://www.youtube.com/embed/0-ZuZj2TXyk'
    },
    {
        'link': 'https://www.youtube.com/embed/Tpdot1TI8Yw'
    },
    {
        'link': 'https://www.youtube.com/embed/jJpArxU_53o'
    },
    {
        'link': 'https://www.youtube.com/embed/KI1AyBa6JIA'
    },
    {
        'link': 'https://www.youtube.com/embed/AiTzuCxtuSw'
    },
    {
        'link': 'https://www.youtube.com/embed/0_a-ffZoDsg'
    },
    {
        'link': 'https://www.youtube.com/embed/YOlwdIbWXKA'
    },
    {
        'link': 'https://www.youtube.com/embed/_DAoy68_LEc'
    },
    {
        'link': 'https://www.youtube.com/embed/SH1o61GsFiA'
    },
    {
        'link': 'https://www.youtube.com/embed/ZxILcSMO7Uc'
    },
    {
        'link': 'https://www.youtube.com/embed/5vOobo3GY_E'
    },
    {
        'link': 'https://www.youtube.com/embed/Yup0HojaC4U'
    },
    {
        'link': 'https://www.youtube.com/embed/SH1o61GsFiA'
    },
    {
        'link': 'https://www.youtube.com/embed/Ks4hr_Ltjls'
    },
    {
        'link': 'https://www.youtube.com/embed/jumgGxwIr7A'
    },
    {
        'link': 'https://www.youtube.com/embed/LVclY2xt37E'
    },
    {
        'link': 'https://www.youtube.com/embed/G0pgOITTzxg'
    },
    {
        'link': 'https://www.youtube.com/embed/v8N4358uU64'
    },
]

life_church = [
    {
        'link': 'https://www.youtube.com/embed/YGnB3OTZoY0'
    },
    {
        'link': 'https://www.youtube.com/embed/BLuw1oDpebI'
    },
    {
        'link': 'https://www.youtube.com/embed/t3Y2Wrolvp4'
    },
    {
        'link': 'https://www.youtube.com/embed/07QupfTSEgA'
    },
    {
        'link': 'https://www.youtube.com/embed/KBy2aSuwDeA'
    },
    {
        'link': 'https://www.youtube.com/embed/TCPoZ9haoOU'
    },
    {
        'link': 'https://www.youtube.com/embed/HANQASntcww'
    },
    {
        'link': 'https://www.youtube.com/embed/gKEs9s7ucLo'
    },
    {
        'link': 'https://www.youtube.com/embed/sYJ0z0Usr6w'
    },
    {
        'link': 'https://www.youtube.com/embed/clG_9XObxOU'
    },
    {
        'link': 'https://www.youtube.com/embed/4fJAaxspReA'
    },
    {
        'link': 'https://www.youtube.com/embed/UEBKwpmKoG0'
    },
    {
        'link': 'https://www.youtube.com/embed/9FpZTMf-3c4'
    },
    {
        'link': 'https://www.youtube.com/embed/NIFDmLC3NUo'
    },
    {
        'link': 'https://www.youtube.com/embed/PjrbF0kPk30'
    },
    {
        'link': 'https://www.youtube.com/embed/bIfg7ilWD7o'
    },
    {
        'link': 'https://www.youtube.com/embed/Wh_a9eLWvaI'
    },
    {
        'link': 'https://www.youtube.com/embed/wFVvNYNFf4Y'
    },
    {
        'link': 'https://www.youtube.com/embed/QKySt8dK7QY'
    },
    {
        'link': 'https://www.youtube.com/embed/LpAHIB_dZZI'
    },
    {
        'link': 'https://www.youtube.com/embed/imUr_VNwe4s'
    },
    {
        'link': 'https://www.youtube.com/embed/oE351_KGnQ0'
    },
]

ted_jr = [
    {
        'link': 'https://www.youtube.com/embed/m-wdb5D0jAE'
    },
    {
        'link': 'https://www.youtube.com/embed/vHRpTICavQc'
    },
    {
        'link': 'https://www.youtube.com/embed/NaRDYGBDzoQ'
    },
    {
        'link': 'https://www.youtube.com/embed/EE7b9U63jFU'
    },
    {
        'link': 'https://www.youtube.com/embed/mTztlZxqB_k'
    },
    {
        'link': 'https://www.youtube.com/embed/2F1CeDLZiQc'
    },
    {
        'link': 'https://www.youtube.com/embed/o5ITaN3kqLE'
    },
    {
        'link': 'https://www.youtube.com/embed/BSD-8owD9H4'
    },
    {
        'link': 'https://www.youtube.com/embed/7JOepX8G_o0'
    },
    {
        'link': 'https://www.youtube.com/embed/hLQyZKDLJTA'
    },
    {
        'link': 'https://www.youtube.com/embed/V_4Bp-e4a4E'
    },
    {
        'link': 'https://www.youtube.com/embed/Fb6nr_PPjzY'
    },
    {
        'link': 'https://www.youtube.com/embed/xVcvCmmmHJ8'
    },
    {
        'link': 'https://www.youtube.com/embed/Ux9sjeFvfJc'
    },
    {
        'link': 'https://www.youtube.com/embed/53Fy56wB2kg'
    },
    {
        'link': 'https://www.youtube.com/embed/ob2SAEbh22w'
    },
    {
        'link': 'https://www.youtube.com/embed/QVJYVgcCp7A'
    },
    {
        'link': 'https://www.youtube.com/embed/kqcrINvcJho'
    },
]

pw_cain = [
    {
        'link': 'https://www.youtube.com/embed/lsRwynMGzvY'
    },
    {
        'link': 'https://www.youtube.com/embed/oEnDohTdgjM'
    },
    {
        'link': 'https://www.youtube.com/embed/1IEJpNIEjh0'
    },
    {
        'link': 'https://www.youtube.com/embed/IdoWYYk675M'
    },
    {
        'link': 'https://www.youtube.com/embed/c-L87atOvfI'
    },
    {
        'link': 'https://www.youtube.com/embed/tHgTiTdei_A'
    },
    {
        'link': 'https://www.youtube.com/embed/alFKY_CcbBI'
    },
    {
        'link': 'https://www.youtube.com/embed/RUHlz7zvjqM'
    },
    {
        'link': 'https://www.youtube.com/embed/C0fMFAvK4fs'
    },
    {
        'link': 'https://www.youtube.com/embed/sRgAiAmRNjc'
    },
    {
        'link': 'https://www.youtube.com/embed/hZIZ13QV-nY'
    },
    {
        'link': 'https://www.youtube.com/embed/HaiMN5kh2Iw'
    },
    {
        'link': 'https://www.youtube.com/embed/U3zmlHrbYvM'
    },
    {
        'link': 'https://www.youtube.com/embed/kE_V4UC4aPU'
    },
    {
        'link': 'https://www.youtube.com/embed/9LBjXEi7zGc'
    },
    {
        'link': 'https://www.youtube.com/embed/H9IZ3aIw9uM'
    },
    {
        'link': 'https://www.youtube.com/embed/k3IMvKa567A'
    },
    {
        'link': 'https://www.youtube.com/embed/O52O255DAGE'
    },
    {
        'link': 'https://www.youtube.com/embed/5Uf6dbn0anc'
    },
    {
        'link': 'https://www.youtube.com/embed/Jkp7DntIuaU'
    },
    {
        'link': 'https://www.youtube.com/embed/7ohWDOEC4oU'
    },
    {
        'link': 'https://www.youtube.com/embed/LUrUJO13ULk'
    },
    {
        'link': 'https://www.youtube.com/embed/kN3h9xQTkEg'
    },
    {
        'link': 'https://www.youtube.com/embed/0D-KSN1QdT0'
    },
    {
        'link': 'https://www.youtube.com/embed/bRV1iKds_Gc'
    },
    {
        'link': 'https://www.youtube.com/embed/ga23crHHMyY'
    },
]

dr_myles = [
    {
        'link': 'https://www.youtube.com/embed/SZ7GasMDTuk'
    },
    {
        'link': 'https://www.youtube.com/embed/a167Vg3WlqA'
    },
    {
        'link': 'https://www.youtube.com/embed/BeCma8ebGUU'
    },
    {
        'link': 'https://www.youtube.com/embed/FANPZ_E2SjQ'
    },
    {
        'link': 'https://www.youtube.com/embed/htjrjNALqow'
    },
    {
        'link': 'https://www.youtube.com/embed/1ZhSWBmZlUk'
    },
    {
        'link': 'https://www.youtube.com/embed/WhXTR7S45rw'
    },
    {
        'link': 'https://www.youtube.com/embed/wCSOFe_0EMM'
    },
    {
        'link': 'https://www.youtube.com/embed/TNy3-f6xgmY'
    },
    {
        'link': 'https://www.youtube.com/embed/1DpmlL4cR_Y'
    },
    {
        'link': 'https://www.youtube.com/embed/1TO3yVW0X18'
    },
    {
        'link': 'https://www.youtube.com/embed/BeCma8ebGUU'
    },
    {
        'link': 'https://www.youtube.com/embed/53nuAnFzIEE'
    },
    {
        'link': 'https://www.youtube.com/embed/e9T0jXYfGeA'
    },
    {
        'link': 'https://www.youtube.com/embed/Q0jxSdAB9Z8'
    },
    {
        'link': 'https://www.youtube.com/embed/z1qQe9yZcOw'
    },
    {
        'link': 'https://www.youtube.com/embed/psZRYmG5S2g'
    },
    {
        'link': 'https://www.youtube.com/embed/aZ7B3amr-hw'
    },
    {
        'link': 'https://www.youtube.com/embed/rSYATfBnjT0'
    },
    {
        'link': 'https://www.youtube.com/embed/h8jiN3KCxmA'
    },
    {
        'link': 'https://www.youtube.com/embed/roWebdV5MxI'
    },
    {
        'link': 'https://www.youtube.com/embed/_XofHku6yw0'
    },
]

bvov = [
    {
        'link': 'https://www.youtube.com/embed/fcN3p1_eClE'
    },
    {
        'link': 'https://www.youtube.com/embed/ZixS7cQfhKo'
    },
    {
        'link': 'https://www.youtube.com/embed/uc3_4Y1eD7M'
    },
    {
        'link': 'https://www.youtube.com/embed/oNpI2Zx_aL4'
    },
    {
        'link': 'https://www.youtube.com/embed/XTX3osKtAbs'
    },
    {
        'link': 'https://www.youtube.com/embed/CbYFCqUCaRk'
    },
    {
        'link': 'https://www.youtube.com/embed/Ek0YMyROEOo'
    },
    {
        'link': 'https://www.youtube.com/embed/1S4GbRBb0tk'
    },
    {
        'link': 'https://www.youtube.com/embed/xKDdsqEx_KA'
    },
    {
        'link': 'https://www.youtube.com/embed/wMjEA50ZVZ8'
    },
    {
        'link': 'https://www.youtube.com/embed/OSutUW5TX-8'
    },
    {
        'link': 'https://www.youtube.com/embed/nxePMJJjAvo'
    },
    {
        'link': 'https://www.youtube.com/embed/aEgrPAxxeOM'
    },
    {
        'link': 'https://www.youtube.com/embed/Ow4HdX0MOL4'
    },
    {
        'link': 'https://www.youtube.com/embed/fabQUW-zzdM'
    },
    {
        'link': 'https://www.youtube.com/embed/D7J7-llebVM'
    },
    {
        'link': 'https://www.youtube.com/embed/MuQj5xnybLQ'
    },
    {
        'link': 'https://www.youtube.com/embed/erc489N7b54'
    },
    {
        'link': 'https://www.youtube.com/embed/xSSlR5FGfxM'
    },
    {
        'link': 'https://www.youtube.com/embed/_NamGkOvHrU'
    },
    {
        'link': 'https://www.youtube.com/embed/utUw3oDE9rA'
    },
]


def is_users(post_user, logged_user):
    return post_user == logged_user




class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        all_users = []
        data_counter = Post.objects.values('author')\
            .annotate(author_count=Count('author'))\
            .order_by('-author_count')[:6]

        for aux in data_counter:
            all_users.append(User.objects.filter(pk=aux['author']).first())
        # if Preference.objects.get(user = self.request.user):
        #     data['preference'] = True
        # else:
        #     data['preference'] = False
        data['preference'] = Preference.objects.all()
        # print(Preference.objects.get(user= self.request.user))
        data['all_users'] = all_users
        print(all_users, file=sys.stderr)
        return data

    def get_queryset(self):
        user = self.request.user
        qs = Follow.objects.filter(user=user)
        follows = [user]
        for obj in qs:
            follows.append(obj.follow_user)
        return Post.objects.filter(author__in=follows).order_by('-date_posted')


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        visible_user = self.visible_user()
        logged_user = self.request.user
        print(logged_user.username == '', file=sys.stderr)

        if logged_user.username == '' or logged_user is None:
            can_follow = False
        else:
            can_follow = (Follow.objects.filter(
                user=logged_user, follow_user=visible_user).count() == 0)
        data = super().get_context_data(**kwargs)

        data['user_profile'] = visible_user
        data['can_follow'] = can_follow
        return data

    def get_queryset(self):
        user = self.visible_user()
        return Post.objects.filter(author=user).order_by('-date_posted')

    def post(self, request, *args, **kwargs):
        if request.user.id is not None:
            follows_between = Follow.objects.filter(
                user=request.user, follow_user=self.visible_user())

            if 'follow' in request.POST:
                new_relation = Follow(user=request.user,
                                      follow_user=self.visible_user())
                if follows_between.count() == 0:
                    new_relation.save()
            elif 'unfollow' in request.POST:
                if follows_between.count() > 0:
                    follows_between.delete()

        return self.get(self, request, *args, **kwargs)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(
            post_connected=self.get_object()).order_by('-date_posted')
        data['comments'] = comments_connected
        data['form'] = NewCommentForm(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
                              author=self.request.user,
                              post_connected=self.get_object())
        new_comment.save()

        return self.get(self, request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

@login_required
def create_post(request):
	user = request.user
	if request.method == "POST":
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save(commit=False)
			data.author = user
			data.save()
			messages.success(request, f'Posted Successfully')
			return redirect('blog-home')
	else:
		form = NewPostForm()
	return render(request, 'blog/post_new.html', {'form':form})




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content','pic','tags']
    template_name = 'blog/post_new.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return is_users(self.get_object().author, self.request.user)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Edit a post'
        return data


# Follow Functionality====================================================================================
class FollowsListView(ListView):
    model = Follow
    template_name = 'blog/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'follows'
        return data


class FollowersListView(ListView):
    model = Follow
    template_name = 'blog/follow.html'
    context_object_name = 'follows'

    def visible_user(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_queryset(self):
        user = self.visible_user()
        return Follow.objects.filter(follow_user=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['follow'] = 'followers'
        return data


# Like Functionality====================================================================================
@login_required
def postpreference(request, postid, userpreference):
    if request.method == "POST":
        eachpost = get_object_or_404(Post, id=postid)
        obj = ''
        valueobj = ''
        try:
            obj = Preference.objects.get(user=request.user, post=eachpost)
            valueobj = obj.value
            valueobj = int(valueobj)
            userpreference = int(userpreference)
            if valueobj != userpreference:
                obj.delete()
                upref = Preference()
                upref.user = request.user
                upref.post = eachpost
                upref.value = userpreference
                if userpreference == 1 and valueobj != 1:
                    eachpost.likes += 1
                    eachpost.dislikes -= 1
                elif userpreference == 2 and valueobj != 2:
                    eachpost.dislikes += 1
                    eachpost.likes -= 1
                upref.save()
                eachpost.save()
                context = {'eachpost': eachpost, 'postid': postid}
                return redirect('blog-home', context)
            elif valueobj == userpreference:
                obj.delete()
                if userpreference == 1:
                    eachpost.likes -= 1
                elif userpreference == 2:
                    eachpost.dislikes -= 1
                eachpost.save()
                context = {'eachpost': eachpost, 'postid': postid}
                return redirect('blog-home')

        except Preference.DoesNotExist:
            upref = Preference()
            upref.user = request.user
            upref.post = eachpost
            upref.value = userpreference
            userpreference = int(userpreference)
            if userpreference == 1:
                eachpost.likes += 1
            elif userpreference == 2:
                eachpost.dislikes += 1
            upref.save()
            eachpost.save()

            context = {'post': eachpost, 'postid': postid}

            return redirect('blog-home')

    else:
        eachpost = get_object_or_404(Post, id=postid)
        context = {'eachpost': eachpost, 'postid': postid}

        return redirect('blog-home')


# Video Functionality====================================================================================
def video(request):
    return render(
        request, 'blog/video.html', {
            'katie_souza': katie_ministry,
            'michael_todd': transformation_church,
            'afrika_mhlophe': afrika_ministry,
            'john_bevere': jl_bevere,
            'td_jakes': potters_house,
            'furtick': elevation,
            'todd_white': Todd,
            'joyce_meyer': Joyce,
            'gray': john_gray,
            'joseph_p': prince,
            'groeschel': life_church,
            'shuttleworth_jr': ted_jr,
            'white_cain': pw_cain,
            'munroe': dr_myles,
            'copeland': bvov
        })


def business(request):
    return render(request, 'blog/business.html')

# Chat Functionality====================================================================================