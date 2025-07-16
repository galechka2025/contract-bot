from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)
from docxtpl import DocxTemplate

(
    NOMER, DATA, NAZVANIE,
    PREDSTAVITEL_OPERATORA, DOKUMENT_OSNOVANIE_OPERATORA,
    PREDSTAVITEL_POLZOVATELYA, DOKUMENT_OSNOVANIE_POLZOVATELYA,
    FIO_OPERATORA, FIO_POLZOVATELYA,
    DOLZHNOST_OPERATORA, DOLZHNOST_POLZOVATELYA,
    YUR_ADRES, POCHTOVYI_ADRES,
    TELEFON, FAKS, EMAIL, KONTAKTNOE_LITSO,
    OGRN, INN, KPP,
    BANK, RS, KS, BIK
) = range(24)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите № договора без символа №:")
    return NOMER

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Чтобы начать — напишите 'Привет' или /start. Для отмены — /cancel.")

async def nomer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['номер_договора'] = update.message.text
    await update.message.reply_text('Введите дату договора в формате "10" июля 2025:')
    return DATA

async def data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['дата_договора'] = update.message.text
    await update.message.reply_text('Введите название организации пользователя (например ООО "Ромашка"):')
    return NAZVANIE

async def nazvanie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['название_пользователя'] = update.message.text
    await update.message.reply_text('Введите должность и ФИО подписанта со стороны оператора в родительном падеже:')
    return PREDSTAVITEL_OPERATORA

async def predstavitel_operatora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['представитель_оператора'] = update.message.text
    await update.message.reply_text('Введите документ, на основании которого оператор имеет право подписи в родительном падеже:')
    return DOKUMENT_OSNOVANIE_OPERATORA

async def dokument_osnovanie_operatora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['документ_основание_оператора'] = update.message.text
    await update.message.reply_text('Введите должность и ФИО подписанта со стороны заказчика в родительном падеже:')
    return PREDSTAVITEL_POLZOVATELYA

async def predstavitel_polzovatelya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['представитель_пользователя'] = update.message.text
    await update.message.reply_text('Введите документ, на основании которого заказчик имеет право подписи в родительном падеже:')
    return DOKUMENT_OSNOVANIE_POLZOVATELYA

async def dokument_osnovanie_polzovatelya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['документ_основание_пользователя'] = update.message.text
    await update.message.reply_text('Введите ФИО подписанта оператора в формате И.И. Иванов:')
    return FIO_OPERATORA

async def fio_operatora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['фио_подписанта_оператора'] = update.message.text
    await update.message.reply_text('Введите ФИО подписанта заказчика в формате И.И. Иванов:')
    return FIO_POLZOVATELYA

async def fio_polzovatelya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['фио_подписанта_пользователя'] = update.message.text
    await update.message.reply_text('Введите должность подписанта оператора в именительном падеже:')
    return DOLZHNOST_OPERATORA

async def dolzhnost_operatora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['должность_подписанта_оператора'] = update.message.text
    await update.message.reply_text('Введите должность подписанта заказчика в именительном падеже:')
    return DOLZHNOST_POLZOVATELYA

async def dolzhnost_polzovatelya(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['должность_подписанта_пользователя'] = update.message.text
    await update.message.reply_text('Введите юридический адрес заказчика:')
    return YUR_ADRES

async def yur_adres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['юр_адрес_пользователя'] = update.message.text
    await update.message.reply_text('Введите почтовый адрес заказчика:')
    return POCHTOVYI_ADRES

async def pochtovyi_adres(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['почтовый_адрес_пользователя'] = update.message.text
    await update.message.reply_text('Введите телефон заказчика:')
    return TELEFON

async def telefon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['телефон_пользователя'] = update.message.text
    await update.message.reply_text('Введите факс заказчика:')
    return FAKS

async def faks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['факс_пользователя'] = update.message.text
    await update.message.reply_text('Введите email заказчика:')
    return EMAIL

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['email_пользователя'] = update.message.text
    await update.message.reply_text('Введите контактное лицо заказчика в именительном падеже:')
    return KONTAKTNOE_LITSO

async def kontaktnoe_litso(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['контактное_лицо_пользователя'] = update.message.text
    await update.message.reply_text('Введите ОГРН заказчика:')
    return OGRN

async def ogrn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['огрн_пользователя'] = update.message.text
    await update.message.reply_text('Введите ИНН заказчика:')
    return INN

async def inn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['инн_пользователя'] = update.message.text
    await update.message.reply_text('Введите КПП заказчика:')
    return KPP

async def kpp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['кпп_пользователя'] = update.message.text
    await update.message.reply_text('Введите наименование банка заказчика:')
    return BANK

async def bank(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['банк_пользователя'] = update.message.text
    await update.message.reply_text('Введите расчетный счёт банка заказчика:')
    return RS

async def rs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['рс_пользователя'] = update.message.text
    await update.message.reply_text('Введите корреспондентский счёт банка заказчика:')
    return KS

async def ks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['кс_пользователя'] = update.message.text
    await update.message.reply_text('Введите БИК банка заказчика:')
    return BIK

async def bik(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['бик_пользователя'] = update.message.text
    await update.message.reply_text('Генерирую договор...')

    doc = DocxTemplate("template.docx")
    doc.render(context.user_data)
    doc.save("contract_result.docx")

    with open("contract_result.docx", "rb") as f:
        await update.message.reply_document(f, filename="contract_result.docx")

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Действие отменено. Чтобы начать заново, напишите 'Привет' или /start.")
    return ConversationHandler.END

def main():
    app = ApplicationBuilder().token("7473455482:AAGawnsxRqIaU58gSroSupIIwVYf_3nGMm0").build()

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", start),
            MessageHandler(filters.Regex("(?i)^(привет|старт|начать|поехали)$"), start)
        ],
        states={
            NOMER: [MessageHandler(filters.TEXT & ~filters.COMMAND, nomer)],
            DATA: [MessageHandler(filters.TEXT & ~filters.COMMAND, data)],
            NAZVANIE: [MessageHandler(filters.TEXT & ~filters.COMMAND, nazvanie)],
            PREDSTAVITEL_OPERATORA: [MessageHandler(filters.TEXT & ~filters.COMMAND, predstavitel_operatora)],
            DOKUMENT_OSNOVANIE_OPERATORA: [MessageHandler(filters.TEXT & ~filters.COMMAND, dokument_osnovanie_operatora)],
            PREDSTAVITEL_POLZOVATELYA: [MessageHandler(filters.TEXT & ~filters.COMMAND, predstavitel_polzovatelya)],
            DOKUMENT_OSNOVANIE_POLZOVATELYA: [MessageHandler(filters.TEXT & ~filters.COMMAND, dokument_osnovanie_polzovatelya)],
            FIO_OPERATORA: [MessageHandler(filters.TEXT & ~filters.COMMAND, fio_operatora)],
            FIO_POLZOVATELYA: [MessageHandler(filters.TEXT & ~filters.COMMAND, fio_polzovatelya)],
            DOLZHNOST_OPERATORA: [MessageHandler(filters.TEXT & ~filters.COMMAND, dolzhnost_operatora)],
            DOLZHNOST_POLZOVATELYA: [MessageHandler(filters.TEXT & ~filters.COMMAND, dolzhnost_polzovatelya)],
            YUR_ADRES: [MessageHandler(filters.TEXT & ~filters.COMMAND, yur_adres)],
            POCHTOVYI_ADRES: [MessageHandler(filters.TEXT & ~filters.COMMAND, pochtovyi_adres)],
            TELEFON: [MessageHandler(filters.TEXT & ~filters.COMMAND, telefon)],
            FAKS: [MessageHandler(filters.TEXT & ~filters.COMMAND, faks)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, email)],
            KONTAKTNOE_LITSO: [MessageHandler(filters.TEXT & ~filters.COMMAND, kontaktnoe_litso)],
            OGRN: [MessageHandler(filters.TEXT & ~filters.COMMAND, ogrn)],
            INN: [MessageHandler(filters.TEXT & ~filters.COMMAND, inn)],
            KPP: [MessageHandler(filters.TEXT & ~filters.COMMAND, kpp)],
            BANK: [MessageHandler(filters.TEXT & ~filters.COMMAND, bank)],
            RS: [MessageHandler(filters.TEXT & ~filters.COMMAND, rs)],
            KS: [MessageHandler(filters.TEXT & ~filters.COMMAND, ks)],
            BIK: [MessageHandler(filters.TEXT & ~filters.COMMAND, bik)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("help", help_command))
    print("🤖 Бот запущен и готов к работе")
    app.run_polling()

if __name__ == '__main__':
    main()
