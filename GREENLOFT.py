import web

urls = (
    '/', 'index',
    '/prayer_table','prayer_table',
    '/ZW','ZW',
)

def getHTML():
    return"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WELCOME TO GREEN LOFT legacy</title>
    <style>
    .center-image {
        display: block;
        margin: 20px auto;
        max-width: 80%; /* 限制图片最大宽度 */
        height: auto; /* 保持图片比例 */
        border-radius: 10px; /* 让图片有圆角效果（可选） */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 添加阴影（可选） */
    }
</style>

    <img src="https://github.com/IvanLee1105/my.photo/blob/main/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202025-02-25%20121222.png?raw=true" alt="公司图片" class="center-image">
    <style>
        body {

            font-family: 'Segoe UI', Arial, sans-serif;
            background:linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
            url('https://github.com/IvanLee1105/my.photo/blob/main/tsg.jpg?raw=true') no-repeat center center;
            color: #333;
            padding: 20px;
            text-align: center;
        }
        .contact-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            display: inline-block;
            margin: 20px;
            padding: 20px;
            text-align: left;
            max-width: 300px;
        }
        .contact-card h2 {
            color: #2A5C82;
            font-size: 1.5em;
            margin-bottom: 10px;
        }
        .contact-card p {
            margin: 5px 0;
        }
        .contact-card a {
            color: #2A5C82;
            text-decoration: none;
        }
        .contact-card a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>联系我们</h1>

    <!-- 第一人信息 -->
    <div class="contact-card">
        <h2>STANLEY WONG</h2>
        <p>职位：老板</p>
        <p>电话：<a href="tel:+60 197256827">+60 19-725 6827</a></p>
        <p>邮箱：<a href="mailto:Greenloftlegacy27@gmail.com">Greenloftlegacy27@gmail.com</a></p>
    </div>

    <!-- 第二人信息 -->
    <div class="contact-card">
        <h2>WAN SAU FONG</h2>
        <p>职位：理财</p>
        <p>电话：<a href="tel:+60 123610303">+60 12-3610303</a></p>
        <p>邮箱：<a href="mailto:Greenloftlegacy27@gmail.com">Greenloftlegacy27@gmail.com</a></p>
    </div>
    <div class="button-container">
        <a href="/prayer_table"><button class="custom-button">天神屋</button></a>
        <a href="/ZW"><button class="custom-button">植物</button></a>
        <style>
    .center-image {
        display: block;
        margin: 20px auto;
        max-width: 80%;
        height: auto;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .button-container {
        text-align: center;
        margin-top: 30px;
    }

    .custom-button {
        background-color: #2A5C82;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
        margin: 10px;
        transition: 0.3s;
    }

    .custom-button:hover {
        background-color: #1e4b66;
    }

    .custom-button a {
        text-decoration: none;
        color: white;
    }
</style>

    </div>
</body>
</html>
"""

def tianshenwu():
    return"""
    <!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我们的服务</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f5f5f5;
            color: #333;
            text-align: center;
            padding: 20px;
        }

        h1 {
            color: #2A5C82;
        }

        .product-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 20px;
        }

        .product-card {
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            width: 250px;
            text-align: center;
        }

        .product-card img {
            width: 100%;
            border-radius: 10px;
        }

        .product-card h2 {
            font-size: 1.2em;
            margin: 10px 0;
            color: #2A5C82;
        }

        .product-card p {
            font-size: 1em;
            margin: 5px 0;
        }

        .back-button {
            display: inline-block;
            margin-top: 30px;
            padding: 10px 20px;
            font-size: 16px;
            background-color: #2A5C82;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            transition: 0.3s;
        }

        .back-button:hover {
            background-color: #1e4b66;
        }
    </style>
</head>
<body>

    <h1>我们的服务</h1>

    <!-- 商品展示区域 -->
    <div class="product-container">
        <!-- 商品1 -->
        <div class="product-card">
            <img src="product1.jpg" alt="产品1">
            <h2>产品名称 1</h2>
            <p>价格：￥100</p>
        </div>

        <!-- 商品2 -->
        <div class="product-card">
            <img src="product2.jpg" alt="产品2">
            <h2>产品名称 2</h2>
            <p>价格：￥150</p>
        </div>

        <!-- 商品3 -->
        <div class="product-card">
            <img src="product3.jpg" alt="产品3">
            <h2>产品名称 3</h2>
            <p>价格：￥200</p>
        </div>
    </div>

    <!-- 返回按钮 -->
    <a href="/" class="back-button">返回首页</a>

</body>
</html>
"""

webpage = web.application(urls, globals())

class index:
    def GET(self):
        return getHTML()
    
class prayer_table():
    def GET(self):
        return tianshenwu()
    
if __name__ == "__main__":
    webpage.run()

