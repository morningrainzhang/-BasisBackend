# BasisBackend
后端开发人员必备基础知识

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

## 底层
1. 线程
1. 进程
为什么实现进程
1. 协程以及协程的实现原理
1. GIL
1. 对加密的了解

## mysql
1. 常用数据类型
1. char varchar的区别
1. 数据表链接查询
1. 数据库的索引，说一下非主键索引是怎么实现的？
存储过程
NoSQL了解么，和关系数据库的区别
MySQL优化
MySQL索引设计
MySQL锁的理解
分区和分表
最左匹配，联合索引，在哪种情况下建立索引，B树原理，explain查看语句
事务
原生语句
myisam和innodb的锁分别是什么 
1000万个数据里面删掉1000条，如何优化 
join么，有几种，有何区别，A LEFT JOIN B，查询的结果中，B没有的那部分是如何显示的（
BTree索引和hash索引的区别

## redis 了解
实现一个聊天室 不同的人发消息怎么所有人都看到，需要http长链接
redis有几种常用存储类型
如何设计性能测试平台

十万个人抢100个红包

redis持久化，如果redis现需要重启，rdb模式下怎么在重启前保存数据 

## re
正则熟悉吗，匹配一个邮箱
## 算法问题
生成器 递归
斐波那契数列
输入‘22+33’这样的字符串，用面向对象实现，尽量考虑扩展性
编程实现顺序数组错位后的查找
编程实现二分查找

## python
python3要用python2的包怎么办 
不用web框架，python里面有什么包可以开启一个web服务 
全局变量和部分变量
新式类的继承问题
浅拷贝与深拷贝的实现方式、区别；deepcopy如果你来设计，如何实现
__new__() 与 __init__()的区别
1. 内置函数
1. 装饰器
装饰器原理是使用了闭包实现的，是一种面向切面编程的模式
1. 对闭包的理解
1. 对函数对象的理解
函数是一个对象。
作为对象，

1. 可以赋值给一个变量
2. 可以作为元素添加到集合对象中
3. 可以作为参数传递给其他函数
4. 可以作为函数的返回值
支持函数的嵌套
实现了 __call__ 的类也可以作为函数

1. *args 和 **kwargs 是什么，为什么要使用它们？
经典问题，一次可以上1个台阶，也可以上2个...n个，问一共有多少种上法

手写快排；堆排；几种常用排序的算法复杂度是多少；快排平均复杂度多少，最坏情况如何优化； 
手写：已知一个长度n的无序列表，元素均是数字，要求把所有间隔为d的组合找出来，你写的解法算法复杂度多少； 
手写：一个列表A=[A1，A2，…,An]，要求把列表中所有的组合情况打印出来； 
手写：用一行python写出1+2+3+…+10**8 ； 
手写python：用递归的方式判断字符串是否为回文； 
单向链表长度未知，如何判断其中是否有环； 
单向链表如何使用快速排序算法进行排序； 
手写：一个长度n的无序数字元素列表，如何求中位数，如何尽快的估算中位数，你的算法复杂度是多少； 
如何遍历一个内部未知的文件夹（两种树的优先遍历方式）

## 数据结构
单链表逆置，编程实现
非递归实现二叉树的中序遍历
堆栈


## 排序算法
快速排序热热身，分析一下复杂度，如果不使用额外的空间，应该怎么写

## 操作系统
操作系统进行文件操作，都会需要什么步骤
Linux对内存进行操作的命令

## 其他
你最近看的三本书