## 页面开发说明
* 页面模板目录 `registration/templates/` 下
* 目前目录 `pages/` 下的所有页面均继承自基础布局模板 `base-layout.html`
* 页面模板语法需要遵循Django框架的模板规范
* `base-layout.html` 块(block)结构说明
	```
	<!DOCTYPE HTML>
	<html>
	<head>
		<title>{% block page_title %}<!-- 页面标题 -->{% endblock %}</title>
		<!-- 公共css引入： bootstrap、animate、icomoon 等 -->
		{% block head_extra_style %}<!-- 头部额外style(link-css等) -->{% endblock %}
		<!-- js针对IE兼容(respond) 和 Modernizr -->
		{% block head_extra_script %}<!-- 头部额外script(js等) -->{% endblock %}
	</head>
	<body>
		<!-- 页头导航 -->
		{% block page_main %}<!-- 页面正文 -->{% endblock %}
		<!-- 页脚 -->
		<!-- 公共js引入: jquery、bootstrap 和 jquery插件 等 -->
		<!-- js全局变量 `window.GLOGAL` 定义、ajax全局设置 -->
		{% block page_footer %}<!-- 自定义js -->{% endblock %}
	</body>
	</html>
	```
* 子页面继承 `base-layout.html` 后, 重写不同的块(block), 在不同的块(block)中编写独有的内容
* js中对全局变量 `window.GLOGA` 的使用需要根据页面顺序, 再其定义之后使用