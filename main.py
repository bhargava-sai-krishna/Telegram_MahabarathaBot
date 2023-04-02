from telegram import*
from  telegram.ext import *
from requests import *
import keyboards

upd=Updater(token="5843114073:AAGTpOhbZwxtK9R2H5TykmjgQMPMIBdl38s")
dip=upd.dispatcher

parva_idn=''
sub_parva_idn=''

def processor():
    global parva_idn
    print(parva_idn)
    if parva_idn=='maha01.txt':
        return keyboards.maha01
    if parva_idn=='maha02.txt':
        return keyboards.maha02
    if parva_idn=='maha03.txt':
        return keyboards.maha03
    if parva_idn=='maha04.txt':
        return keyboards.maha04
    if parva_idn=='maha05.txt':
        return keyboards.maha05
    if parva_idn=='maha06.txt':
        return keyboards.maha06
    if parva_idn=='maha07.txt':
        return keyboards.maha07
    if parva_idn=='maha08.txt':
        return keyboards.maha08
    if parva_idn=='maha09.txt':
        return keyboards.maha09
    if parva_idn=='maha10.txt':
        return keyboards.maha10
    if parva_idn=='maha11.txt':
        return keyboards.maha11
    if parva_idn=='maha12.txt':
        return keyboards.maha12
    if parva_idn=='maha13.txt':
        return keyboards.maha13
    if parva_idn=='maha14.txt':
        return keyboards.maha14
    if parva_idn=='maha15.txt':
        return keyboards.maha15
    if parva_idn=='maha16.txt':
        return keyboards.maha16
    if parva_idn=='maha17.txt':
        return keyboards.maha17
    if parva_idn=='maha18.txt':
        return keyboards.maha18


chapter_count={1:236,
               2:80,
               3:313,
               4:72,
               5:199,
               6:124,
               7:203,
               8:96,
               9:65,
               10:18,
               11:27,
               12:365,
               13:168,
               14:92,
               15:39,
               16:8,
               17:3,
               18:6
              }

def intToRoman(num):
	m = ["", "M", "MM", "MMM"]
	c = ["", "C", "CC", "CCC", "CD", "D",
		"DC", "DCC", "DCCC", "CM "]
	x = ["", "X", "XX", "XXX", "XL", "L",
		"LX", "LXX", "LXXX", "XC"]
	i = ["", "I", "II", "III", "IV", "V",
		"VI", "VII", "VIII", "IX"]
	thousands = m[num // 1000]
	hundreds = c[(num % 1000) // 100]
	tens = x[(num % 100) // 10]
	ones = i[num % 10]

	ans = (thousands + hundreds +
		tens + ones)

	return ans

def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1

def romanToDecimal(str):
	res = 0
	i = 0

	while (i < len(str)):
		s1 = value(str[i])
		if (i + 1 < len(str)):
			s2 = value(str[i + 1])
			if (s1 >= s2):
				res = res + s1
				i = i + 1
			else:
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1
	return res
   

def parva_selecter():
    b1=InlineKeyboardButton('Parva-1',callback_data='maha01.txt')
    b2=InlineKeyboardButton('Parva-2',callback_data='maha02.txt')
    b3=InlineKeyboardButton('Parva-3',callback_data='maha03.txt')
    b4=InlineKeyboardButton('Parva-4',callback_data='maha04.txt')
    b5=InlineKeyboardButton('Parva-5',callback_data='maha05.txt')
    b6=InlineKeyboardButton('Parva-6',callback_data='maha06.txt')
    b7=InlineKeyboardButton('Parva-7',callback_data='maha07.txt')
    b8=InlineKeyboardButton('Parva-8',callback_data='maha08.txt')
    b9=InlineKeyboardButton('Parva-9',callback_data='maha09.txt')
    b10=InlineKeyboardButton('Parva-10',callback_data='maha10.txt')
    b11=InlineKeyboardButton('Parva-11',callback_data='maha11.txt')
    b12=InlineKeyboardButton('Parva-12',callback_data='maha12.txt')
    b13=InlineKeyboardButton('Parva-13',callback_data='maha13.txt')
    b14=InlineKeyboardButton('Parva-14',callback_data='maha14.txt')
    b15=InlineKeyboardButton('Parva-15',callback_data='maha15.txt')
    b16=InlineKeyboardButton('Parva-16',callback_data='maha16.txt')
    b17=InlineKeyboardButton('Parva-17',callback_data='maha17.txt')
    b18=InlineKeyboardButton('Parva-18',callback_data='maha18.txt')
    keyboard=[
    [b1, b2, b3],
    [b4, b5, b6],
    [b7, b8, b9],
    [b10, b11, b12],
    [b13, b14, b15],
    [b16, b17, b18]]
    return InlineKeyboardMarkup(keyboard)

def start_command(update: Update,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='This bot gives summary of each parva and sub-parva in mahabaratha use /select_parva to select parva you want to work with\nuse /select_sub_parva to select sub parva',)

def parva_selector_command(update: Update,context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='select the Parva that you want to know about', reply_markup=parva_selecter())

def sub_parva_selector_command(update: Update,context: CallbackContext):
    global parva_idn
    keyBoard=processor()
    context.bot.send_message(chat_id=update.effective_chat.id,text='select the sub parva that you want to know about', reply_markup=keyBoard)

def queryhandler(update: Update,context: CallbackContext):
    global parva_idn
    global sub_parva_idn
    query=update.callback_query.data
    update.callback_query.answer()
    if(query[0]=='m'):
        parva_idn=query
    else:
        sub_parva_idn=query
        required_section=sub_parva_idn[8:]
        f=open(parva_idn)
        a=romanToDecimal(required_section)
        b=a+1
        b1=intToRoman(b)
        b1='SECTION '+b1
        flag=False
        req_str=''
        for line in f:
            if line.strip() == sub_parva_idn:
                flag = True
            if flag:
                req_str=req_str+line
            if line.strip() == b1:
                flag = False
        req_str=req_str.replace(b1,"")  
        if len(req_str)>4090:
            chunk_size=4090
            chunks = [req_str[i:i+chunk_size] for i in range(0, len(req_str), chunk_size)] 
            for chunk in chunks:
                context.bot.send_message(chat_id=update.effective_chat.id, text=chunk)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,text=req_str)


dip.add_handler(CommandHandler('start',start_command))
dip.add_handler(CommandHandler('select_parva',parva_selector_command))
dip.add_handler(CommandHandler('select_sub_parva',sub_parva_selector_command))
dip.add_handler(CallbackQueryHandler(queryhandler))

upd.start_polling()
#break point for the library should be SECTION with case sensitivity