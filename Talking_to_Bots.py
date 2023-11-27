import logging 
        from telegram import InlineKeyboardButton, 
          InlineKeyboardMarkup 
        from telegram.ext import Updater,  
          CommandHandler, CallbackQueryHandler 
        import emoji 
 
        logging.basicConfig(format='%(asctime)s  
          - %(name)s - %(levelname)s - %(message)s', 
        level=logging.INFO) 
 
 
        def start(bot, update): 
            keyboard = [ 
                [InlineKeyboardButton("Happy", callback_data='1'), 
                InlineKeyboardButton("Whatever", callback_data='2')], 
                [InlineKeyboardButton("Sad", callback_data='3')]] 
 
            reply_markup = InlineKeyboardMarkup(keyboard) 
 
            update.message.reply_text('Hey there!  
              How do you feel today?', reply_markup=reply_markup) 
 
 
        def button(bot, update): 
            query = update.callback_query 
        if query.data == "1": 
                em = emoji.emojize(':smile:', use_aliases=True) 
                bot.editMessageText(text="Oh wow! %s " % em, 
        chat_id=query.message.chat_id, 
        message_id=query.message.message_id) 
 
        if query.data == "2": 
                em = emoji.emojize(':expressionless:', use_aliases=True) 
                bot.editMessageText(text="Does it matter? %s " % em, 
        chat_id=query.message.chat_id, 
        message_id=query.message.message_id) 
 
 
        if query.data == "3": 
            em = emoji.emojize(':disappointed:', use_aliases=True) 