> 前提说明:
> * API调用遵循RESTful规范
> * jQuery `$.ajax()` 方法的 `type`参数可选值:
>     - `GET`: 查询 数据列表 或 单个数据
>     - `POST`: 添加 数据
>     - `PUT`: 更新 数据
>     - `DELETE`: 删除 数据
>     - `OPTIONS`:  查看Api信息
>     - `PATCH`: 更新 数据
> * `DELETE`、`OPTIONS` 无需`data`参数
> * `GET` `data`参数可选, 用户查询筛选
> * `POST`、`PUT` 需要完整`data`参数
> * `PATCH` 暂时保留不使用
> * 页面中相关的js常量:
>     ```js
>     // API根路径
>     GLOGAL.API_BASE = "/api/";
>     // 当前用户(可能未登录)
>     GLOGAL.CURRENT_USER = {
>         "id": 2,
>         "username": "admin",
>         "phone": "13271955906",
>         "url": "http://127.0.0.1:8989/api/users/2/"
>     };
>     // 用户是否登录
>     GLOGAL.CURRENT_LOGINED = true;
>     ```
> * 注意: 调用api的请求`url`必须以`/`结尾

## 示例 - jQuery 发送 ajax 调用 Api
- 添加/更新 通用代码:
    ```js
    var data = {
        /*内容省略, 参见下方 `data` 结构*/
    };
    $.ajax({ 
        /* type, url 省略 */
        data: JSON.stringify(data),
        processData: false,
        contentType:"application/json; charset=utf-8",
        dataType: "json",
        success: function(resp){
            console.log(resp);
        },
        error: function(jqXHR){
            alert("Error: " + jqXHR.status);
        },
    });
    ```
- 带有queryString参数的查询 通用代码:
    ```js
    var data = {
        /*内容省略, 可为空*/
    };
    $.ajax({ 
        /* type, url 省略 */
        data: data,
        dataType: "json",
        success: function(resp){
            console.log(resp);
        },
        error: function(jqXHR){
            alert("Error: " + jqXHR.status);
        },
    });
    ```
- 删除/无queryString参数的查询 通用代码:
    ```js
    $.ajax({ 
        /* type, url 省略 */
        dataType: "json",
        success: function(resp){
            console.log(resp);
        },
        error: function(jqXHR){
            alert("Error: " + jqXHR.status);
        },
    });

## 示例 - 请求 和 `data` 结构
> * 注
>     - 以下数据中的 `inspector` 取自 `GLOGAL.CURRENT_USER.url`
>     - 请求路径请以 `GLOGAL.API_BASE` 作为前缀拼接
>     - json 数据中的`url`格式的数据均非手动拼接得到, 而是取自现有数据

1. 添加 机构需求(单个)
    ```
    POST /api/organization-demands/
    ```
    ```json
    {
        "organization": "http://127.0.0.1:8989/api/organizations/1/",
        "name": "医用酒精",
        "remark": null,
        "amount": -1,
        "receive_amount": 0
    }
    ```
    注: `organization` 取自查询到的 `organization` 数据
2. 添加 机构募捐信息
    ```
    POST /api/organizations/
    ```
    * demo-01
    ```json
    {
        "contacts": [],
        "demands": [],
        "province": "湖北省",
        "city": "武汉市",
        "name": "武汉市人民医院",
        "address": "武汉",
        "source": "微信",
        "verified": false,
        "is_manual": false,
        "inspector": "http://127.0.0.1:8989/api/users/2/",
        "emergency": 0
    }
    ```
    * demo-02 (后端更新, 添加 `organization` 时, 嵌套数据 `contact` 和 `demand` 去掉url, `inspector` 自动取自当前登录用户)
    ```json
    {
        "contacts": [
            {
                "name": "张医生",
                "phone": "12345678971"
            }
        ],
        "demands": [
            {
                "name": "口罩",
                "remark": "GB2612-2006标准"
            },
            {
                "name": "防护服",
                "amount": 100
            }
        ],
        "province": "湖南省",
        "city": "怀化市",
        "name": "怀化市人民医院"
    }
    ```

3. 更新 机构募捐信息
    ```
    PUT /api/organizations/2/
    ```
    ```json
    {
        "url": "http://127.0.0.1:8989/api/organizations/2/",
        "id": 2,
        "contacts": [
            {
                "organization": "http://127.0.0.1:8989/api/organizations/2/",
                "name": "12345678960",
                "phone": "12345678960"
            }
        ],
        "demands": [],
        "province": "湖北省",
        "city": "武汉市",
        "name": "武汉市人民医院",
        "address": "武汉",
        "source": "微信",
        "verified": false,
        "add_time": "2020-02-01T11:13:16.896248+08:00",
        "is_manual": false,
        "inspector": "http://127.0.0.1:8989/api/users/2/",
        "emergency": 0
    }
    ```

## API自定义查询参数
* `GET /api/organizations/`
    + 精确查询
        - `province`: `string` 省, 优先级高于`scope`
        - `city`: `string` 市
        - `inspector`: `integer` 信息提交者用户id
        - `name`: `string` 机构名, 优先级高于`fuzzy_name`
        - `address`: `string` 机构地址, 优先级高于`fuzzy_address`
        - `verified`: `bool`(`true`/`false` 或 `1`/`0`) 是否已验证
    + 模糊查询
        - `fuzzy_name`: `string` 机构名
        - `fuzzy_address`: `string` 机构地址
    + 专用查询
        - `scope`: `string`, 可选值如下:
            * `wuhan`: 武汉(武汉市)
            * `hubei`: 武汉周边(湖北省中除武汉外的城市)
            * `china`: 全国各地(湖北省以外的行政区划的城市)
    + 通用参数
        - `page`: `integer` 分页查询页码