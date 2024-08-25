# Multi-ue-Registration

对UERANSIM中的UE进行批量Copy以及向OAI核心网进行批量注册。

**涉密项目，后续技术细节不给予展示，以下内容为常识。**

此部分为脚本复现：

实现功能： 对URRANSIM中配置的UE进行批量生成；

脚本解释： run-{nums}.sh   nums：UE数量；

# 实现思路：

**基本参数设置**
   
   * imsi：国际移动用户标识（IMSI），每个用户都有唯一的 IMSI。代码通过 imsi-20893000000{sufix} 格式生成 IMSI，其中 {sufix} 是一个递增的数字，用来区分不同的用户。

   * permanentKeyValue：这是用户的永久密钥，用于认证。代码生成的密钥是 8baf473fxxxxxxxxd7097c{sufix}，其中 {sufix} 是和 IMSI 对应的部分，确保每个用户都有不同的密钥。

* ue_register 函数
   
   * 该函数负责构建 HTTP POST 请求，将用户的订阅数据发送到 5G 核心网的订阅服务器。

* URL 格式为 http://XXXXXXX:5000/api/subscriber/{imsi}/20893，其中 imsi 是用户的 IMSI，20893 是 PLMN ID（公共陆地移动网络标识），用于标识网络运营商。

* payload 是 JSON 格式的请求体，包含了用户的认证和订阅信息：

* AuthenticationSubscription：认证相关的信息，如 AMF、认证方法、OPC、密钥等。

* AccessAndMobilitySubscriptionData：访问和移动性管理相关的数据，如用户的移动性策略、速率等。

* SessionManagementSubscriptionData：会话管理相关的数据，如 PDN（分组数据网络）连接、QoS（服务质量）等。

* SmfSelectionSubscriptionData：SMF（会话管理功能）选择相关的信息。

* AmPolicyData 和 SmPolicyData：策略相关的数据。

* headers 包含了请求的元数据，如 Content-Type、User-Agent 等。

* api_request 函数
   
   * 该函数用于生成大量的用户并调用 ue_register 函数进行注册。

* count 定义了要注册的用户数量，代码中设置为 1000, 使用一个 for 循环遍历每个用户，并生成对应的 imsi 和 permanentKeyValue。 

* 使用 time.sleep(1) 控制每次注册请求之间的间隔，避免过多的请求同时发送导致服务器负载过高。

# 实现思路总结

* 用户数据生成：代码通过简单的字符串拼接生成每个用户的 IMSI 和永久密钥。

* HTTP 请求发送：使用 requests 库发送 POST 请求，将用户数据发送到指定的服务器进行注册。

* 批量处理：通过 for 循环批量生成和注册多个用户，并且通过 time.sleep 控制请求发送的速率。

# 应用场景

* 通过模拟多个用户的注册，测试服务器在高负载下的表现，以及认证和会话管理的处理能力。
