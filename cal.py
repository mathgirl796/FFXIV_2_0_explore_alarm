__all__ = ['cal']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['note', 'getHour', 'loadPage', 'zoneRates', 'getPerTime', 'getMinute', 'checkTime', 'zoneWeathers', 'init', 'getWeatherVar'])
@Js
def PyJsHoisted_loadPage_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('init')()
    var.get('setInterval')(Js('init()'), Js(3000.0))
PyJsHoisted_loadPage_.func_name = 'loadPage'
var.put('loadPage', PyJsHoisted_loadPage_)
@Js
def PyJsHoisted_getHour_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['timeEarth', 's', 'timeAdjust', 'h', 'timeGame', 'label', 'timeEorzea', 'm'])
    pass
    var.put('timeAdjust', Js(1278950400.0))
    var.put('timeGame', Js(144.0))
    var.put('timeEarth', Js(7.0))
    var.put('s', var.get('Date').create().callprop('getTime'))
    var.put('timeEorzea', var.get('Math').callprop('round', ((((var.get('s')/Js(1000.0))-var.get('timeAdjust'))*var.get('timeGame'))/var.get('timeEarth'))))
    var.put('timeEorzea', (var.get('Math').callprop('round', (var.get('timeEorzea')/Js(10.0)))*Js(10.0)))
    var.put('h', var.get('Math').callprop('floor', ((var.get('timeEorzea')%Js(86400.0))/Js(3600.0))))
    var.put('m', var.get('Math').callprop('floor', ((var.get('timeEorzea')%Js(3600.0))/Js(60.0))))
    return var.get('h')
PyJsHoisted_getHour_.func_name = 'getHour'
var.put('getHour', PyJsHoisted_getHour_)
@Js
def PyJsHoisted_getMinute_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['timeEarth', 's', 'timeAdjust', 'timeGame', 'label', 'timeEorzea', 'm'])
    pass
    var.put('timeAdjust', Js(1278950400.0))
    var.put('timeGame', Js(144.0))
    var.put('timeEarth', Js(7.0))
    var.put('s', var.get('Date').create().callprop('getTime'))
    var.put('timeEorzea', var.get('Math').callprop('round', ((((var.get('s')/Js(1000.0))-var.get('timeAdjust'))*var.get('timeGame'))/var.get('timeEarth'))))
    var.put('timeEorzea', (var.get('Math').callprop('round', (var.get('timeEorzea')/Js(10.0)))*Js(10.0)))
    var.put('m', var.get('Math').callprop('floor', ((var.get('timeEorzea')%Js(3600.0))/Js(60.0))))
    return var.get('m')
PyJsHoisted_getMinute_.func_name = 'getMinute'
var.put('getMinute', PyJsHoisted_getMinute_)
@Js
def PyJsHoisted_getWeatherVar_(timeMillis, this, arguments, var=var):
    var = Scope({'timeMillis':timeMillis, 'this':this, 'arguments':arguments}, var)
    var.registers(['calcBase', 'step2', 'timeMillis', 'increment', 'h', 'bell', 'm', 'unixSeconds', 'step1', 'totalDays'])
    var.put('unixSeconds', var.get('parseInt')((var.get('timeMillis')/Js(1000.0))))
    var.put('bell', (var.get('unixSeconds')/Js(175.0)))
    var.put('h', ((var.get('bell')/Js(3600.0))%Js(24.0)))
    var.put('m', (var.get('bell')%Js(60.0)))
    var.put('increment', (((var.get('bell')+Js(8.0))-(var.get('bell')%Js(8.0)))%Js(24.0)))
    var.put('totalDays', (var.get('unixSeconds')/Js(4200.0)))
    var.put('totalDays', PyJsBshift((var.get('totalDays')<<Js(32.0)),Js(0.0)))
    var.put('calcBase', ((var.get('totalDays')*Js(100.0))+var.get('increment')))
    var.put('step1', PyJsBshift(((var.get('calcBase')<<Js(11.0))^var.get('calcBase')),Js(0.0)))
    var.put('step2', PyJsBshift((PyJsBshift(var.get('step1'),Js(8.0))^var.get('step1')),Js(0.0)))
    var.get('h')
    return (var.get('step2')%Js(100.0))
PyJsHoisted_getWeatherVar_.func_name = 'getWeatherVar'
var.put('getWeatherVar', PyJsHoisted_getWeatherVar_)
@Js
def PyJsHoisted_init_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['nowTime', 'rs', 'ret', 'weatherRs', 'wsOrder', 'place', 'j', 'map', 'serial', 'k', 'zoneWeather', 'endTime', 'h', 'i', 'm', 'startTime', 'per', 'canDo', 'ws', 'weather', 'rates', 'emotion'])
    var.put('ret', Js(''))
    var.put('rs', Js('无'))
    var.put('canDo', Js(False))
    var.put('h', var.get('getHour')())
    var.put('ws', var.get('getWeatherVar')(var.get('Date').create().callprop('getTime')))
    for PyJsTemp in var.get('note'):
        var.put('i', PyJsTemp)
        var.put('serial', var.get('note').get(var.get('i')))
        pass
        #for JS loop
        var.put('j', Js(0.0))
        while (var.get('j')<var.get('serial').get('length')):
            try:
                if (var.get('j')==Js(0.0)):
                    var.put('map', var.get('serial').get(var.get('j')))
                else:
                    if (var.get('j')==Js(1.0)):
                        var.put('weather', var.get('serial').get(var.get('j')))
                    else:
                        if (var.get('j')==Js(2.0)):
                            var.put('startTime', var.get('Number')(var.get('serial').get(var.get('j'))))
                        else:
                            if (var.get('j')==Js(3.0)):
                                var.put('endTime', var.get('Number')(var.get('serial').get(var.get('j'))))
                            else:
                                if (var.get('j')==Js(4.0)):
                                    var.put('place', var.get('serial').get(var.get('j')))
                                else:
                                    var.put('emotion', var.get('serial').get(var.get('j')))
            finally:
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
        var.put('rates', var.get('zoneRates').get(var.get('map')))
        var.put('wsOrder', Js(0.0))
        #for JS loop
        var.put('k', Js(0.0))
        while (var.get('k')<(var.get('rates').get('length')-Js(1.0))):
            try:
                if (var.get('ws')>=var.get('rates').get(var.get('k'))):
                    (var.put('wsOrder',Js(var.get('wsOrder').to_number())+Js(1))-Js(1))
                else:
                    break
            finally:
                    (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
        var.put('zoneWeather', var.get('zoneWeathers').get(var.get('map')))
        var.put('weatherRs', var.get('zoneWeather').get(var.get('wsOrder')))
        if ((var.get('weather')==var.get('weatherRs')) and var.get('checkTime')(var.get('h'), var.get('startTime'), var.get('endTime'))):
            if var.get('canDo').neg():
                var.put('canDo', Js(True))
                var.put('rs', Js(''))
            var.put('place', var.get('place').callprop('replace', Js('_'), Js(',')))
            var.put('rs', ((((((((((((((Js('探索笔记[')+var.get('i'))+Js(']：'))+var.get('map'))+Js(' | 坐标：'))+var.get('place'))+Js(' | 时间：'))+var.get('startTime'))+Js(':00-'))+(var.get('endTime')-Js(1.0)))+Js(':59 | 天气:'))+var.get('weather'))+Js(' | 情感动作：'))+var.get('emotion'))+Js('\r')))
            var.put('m', var.get('getMinute')())
            var.put('nowTime', (var.get('h')+(var.get('m')/Js(60.0))))
            var.put('per', var.get('getPerTime')(var.get('nowTime'), var.get('startTime'), var.get('endTime')))
            var.put('ret', ((((((((((((((((var.get('i')+Js('|'))+var.get('map'))+Js('|'))+var.get('place'))+Js('|'))+var.get('startTime'))+Js(':00-'))+(var.get('endTime')-Js(1.0)))+Js(':59'))+Js('|'))+var.get('weather'))+Js('|'))+var.get('emotion'))+Js('|'))+var.get('per'))+Js('%\n')), '+')
    return var.get('ret')
PyJsHoisted_init_.func_name = 'init'
var.put('init', PyJsHoisted_init_)
@Js
def PyJsHoisted_checkTime_(now, start, end, this, arguments, var=var):
    var = Scope({'now':now, 'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
    var.registers(['start', 'now', 'end'])
    if (var.get('start')<var.get('end')):
        if ((var.get('now')>=var.get('start')) and (var.get('now')<var.get('end'))):
            return Js(True)
        else:
            return Js(False)
    else:
        if (var.get('now')>=var.get('start')):
            return Js(True)
        else:
            if (var.get('now')<var.get('end')):
                return Js(True)
            else:
                return Js(False)
PyJsHoisted_checkTime_.func_name = 'checkTime'
var.put('checkTime', PyJsHoisted_checkTime_)
@Js
def PyJsHoisted_getPerTime_(now, start, end, this, arguments, var=var):
    var = Scope({'now':now, 'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
    var.registers(['start', 'end', 'all', 'rs', 'now'])
    pass
    if (var.get('start')<var.get('end')):
        var.put('all', (var.get('end')-var.get('start')))
        var.put('rs', (((var.get('now')-var.get('start'))/var.get('all'))*Js(100.0)))
    else:
        var.put('all', ((Js(24.0)-var.get('start'))+var.get('end')))
        if (var.get('now')>var.get('start')):
            var.put('rs', (((var.get('now')-var.get('start'))/var.get('all'))*Js(100.0)))
        else:
            var.put('rs', ((((var.get('all')-var.get('end'))+var.get('now'))/var.get('all'))*Js(100.0)))
    return var.get('Math').callprop('round', var.get('rs'))
PyJsHoisted_getPerTime_.func_name = 'getPerTime'
var.put('getPerTime', PyJsHoisted_getPerTime_)
var.put('note', Js({'1':Js([Js('海都'), Js('晴朗'), Js('8'), Js('12'), Js('上层(9_7)'), Js('张望')]),'2':Js([Js('海都'), Js('碧空'), Js('18'), Js('5'), Js('下层(7_15)'), Js('张望')]),'3':Js([Js('中拉诺西亚'), Js('小雨'), Js('5'), Js('8'), Js('(20_19）'), Js('祈祷')]),'4':Js([Js('中拉诺西亚'), Js('晴朗'), Js('12'), Js('17'), Js('(16_17)'), Js('张望')]),'5':Js([Js('中拉诺西亚'), Js('阴云'), Js('8'), Js('12'), Js('(25_27)'), Js('张望')]),'6':Js([Js('拉诺西亚低地'), Js('晴朗'), Js('18'), Js('5'), Js('(23_40)'), Js('张望')]),'7':Js([Js('拉诺西亚低地'), Js('薄雾'), Js('5'), Js('8'), Js('(33_19)'), Js('张望')]),'8':Js([Js('西拉诺西亚'), Js('晴朗'), Js('5'), Js('8'), Js('(29_30)'), Js('张望')]),'9':Js([Js('森都'), Js('阴云'), Js('12'), Js('17'), Js('旧街(12_8)'), Js('张望')]),'10':Js([Js('森都'), Js('碧空'), Js('18'), Js('5'), Js('旧街(10_6)'), Js('张望')]),'11':Js([Js('黑衣森林中央林区'), Js('晴朗'), Js('12'), Js('17'), Js('(21_21)'), Js('坐下')]),'12':Js([Js('黑衣森林东部林区'), Js('晴朗'), Js('8'), Js('12'), Js('(17_18)'), Js('祈祷')]),'13':Js([Js('黑衣森林东部林区'), Js('碧空'), Js('18'), Js('5'), Js('(22_26)'), Js('张望')]),'14':Js([Js('沙都'), Js('晴朗'), Js('5'), Js('8'), Js('来生回廊(11_11)'), Js('敬礼')]),'15':Js([Js('沙都'), Js('阴云'), Js('12'), Js('17'), Js('来生回廊(11_11)'), Js('张望')]),'16':Js([Js('西萨纳兰'), Js('晴朗'), Js('18'), Js('5'), Js('(22_22)'), Js('张望')]),'17':Js([Js('中萨纳兰'), Js('薄雾'), Js('8'), Js('12'), Js('(15_22)'), Js('张望')]),'18':Js([Js('东萨纳兰'), Js('小雨'), Js('17'), Js('18'), Js('(19_24)'), Js('安慰')]),'19':Js([Js('东萨纳兰'), Js('阴云'), Js('8'), Js('12'), Js('(14_18)'), Js('张望')]),'20':Js([Js('东萨纳兰'), Js('晴朗'), Js('5'), Js('8'), Js('(21_20)'), Js('祈祷')]),'21':Js([Js('中拉诺西亚'), Js('晴朗'), Js('12'), Js('17'), Js('(20_13)'), Js('张望')]),'22':Js([Js('中拉诺西亚'), Js('碧空'), Js('5'), Js('8'), Js('(25_17)'), Js('张望')]),'23':Js([Js('拉诺西亚低地'), Js('小雨'), Js('12'), Js('17'), Js('(31_12)'), Js('张望')]),'24':Js([Js('东拉诺西亚'), Js('碧空'), Js('8'), Js('12'), Js('(32_23)'), Js('坐下')]),'25':Js([Js('东拉诺西亚'), Js('小雨'), Js('18'), Js('5'), Js('(29_33)'), Js('张望')]),'26':Js([Js('西拉诺西亚'), Js('碧空'), Js('17'), Js('18'), Js('(26_26)'), Js('祈祷')]),'27':Js([Js('西拉诺西亚'), Js('强风'), Js('18'), Js('5'), Js('(17_36)'), Js('张望')]),'28':Js([Js('西拉诺西亚'), Js('晴朗'), Js('8'), Js('12'), Js('(22_22)'), Js('张望')]),'29':Js([Js('西拉诺西亚'), Js('碧空'), Js('12'), Js('17'), Js('(19_23)'), Js('张望')]),'30':Js([Js('拉诺西亚高地'), Js('晴朗'), Js('17'), Js('18'), Js('(30_22)'), Js('张望')]),'31':Js([Js('拉诺西亚高地'), Js('碧空'), Js('12'), Js('17'), Js('(13_21)'), Js('张望')]),'32':Js([Js('拉诺西亚高地'), Js('雷雨'), Js('18'), Js('5'), Js('(29_25)'), Js('张望')]),'33':Js([Js('拉诺西亚外地'), Js('晴朗'), Js('18'), Js('5'), Js('(12_15)'), Js('张望')]),'34':Js([Js('拉诺西亚外地'), Js('阴云'), Js('5'), Js('8'), Js('(17_16)'), Js('张望')]),'35':Js([Js('拉诺西亚外地'), Js('碧空'), Js('12'), Js('17'), Js('(23_11)'), Js('张望')]),'36':Js([Js('拉诺西亚外地'), Js('小雨'), Js('18'), Js('5'), Js('(15_10)'), Js('坐下')]),'37':Js([Js('森都'), Js('晴朗'), Js('8'), Js('12'), Js('新街(14_14)'), Js('张望')]),'38':Js([Js('森都'), Js('小雨'), Js('5'), Js('8'), Js('旧街(14_5)'), Js('张望')]),'39':Js([Js('黑衣森林中央林区'), Js('小雨'), Js('5'), Js('8'), Js('(23_19)'), Js('张望')]),'40':Js([Js('黑衣森林中央林区'), Js('碧空'), Js('18'), Js('5'), Js('(13_23)'), Js('张望')]),'41':Js([Js('黑衣森林中央林区'), Js('晴朗'), Js('12'), Js('17'), Js('(16_22)'), Js('张望')]),'42':Js([Js('黑衣森林中央林区'), Js('碧空'), Js('11'), Js('14'), Js('(26_18)'), Js('张望')]),'43':Js([Js('黑衣森林东部林区'), Js('打雷'), Js('18'), Js('5'), Js('(21_10)'), Js('张望')]),'44':Js([Js('黑衣森林南部林区'), Js('雷雨'), Js('8'), Js('12'), Js('(17_20)'), Js('张望')]),'45':Js([Js('黑衣森林南部林区'), Js('碧空'), Js('8'), Js('12'), Js('(14_33)'), Js('张望')]),'46':Js([Js('黑衣森林南部林区'), Js('薄雾'), Js('12'), Js('17'), Js('(33_23)'), Js('张望')]),'47':Js([Js('黑衣森林南部林区'), Js('晴朗'), Js('5'), Js('8'), Js('(25_21)'), Js('张望')]),'48':Js([Js('黑衣森林北部林区'), Js('晴朗'), Js('12'), Js('17'), Js('(18_19)'), Js('张望')]),'49':Js([Js('黑衣森林北部林区'), Js('碧空'), Js('18'), Js('5'), Js('(15_32)'), Js('张望')]),'50':Js([Js('黑衣森林北部林区'), Js('阴云'), Js('8'), Js('12'), Js('(15_27)'), Js('张望')]),'51':Js([Js('西萨纳兰'), Js('碧空'), Js('17'), Js('18'), Js('(8_5)'), Js('张望')]),'52':Js([Js('西萨纳兰'), Js('晴朗'), Js('12'), Js('17'), Js('(12_14)'), Js('指向')]),'53':Js([Js('中萨纳兰'), Js('扬沙'), Js('18'), Js('5'), Js('(21_17)'), Js('张望')]),'54':Js([Js('中萨纳兰'), Js('碧空'), Js('12'), Js('17'), Js('(18_26)'), Js('坐下')]),'55':Js([Js('东萨纳兰'), Js('碧空'), Js('12'), Js('17'), Js('(30_26)'), Js('张望')]),'56':Js([Js('东萨纳兰'), Js('晴朗'), Js('8'), Js('12'), Js('(10_16)'), Js('张望')]),'57':Js([Js('东萨纳兰'), Js('暴雨'), Js('18'), Js('5'), Js('(25_14)'), Js('祈祷')]),'58':Js([Js('南萨纳兰'), Js('薄雾'), Js('5'), Js('8'), Js('(12_22)'), Js('祈祷')]),'59':Js([Js('南萨纳兰'), Js('晴朗'), Js('5'), Js('8'), Js('(19_20)'), Js('张望')]),'60':Js([Js('南萨纳兰'), Js('热浪'), Js('12'), Js('17'), Js('(21_38)'), Js('张望')]),'61':Js([Js('南萨纳兰'), Js('晴朗'), Js('12'), Js('17'), Js('(23_11)'), Js('张望')]),'62':Js([Js('南萨纳兰'), Js('热浪'), Js('5'), Js('8'), Js('(14_26)'), Js('激励')]),'63':Js([Js('北萨纳兰'), Js('碧空'), Js('5'), Js('8'), Js('(21_24)'), Js('敬礼')]),'64':Js([Js('北萨纳兰'), Js('晴朗'), Js('18'), Js('5'), Js('(20_29)'), Js('张望')]),'65':Js([Js('北萨纳兰'), Js('晴朗'), Js('12'), Js('17'), Js('(20_22)'), Js('张望')]),'66':Js([Js('北萨纳兰'), Js('阴云'), Js('8'), Js('12'), Js('(19_17)'), Js('张望')]),'67':Js([Js('北萨纳兰'), Js('薄雾'), Js('18'), Js('5'), Js('(26_22)'), Js('张望')]),'68':Js([Js('库尔扎斯中央高地'), Js('碧空'), Js('17'), Js('18'), Js('(25_29)'), Js('张望')]),'69':Js([Js('库尔扎斯中央高地'), Js('薄雾'), Js('18'), Js('5'), Js('(25_29)'), Js('张望')]),'70':Js([Js('库尔扎斯中央高地'), Js('暴雪'), Js('8'), Js('12'), Js('(11_15)'), Js('张望')]),'71':Js([Js('库尔扎斯中央高地'), Js('晴朗'), Js('5'), Js('8'), Js('(12_17)'), Js('张望')]),'72':Js([Js('库尔扎斯中央高地'), Js('碧空'), Js('17'), Js('18'), Js('(7_28)'), Js('张望')]),'73':Js([Js('库尔扎斯中央高地'), Js('暴雪'), Js('18'), Js('5'), Js('(7_31)'), Js('张望')]),'74':Js([Js('库尔扎斯中央高地'), Js('晴朗'), Js('8'), Js('12'), Js('(2_21)'), Js('张望')]),'75':Js([Js('库尔扎斯中央高地'), Js('晴朗'), Js('12'), Js('17'), Js('(26_17)'), Js('张望')]),'76':Js([Js('库尔扎斯中央高地'), Js('碧空'), Js('5'), Js('8'), Js('(28_10)'), Js('张望')]),'77':Js([Js('摩杜纳'), Js('妖雾'), Js('12'), Js('17'), Js('(9_13)'), Js('张望')]),'78':Js([Js('摩杜纳'), Js('晴朗'), Js('18'), Js('5'), Js('(27_8)'), Js('张望')]),'79':Js([Js('摩杜纳'), Js('碧空'), Js('12'), Js('17'), Js('(18_17)'), Js('张望')]),'80':Js([Js('摩杜纳'), Js('晴朗'), Js('17'), Js('18'), Js('(26_21)'), Js('坐下')])}))
var.put('zoneWeathers', Js({'海都':Js([Js('阴云'), Js('碧空'), Js('晴朗'), Js('薄雾'), Js('小雨')]),'中拉诺西亚':Js([Js('阴云'), Js('碧空'), Js('晴朗'), Js('微风'), Js('薄雾'), Js('小雨')]),'拉诺西亚低地':Js([Js('阴云'), Js('碧空'), Js('晴朗'), Js('微风'), Js('薄雾'), Js('小雨')]),'东拉诺西亚':Js([Js('薄雾'), Js('碧空'), Js('晴朗'), Js('阴云'), Js('小雨'), Js('暴雨')]),'西拉诺西亚':Js([Js('薄雾'), Js('碧空'), Js('晴朗'), Js('阴云'), Js('微风'), Js('强风')]),'拉诺西亚高地':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('打雷'), Js('雷雨')]),'拉诺西亚外地':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('小雨')]),'海雾村':Js([Js('阴云'), Js('碧空'), Js('晴朗'), Js('晴朗'), Js('薄雾'), Js('小雨')]),'森都':Js([Js('小雨'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空'), Js('晴朗')]),'黑衣森林中央林区':Js([Js('打雷'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空'), Js('晴朗')]),'黑衣森林东部林区':Js([Js('打雷'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空'), Js('晴朗')]),'黑衣森林南部林区':Js([Js('薄雾'), Js('雷雨'), Js('打雷'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空')]),'黑衣森林北部林区':Js([Js('薄雾'), Js('暴雨'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空')]),'薰衣草苗圃':Js([Js('阴云'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空'), Js('晴朗')]),'沙都':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('小雨')]),'西萨纳兰':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('小雨')]),'中萨纳兰':Js([Js('扬沙'), Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('小雨')]),'东萨纳兰':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('小雨'), Js('暴雨')]),'南萨纳兰':Js([Js('热浪'), Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾')]),'北萨纳兰':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾')]),'高脚孤丘':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('小雨')]),'伊修加德':Js([Js('小雪'), Js('晴朗'), Js('碧空'), Js('阴云'), Js('薄雾')]),'库尔扎斯中央高地':Js([Js('暴雪'), Js('小雪'), Js('晴朗'), Js('碧空'), Js('阴云'), Js('薄雾')]),'库尔扎斯西部高地':Js([Js('暴雪'), Js('小雪'), Js('晴朗'), Js('碧空'), Js('阴云'), Js('薄雾')]),'阿巴拉提亚云海':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('微风'), Js('灵风')]),'魔大陆':Js([Js('晴朗'), Js('阴云'), Js('打雷')]),'空岛':Js([Js('晴朗'), Js('薄雾'), Js('微风'), Js('灵风')]),'田园郡':Js([Js('阴云'), Js('薄雾'), Js('小雨'), Js('暴雨'), Js('碧空'), Js('晴朗')]),'龙堡中央高地':Js([Js('阴云'), Js('薄雾'), Js('打雷'), Js('扬沙'), Js('碧空'), Js('晴朗')]),'龙堡内陆低地':Js([Js('阴云'), Js('薄雾'), Js('小雨'), Js('暴雨'), Js('碧空'), Js('晴朗')]),'翻云雾海':Js([Js('阴云'), Js('强风'), Js('灵电'), Js('碧空'), Js('晴朗')]),'摩杜纳':Js([Js('阴云'), Js('薄雾'), Js('妖雾'), Js('碧空'), Js('晴朗')]),'神拳痕':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('打雷')]),'基拉巴尼亚边区':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('打雷')]),'基拉巴尼亚山区':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('微风'), Js('扬沙')]),'基拉巴尼亚湖区':Js([Js('碧空'), Js('晴朗'), Js('阴云'), Js('薄雾'), Js('雷雨')]),'黄金港':Js([Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空')]),'白银乡':Js([Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空')]),'红玉海':Js([Js('打雷'), Js('微风'), Js('阴云'), Js('晴朗'), Js('碧空')]),'延夏':Js([Js('暴雨'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空')]),'太阳神草原':Js([Js('强风'), Js('微风'), Js('小雨'), Js('薄雾'), Js('阴云'), Js('晴朗'), Js('碧空')]),'常风':Js([Js('晴朗'), Js('强风'), Js('暴雨'), Js('小雪')]),'恒冰':Js([Js('碧空'), Js('薄雾'), Js('热浪'), Js('小雪'), Js('打雷'), Js('暴雪')]),'涌火':Js([Js('晴朗'), Js('热浪'), Js('打雷'), Js('暴雪'), Js('灵风'), Js('小雪')]),'丰水':Js([Js('晴朗'), Js('暴雨'), Js('妖雾'), Js('雷雨'), Js('小雪')])}))
var.put('zoneRates', Js({'海都':Js([Js(20.0), Js(50.0), Js(80.0), Js(90.0), Js(100.0)]),'中拉诺西亚':Js([Js(20.0), Js(50.0), Js(70.0), Js(80.0), Js(90.0), Js(100.0)]),'拉诺西亚低地':Js([Js(20.0), Js(50.0), Js(70.0), Js(80.0), Js(90.0), Js(100.0)]),'东拉诺西亚':Js([Js(5.0), Js(50.0), Js(80.0), Js(90.0), Js(95.0), Js(100.0)]),'西拉诺西亚':Js([Js(10.0), Js(40.0), Js(60.0), Js(80.0), Js(90.0), Js(100.0)]),'拉诺西亚高地':Js([Js(30.0), Js(50.0), Js(70.0), Js(80.0), Js(90.0), Js(100.0)]),'拉诺西亚外地':Js([Js(30.0), Js(50.0), Js(70.0), Js(85.0), Js(100.0)]),'海雾村':Js([Js(20.0), Js(50.0), Js(70.0), Js(80.0), Js(90.0), Js(100.0)]),'森都':Js([Js(5.0), Js(20.0), Js(30.0), Js(40.0), Js(55.0), Js(85.0), Js(100.0)]),'黑衣森林中央林区':Js([Js(5.0), Js(20.0), Js(30.0), Js(40.0), Js(55.0), Js(85.0), Js(100.0)]),'黑衣森林东部林区':Js([Js(5.0), Js(20.0), Js(30.0), Js(40.0), Js(55.0), Js(85.0), Js(100.0)]),'黑衣森林南部林区':Js([Js(5.0), Js(10.0), Js(25.0), Js(30.0), Js(40.0), Js(70.0), Js(100.0)]),'黑衣森林北部林区':Js([Js(5.0), Js(10.0), Js(25.0), Js(30.0), Js(40.0), Js(70.0), Js(100.0)]),'薰衣草苗圃':Js([Js(5.0), Js(20.0), Js(30.0), Js(40.0), Js(55.0), Js(85.0), Js(100.0)]),'沙都':Js([Js(40.0), Js(60.0), Js(85.0), Js(95.0), Js(100.0)]),'西萨纳兰':Js([Js(40.0), Js(60.0), Js(85.0), Js(95.0), Js(100.0)]),'中萨纳兰':Js([Js(15.0), Js(55.0), Js(75.0), Js(85.0), Js(95.0), Js(100.0)]),'东萨纳兰':Js([Js(40.0), Js(60.0), Js(70.0), Js(80.0), Js(85.0), Js(100.0)]),'南萨纳兰':Js([Js(20.0), Js(60.0), Js(80.0), Js(90.0), Js(100.0)]),'北萨纳兰':Js([Js(5.0), Js(20.0), Js(50.0), Js(100.0)]),'高脚孤丘':Js([Js(40.0), Js(60.0), Js(85.0), Js(95.0), Js(100.0)]),'伊修加德':Js([Js(60.0), Js(70.0), Js(75.0), Js(90.0), Js(100.0)]),'库尔扎斯中央高地':Js([Js(20.0), Js(60.0), Js(70.0), Js(75.0), Js(90.0), Js(100.0)]),'库尔扎斯西部高地':Js([Js(20.0), Js(60.0), Js(70.0), Js(75.0), Js(90.0), Js(100.0)]),'阿巴拉提亚云海':Js([Js(30.0), Js(60.0), Js(70.0), Js(80.0), Js(90.0), Js(100.0)]),'魔大陆':Js([Js(35.0), Js(70.0), Js(100.0)]),'空岛':Js([Js(30.0), Js(60.0), Js(90.0), Js(100.0)]),'田园郡':Js([Js(10.0), Js(20.0), Js(30.0), Js(40.0), Js(70.0), Js(100.0)]),'龙堡中央高地':Js([Js(10.0), Js(20.0), Js(30.0), Js(40.0), Js(70.0), Js(100.0)]),'龙堡内陆低s':Js([Js(10.0), Js(20.0), Js(30.0), Js(40.0), Js(70.0), Js(100.0)]),'翻云雾海':Js([Js(10.0), Js(20.0), Js(40.0), Js(70.0), Js(100.0)]),'摩杜纳':Js([Js(15.0), Js(30.0), Js(60.0), Js(75.0), Js(100.0)]),'神拳痕':Js([Js(15.0), Js(60.0), Js(80.0), Js(90.0), Js(100.0)]),'基拉巴尼亚边区s':Js([Js(15.0), Js(60.0), Js(80.0), Js(90.0), Js(100.0)]),'基拉巴尼亚山区':Js([Js(10.0), Js(60.0), Js(75.0), Js(85.0), Js(95.0), Js(100.0)]),'基拉巴尼亚湖区':Js([Js(20.0), Js(60.0), Js(80.0), Js(90.0), Js(100.0)]),'黄金港':Js([Js(10.0), Js(20.0), Js(40.0), Js(80.0), Js(100.0)]),'白银乡':Js([Js(10.0), Js(20.0), Js(40.0), Js(80.0), Js(100.0)]),'红玉海':Js([Js(10.0), Js(20.0), Js(35.0), Js(75.0), Js(100.0)]),'延夏':Js([Js(5.0), Js(15.0), Js(25.0), Js(40.0), Js(80.0), Js(100.0)]),'太阳神草原':Js([Js(5.0), Js(10.0), Js(17.0), Js(25.0), Js(35.0), Js(75.0), Js(100.0)]),'常风':Js([Js(30.0), Js(60.0), Js(90.0), Js(100.0)]),'恒冰':Js([Js(10.0), Js(28.0), Js(46.0), Js(64.0), Js(82.0), Js(100.0)]),'涌火':Js([Js(10.0), Js(28.0), Js(46.0), Js(64.0), Js(82.0), Js(100.0)]),'丰水':Js([Js(12.0), Js(34.0), Js(56.0), Js(78.0), Js(100.0)])}))
pass
pass
pass
pass
pass
pass
pass
var.get('init')()


# Add lib to the module scope
cal = var.to_python()