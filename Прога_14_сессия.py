import pandas as pd

#Внимание-внимание!!!
#Для этой программы необходимы нуклеотидные последовательности (только они, одна строка, без дополнительных пояснений)
#Предполагается, что они идут в формате TXT!!!
#Будьте внимательны и аккуратны!
#При желании перые строчки кода о добавлении определенным образом определенного формата можно редактировать
#Считаем, что файлы находятся в рабочем каталоге, проверяем это через os.getcwd()
#Если находится не в рабочем каталоге, меняем рабочий каталог на нужный с помощью os.chdir(path)

first_chromo = pd.read_txt("Здесь был ваш файл с 1 хромосомой")
second_chromo = pd.read_txt("Здесь был ваш файл со 2 хромосомой")
third_chromo = pd.read_txt("Здесь был ваш файл с 3 хромосомой")
four_chromo = pd.read_txt("Здесь был ваш файл с 4 хромосомой")
five_chromo = pd.read_txt("Здесь был ваш файл с 5 хромосомой")
six_chromo = pd.read_txt("Здесь был ваш файл с 6 хромосомой")
seven_chromo = pd.read_txt("Здесь был ваш файл с 7 хромосомой")
eight_chromo = pd.read_txt("Здесь был ваш файл с 8 хромосомой")
nine_chromo = pd.read_txt("Здесь был ваш файл с 9 хромосомой")
ten_chromo = pd.read_txt("Здесь был ваш файл с 10 хромосомой")
elevn_chromo = pd.read_txt("Здесь был ваш файл с 11 хромосомой")
twelve_chromo = pd.read_txt("Здесь был ваш файл с 12 хромосомой")
thirteen_chromo = pd.read_txt("Здесь был ваш файл с 13 хромосомой")
fourteen_chromo = pd.read_txt("Здесь был ваш файл с 14 хромосомой")
fifteen_chromo = pd.read_txt("Здесь был ваш файл с 15 хромосомой")
sixteen_chromo = pd.read_txt("Здесь был ваш файл с 16 хромосомой")
seventeen_chromo = pd.read_txt("Здесь был ваш файл с 17 хромосомой")
eighteen_chromo = pd.read_txt("Здесь был ваш файл с 18 хромосомой")
nineteen_chromo = pd.read_txt("Здесь был ваш файл с 19 хромосомой")
twenty_chromo = pd.read_txt("Здесь был ваш файл с 20 хромосомой")
twenty_one_chromo = pd.read_txt("Здесь был ваш файл с 21 хромосомой")
twenty_two_chromo = pd.read_txt("Здесь был ваш файл с 22 хромосомой")
X_chromo = pd.read_txt("Здесь был ваш файл с Х хромосомой")
Y_chromo = pd.read_txt("Здесь был ваш файл с Y хромосомой")

firstg = first_chromo.count("GGAAT") #ставим отдельные переменные для количества пентамеров
secondg = second_chromo.count("GGAAT")
thirdg = third_chromo.count("GGAAT")
fourg = four_chromo.count("GGAAT")
fiveg = five_chromo.count("GGAAT")
sixg = six_chromo.count("GGAAT")
seveng = seven_chromo.count("GGAAT")
eightg = eight_chromo.count("GGAAT")
nineg = nine_chromo.count("GGAAT")
teng = ten_chromo.count("GGAAT")
elevng = elevn_chromo.count("GGAAT")
twelveg = twelve_chromo.count("GGAAT")
thirteeng = thirteen_chromo.count("GGAAT")
fourteeng =  fourteen_chromo.count("GGAAT")
fifteeng = fifteen_chromo.count("GGAAT")
sixteeng = sixteen_chromo.count("GGAAT")
seventeeng = seventeen_chromo.count("GGAAT")
eighteeng = eighteen_chromo.count("GGAAT")
nineteeng = nineteen_chromo.count("GGAAT")
twentyg = twenty_chromo.count("GGAAT")
twentyg_one = twenty_one_chromo.count("GGAAT")
twentyg_two = twenty_two_chromo.count("GGAAT")
X_chromog = X_chromo.count("GGAAT")
Y_chromog = Y_chromo.count("GGAAT")


firsta = first_chromo.count("ATTTC")
seconda = second_chromo.count("ATTTC")
thirda = third_chromo.count("ATTTC")
foura = four_chromo.count("ATTTC")
fivea = five_chromo.count("ATTTC")
sixa = six_chromo.count("ATTTC")
sevena = seven_chromo.count("ATTTC")
eighta = eight_chromo.count("ATTTC")
ninea = nine_chromo.count("ATTTC")
tena = ten_chromo.count("ATTTC")
elevna = elevn_chromo.count("ATTTC")
twelvea = twelve_chromo.count("ATTTC")
thirteena = thirteen_chromo.count("ATTTC")
fourteena =  fourteen_chromo.count("ATTTC")
fifteena = fifteen_chromo.count("ATTTC")
sixteena = sixteen_chromo.count("ATTTC")
seventeena = seventeen_chromo.count("ATTTC")
eighteena = eighteen_chromo.count("ATTTC")
nineteena = nineteen_chromo.count("ATTTC")
twentya = twenty_chromo.count("ATTTC")
twentya_one = twenty_one_chromo.count("ATTTC")
twentya_two = twenty_two_chromo.count("ATTTC")
X_chromoa = X_chromo.count("ATTTC")
Y_chromoa = Y_chromo.count("ATTTC")

data = [[firstg, firsta],
         [secondg, seconda],
         [thirdg, thirda],
         [fourg, foura],
         [fiveg, fivea],
         [sixg, sixa],
         [seveng, sevena],
         [eightg, eighta],
         [nineg, ninea],
         [teng, tena],
         [elevng, elevna],
         [twelveg, twelvea],
         [thirteeng, thirteena],
         [fourteeng, fourteena],
         [fifteeng, fifteena],
         [sixteeng, sixteena],
         [seventeeng, seventeena],
         [eighteeng, eighteena],
         [nineteeng, nineteena],
         [twentyg, twentya],
         [twentyg_one, twentya_one],
         [twentyg_two, twentya_two],
         [X_chromog, X_chromoa],
         [Y_chromog, Y_chromoa]]
        
columns = ["GGAAT", "ATTTC"] # определяем названия столбцов
rows = ['1ch', '2ch', '3ch', '4ch', '5ch', '6ch', '7ch', '8ch', '9ch',  '10ch', '11ch', '12ch', '13ch', '14ch', '15ch', '16ch', '17ch', '18ch', '19ch', '20ch', '21ch', '22ch', 'Xch', 'Ych'] # определяем названия строк

df = pd.DataFrame(data, columns=columns, index=rows)

df.to_csv("Пентамеры в GRCh38.tsv", sep="\t")




























