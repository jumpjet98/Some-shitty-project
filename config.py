from enum import Enum

token = ''

db_file = "database.vdb"

greetings_message="Здравствуйте! \nЯ - оплот студенческого проекта, \nа вовсе не официальный бот служб жкх. \nИзвините, если я Вас разочаровал. \nНо от меня всё же есть польза.\n"
water_problems_settings0="Позвоните по номеру горячей линии\n*246-99-99* \nДля возврата в главное меню введите _/start_"
water_problems_settings1="Позвоните по номеру центральной диспетчерской службы\n*249-46-26* или *246-43-86* \n"
light_problems_setting0="Позвоните по номеру единой диспетчерской службы \n'Городские электросети'\n*433-38-22* или *433-85-07*\nДля возврата в главное меню введите _/start_"
light_problems_setting1="Позвоните по номеру аварийной службы\nЗаречная часть: *272-07-41*\nНагорная часть: *428-08-68*\nДя возврата в главное меню введите _/start_"
gas_problems_setting0="Позвоните по номеру Центральной аварийно-диспетчерская службы:\n*252-33-00*, *252-22-07*, *436-05-53*\nДля возврата в главное меню введите _/start_"
gas_problems_setting1='Позвоните по номеру единой справочной службы "Теплоэнерго":\n*277-91-31*\nДля возврата в главное меню введите _/start_'
payment_adress="(https://www.nn.ru/oplatauslug/)"


jokes = ['Стесняюсь спросить: управляющие компании - так они нас обслуживают или они нами управляют?',
         'Две недели можно и в холодной воде помыться. Нежные какие, блин, нашлись. '
         'Детей и жену уже приучил.Сам пока для себя грею.',
         'А Путину летом тоже воду отключают?',
         'Сегодня видел парня лет 18-ти, который во дворе долбил лёд. '
         'А на спине у него распечатка: "Я не дворник. Меня просто задолбало здесь падать".',
         'Если вы, бессовестные, вовремя не оплатили ЖКУ, то они не могут вовремя украсть.',
         'Как птица гриф \n взлетел тариф.\n А пояснять вам, люди, надо ль \n какую ждет стервятник падаль?',
         'Тариф на холодную воду повышен для новосибирцев на 20 %, на горячую воду '
         '— на 15,9 %, на водоотведение — на 20,1 %, на отопление — на 14,9 %. '
         'Руководитель департамента по тарифам НСО Гарей Асмодьяров '
         'в качестве причины повышения тарифов назвал излишнюю экономность горожан.',
         'Декабрь 2009 г. Ростов-на-Дону, число не помню,но в народе этот день назвали белый четверг. '
         'Неожиданно зимой выпал снег, выпало много снега (что для Ростова редкость). '
         'И как следствие транспортный коллапс и прочие сопутствующие радости. '
         'На сайте местных новостей торжественно сообщили, что Администрацией приобретено '
         '800 единиц снегоуборочной техники. В 2010 г. в декабре, как ни удивительно,снег выпал опять. '
         'Отсутствие снегоуборочной техники на улицах города объяснялось, тем что в этом году забыли '
         'выделить деньги на заправку этой техники и зарплату водителям. '
         'Потом всё кануло в небытие. Жаль, что не догадалась, хотя бы на память, скриншот сделать.',
         ]


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    SET_NAME = "1"   # Приветствие, запись имени
    MENU = '2'
    WATER = '3'         # Подменю ВОДА
    PAY = '100'
    COST_W = '3.1'
    PROBLEM_W = '3.2'
    BROKEN_PIPE = '3.2.1'
    NO_W = '3.2.2'
    NO_HW = '3.2.3'
    OTHER_W = '3.2.4'
    ELECTR = '4'           # Подменю ЭЛЕКТРИЧЕСТВО
    COST_E = '4.1'
    PROBLEM_E = '4.2'
    NO_E = '4.2.1'
    WIRE = '4.2.2'
    OTHER_E = '4.2.3'
    GAS = '5'               # Подменю ГАЗ
    COST_G = '5.1'
    PROBLEM_G = '5.2'
    LEAK = '5.2.1'
    NO_G = '5.2.2'
    HTN = '5.2.3'
    OTHER_G = '5.2.4'
    OTHER = '6'             # Подменю ДРУГОЕ
    JOKES = '6.1'
    GRADE = '6.2'
    SHARE_NUM = '99'      # Поделиться номером телефона




# S_ENTER_AGE = "2"
# S_SEND_PIC = "3"