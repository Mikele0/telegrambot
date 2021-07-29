import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
from mcstatus import MinecraftServer



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)





def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('eccomi ora sono attivo cazzi tuoi')
    time.sleep(4)
    update.message.reply_text('ok a parte gli scherzi sono io propio io il bot unico e fantastico di Mikele0_0, seguilo su twitch.tv/mikele0_0 , poi entra sul nostro server minecraft : ci stiamo ancora lavorando')



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('cazzo vuoi io non ti aiuto')



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)



def echo(update, context):
    if update.message.text == 'scemo' or update.message.text == 'stupido' or update.message.text == 'coglione' or update.message.text == 'Scemo' or update.message.text == 'Stupido' or update.message.text == 'Coglione':

        num = random.randint(0,4)


        if num == 1 :
            update.message.reply_text('ma vaffanculo SCIEMO DI MELDA')
        else:
            if num == 2:
                update.message.reply_text('come ti permetti COGLIONE GALATTICO')
            else:
                if num == 3:
                    update.message.reply_text('vai a fare i pompini in autostrada')
                else:
                    if num == 4:
                        update.message.reply_text('a bukkin e mammt')





    else:
            if update.message.text == 'hahaha' or update.message.text == 'hahah' or update.message.text == 'haha' or update.message.text == 'ahahah' or update.message.text == 'ahah'or update.message.text == 'Hahaha' or update.message.text == 'Ahaha':
                update.message.reply_text('cazzo ti ridi')
            else:
                if update.message.text == 'Nerdiniland' or update.message.text == 'nerdiniland' or update.message.text == 'NerdiniLand':
                    server = MinecraftServer.lookup("22_07_2021.exaroton.me")
                    status = server.status()
                    print("il server ha {0} giocatoru con un ping di {1} ms".format(status.players.online, status.latency))
                    if status.players.online == 1:
                        stato = "c'è un giocatore online"
                        update.message.reply_text(stato)
                    else:
                        stato = " NerdiniLand è IL server minecraft più bello del mondo in questo momento ci sono {0} giocatori online tu sarai il prossimo ad entrare".format(status.players.online)
                        update.message.reply_text(stato)

                else:
                    if update.message.text == 'porno trans':
                        update.message.reply_text('gay')
                        time.sleep(5)
                        update.message.reply_text('www.pornotrans.com')
















def main():
    """Start the bot."""

    updater = Updater("1943165363:AAEIQEDO5FB-1nUYDkSWtzalu8gd1EWROLs", use_context=True)


    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))



    dp.add_handler(MessageHandler(Filters.text, echo))


    dp.add_error_handler(error)


    updater.start_polling()



    updater.idle()
    


if __name__ == '__main__':
    main()
