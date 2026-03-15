const { Telegraf, Markup } = require('telegraf');

// ================= НАСТРОЙКИ (МЕНЯЙ ТУТ) =================
const TOKEN = "8464569638:AAH03bPYRN-k6QXo8hTOXTPd4lPMIo1dv9s"; 
const ADMIN_ID = 8014629371; // Твой ID (цифрами, без кавычек)
const MY_NICK = "vishenka"; // Твой ник в ТГ БЕЗ @
const PAY_INFO = "тимофей 89126616714 Тинькофф "; // Твой номер для оплаты
// =========================================================

const bot = new Telegraf(TOKEN);

const mainMenu = (ctx) => {
    return ctx.replyWithHTML(
        <b>💰 STANDOFF GOLD EXCHANGE</b>\n\n +
        📥 <b>Скупаем:</b> по 0.55₽\n +
        📤 <b>Продаем:</b> по 0.65₽\n\n +
        <i>Выбирай раздел:</i>,
        Markup.inlineKeyboard([
            [Markup.button.callback('🛒 КУПИТЬ', 'buy_menu'), Markup.button.callback('💰 ПРОДАТЬ', 'sell_menu')],
            [Markup.button.callback('⭐️ ОТЗЫВЫ', 'reviews'), Markup.button.callback('👨‍💻 САППОРТ', 'support')]
        ])
    );
};

bot.start((ctx) => mainMenu(ctx));
bot.action('main_menu', (ctx) => { ctx.answerCbQuery(); mainMenu(ctx); });

bot.action('buy_menu', (ctx) => {
    ctx.answerCbQuery();
    ctx.replyWithHTML(
        <b>🛒 ПОКУПКА (0.65₽)</b>\n\n +
        • 100г — <b>65₽</b>\n +
        • 500г — <b>325₽</b>\n +
        • 1000г — <b>650₽</b>,
        Markup.inlineKeyboard([
            [Markup.button.callback('Купить 100г', 'buy_100')],
            [Markup.button.callback('Купить 500г', 'buy_500')],
            [Markup.button.callback('⬅️ НАЗАД', 'main_menu')]
        ])
    );
});

bot.action('sell_menu', (ctx) => {
    ctx.answerCbQuery();
    ctx.replyWithHTML(
        <b>💰 ПРОДАЖА (0.55₽)</b>\n\n +
        Скупаем от 100г. Выплаты на Qiwi/Карту.\n\n +
        Жми кнопку ниже, чтобы связаться:,
        Markup.inlineKeyboard([
            [Markup.button.url('🤝 ПРОДАТЬ ГОЛДУ', 'https://t.me/' + MY_NICK)],
            [Markup.button.callback('⬅️ НАЗАД', 'main_menu')]
        ])
    );
});

bot.action('buy_100', (ctx) => {
    ctx.replyWithHTML(
        ⚠️ <b>ОПЛАТА ЗАКАЗА</b>\n\n +
        Сумма: <b>65₽</b>\n +
        Номер: <code>${PAY_INFO}</code>\n\n +
        <i>После оплаты скинь чек в личку: @${MY_NICK}</i>
    );
    bot.telegram.sendMessage(ADMIN_ID, 🚀 ЗАКАЗ: @${ctx.from.username} хочет купить 100г);
});

bot.action('support', (ctx) => {
    ctx.replyWithHTML(👨‍💻 <b>ПОДДЕРЖКА:</b> @${MY_NICK});
});

bot.action('reviews', (ctx) => {
    ctx.replyWithHTML(⭐️ <b>ОТЗЫВЫ:</b> [ТВОЯ_ССЫЛКА]);
});

bot.launch();
console.log('🚀 БОТ ЗАПУЩЕН!');
