import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard
import random
import requests
token = """ваш токен"""

vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
k = random.randint(5000, 10000000)
n_M = [
    ['Na + ICl', 'NaCl + ICl', 'I2 + NaCl + ICl', 'NaCl + I2', 'Выбор темы'],
    ['FeCl3 + H2', 'FeCl2+ Cl2+ H2O', 'FeCl2 + H2', 'FeCl2 + H2+ Cl2', 'Выбор темы'],
    ['C2O', 'CO', 'CO + O2', 'C2O+ O2', 'Выбор темы'],
    ['H3PO4 + H2O + NO', 'PH3 + NO2', 'HNO2 + H3PO4', 'H3PO4 + H2O + NO2', 'Выбор темы'],
    ['H2O + Cu', 'Cu(OH)2 + H2O', 'CuH2 + H2O', 'Cu(OH)2', 'Выбор темы'],
    ['CO + Fe3C4', 'Fe + CO', 'Fe3C4 + O2', 'Fe + CO2', 'Выбор темы'],
    ['SO2 + H2O2', 'SO3 + H2O', 'SO2 + SO3 + H2O', 'SO2 + H2O', 'Выбор темы'],
    ['H2O2', 'H2O + H2O2', 'не идет', 'H2O', 'Выбор темы'],
    ['H2SiO3 + Na4Si', 'Na2SiO3 + H2SiO3', 'Na2SiO3 + NaH', 'Na2SiO3 + H2', 'Выбор темы'],
    ['NaClO2 + NaCl + H2O', 'Cl2O7 + NaClO + H2O', 'NaClO + H2O + NaCl', 'NaClO4 + NaCl + H2O', 'Выбор темы'],
    ['FeCl4', 'FeCl3', 'не идет', 'FeCl3 + Fe', 'Выбор темы'],
    ['PCl3', 'PCl5', 'PCl3 + PCl5', 'не идет', 'Выбор темы'],
    ['не идет', 'PCl3 + PCl5', 'PCl5', 'PCl3', 'Выбор темы'],
    ['CO2+ NO + H2O', 'CO2 + NO2 + H2', 'CO2+ NO2 + H2O', 'CO2 + NO + H2', 'Выбор темы'],
    ['KCl + BrCl', 'KCl + BrCl + Br2', 'Br2 + KClO', 'KCl + Br2', 'Выбор темы'],
    ['H2S + H2 + K2SO4', 'K2S +K2SO3 + H2O', 'K2SO4 + K2S + H2O', 'H2 + K2SO4 +  H2O', 'Выбор темы'],
    ['CO2 + H2', 'CH4 + CO2', 'CO2 + CO + H2', 'CO + H2', 'Выбор темы'],
    ['H2+ OF2', 'HF + H2O2', 'OF2 + HF', 'HF + O2', 'Выбор темы'],
    ['KH2PO4 + PH3', 'P2O5 + H2 + KH2PO2', 'KH2PO2 + PH3', 'K2HPO4 + PH3', 'Выбор темы'],
    ['FeCl3', 'FeCl2', 'не идет', 'FeCl3 + FeCl2', 'Выбор темы'],
    ['SO3 + Na2O', 'SO3 + Na2S', 'Na2O + Na2S', 'Na2SO4', 'Выбор темы'],
    ['CuSO4', 'CuO  + SO3', 'CuO + SO2', 'CuO  + SO3 + CuSO4', 'Выбор темы'],
    ['SiO2 + CaCO3 + P', 'CO2 + CaSiO3  + P', 'CaCO3 + SiO2 + P', 'CaSiO3  + CO + P', 'Выбор темы'],
    ['NO2 + H3PO3', 'NO + H3PO4', 'NO2 + H3PO4', 'H2 + NO + H3PO4', 'Выбор темы'],
    ['S + H3PO4', 'H2O + SO2 + H3PO4', 'SO2 + H3PO4', 'H2S + H3PO4', 'Выбор темы'],
    ['N2 + H2O', 'H2 + NO', 'H2 + N2 + H2O', 'NO + H2O', 'Выбор темы'],
    ['HNO3', 'NO2 + H2O', 'HNO3+ H2O', 'H2O + N2', 'Выбор темы'],
    ['NO + SO2', 'NO + SO3', 'SO3+ N2', 'SO2 + N2', 'Выбор темы'],
    ['O2 + KCl + P2O5', 'P2O3 + KClO', 'P2O3 + Cl2 + KCl', 'KCl + P2O5', 'Выбор темы'],
    ['CO + KBr', ' Br2 + KBrO + CO', 'KBrO + CO', 'CO2  + KBr', 'Выбор темы'],
    ['HI + O2', 'HI + I2O5', 'HIO3 + HI', 'HIO3 + H2O', 'Выбор темы'],
    ['Cl2O5 + HIO3', 'O2 + I2O5 + HCl', 'HIO3 + HCl', 'HIO3 + I2O5 + HCl', 'Выбор темы'],
    ['KNO3 + NO + HBr', 'H2O2 + KNO3 + HBr', 'KNO3 + HBr', 'KNO3 + N2  + HBrO3', 'Выбор темы'],
    ['N2 + HIO + H2', 'HIO + NO2 + H2O', 'NO2 + HI + H2O', 'HIO3 + NO2 + H2O', 'Выбор темы'],
    ['H2SO3 + NO+ H2O', 'NO2 + H2O + H2S', 'H2SO4 + NO+ H2O', 'H2SO4 + NO2 + H2O', 'Выбор темы'],
    ['HNO3  + N2O5', 'NO + HNO2', 'HNO3', 'HNO3 + HNO2', 'Выбор темы'],
    ['H2O2 + NO2', 'H2O + NO2', 'H2O2 + N2', 'N2 + H2O', 'Выбор темы'],
    ['KClO4 + H2O + KCl', 'KCl + H2O', 'KClO3 + KCl + H2O', 'KClO +  KClO4 + H2O', 'Выбор темы'],
    ['СаС2 + CO2', 'CaCO3', 'Ca + CO', 'СаС2 + СО', 'Выбор темы'],
    ['CuCO3', 'Cu + CO', 'Cu + CO2', 'CuCO3 + Cu', 'Выбор темы'],
    ['CO2 + Cl2O5', 'COCl2 + CO2', 'Cl2O5 + C', 'COCl2', 'Выбор темы'],
    ['F2 + SiF4 + H2', 'F2 + SiH4', 'SiF4 + SiH4', 'SiF4 + H2', 'Выбор темы'],
    ['H2SiO3', 'SiO + H2', 'Si + H2O', 'SiO2 + H2O', 'Выбор темы'],
    ['H2S + S + CO2', 'H2 + SO2 + CO2', 'CO2 + S + H2O', 'SO2 + CO2 + H2O', 'Выбор темы'],
    ['Na2Cr2O7 + CrCl2 + H2O', 'NaClO + CrCl2 + H2O', 'NaCl + Na2Cr2O7 + H2O', 'NaCl +Na2CrO4 + H2O', 'Выбор темы'],
    ['KClO3 + H2 + K2CO3', 'K2CO3  + Cl2O5 + H2O', 'H2O + K2CO3  + KClO3', 'K2CO3 + KCl + H2O', 'Выбор темы'],
    ['CH4 + H2O', 'CH4 + H2O2', 'H2O2 + CO2', 'CO2 + H2O', 'Выбор темы'],
    ['CO2 + SiC', 'Si + CO', 'CO2 + Si', 'CO + SiC', 'Выбор темы'],
    ['SO2  + HBr + KOH', 'HBr + SO2 + K2SO4', 'K2SO4 + HBr + KOH', 'K2SO4 + HBr', 'Выбор темы'],
    ['KClO3 + CO2', 'CO2 + CO + KClO3', 'KCl + KClO3 + CO2', 'H2O2 +  CO + KClO3', 'Выбор темы'],
    ['Al2O3  + SO2', 'Al2O3 + SO3', 'SO2 + Al', 'Al + SO3', 'Выбор темы'],
    ['K2SO4 + HCl + SO2', 'K2SO4 + S + HClO3', 'K2SO4 + SO2 + HClO3', 'K2SO4 + HCl', 'Выбор темы']
]
M = [
    ['Al2(SO4)3 + H2', 'Al2(SO4)3 + H2O + S', 'Al2(SO4)3 + H2O + SO2', 'Al2(SO4)3 + H2O', 'Выбор темы'],
    ['NaAlO2 + H2 + Al(OH)3', 'Na[Al(OH)4] + H2 ', 'Na[Al(OH)4] + NaAlO2 + H2', 'Na[Al(OH)4] + Al(OH)3 + H2', 'Выбор темы'],
    ['ZnSO4 + Cu + O2', 'ZnS  + CuO + O2', 'ZnSO4 + Cu ', 'ZnS  + CuO', 'Выбор темы'],
    ['Cu(NO3)2 + H2', 'Cu(NO3)2 + NH4NO3 + H2O', 'Cu(NO3)2 + NO2+ H2', 'Cu(NO3)2 + NO2 + H2O', 'Выбор темы'],
    ['AlBr3', 'не идет', 'Al7Br3', 'AlBr2', 'Выбор темы'],
    ['K2O', 'K2O2', 'KO3', 'KO2', 'Выбор темы'],
    ['MgH2 + Br2', 'MgH2 + Br2 + H2', 'MgBr2 + MgH2 + Br2', 'MgBr2 + H2', 'Выбор темы'],
    ['Zn3P2 + H2O', 'Zn3(PO4)2 + H2', 'Zn3(PO4)2 + H2O', 'Zn3(PO4)2 + Zn3P2 + H2', 'Выбор темы'],
    ['SnHS + S', 'SnS2 + H2 + S', 'SnS2 + S', 'SnS2 + H2', 'Выбор темы'],
    ['Al2O3 + Mn2O7', 'Mn2O7 + Al2O3 + O2', 'Mn + Al2O3', 'Mn + Al2O3 + O2', 'Выбор темы'],
    ['AgNO3 + NO + H2O', 'AgNO3 + H2O', 'AgNO3 + H2', 'AgNO3 + H2O + NO2', 'Выбор темы'],
    ['Li2O', 'не идет', 'LiO2', 'Li2O2', 'Выбор темы'],
    ['ZnO + Li2[Zn(OH)4', 'Li2ZnO2+ H2', 'Zn(OH)2 + Li2ZnO2', 'Li2[Zn(OH)4 + H2', 'Выбор темы'],
    ['FeSO4 + H2O + SO2', 'FeSO4 + H2O', 'FeSO4 + H2', 'Fe2(SO4)3 +SO2 + H2O', 'Выбор темы'],
    ['Fe2(SO4)3 +H2O + SO2', 'FeSO4+ H2', 'Fe2(SO4)3 + H2', 'FeSO4 + H2O + SO2', 'Выбор темы'],
    ['Fe2O3', 'Fe3O4', 'не идет', 'FeO', 'Выбор темы'],
    ['Al2S3 + CuO', 'Al2(SO4)3 + CuS', 'Al2(SO4)3 + Cu', 'Al2(SO4)3 + CuO', 'Выбор темы'],
    ['Al2O3 +KIO3', 'Al2O3 +KIO3 + I2', 'KAlO2 + I2', 'KI + Al2O3', 'Выбор темы'],
    ['Co(NO3)2 + NO + H2O', 'Co(NO3)2 + NO2 + H2O', 'Co(NO3)2 + H2', 'Co(NO3)2 + NO2 + H2O', 'Выбор темы'],
    ['Ca(NO3)2 + H2', 'Ca3N2 + H2O', 'Ca(NO3)2 + H2O + NO', 'Ca(NO2)2 + H2', 'Выбор темы'],
    ['Al2O3 + H2O2', 'Al2O3 + H2', 'Al(OH)3 + H2O2', 'Al(OH)3 + H2', 'Выбор темы'],
    ['Fe(OH)3 + H2', 'Fe(OH)3', 'FeO +  H2', 'Fe3O4 + H2', 'Выбор темы'],
    ['H2  + K2O', 'KOH', 'K2O + KOH', 'KOH + H2', 'Выбор темы'],
    ['Pb(OH)2', 'PbO + H2', 'H2 + PbO2', 'Pb(OH)2 + H2', 'Выбор темы'],
    ['Fe(OH)2', 'FeO + Fe(OH)2', 'Fe2O3 + Fe(OH)2', 'Fe(OH)3', 'Выбор темы'],
    ['Cu2Cl', 'CuCl + Cl2', 'Cu2Cl+ Cl2', 'CuCl', 'Выбор темы'],
    ['FeCl4', 'FeCl + Cl2', 'FeCl2', 'FeCl2 + Cl2', 'Выбор темы'],
    ['CuCl + FeCl3', 'CuCl2 + Fe', 'CuCl + Fe', 'FeCl2 + CuCl2', 'Выбор темы'],
    ['FeI2', 'FeI3', 'FeI2 + FeI3', 'не идет', 'Выбор темы'],
    ['CuI', 'CuI2 + CuI', 'CuI2', 'не идет', 'Выбор темы'],
    ['Cr(NO3)3 + NO2 + H2O', 'Cr(NO3)3 + NH4NO3 + H2', 'Cr(NO3)3 + H2', 'Cr(NO3)2 + NO2 + H2O', 'Выбор темы'],
    ['Na2O', 'NaO2', 'не идет', 'Na2O2', 'Выбор темы'],
    ['Na3N + NH4NO3 + H2O', 'NaNO3 + NO2 + H2O', 'NaNO3 + NH4NO3 + H2O', 'NaNO3 + H2', 'Выбор темы'],
    ['FeS', 'FeS + Fe2S3', 'не идет', 'Fe2S3', 'Выбор темы'],
    ['Be(OH)2 + Na2O', 'BeO + Na2O + H2', 'Na + Be(OH)2', 'Na2BeO2 + H2', 'Выбор темы'],
    ['Fe(NO3)2 + FeO', 'NO2 + FeO', 'Fe(NO3)2', 'Fe(NO3)2 + NO2', 'Выбор темы'],
    ['Al2O3 +Fe2O3', 'Al2(FeO2)3', 'Fe2O3 + Al2(FeO2)3', 'Fe + Al2O3', 'Выбор темы'],
    ['Fe(OH)3', 'Fe(OH)3 + H2O2', 'FeO + H2O2', 'FeO + Fe(OH)3', 'Выбор темы'],
    ['Fe2O3 + SO2', 'Fe2O3 +  SO3', 'FeO + S', 'FeO + SO2', 'Выбор темы'],
    ['MgCO3', 'MgO + CO', 'MgO + C', 'MgCO3 +  CO', 'Выбор темы'],
    ['Mg3N2 + KOH', 'KOH + Mg(OH)2 + H2', 'N2+ KOH + Mg(OH)2', 'KOH + Mg(OH)2 + NH3', 'Выбор темы'],
    ['BaS + CO2', 'BaCO3 + S', 'BaCO3+ SO2', 'BaS + CO', 'Выбор темы'],
    ['BaS + H2O', 'BaS + S + H2O', 'BaS + H2O + SO2', 'BaS + + H2O2', 'Выбор темы'],
    ['Al2(SO4)3 + SO2 + H2O', 'Al2(SO4)3 + H2', 'Al2O3+ SO2 + H2O', 'Al2(SO4)3 + S + H2O', 'Выбор темы'],
    ['Al(NO3)3 + NH4NO3 + H2O', 'Al(NO3)3 + NO + H2O', 'Al(NO3)3 + NO2 + H2O', 'Al(NO3)3 + H2', 'Выбор темы'],
    ['Al(OH)3 + NaNO3 + H2', 'Na[Al(OH)4] + H2 + NaNO3', 'Na[Al(OH)4] + H2 + N2', 'Na[Al(OH)4] + NH3', 'Выбор темы'],
    ['K2MnO4+ Al2O3 + H2', 'K[Al(OH)4] + MnO2 + + H2', 'K[Al(OH)4] + MnO2', 'K2MnO4 + K[Al(OH)4]', 'Выбор темы'],
    ['N2O + Cu2O', 'CuO + N2', 'N2 + Cu2O', 'CuO + N2O', 'Выбор темы'],
    ['ZnO + N2 + Zn(NO3)2', 'ZnO + N2', 'Zn(NO3)2', 'NO + ZnO', 'Выбор темы'],
    ['Mg(OH)2 + SO2 + K2SO4', 'K2SO4 + MgSO4 + H2', 'Mg(OH)2 + K2SO4', 'Mg(HSO4)2 + K2SO4', 'Выбор темы']
]
p = ['NaCl + I2', 'FeCl2 + H2', 'CO', 'NO2 + H3PO4 + H2O', 'H2O + Cu', 'Fe + CO', 'SO2 + H2O', 'H2O', 'Na2SiO3 + H2', 'NaClO + H2O + NaCl', 'FeCl3', 'PCl5', 'CO2+ NO2 + H2O', 'KCl + Br2', 'K2S +K2SO3 + H2O', 'CO + H2', 'HF + O2', 'KH2PO2 + PH3', 'FeCl3', 'Na2SO4', 'CuO + SO2', 'CaSiO3  + CO + P', 'NO + H3PO4', 'H2O + SO2 + H3PO4', 'N2 + H2O', 'H2O + N2', 'SO2 + N2', 'KCl + P2O5', 'CO2  + KBr', 'HIO3 + H2O', 'HIO3 + HCl', 'KNO3 + HBr', 'HIO3 + NO2 + H2O', 'H2SO4 + NO2 + H2O', 'HNO3', 'N2 + H2O', 'KClO3 + KCl + H2', 'СаС2 + СО', 'Cu + CO', 'COCl2', 'SiF4 + H2', 'SiO2 + H2O', 'SO2 + CO2 + H2O', 'NaCl +Na2CrO4 + H2O', 'K2CO3 + KCl + H2O', 'CH4 + H2O', 'Si + CO', 'K2SO4 + HBr', 'KCl + KClO3 + CO2', 'Al2O3 + SO3', 'K2SO4 + HCl']
p1 = ['Al2(SO4)3 + H2', 'Na[Al(OH)4] + H2', 'ZnSO4 + Cu', 'Cu(NO3)2 + NO2 + H2O', 'AlBr3', 'KO2', 'MgBr2 + H2', 'Zn3(PO4)2 + H2', 'SnS2 + H2', 'Mn + Al2O3', 'AgNO3 + H2', 'Li2O', 'Li2[Zn(OH)4 + H2', 'FeSO4 + H2', 'Fe2(SO4)3 +H2O + SO2', 'Fe3O4', 'Al2(SO4)3 + Cu', 'KI + Al2O3', 'Co(NO3)2 + NO2 + H2O', 'Ca(NO2)2 + H2', 'Al(OH)3 + H2', 'Fe3O4 + H2', 'KOH + H2', 'PbO + H2', 'Fe(OH)3', 'CuCl', 'FeCl2', 'FeCl2 + CuCl2', 'FeI2', 'CuI', 'Cr(NO3)3 + NO2 + H2O', 'Na2O2', 'NaNO3 + NH4NO3 + H2O', 'FeS', 'Na2BeO2 + H2', 'Fe(NO3)2', 'Fe + Al2O3', 'Fe(OH)3', 'Fe2O3 + SO2', 'MgO + C', 'KOH + Mg(OH)2 + NH3', 'BaS + CO', 'BaS + H2O', 'Al2(SO4)3 + SO2 + H2O', 'Al(NO3)3 + NO2 + H2O', 'Na[Al(OH)4] + NH3', 'K2MnO4 + K[Al(OH)4]', 'CuO + N2', 'ZnO + N2', 'K2SO4 + MgSO4 + H2']
select_topic = [["Химические свойства металлов", "Химические свойства НЕметаллов"]]
counter = 0
bul = None


def get_keys(list_keys):
    global counter
    kb = VkKeyboard(one_time=True)
    for i in range(len(list_keys[counter]) - 1):
        kb.add_button(label=list_keys[counter][i], color="positive")
        kb.add_line()

    else:
        kb.add_button(label=list_keys[counter][len(list_keys[counter]) - 1], color="negative")
    kb = kb.get_keyboard()
    counter += 1
    return kb


def sender(user_id, text, rand, ls=None):
    global counter
    vk.messages.send(  # Отправляем сообщение
        user_id=user_id,
        message=text,
        random_id=rand,
        keyboard=get_keys(ls),
        attachment=sender_photo(counter)
        )


def sender_photo(c):
    global bul, text_client, end
    if text_client == 'старт' or text_client == 'привет' or text_client == 'хочу' or text_client == 'да' or text_client == 'выбор темы' or end == 1:
        pass

    elif bul is True:
        a = vk_session.method("photos.getMessagesUploadServer")
        b = requests.post(a['upload_url'], files={'photo': open(str(c - 1) + '_m.jpg', 'rb')}).json()
        c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'],
                                                           'hash': b['hash']})[0]
        d = "photo{}_{}".format(c["owner_id"], c["id"])
        return d
    elif bul is False:
        a = vk_session.method("photos.getMessagesUploadServer")
        b = requests.post(a['upload_url'], files={'photo': open(str(c - 1) + '_nm.jpg', 'rb')}).json()
        c = vk_session.method('photos.saveMessagesPhoto', {'photo': b['photo'], 'server': b['server'],
                                                           'hash': b['hash']})[0]
        d = "photo{}_{}".format(c["owner_id"], c["id"])
        return d


def get_keys_adv():
    kb = VkKeyboard(one_time=True)
    kb.add_button(label='Далее', color="positive")
    kb.add_line()
    kb.add_button(label='Выбор темы', color="negative")
    kb = kb.get_keyboard()
    return kb


def sender_adv(user_id, rand):
    global fail
    word = 'Ого, ты уже допустил несколько ошибок и потерял заветные баллы для поступления на бюджет... 😢 Но это поправимо! \n\n Мы подготовили для тебя готовый курс подготовки к ЕГЭ по химии 🔥 Учитель — Антон Асламов, который сам сдал ЕГЭ по химии на 100 баллов ( и ты сможешь!). \n\nУспей пройти курс, часики-то тикают: https://vk.cc/c1s0px \n\nПодарочек: специальная ссылка, которая дает 30% на готовый курс 😱 \n\n ✅2030 руб. за готовый курс \n ❌Вместо 2 900 \n \n 😎 Забрать скидку: https://vk.cc/c1s0px'
    vk.messages.send(
        user_id=user_id,
        message=word,
        random_id=rand,
        keyboard=get_keys_adv(),
    )
    fail = 0


end = 0
fail = 0

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        k += 531514545
        text_client_2 = event.text
        text_client = str(event.text).lower()

        if counter <= len(M)-1:
            if fail >= 2:
                sender_adv(event.user_id, k)

            elif text_client == 'старт' or text_client == 'привет' or text_client == 'хочу' or text_client == 'да':
                counter = 0
                sender(event.user_id, "Выбери тему, которую хочешь прокачать", k, select_topic)
                counter = 0

            elif text_client == 'выбор темы':
                counter = 0
                sender(event.user_id, "Выбери тему, которую хочешь прокачать", k, select_topic)
                counter = 0

            elif text_client == 'химические свойства металлов':
                bul = True
                sender(event.user_id, 'Выбери правильный ответ', k, M)

            elif text_client == 'химические свойства неметаллов':
                bul = False
                sender(event.user_id, 'Выбери правильный ответ', k, n_M)

            elif bul is True:
                if text_client_2 in p1:
                    sender(event.user_id, "Круто! Вы правильно решили предыдущее задание", k, M)
                else:
                    sender(event.user_id, "К сожалению, предыдущее задание Вы решили неправильно, попробуйте еще раз", k, M)
                    fail += 1
                    print(fail)

            elif bul is False:
                if text_client_2 in p:
                    sender(event.user_id, "Круто! Вы правильно решили предыдущее задание", k, n_M)
                else:
                    sender(event.user_id, "К сожалению, предыдущее задание Вы решили неправильно, попробуйте еще раз", k, n_M)
                    fail += 1
                    print(fail)

            elif text_client == 'далее' and bul is True:
                sender(event.user_id, 'Выбери правильный ответ', k, M)

            elif text_client == 'далее' and bul is False:
                sender(event.user_id, 'Выбери правильный ответ', k, n_M)

        elif bul is True:
            if text_client_2 in p1:
                counter = 0
                end = 1
                sender(event.user_id, "Круто! Вы правильно решили предыдущее задание\n\nНа сегодня Вы прорешали все задания в этой теме, прокачайте и другую тему\n\nВыбери тему, которую хочешь прокачать", k, select_topic)
                end = 0
                counter = 0
            else:
                counter = 0
                end = 1
                sender(event.user_id, "К сожалению, предыдущее задание Вы решили неправильно\n\nНа сегодня Вы прорешали все задания в этой теме, прокачайте и другую тему\n\nВыбери тему, которую хочешь прокачать", k, select_topic)
                fail += 1
                end = 0
                counter = 0
        elif bul is False:
            if text_client_2 in p1:
                counter = 0
                end = 1
                sender(event.user_id, "Круто! Вы правильно решили предыдущее задание\n\nНа сегодня Вы прорешали все задания в этой теме, прокачайте и другую тему\n\nВыбери тему, которую хочешь прокачать", k, select_topic)
                end = 0
                counter = 0
            else:
                counter = 0
                end = 1
                sender(event.user_id, "К сожалению, предыдущее задание Вы решили неправильно\n\nНа сегодня Вы прорешали все задания в этой теме, прокачайте и другую тему\n\nВыбери тему, которую хочешь прокачать", k, select_topic)
                fail += 1
                end = 0
                counter = 0