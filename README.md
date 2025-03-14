# TON Coding Challenge 2025

为了帮助大家快速掌握 TON 生态的开发技能，我们特别设计了有趣的编程入门挑战赛。快来参与并有机会赢取 Telegram Premium 大会员！详细的比赛规则请查看群组公告。

https://t.me/TON_HongKong


> 如何参与？
> 
> Fork 本仓库的代码，回答下面的问题，然后发起一个 Pull Requests 就算成功参与。

---

## 任务 1：开发一个 bot 支持文本和命令消息回复 (30分)

### 任务描述：

1. 用户输入 wallet 或者 /wallet 后，bot 回复你的 TON 钱包地址
2. 用户输入 tg 或者 /tg 后，bot 回复你的 Telegram 用户名

### 你的答案：
（ 你的 TON 钱包地址将用于接受 SBT，你的Telegram 用户名用于接受 Telegram Premium 会员奖励）

1. Wallet address =  ?
2. Telegram username =  ?

---

## 任务 2：实现一个二级菜单功能

### 任务描述：

1. TON 的主网和测试网的合约地址有不同的格式
2. 因为 TON 是基于消息模式的，消息发送方可以指定回弹(bounceable)异常消息，在接收方地址上有差异
3. 因此，根据一个合约地址是否是主网，以及是否可以回弹(bounceable)，共有 4 个地址格式
4. 通过 [TON SDK](https://docs.ton.org/v3/guidelines/dapps/apis-sdks/sdk) 中的 Address 类可以处理不同格式的地址

### 你的答案：

（写下你的钱包地址的 4 个不同格式的值）

1. mainnet, bounceable =  ?
2. mainnet, non-bounceable =  ?
3. testnet, bounceable =  ?
4. testnet, non-bounceable =  ?

---

## 任务 3：通过 TON SDK 解析这个，获取对应信息

### 任务描述：

1. 下面有一串”`b5ee9c72`”开头的 [Bag of Cell](https://www.notion.so/1745274bd2cf80e4b8efeae385fea2b3?pvs=21) 编码
2. 这个编码包含一个 64 bit 的 unit，后面是一个 Address，再后面是一串字符串
3. 通过 [TON SDK](https://docs.ton.org/v3/guidelines/dapps/apis-sdks/sdk) 中的 Cell、Slice 等类进行解析，将 unit，address 和 string 的值打印出来

b5ee9c7241010101003600006700000000000007e98007ebd0a3f5bd5b9b3c4e0b75b17ea9db2b7e0c6074aa8b2683ce6ea571587550890cad8d8de40a89e9c43037e8b30d

### 你的答案：

（将 unit，address 和 string 的值打印出来）

1. unit = ?
2. address = ?
3. string = ?

---
