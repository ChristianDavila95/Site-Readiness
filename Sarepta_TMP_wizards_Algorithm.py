import pandas as pd
databeta = pd.read_csv(r' ', sep=" ", header=None)
databeta.columns = ["Patient","Anti-AAVrh74", "Elispot Ganma-IFN", "Distance in Km"]
needle1 = databeta["Anti-AAVrh74"].tolist()
needle2 = databeta["Elispot Ganma-IFN"].tolist()
needle3 = databeta["Distance in Km"].tolist()
needle4 = databeta["Patient"].tolist()
needlex = str(needle1).strip('[]')
needley = str(needle2).strip('[]')
needlez = str(needle3).strip('[]')
def convert(string):
    converted = list(string.split(", "))
    return converted
needlexx = convert(needlex)
needleyy = convert(needley)
needlezz = convert(needlez)
def lista1(li1):
  return list(map(lambda el:[el], li1))
needle_prime1 = lista1(needlexx)
needle_prime2 = lista1(needleyy)
needle_prime3 = lista1(needlezz)
def drange1(start1, stop1, step1):
  r = start1
  while r < stop1:
    yield r
    r += step1
ia=drange1(1.00,2.01,0.01)
haystack1 = ["%g" % x for x in ia]
result1 = []
iA = 0
def amount_to_advance1():
  return 1
for needle1a in needle_prime1:
 while iA <= len(haystack1) - len(needle1a):
  for iA in range(len(haystack1) - len(needle1a) + 1):
   for jA in range(len(needle1a)):
    if needle1a[jA] != haystack1 [iA + jA]:
      z1 = False
    else:
      z1 = True
      result1.append(iA)
      iA += amount_to_advance1()
  break 
haystackA = ' '.join([str(elem) for elem in haystack1]) 
value1 = []
import re
for needle in needlexx: 
  if re.search(needle, haystackA):
    z1 = 1
    value1.append(z1)
  else:
    z2 = 0
    value1.append(z2)
result1A = []
for h1 in result1:
  result1A += [h1 + 1]
def drange2(start2, stop2, step2):
  r = start2
  while r < stop2:
    yield r
    r += step2
ib=drange2(10.0,50.1,0.1)
haystack2 = ["%g" % x for x in ib]
result2 = []
iB = 0
def amount_to_advance2():
  return 1
for needle2a in needle_prime2:
 while iB <= len(haystack2) - len(needle2a):
  for iB in range(len(haystack2) - len(needle2a) + 1):
   for jB in range(len(needle2a)):
    if needle2a[jB] != haystack2 [iB + jB]:
      z2 = False
    else:
      z2 = True
      result2.append(iB)
      iB += amount_to_advance2()
  break 
haystackB = ' '.join([str(elem) for elem in haystack2]) 
value2 = []
import re
for needle in needleyy: 
  if re.search(needle, haystackB):
    z1 = 1
    value2.append(z1)
  else:
    z2 = 0
    value2.append(z2)
result2A = []
for h2 in result2:
  result2A += [h2 + 1]
def drange3(start3, stop3, step3):
  r = start3
  while r < stop3:
    yield r
    r += step3
ic=drange3(1.0,100.1,0.1)
haystack3 = ["%g" % x for x in ic]
result3 = []
iC = 0
def amount_to_advance3():
  return 1
for needle3a in needle_prime3:
 while iC <= len(haystack3) - len(needle3a):
  for iC in range(len(haystack3) - len(needle3a) + 1):
   for jC in range(len(needle3a)):
    if needle3a[jC] != haystack3 [iC + jC]:
      z3a = False
    else:
      z3b = True
      result3.append(iC)
      iC += amount_to_advance3()
  break
haystackC = ' '.join([str(elem) for elem in haystack3]) 
value3 = []
import re
for needle in needlezz: 
  if re.search(needle, haystackC):
    z1 = 1
    value3.append(z1)
  else:
    z2 = 0
    value3.append(z2)
result3A = []
for h3 in result3:
  result3A += [h3 + 1]
import pandas as pd
dff = pd.DataFrame(list(zip(value1,value2,value3)),
columns =['Antibody', 'Blood Titer', 'Distance'])
dff.columns = ['Antibody', 'Blood titer', 'Distance']
antibody = dff["Antibody"].tolist()
resultalpha = iter(result1A)
alpha = [next(resultalpha) if val == 1 else val for val in antibody] 
blood = dff["Blood titer"].tolist()
resultbeta = iter(result2A)
beta = [next(resultbeta) if val == 1 else val for val in blood] 
distance = dff["Distance"].tolist()
resultteta = iter(result3A)
teta = [next(resultteta) if val == 1 else val for val in distance] 
dfinal = pd.DataFrame(list(zip(alpha,beta,teta)), 
columns =['Antibody', 'Blood Titer', 'Distance'])
list1 = []
list2 = []
list3 = []
for item1 in alpha:
  if 1<= item1 <= 10:
    list1.append(10)
  elif 11 <= item1 <= 20:
    list1.append(9)
  elif 21 <= item1 <= 30:
    list1.append(8)
  elif 31 <= item1 <= 40:
    list1.append(7)
  elif 41 <= item1 <= 50:
    list1.append(6)
  elif 51 <= item1 <= 60:
    list1.append(5)
  elif 61 <= item1 <= 70:
    list1.append(4)
  elif 71 <= item1 <= 80:
    list1.append(3)
  elif 81 <= item1 <= 90:
    list1.append(2)
  elif 91 <= item1 <= 100:
    list1.append(1)
  elif item1 == 0:
    list1.append(0)
for item2 in beta: 
  if 1 <= item2 <= 10:
    list2.append(40)
  elif 11 <= item2 <= 20:
    list2.append(39)
  elif 21 <= item2 <= 30:
    list2.append(38)
  elif 31 <= item2 <= 40:
    list2.append(37)
  elif 41 <= item2 <= 50:
    list2.append(36)
  elif 51 <= item2 <= 60:
    list2.append(35)
  elif 61 <= item2 <= 70:
    list2.append(34)
  elif 71 <= item2 <= 80:
    list2.append(33)
  elif 81 <= item2 <= 90:
    list2.append(32)
  elif 91 <= item2 <= 100:
    list2.append(31)
  elif 101 <= item2 <= 110:
    list2.append(30)
  elif 111 <= item2 <= 120:
    list2.append(29)
  elif 121 <= item2 <= 130:
    list2.append(28)
  elif 131 <= item2 <= 140:
    list2.append(27)
  elif 141 <= item2 <= 150:
    list2.append(26)
  elif 151 <= item2 <= 160:
    list2.append(25)
  elif 161 <= item2 <= 170:
    list2.append(24)
  elif 171 <= item2 <= 180:
    list2.append(23)
  elif 181 <= item2 <= 190:
    list2.append(22)
  elif 191 <= item2 <= 200:
    list2.append(21)
  elif 201 <= item2 <= 210:
    list2.append(20)
  elif 211 <= item2 <= 220:
    list2.append(19)
  elif 221 <= item2 <= 230:
    list2.append(18)
  elif 231 <= item2 <= 240:
    list2.append(17)
  elif 241 <= item2 <= 250:
    list2.append(16)
  elif 251 <= item2 <= 260:
    list2.append(15)
  elif 261 <= item2 <= 270:
    list2.append(14)
  elif 271 <= item2 <= 280:
    list2.append(13)
  elif 281 <= item2 <= 290:
    list2.append(12)
  elif 291 <= item2 <= 300:
    list2.append(11)
  elif 301 <= item2 <= 310:
    list2.append(10)
  elif 311 <= item2 <= 320:
    list2.append(9)
  elif 321 <= item2 <= 330:
    list2.append(8)
  elif 331 <= item2 <= 340:
    list2.append(7)
  elif 341 <= item2 <= 350:
    list2.append(6)
  elif 351 <= item2 <= 360:
    list2.append(5)
  elif 361 <= item2 <= 370:
    list2.append(4)
  elif 371 <= item2 <= 380:
    list2.append(3)
  elif 381 <= item2 <= 390:
    list2.append(2)
  elif 391 <= item2 <= 400:
    list2.append(1)
  elif item2 ==0:
    list2.append(0)
for item3 in teta: 
  if 1 <= item3 <= 50:
    list3.append(3)
  elif 51 <= item3 <= 100:
    list3.append(2.9)
  elif 101 <= item3 <= 150:
    list3.append(2.8)
  elif 151 <= item3 <= 200:
    list3.append(2.7)
  elif 201 <= item3 <= 250:
    list3.append(2.6)
  elif 251 <= item3 <= 300:
    list3.append(2.5)
  elif 301 <= item3 <= 350:
    list3.append(2.4)
  elif 351 <= item3 <= 400:
    list3.append(2.3)
  elif 401 <= item3 <= 450:
    list3.append(2.1)
  elif 451 <= item3 <= 500:
    list3.append(2)
  elif 501 <= item3 <= 550:
    list3.append(1.9)
  elif 551 <= item3 <= 600:
    list3.append(1.8)
  elif 601 <= item3 <= 650:
    list3.append(1.7)
  elif 651 <= item3 <= 700:
    list3.append(1.6)
  elif 701 <= item3 <= 750:
    list3.append(1.5)
  elif 751 <= item3 <= 800:
    list3.append(1.4)
  elif 801 <= item3 <= 850:
    list3.append(1.3)
  elif 851 <= item3 <= 900:
    list3.append(1.2) 
  elif 901 <= item3 <= 950:
    list3.append(1.1)
  elif 951 <= item3 <= 990:
    list3.append(1)    
  elif item3 ==0:
    list3.append(0)
dflist1 = pd.DataFrame(list1)
dflist2 = pd.DataFrame(list2)
dflist3 = pd.DataFrame(list3)
scorelist = dflist1 + dflist2 + dflist3
scorelist.columns = ['score']
score = scorelist["score"].tolist()
lfinal = pd.DataFrame(list(zip(needle4,list1,list2,list3,score)),
columns =['Patient','Anti-AAVrh74', 'Elispot Ganma-IFN', 'Distance in Km','Score'])
aa = lfinal.sort_values(by=['Score'], ascending=False)
print(databeta)
print(lfinal)
print(aa)