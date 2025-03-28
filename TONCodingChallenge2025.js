// 加载环境变量
require('dotenv').config();

const TelegramBot = require('node-telegram-bot-api');

// 从环境变量读取 bot token
const token = process.env.TELEGRAM_BOT_TOKEN;

// 创建一个新的 bot 实例
const bot = new TelegramBot(token, {polling: true});

// 从环境变量读取 TON 钱包地址
const MY_TON_WALLET = process.env.MY_TON_WALLET;

// 从环境变量读取 Telegram 用户名
const MY_TELEGRAM_USERNAME = process.env.MY_TELEGRAM_USERNAME;

// 监听消息
bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const text = msg.text.toLowerCase();

  // 处理 menu 命令
  if (text === 'menu' || text === '/menu') {
    const options = {
      reply_markup: {
        inline_keyboard: [
          [
            { text: 'A', callback_data: 'menu_a' },
            { text: 'B', callback_data: 'menu_b' }
          ]
        ]
      }
    };
    bot.sendMessage(chatId, '请选择一个选项:', options);
  }

  // 处理 wallet 命令
  else if (text === 'wallet' || text === '/wallet') {
    bot.sendMessage(chatId, `我的 TON 钱包地址是: ${MY_TON_WALLET}`);
  }
  
  // 处理 tg 命令
  else if (text === 'tg' || text === '/tg') {
    bot.sendMessage(chatId, `我的 Telegram 用户名是: ${MY_TELEGRAM_USERNAME}`);
  }
});

// 处理回调查询
bot.on('callback_query', async (callbackQuery) => {
  const messageId = callbackQuery.message.message_id;
  const chatId = callbackQuery.message.chat.id;
  const data = callbackQuery.data;

  if (data === 'menu_a') {
    const options = {
      reply_markup: {
        inline_keyboard: [
          [
            { text: 'A-1', callback_data: 'a_1' },
            { text: 'A-2', callback_data: 'a_2' }
          ],
          [
            { text: 'Go Back', callback_data: 'go_back' }
          ]
        ]
      }
    };
    await bot.editMessageText('您选择了 A，以下是二级菜单:', {
      chat_id: chatId,
      message_id: messageId,
      reply_markup: options.reply_markup
    });
  } else if (data === 'go_back') {
    const options = {
      reply_markup: {
        inline_keyboard: [
          [
            { text: 'A', callback_data: 'menu_a' },
            { text: 'B', callback_data: 'menu_b' }
          ]
        ]
      }
    };
    await bot.editMessageText('返回到一级菜单:', {
      chat_id: chatId,
      message_id: messageId,
      reply_markup: options.reply_markup
    });
  }
  
  // 回应回调查询以消除加载状态
  await bot.answerCallbackQuery(callbackQuery.id);
});

console.log('机器人已启动...');
