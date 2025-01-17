'''
在代码“def do_GET(self)"中，"###"从上至下为"chat.html,""script.js,""样式.css,"使用时请加上相对路径，如“动物/聊天.html”.
”
"***"为你的IPv4地址
'''
 BaseHTTPRequestHandler, HTTPServer
importjson导入

class类 SimpleHTTPRequestHandler（BaseHTTPRequestHandler）:SimpleHTTPRequestHandler（BaseHTTPRequestHandler）：(BaseHTTP请求处理器):
定义文件 do_GET（self）:定义文件 do_GET(自己):
自我。发送响应（200）发送响应(200)
自我。发送标题（"内容类型"， 'text/html'）发送标题("内容类型", 'text/html')
自我。结束头部（）结束头部()
将打开（'###'， 作为文件：与打开（'###'，'rb'）作为文件:
自我。wfile.写入（文件）.阅读（））w文件.写(文件。阅读())
将打开（'###'， 作为文件：与打开（'###'，'rb'）作为文件:
自我。wfile.写（b）'<script src="script.js"></script>'）无聊。写(b'<script src="script.js"></script>')
将打开（'###'， 作为文件：与打开（'###'，'rb'）作为文件:
自我。wfile.写（b）'<style>'）无聊。写(b'<style>')
写入（文件）.阅读（））w文件.写（文件.阅读（））
'</style>'

定义文件 do_POST（self）:定义文件 do_POST(自己):
'/消息'
self.handle_message（）处理消息（）
其他:
self.send_response（404）发送响应（404）
Self.结束标题（）

定义文件 handle_message（self）:
content_length = int（self.标题[“内容长度”]）
post_data = self.rfile.读取（内容长度）
'utf-8'
        
#检查消息是否存在
如果数据中包含“消息”和数据“消息”:
"收到的消息:"
#将消息保存到文件中
）作为文件:
文件.write（data['message'] + '\n')
        
self.send_response（200）
self.send_header（'Content-type'，'application/json'）
self.end_header（）
response = json.dump（{'status':'success'，'data': data}）
self.wfile.write（response.encode（'utf-8'）

def run（server_class=HTTPServer，handler_class=SimpleHTTPRequestHandler，端口=8080）：
服务器地址=（'***'，端口）#监听所有接口
服务器类（服务器地址，处理程序类）
打印（f"在端口{port}上启动httpd服务器”）
httpd.serve_forever（）

如果__名__=="__主"：
运行（）
