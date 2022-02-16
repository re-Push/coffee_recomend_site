# 미리 뽑아놓은 커피리스트와 사용자가 정한 커피리스트의 각 항목 별 차이의 절댓값의 합산이 가장적은 결과값 도출하기

# 리스트 coffee bean = [body,acidity,sweet,flavor,bitter]
lobster_uganda = [4, 2, 3, 3, 4]
brazil_cerrado = [4, 2, 3, 4, 3]
brazil_kenya = [4, 2, 3, 4, 3]
ethiopia_sidamo = [4, 5, 2, 4, 1]
colombia_supremo = [4, 2, 3, 4, 2]
guatemala = [5, 3, 5, 4, 3]
ethiopia_yirgacheffe = [4, 5, 3, 4, 3]
kenya_AA = [4, 5, 3, 4, 3]
indonesia_java = [4, 2, 3, 4, 2]
indonesia_mandeling = [4, 2, 3, 4, 2]
indonesia_bali_kantamani = [3, 2, 3, 4, 2]
indonesia_go_mountain = [3, 4, 3, 4, 2]
indonesia__toraja = [4, 5, 3, 4, 2]
india_monsund_maliva = [4, 4, 4, 5, 3]
colombia_excelso = [3, 5, 3, 5, 2]
guatemala_SHB = [3, 4, 3, 5, 3]
nicaragua_SHB = [3, 4, 3, 3, 3]
mexico_altura_SHB = [2, 3, 3, 4, 2]
elsalvador_pensi_SHB = [2, 3, 3, 4, 2]
costa_rica_SHB = [2, 3, 4, 3, 3]
panama_SHB = [3, 4, 3, 5, 4]
Dominica_AA = [1, 4, 3, 2, 2]
brazil_santos = [2, 3, 3, 4, 2]
brazil_santos_decaffeinated = [2, 3, 3, 4, 2]
honduras_SHG = [3, 4, 2, 3, 2]
peru_HB_GRADE1 = [4, 4, 4, 5, 3]
ethiopia_yirgachev = [4, 5, 3, 4, 3]
mocha_sidamo = [4, 5, 3, 4, 3]
rwanda_AB_plus = [4, 3, 3, 2, 3]
malawi_AAA_plus = [4, 3, 3, 5, 4]
zimbabwe_AA_plus = [4, 5, 3, 4, 3]
tanzania_AA_plus = [4, 5, 3, 4, 3]

# 결과값 리스트
list_beans = [lobster_uganda, brazil_cerrado, brazil_kenya, ethiopia_sidamo, colombia_supremo, guatemala,
              ethiopia_yirgacheffe, kenya_AA, indonesia_java, indonesia_mandeling, indonesia_bali_kantamani,
              indonesia_go_mountain, indonesia__toraja, india_monsund_maliva, colombia_excelso, guatemala_SHB,
              nicaragua_SHB, mexico_altura_SHB, elsalvador_pensi_SHB, costa_rica_SHB, panama_SHB, Dominica_AA,
              brazil_santos, brazil_santos_decaffeinated, honduras_SHG, peru_HB_GRADE1, ethiopia_yirgachev,
              mocha_sidamo, rwanda_AB_plus, malawi_AAA_plus, zimbabwe_AA_plus, tanzania_AA_plus]
print(list_beans)

list_beans_name = ["lobster_uganda", "brazil_cerrado", "brazil_kenya", "ethiopia_sidamo", "colombia_supremo",
                   "guatemala", "ethiopia_yirgacheffe", "kenya_AA", "indonesia_java", "indonesia_mandeling",
                   "indonesia_bali_kantamani", " indonesia_go_mountain", "indonesia__toraja", "india_monsund_maliva",
                   "colombia_excelso", "guatemala_SHB", "nicaragua_SHB", "mexico_altura_SHB", "elsalvador_pensi_SHB",
                   "costa_rica_SHB", "panama_SHB", "Dominica_AA", "brazil_santos", "brazil_santos_decaffeinated",
                   "honduras_SHG", "peru_HB_GRADE1", "ethiopia_yirgachev", "mocha_sidamo", "rwanda_AB_plus",
                   "malawi_AAA_plus", "zimbabwe_AA_plus", "tanzania_AA_plus"]

# 사용자가 선택한 결과
body = 5
acidity = 4
sweet = 3
flavor = 4
bitter = 3

# 첫 번째 열 비교해서 합산하기
result_body = []
for i in range(len(list_beans)):
    result_body.append(abs(body - list_beans[i][0]))
print(result_body)
# 두 번째 열 비교해서 합산하기
result_acidity = []
for i in range(len(list_beans)):
    result_acidity.append(abs(acidity - list_beans[i][1]))
print(result_acidity)

# 세 번째 열 비교해서 합산하기
result_sweet = []
for i in range(len(list_beans)):
    result_sweet.append(abs(sweet - list_beans[i][2]))
print(result_sweet)

# 네 번째 열 비교해서 합산하기
result_flavor = []
for i in range(len(list_beans)):
    result_flavor.append(abs(flavor - list_beans[i][3]))
print(result_flavor)

# 다섯 번째 열 비교해서 합산하기
result_bitter = []
for i in range(len(list_beans)):
    result_bitter.append(abs(bitter - list_beans[i][4]))
print(result_bitter)

# 각 결과값 합치기
result = []
for i in range(len(list_beans)):
    result.append((result_body[i] + result_acidity[i] + result_sweet[i] + result_flavor[i] + result_bitter[i]))
print(result)

# 가장 차이가 적은 결과 출력하기
result_min = min(result)
ideal_bean_index = result.index(result_min)
print(ideal_bean_index)
print(list_beans_name[result.index(result_min)])

# 동점인 결과값 출력하기
# res_list = list(filter(lambda x: result == result_min, range(len(result))))
res_list = [i for i, value in enumerate(result) if value == min(result)]
print(str(res_list))
print(res_list)

# 두 번째로 작은 결과값
