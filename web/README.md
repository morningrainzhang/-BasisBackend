## WEB
1. 三次握手
1. 四次挥手
1. 三次握手四次挥手的原因
1. cookie session的区别
1. http协议 
1. RESTful的理解
1. 浏览器从输入url到页面渲染的过程
1. 域名怎么解析
1. CSRF的理解
1. XSS原理
1. 浏览器缓存的理解
1. nginx作用 
1. 三个web框架区别（flask，django，tornado） 
1. django和flask orm感觉哪个好用 
1. nginx是什么，负载均衡什么意思
1. 跨域

### 三次握手
1. 客户端向服务器端发送一个SYN，并设定连接的序号为随机数A。
2. 服务器端回送一个SYN为随机数B以及一个ACK为A+1。
3. 客户端表示接受到确认，返回ACK为B+1。完成三次握手，连接开始。

### 四次挥手
客户端向服务器端发送FIN报文表示断开请求，服务器发送ACK表示接收到信息，客户端此时进入FIN_WAIT状态。服务器端发送数据完毕后发送FIN报文，客户端发送ACK表示确认，进入TIME_WAIT（假设网络不可靠）。如果2MSL(最大报文段生存时间)内没有收到回复，则CLOSE

### HTTP长连接，HTTP短连接
HTTP长连接是通过控制headers中Connection参数来对服务器进行长连接要求：

* Connection:keep-alive
* Keep-Alive: timeout=60

但是决定权在于服务端的connection，一次HTTP操作的终点操作在服务端上，关闭也是由服务端发起的。

长连接优点：
每个连接的建立都是需要资源消耗和时间消耗的。
长连接可以省去较多的TCP建立和关闭的操作，减少浪费，节约时间。对于频繁请求资源的客户来说，较适用长连接。
短连接优点：
管理起来比较简单，存在的连接都是有用的连接，不需要额外的控制手段。可以同时处理大量连接请求。但是如果连接请求量太大的话，可能造成服务器停止工作。
### HTTP长连接，TCP长连接区别
HTTP中Keep-Alive目的是维持连接，以供复用。目的是减少TCP连接次数，提高服务器性能以及httpd服务器吞吐率。
但是长时间的tcp连接容易导致系统资源无效占用。配置不当的keep-alive，有时比重复利用连接带来的损失还更大。

TCP中keep-alive是TCP的一种检测TCP连接状况的机制，涉及到三个参数tcp_keepalive_time, tcp_keepalive_intvl, tcp_keepalive_probes。
当网络两端建立了TCP连接之后，闲置（双方没有任何数据流往来）了tcp_keepalive_time后，服务器内核就会尝试向客户端发送侦测包，来判断TCP连接状况(有可能客户端崩溃、强制关闭了应用、主机不可达等等)。如果没有收到对方的回答(ack包)，则会在 tcp_keepalive_intvl后再次尝试发送侦测包，直到收到对方的ack。如果一直没有收到对方的ack,一共会尝试 tcp_keepalive_probes次。如果尝试tcp_keepalive_probes,依然没有收到对方的ack包，则会丢弃该TCP连接。TCP连接默认闲置时间是2小时，一般设置为30分钟足够了。
