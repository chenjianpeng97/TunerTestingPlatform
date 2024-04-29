# -*- coding: utf-8 -*-
# @Project: auto_test
# @Description: 响应消息统一处理
# @Time   : 2024-02-01 10:00
# @Author : 毛鹏
RESPONSE_MSG_0001 = (200, '获取数据成功')
RESPONSE_MSG_0002 = (200, '新增一条记录成功')
RESPONSE_MSG_0003 = (300, '保存数据时报错，请检查数据')
RESPONSE_MSG_0004 = (300, '修改数据时报错，请检查数据')
RESPONSE_MSG_0005 = (200, '删除成功')
RESPONSE_MSG_0006 = (300, '接口同步包含部分失败')
RESPONSE_MSG_0007 = (200, '接口同步成功')
RESPONSE_MSG_0008 = (300, '复制API接口失败，请检查数据')
RESPONSE_MSG_0009 = (200, '复制API接口成功')
RESPONSE_MSG_0010 = (200, '获取用例详情数据成功')
RESPONSE_MSG_0011 = (200, '新增API到用例成功')
RESPONSE_MSG_0012 = (300, '新增API到用例失败')
RESPONSE_MSG_0013 = (200, '调整API用例排序成功')
RESPONSE_MSG_0014 = (200, '刷新接口数据成功')
RESPONSE_MSG_0015 = (300, '刷新接口数据失败')
RESPONSE_MSG_0016 = (200, '获取UI页面步骤详情数据成功')
RESPONSE_MSG_0017 = (200, '获取操作类型成功')
RESPONSE_MSG_0018 = (200, '获取断言类型成功')
RESPONSE_MSG_0019 = (200, '获取断言方法成功')
RESPONSE_MSG_0020 = (200, '设置UI页面步骤排序成功')
RESPONSE_MSG_0021 = (200, '修改UI公共参数状态成功')
RESPONSE_MSG_0022 = (200, '新增项目成功')
RESPONSE_MSG_0023 = (300, '新增项目失败，请检查数据')
RESPONSE_MSG_0024 = (200, '删除项目成功')
RESPONSE_MSG_0025 = (200, '获取所有项目名称成功')
RESPONSE_MSG_0026 = (200, '获取所有项目测试文件成功')
RESPONSE_MSG_0027 = (200, '上传文件成功')
RESPONSE_MSG_0028 = (300, '请先选择所属项目再上传')
RESPONSE_MSG_0029 = (300, '文件不存在')
RESPONSE_MSG_0030 = (200, '文件删除成功')
RESPONSE_MSG_0031 = (200, '获取全部项目模块名称成功')
RESPONSE_MSG_0032 = (200, '获取所有角色成功')
RESPONSE_MSG_0033 = (200, '获取用户名称成功')
RESPONSE_MSG_0034 = (200, '修改用户绑定项目成功')
RESPONSE_MSG_0035 = (300, '修改用户绑定项目失败')
RESPONSE_MSG_0036 = (200, '修改用户绑定测试环境成功')
RESPONSE_MSG_0037 = (200, '修改用户绑定测试环境失败')
RESPONSE_MSG_0038 = (300, '原始密码不正确')
RESPONSE_MSG_0039 = (300, '两次密码输入不一致')
RESPONSE_MSG_0040 = (200, '修改密码成功')
RESPONSE_MSG_0041 = (200, '修改用户绑定测试环境和项目成功')
RESPONSE_MSG_0042 = (300, '用户名或密码错误')
RESPONSE_MSG_0043 = (200, '登录成功')
RESPONSE_MSG_0044 = (200, '获取菜单列表成功')
RESPONSE_MSG_0045 = (300, '请检查系统代理，并设置为关闭在进行测试')
RESPONSE_MSG_0046 = (200, '通知发送成功')
RESPONSE_MSG_0047 = (200, '修改通知状态成功')
RESPONSE_MSG_0048 = (300, '刷新用例步骤时，检测到步骤中包含操作类型，但是操作的数据都是空的，需要补充操作的数据')
RESPONSE_MSG_0049 = (200, '获取UI用例步骤数据成功')
RESPONSE_MSG_0050 = (200, '刷新UI用例步骤数据成功')
RESPONSE_MSG_0051 = (200, '设置UI用例排序成功')
RESPONSE_MSG_0052 = (200, '获取UI页面名称成功')
RESPONSE_MSG_0053 = (300, '该模块暂无页面，请先添加页面并收集元素')
RESPONSE_MSG_0054 = (300, '复制UI页面失败')
RESPONSE_MSG_0055 = (200, '复制UI页面成功')
RESPONSE_MSG_0056 = (300, '当前类型已有开启状态')
RESPONSE_MSG_0057 = (200, '修改UI配置成功')
RESPONSE_MSG_0058 = (300, '请先选择项目后再尝试')
RESPONSE_MSG_0059 = (200, '浏览器正在启动中...')
RESPONSE_MSG_0060 = (200, 'Redis缓存中不存在')
RESPONSE_MSG_0061 = (200, '获取随机的数据类型方法成功')
RESPONSE_MSG_0062 = (200, '获取随机数据成功')
RESPONSE_MSG_0063 = (300, '请先输入函数名称')
RESPONSE_MSG_0064 = (200, '获取定时任务用例列表成功')
RESPONSE_MSG_0065 = (200, '获取用例名称成功')
RESPONSE_MSG_0066 = (300, '批量设置到定时任务失败')
RESPONSE_MSG_0067 = (200, '批量设置到定时任务成功')
RESPONSE_MSG_0068 = (300, '复制API信息失败')
RESPONSE_MSG_0069 = (200, '复制API信息成功')
RESPONSE_MSG_0070 = (200, '修改API状态成功')
RESPONSE_MSG_0071 = (200, '获取API名称成功')
RESPONSE_MSG_0072 = (200, '执行测试API完成')
RESPONSE_MSG_0073 = (200, '复制UI用例成功')
RESPONSE_MSG_0074 = (200, '{}已收到全部用例，正在执行中...')
RESPONSE_MSG_0075 = (300, '复制UI用例失败，请检查数据')
RESPONSE_MSG_0076 = (200, '获取枚举类型成功')
RESPONSE_MSG_0077 = (200, '获取元素数据成功')
RESPONSE_MSG_0078 = (200, '判断元素中是否包含${}完成')
RESPONSE_MSG_0079 = (200, '修改元素iframe状态成功')
RESPONSE_MSG_0080 = (200, '获取元素名称成功')
RESPONSE_MSG_0081 = (200, '{}已收到元素，正在定位中...')
RESPONSE_MSG_0082 = (200, '修改一条记录成功')
RESPONSE_MSG_0083 = (200, '查询不同类型结果成功')
RESPONSE_MSG_0084 = (200, '获取API图表数据成功')
RESPONSE_MSG_0085 = (200, '翻转状态成功')
RESPONSE_MSG_0086 = (200, '获取用例名称成功')
RESPONSE_MSG_0087 = (200, '获取步骤名称成功')
RESPONSE_MSG_0088 = (200, '复制UI页面步骤成功')
RESPONSE_MSG_0089 = (300, '复制UI页面步骤失败')
RESPONSE_MSG_0090 = (200, '获取元素结果成功')
RESPONSE_MSG_0091 = (200, '获取UI图表数据成功')
RESPONSE_MSG_0092 = (200, '获取图表数据成功')
RESPONSE_MSG_0093 = (200, '获取用例总数成功')
RESPONSE_MSG_0094 = (200, '获取用例执行数成功')
RESPONSE_MSG_0095 = (200, '获取测试对象名称成功')
RESPONSE_MSG_0096 = (200, '修改SQL断言状态成功')
RESPONSE_MSG_0097 = (200, '修改定时任务状态成功')
RESPONSE_MSG_0098 = (200, '修改通知状态成功')
RESPONSE_MSG_0099 = (200, '获取定时任务列表成功')
RESPONSE_MSG_0100 = (200, '触发定时任务成功，任务正在进行中...')
RESPONSE_MSG_0101 = (200, '获取设备在线列表成功')
RESPONSE_MSG_0102 = (200, '获取设备在线列表成功')
RESPONSE_MSG_0103 = (200, '获取定时策略名称成功')
RESPONSE_MSG_0104 = (200, '修改API参数状态成功')
RESPONSE_MSG_0105 = (200, '设置API公共参数成功')
RESPONSE_MSG_0106 = (200, '获取用例级别成功')
RESPONSE_MSG_0107 = (200, '设置定时任务执行用例排序成功')
RESPONSE_MSG_0108 = (200, '批量设置定时任务执行环境成功')
RESPONSE_MSG_0109 = (200, '批量设置定时任务执行环境失败')
RESPONSE_MSG_0110 = (300, '该项目未配置mysql，不允许开启sql类型的自定义参数')
RESPONSE_MSG_0111 = (200, 'API用例执行完成')
RESPONSE_MSG_0112 = (300, '该定时任务中已经包含了您选择的用例，无需重复选择')
RESPONSE_MSG_0113 = (200, '获取最近的一条测试结果成功')
RESPONSE_MSG_0114 = (200, '用户注册成功')
RESPONSE_MSG_0115 = (300, '用户名重复，请重新输入用户名')
